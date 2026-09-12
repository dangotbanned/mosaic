from __future__ import annotations

import functools
import re
import typing
from collections import deque
from importlib import import_module
from types import ModuleType
from typing import TYPE_CHECKING, Any, ClassVar, Final, Literal as L, Protocol, assert_never

from tools.codegen.convert import kebab_case
from tools.common import ensure_type
from tools.ir.mlir import nodes
from tools.ir.mlir.common import into_name_map, into_ref_map, sort_key_mlir_dict
from tools.ir.mlir.definition import Definition
from tools.ir.mlir.nodes import ClosedDict, Union
from tools.ir.mlir.root import Root
from tools.ir.mlir.scopes import Matcher, is_inner_union
from tools.models import config as cfg

if TYPE_CHECKING:
    from collections.abc import Callable, Collection, Iterable, Iterator, Mapping, Sequence, Set

    from tools.ir.mlir.nodes import MLIR
    from tools.models.base import DefName, IdName

type RootsMut = deque[Root]


__all__ = ("Action", "from_config")


class Action(Protocol):
    """A mutating operation over a stack of [`tools.ir.mlir.Root`][].

    An `Action` can produce new `Root`s, update those that exist or remove them entirely.

    These traits define the shape of `run`, which requires the output of each `Action` to be collected before starting another.
    """

    def run(self, roots: RootsMut, /) -> Iterator[Root]: ...
    @property
    def kind(self) -> cfg.ActionKind: ...


class _Base[O: cfg.IterOver](Protocol):
    __slots__ = ("matcher",)
    matcher: Matcher
    _kind: ClassVar[cfg.ActionKind]

    @property
    def over(self) -> O: ...
    @property
    def kind(self) -> cfg.ActionKind:
        return self._kind

    def run(self, roots: RootsMut) -> Iterator[Root]:
        msg = f"{type(self).__name__}.{self.run.__name__}() is not yet implemented"
        raise NotImplementedError(msg)

    def __repr__(self) -> str:
        return f"<{self.kind}: {self.matcher}>"

    def __init_subclass__(cls, **kwds: Any) -> None:
        super().__init_subclass__(**kwds)
        name = cls.__name__
        if not name.startswith("_"):
            kind = kebab_case(name)
            if kind not in cfg._ACTION_KIND:
                msg = (
                    f"{name!r} should be the PascalCase version of a kebab-case `action` value.\n"
                    f"But {kind!r} is not one of: {cfg._ACTION_KIND!r}\n\n"
                    f"Hints:\n- try updating {cfg.ActionKind}?\n- spell {name!r} differently?"
                )
                raise TypeError(msg)
            cls._kind = kind


class _MultiOver[O: cfg.IterOver](_Base[O], Protocol):
    __slots__ = ("_over",)
    _over: O

    @property
    def over(self) -> O:
        return self._over


@typing.final
class Plugin(_MultiOver[cfg.IterOver]):
    __slots__ = ("entry_point", "extra")
    entry_point: str
    extra: Mapping[str, Any]

    _PATTERN: ClassVar = re.compile(cfg.ENTRY_POINT_PATTERN["python"])

    def __init__(self, config: cfg.PluginAction) -> None:
        self.matcher = Matcher.from_scopes(config.scope)
        self.entry_point = config.entry_point
        self.extra = config.extra
        self._over = config.scope.over

    def load(self) -> PluginImpl:
        if (
            (match := self._PATTERN.match(self.entry_point))
            and (name := match.group("module"))
            and (module := import_module(name))
            and (
                loaded := functools.reduce(
                    getattr, filter(None, (match.group("attr") or "").split(".")), module
                )
            )
        ):
            if isinstance(loaded, ModuleType) or not _is_plugin_impl(loaded):
                msg = f"{type(loaded).__name__!r} is not a callable, got:\n{loaded!r}"
                raise TypeError(msg)
            return loaded
        msg = f"Entry point {self.entry_point!r} not found."
        raise NotImplementedError(msg)

    def run(self, roots: RootsMut) -> Iterator[Root]:
        yield from self.load()(self, roots)


class PluginImpl(Protocol):
    def __call__(self, action: Plugin, roots: RootsMut, /) -> Iterator[Root]: ...


def _is_plugin_impl(obj: Any) -> typing.TypeIs[PluginImpl]:
    return callable(obj)


def actions_plugin[Fn: PluginImpl](function: Fn, /) -> Fn:
    """Decorate a plugin function for type checking.

    Args:
        function: The function to decorate.
            At runtime the function is returned unchanged.

    ## Examples
    ```py
    from tools.ir import mlir
    from collections.abc import Iterator


    @mlir.actions_plugin
    def something(action: mlir.Plugin, roots: mlir.RootsMut) -> Iterator[mlir.Root]:
        matcher = action.matcher
        for root in roots:
            if matcher.matches_root(root):
                # do something with root ...
                ...
            yield root
    ```
    """
    return function


