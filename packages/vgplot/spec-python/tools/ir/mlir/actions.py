from __future__ import annotations

from collections import deque
from typing import TYPE_CHECKING, Any, ClassVar, Protocol, Self, assert_never

from tools.ir.mlir.common import into_ref_map
from tools.ir.mlir.root import Root
from tools.ir.mlir.scopes import Matcher
from tools.models import config as cfg

if TYPE_CHECKING:
    from collections.abc import Callable, Collection, Iterable, Iterator, Mapping, Sequence, Set

    from tools.ir.mlir.definition import Definition
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


class _Base[C: cfg._BaseAction]:
    __slots__ = ("matcher",)
    matcher: Matcher
    _kind: ClassVar[cfg.ActionKind]

    @property
    def kind(self) -> cfg.ActionKind:
        return self._kind

    @property
    def ref_follow_depth(self) -> cfg.Depth:
        return self.matcher.ref_follow_depth

    @property
    def over(self) -> cfg.IterOver:
        return self.matcher.over

    @classmethod
    def from_config(cls, config: C) -> Self:
        self = cls.__new__(cls)
        self.matcher = Matcher.from_scopes(config.scope)
        return self

    def run(self, roots: RootsMut) -> Iterator[Root]:
        msg = f"{type(self).__name__}.{self.run.__name__}() is not yet implemented"
        raise NotImplementedError(msg)


class NewTree(_Base[cfg.NewTreeAction]):
    __slots__ = ("id_output", "into_ext_ref")
    id_output: IdName
    into_ext_ref: Mapping[DefName, IdName]
    _kind = "new-tree"

    def __repr__(self) -> str:
        return f"<{self.kind}: {self.id_output}>"

    @classmethod
    def from_config(cls, config: cfg.NewTreeAction) -> Self:
        self = super().from_config(config)
        self.id_output = config.id
        self.into_ext_ref = config.into_ext_ref
        return self

    def run(self, roots: RootsMut) -> Iterator[Root]:  # ruff: ignore[complex-structure]
        matcher = self.matcher
        defs_moved = {}

        # NOTE: 1st pass collects everything that moves
        for root in roots:
            # TODO @dangotbanned: Make it safe to use omit `id`
            # The bug is that the fast paths do an exact lookup for `definitions` on an "always" id match,
            # but "include" should not mean "require"
            if matcher.id.matches(root.id):
                if self.over == "descendants":
                    find = self._over_descendants_find

                elif self.over == "definitions":
                    find = self._over_definitions_find

                else:
                    raise not_yet_error(self)

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
        follow_until = self.ref_follow_depth
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


class Remove(_Base[cfg.RemoveAction]):
    _kind = "remove"

    def run(self, roots: RootsMut) -> Iterator[Root]:
        matcher = self.matcher
        for root in roots:
            if matcher.id.matches(root.id):
                if matcher.over == "definitions":
                    for def_name in tuple(name for name, _ in matcher.matching_definitions(root)):
                        root.pop(def_name)
                    yield root
                else:
                    raise not_yet_error(self)
            else:
                yield root


def not_yet_error(action: _Base[Any]) -> NotImplementedError:
    msg = f"Using both (action={action.kind!r}, over={action.over!r}) is not yet implemented."
    return NotImplementedError(msg)


def dangling_ref_error(
    action: NewTree, def_name: DefName, defn: Definition[Any], defs_moved: Iterable[DefName]
) -> TypeError:
    msg = (
        f"{def_name!r} has references that are not owned by {action.id_output!r}, got:\n"
        f"{ {ref.ref for ref in defn.refs}.difference(defs_moved) }.\n\n"
        "Hints:\n"
        "- consider increasing `scope.ref_follow_depth` to collect more references\n"
        "- consider using `into_ext_ref` to define a cyclic dependency"
    )
    return TypeError(msg)


def from_config(configs: Sequence[cfg.Action], /) -> Iterator[tuple[int, Action]]:
    for idx, config in enumerate(configs):
        match config:
            case cfg.RemoveAction():
                item = Remove.from_config(config)
            case cfg.NewTreeAction():
                item = NewTree.from_config(config)
            case cfg.AsRefAction():
                msg = f"TODO @dangotbanned: action='as-ref', got: {config!r}"
                raise NotImplementedError(msg)
            case _:
                assert_never(config)

        yield idx, item
