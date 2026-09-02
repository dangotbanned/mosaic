from __future__ import annotations

import typing
from collections import deque
from typing import TYPE_CHECKING, Any, ClassVar, Final, Literal as L, Protocol, assert_never

from tools.codegen.convert import kebab_case
from tools.ir.mlir import nodes
from tools.ir.mlir.common import into_name_map, into_ref_map
from tools.ir.mlir.definition import Definition
from tools.ir.mlir.root import Root
from tools.ir.mlir.scopes import Matcher
from tools.models import config as cfg

if TYPE_CHECKING:
    from collections.abc import Callable, Collection, Iterable, Iterator, Mapping, Sequence, Set

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


type Todo = typing.Any


class _MultiOver[O: cfg.IterOver](_Base[O], Protocol):
    __slots__ = ("_over",)
    _over: O

    @property
    def over(self) -> O:
        return self._over


class AsRef[O: L["children", "descendants"]](_MultiOver[O]):
    __slots__ = ("match_doc", "name", "type")

    def __init__(
        self,
        matcher: Matcher,
        over: O,
        name: DefName,
        type: Todo,  # ruff: ignore[builtin-argument-shadowing]
        *,
        match_doc: bool,
    ) -> None:
        self.matcher = matcher
        self._over = over
        self.name = name
        self.type = type
        self.match_doc = match_doc


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
    __slots__ = ()

    @property
    def over(self) -> L["definitions"]:
        return "definitions"

    def run(self, roots: RootsMut) -> Iterator[Root]:
        matcher = self.matcher
        for root in roots:
            if matcher.id.matches(root.id):
                for def_name in tuple(name for name, _ in matcher.matching_definitions(root)):
                    root.pop(def_name)
            yield root

    def __init__(self, matcher: Matcher) -> None:
        self.matcher = matcher


class AsDefs(_Base[L["children"]]):
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
                new_defs = {}
                for (def_name, defn), children in matcher.matching_children(root):
                    # NOTE: Simpler to just handle the case I have, before generalizing to anything
                    if not isinstance(defn.inner, nodes.Union):
                        msg = f"TODO: Support {defn.inner.__class__.__name__!r} as a parent type in {self.kind!r}, got:\n{defn!r}"
                        raise NotImplementedError(msg)
                    new_members = []
                    for idx, child in enumerate(children, 1):
                        child_name = f"{def_name}{idx}"
                        new_defs[child_name] = Definition.from_mlir(child.with_doc(defn.inner.doc))
                        new_members.append(nodes.ref(child_name))
                    new_defs[def_name] = Definition.from_mlir(
                        defn.inner.__replace__(members=tuple(new_members))
                    )
                if new_defs:
                    root.definitions.update(new_defs)
            yield root


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
            yield root

    def _handle_root(self, root: Root) -> Root:
        new_defs: dict[str, Definition[nodes.MLIR]] = {}
        repl_old_new: dict[nodes.MLIR, nodes.MLIR] = {}
        for (def_name, defn), it_fields in self.matcher.matching_fields(root):
            for old_name, old_field in it_fields:
                old_field_type = old_field.type
                new_def_name = old_name.capitalize()
                if _has_fields(old_field_type):
                    new_defs[new_def_name] = Definition.from_mlir(
                        old_field_type.with_doc(old_field.doc)
                    )
                    repl_old_new[old_field_type] = nodes.ref(new_def_name)
                elif old_types := [
                    desc for desc in old_field_type.iter_descendants() if _has_fields(desc)
                ]:
                    # Need to defer creating the name until we know that there are more than 2
                    if len(old_types) == 1:
                        old_type = old_types[0]
                        new_defs[new_def_name] = Definition.from_mlir(old_type)
                        repl_old_new[old_type] = nodes.ref(new_def_name)
                    else:
                        # TODO @dangotbanned: doesn't work well for tip.format
                        # dcg splits that out as `Format`
                        # I have `Tip1`, `Tip2`
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

    _SUPPORTED: Final = nodes.ClosedDict, nodes.ExtraDict, nodes.OpenDict, nodes.NamedTuple

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


_HAS_FIELDS: Final = (nodes.ClosedDict, nodes.ExtraDict, nodes.OpenDict)


def _has_fields(obj: Any) -> typing.TypeIs[nodes.ClosedDict | nodes.ExtraDict | nodes.OpenDict]:
    return isinstance(obj, _HAS_FIELDS)


def dangling_ref_error(
    action: NewTree[Any], def_name: DefName, defn: Definition[Any], defs_moved: Iterable[DefName]
) -> TypeError:
    msg = (
        f"{def_name!r} has references that are not owned by {action.id_output!r}, got:\n"
        f"{ {ref.ref for ref in defn.refs}.difference(defs_moved) }.\n\n"
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
            case cfg.RemoveAction(scope=scope):
                item = Remove(Matcher.from_scopes(scope))
            case cfg.NewTreeAction(scope=scope, id=id, into_ext_ref=into_ext_ref):
                item = NewTree(Matcher.from_scopes(scope), scope.over, id, into_ext_ref)
            case cfg.AsRefAction(scope=scope, name=name, type=type, match_doc=match_doc):
                # NOTE: Pretty cool that `pyright` reports this here tbf
                item = AsRef(  # pyright: ignore[reportAbstractUsage]
                    Matcher.from_scopes(scope), scope.over, name, type, match_doc=match_doc
                )
            case cfg.AsDefsAction(scope=scope):
                item = AsDefs(Matcher.from_scopes(scope))
            case cfg.RenameFieldsAction(scope=scope, overrides=overrides):
                item = RenameFields(Matcher.from_scopes(scope), overrides)
            case cfg.AsDefsFieldAction(scope=scope):
                item = AsDefsField(Matcher.from_scopes(scope))
            case _:
                assert_never(config)

        yield idx, item