class NewTree[O: L["definitions", "descendants"]](_MultiOver[O]):
    __slots__ = ("id_output", "into_ext_ref")
    id_output: IdName
    into_ext_ref: Mapping[DefName, IdName]

    def __repr__(self) -> str:
        return f"<{self.kind}: {self.id_output}>"

    def __init__(
        self, matcher: Matcher, over: O, id: IdName, into_ext_ref: Mapping[DefName, IdName]
    ) -> None:
        self.matcher = matcher
        self._over = over
        self.id_output = id
        self.into_ext_ref = into_ext_ref

    def run(self, roots: RootsMut) -> Iterator[Root]:
        matcher = self.matcher
        defs_moved = {}

        # NOTE: 1st pass collects everything that moves
        if self.over == "descendants":
            find = self._over_descendants_find
        else:
            find = self._over_definitions_find
        for root in roots:
            # TODO @dangotbanned: Make it safe to use omit `id`
            # The bug is that the fast paths do an exact lookup for `definitions` on an "always" id match,
            # but "include" should not mean "require"
            if matcher.id.matches(root.id):
                defs_moved.update((def_name, root.pop(def_name)) for def_name in find(root))

        # NOTE: 2nd pass fixes stale refs that remain
        defs_moved_keys = defs_moved.keys()
        is_disjoint: Callable[[Iterable[DefName]], bool] = defs_moved_keys.isdisjoint
        is_superset: Callable[[Set[DefName]], bool] = defs_moved_keys.__ge__
        for root in roots:
            has_stale_refs = [
                def_name
                for def_name, defn in root.def_items()
                if (refs := defn.refs) and not is_disjoint({ref.ref for ref in refs})
            ]
            if has_stale_refs:
                ref_map = into_ref_map(defs_moved, self.id_output)
                for def_name in has_stale_refs:
                    root.replace(def_name, root[def_name].inner.with_ext_refs(ref_map))

        # NOTE: Finally, create the new tree
        circular = {}
        for def_name, defn in defs_moved.items():
            if not is_superset({ref.ref for ref in defn.refs}):
                if self.into_ext_ref:
                    circular[def_name] = defn.from_mlir(
                        defn.inner.with_ext_refs(self.into_ext_ref.get)
                    )
                else:
                    raise dangling_ref_error(self, def_name, defn, defs_moved_keys)

        roots.append(Root(id=self.id_output, definitions=defs_moved | circular))

        yield from roots

    def _over_definitions_find(self, root: Root) -> Collection[DefName]:
        if take := tuple(name for name, _ in self.matcher.matching_definitions(root)):
            return take
        msg = f"Did not find any matches for {self!r}"
        raise NotImplementedError(msg)

    def _over_descendants_find(self, root: Root) -> Collection[DefName]:
        take: set[DefName] = set()
        follow_until = self.matcher.ref_follow_depth
        for name, defn in self.matcher.matching_definitions(root):
            take.add(name)
            refs = defn.refs
            if refs and (todo := {ref.ref for ref in refs}.difference(take)):
                take.update(todo)
                while todo:
                    depth = 0
                    branch = {todo.pop()}
                    while depth != follow_until and branch:
                        resolved = root[branch.pop()]
                        depth += 1
                        if resolved.refs and (
                            found_more := {ref.ref for ref in resolved.refs}.difference(take)
                        ):
                            branch.update(found_more)
                        take.update(branch)
        if not take:
            msg = f"Did not find any matches for {self!r}"
            raise NotImplementedError(msg)
        return take


class Remove(_Base[L["definitions"]]):
    __slots__ = ("preserve_children",)
    preserve_children: bool

    @property
    def over(self) -> L["definitions"]:
        return "definitions"

    def _replace_with_children(
        self, roots: RootsMut, defs_removed: dict[DefName, Definition[nodes.Union]]
    ) -> Iterator[Root]:
        is_disjoint: Callable[[Iterable[DefName]], bool] = defs_removed.keys().isdisjoint
        explain = f"TODO: Support non-union types in {self.kind!r} w/ `preserve_children=True`"
        for root in roots:
            if has_stale_refs := [
                def_name
                for def_name, defn in root.def_items()
                if (refs := defn.refs) and not is_disjoint({ref.ref for ref in refs})
            ]:
                for def_name in has_stale_refs:
                    stale_inner = ensure_type(
                        root[def_name].inner, nodes.Union, name=def_name, explain=explain
                    )
                    new_members = deque()
                    for member in stale_inner.members:
                        if isinstance(member, nodes.Reference) and (
                            found := defs_removed.get(member.ref)
                        ):
                            new_members.extend(found.inner.members)
                        else:
                            new_members.append(member)
                    root.replace(def_name, stale_inner.__replace__(members=tuple(new_members)))
            yield root

    def run(self, roots: RootsMut) -> Iterator[Root]:
        matcher = self.matcher
        defs_removed: dict[DefName, Definition[nodes.Union]] = {}
        for root in roots:
            if matcher.id.matches(root.id):
                for def_name in tuple(name for name, _ in matcher.matching_definitions(root)):
                    removed = root.pop(def_name)
                    if self.preserve_children and is_inner_union(removed):
                        defs_removed[def_name] = removed
        if defs_removed:
            yield from self._replace_with_children(roots, defs_removed)
        else:
            yield from roots

    def __init__(self, matcher: Matcher, *, preserve_children: bool) -> None:
        self.matcher = matcher
        self.preserve_children = preserve_children


class AsDefs(_Base[L["children"]]):
    __slots__ = ("discriminator",)
    discriminator: str

    @property
    def over(self) -> L["children"]:
        return "children"

    def __init__(self, matcher: Matcher, discriminator: str) -> None:
        self.matcher = matcher
        self.discriminator = discriminator

    def run(self, roots: RootsMut) -> Iterator[Root]:
        matcher = self.matcher
        for root in roots:
            if matcher.id.matches(root.id):
                yield self._on_root(root)
            else:
                yield root

    def _on_root(self, root: Root) -> Root:
        new_defs = {}
        for (def_name, defn), children in self.matcher.matching_children(root):
            # NOTE: Simpler to just handle the case I have, before generalizing to anything
            defn_inner = ensure_type(
                defn.inner, Union, explain=f"TODO: Support non-union parent types in {self.kind!r}"
            )
            if self.discriminator:
                it = self._name_via_discriminator(def_name, defn_inner, children)
            else:
                it = self._name_infer(def_name, defn_inner, children)
            new_defs.update(((name, Definition.from_mlir(node)) for name, node in it))
        if new_defs:
            root.definitions.update(new_defs)
        return root

    def _name_via_discriminator(
        self, def_name: DefName, defn_inner: Union, children: Iterable[MLIR]
    ) -> Iterator[tuple[DefName, MLIR]]:
        field = self.discriminator
        new_members = []
        for child in children:
            field_type = ensure_type(
                ensure_type(child, ClosedDict).fields[field].type, nodes.Literal
            )
            value = str(field_type.members[0])
            name = f"{def_name}{value[0].upper()}{value[1:]}"
            new_members.append(nodes.ref(name))
            yield name, child.with_doc(defn_inner.doc)
        yield def_name, defn_inner.__replace__(members=tuple(new_members))

    def _name_infer(
        self, def_name: DefName, defn_inner: Union, children: Iterable[MLIR]
    ) -> Iterator[tuple[DefName, MLIR]]:
        # Need to hold off on naming them until I've seen all the field names, which can then be used to sort
        # NOTE: Any other type must passthrough as-is
        todo = []
        new_members = []
        for child in children:
            if isinstance(child, ClosedDict):
                todo.append(child)
            else:
                new_members.append(child)
        if len(todo) != 1:
            todo.sort(key=sort_key_mlir_dict)
        for idx, child in enumerate(todo, 1):
            name = f"{def_name}{idx}"
            new_members.append(nodes.ref(name))
            yield name, child.with_doc(defn_inner.doc)
        yield def_name, defn_inner.__replace__(members=tuple(new_members))

    def _name_children(
        self, def_name: DefName, children: Iterable[MLIR]
    ) -> Iterator[tuple[DefName, MLIR]]:
        field = self.discriminator
        for child in children:
            field_type = ensure_type(
                ensure_type(child, nodes.ClosedDict).fields[field].type, nodes.Literal
            )
            value = str(field_type.members[0])
            yield f"{def_name}{value[0].upper()}{value[1:]}", child


class AsDefsField(_Base[L["children"]]):
    """Name all anonymous types within a field, which are not valid syntactically in python.

    This is a pretty annoying problem, because there are so few cases of them but they're all different.
    """

    __slots__ = ()

    @property
    def over(self) -> L["children"]:
        return "children"

    def __init__(self, matcher: Matcher) -> None:
        self.matcher = matcher

    def run(self, roots: RootsMut) -> Iterator[Root]:
        matcher = self.matcher
        for root in roots:
            if matcher.id.matches(root.id):
                yield self._handle_root(root)
            else:
                yield root

    def _handle_root(self, root: Root) -> Root:
        new_defs: dict[str, Definition[nodes.MLIR]] = {}
        repl_old_new: dict[nodes.MLIR, nodes.MLIR] = {}
        for (def_name, defn), it_fields in self.matcher.matching_fields(root):
            for old_name, old_field in it_fields:
                old_field_type = old_field.type
                new_def_name = old_name.capitalize()
                if nodes.is_dict(old_field_type):
                    new_defs[new_def_name] = Definition.from_mlir(
                        old_field_type.with_doc(old_field.doc)
                    )
                    repl_old_new[old_field_type] = nodes.ref(new_def_name)
                elif old_types := [
                    desc for desc in old_field_type.iter_descendants() if nodes.is_dict(desc)
                ]:
                    # Need to defer creating the name until we know that there are more than 2
                    if len(old_types) == 1:
                        old_type = old_types[0]
                        new_defs[new_def_name] = Definition.from_mlir(old_type)
                        repl_old_new[old_type] = nodes.ref(new_def_name)
                    else:
                        for idx, old_type in enumerate(old_types, 1):
                            new_def_name_i = f"{new_def_name}{idx}"
                            new_defs[new_def_name_i] = Definition.from_mlir(old_type)
                            repl_old_new[old_type] = nodes.ref(new_def_name_i)
            if repl_old_new:
                new_defs[def_name] = Definition.from_mlir(defn.inner.find_replace(repl_old_new))
        if new_defs:
            root.definitions.update(new_defs)
        return root


class RenameFields(_Base[L["definitions"]]):
    __slots__ = ("overrides",)
    overrides: Mapping[str, str]

    _SUPPORTED: Final = nodes.ClosedDict, nodes.ExtraDict, nodes.OpenDict

    @property
    def over(self) -> L["definitions"]:
        return "definitions"

    def __init__(self, matcher: Matcher, overrides: Mapping[str, str]) -> None:
        self.matcher = matcher
        self.overrides = overrides

    def run(self, roots: RootsMut) -> Iterator[Root]:
        matcher = self.matcher
        name_map = into_name_map(self.overrides)
        for root in roots:
            if matcher.id.matches(root.id):
                new_defs = {}
                for def_name, defn in matcher.matching_definitions(root):
                    inner = defn.inner
                    if not isinstance(inner, self._SUPPORTED):
                        raise rename_fields_error(self, def_name, defn)
                    maybe_replace = inner.rename_fields(name_map)
                    if maybe_replace is not inner:
                        new_defs[def_name] = defn.__replace__(inner=maybe_replace)
                if new_defs:
                    root.definitions.update(new_defs)
            yield root


def dangling_ref_error(
    action: NewTree[Any], def_name: DefName, defn: Definition[Any], defs_moved: Iterable[DefName]
) -> TypeError:
    msg = (
        f"{def_name!r} has references that are not owned by {action.id_output!r}, "
        f"got: {sorted({ref.ref for ref in defn.refs}.difference(defs_moved))}.\n"
        "Hints:\n"
        "- consider increasing `scope.ref_follow_depth` to collect more references\n"
        "- consider using `into_ext_ref` to define a cyclic dependency"
    )
    return TypeError(msg)


def rename_fields_error(
    action: RenameFields, def_name: DefName, defn: Definition[Any]
) -> TypeError:
    options = [tp.__name__ for tp in action._SUPPORTED]
    msg = (
        f"{action.kind!r} is not supported for node types that do not define fields, got:\n  {def_name!r}: {defn.inner.__class__.__name__!r}"
        f"\n\nHint:\n- refine the search with `scope.include.definition.nodes = {options!r}"
    )
    return TypeError(msg)


def from_config(configs: Sequence[cfg.Action], /) -> Iterator[tuple[int, Action]]:
    for idx, config in enumerate(configs):
        match config:
            case cfg.RemoveAction(scope=scope, preserve_children=preserve):
                item = Remove(Matcher.from_scopes(scope), preserve_children=preserve)
            case cfg.NewTreeAction(scope=scope, id=id, into_ext_ref=into_ext_ref):
                item = NewTree(Matcher.from_scopes(scope), scope.over, id, into_ext_ref)
            case cfg.AsDefsAction(scope=scope, discriminator=discriminator):
                item = AsDefs(Matcher.from_scopes(scope), discriminator)
            case cfg.RenameFieldsAction(scope=scope, overrides=overrides):
                item = RenameFields(Matcher.from_scopes(scope), overrides)
            case cfg.AsDefsFieldAction(scope=scope):
                item = AsDefsField(Matcher.from_scopes(scope))
            case cfg.PluginAction():
                item = Plugin(config)
            case _:
                assert_never(config)

        yield idx, item
