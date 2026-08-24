from __future__ import annotations

from collections import deque
from typing import TYPE_CHECKING, ClassVar, Protocol, Self, assert_never

from tools.ir.mlir.common import into_ref_map
from tools.ir.mlir.root import Root
from tools.ir.mlir.scopes import Matcher
from tools.models import config as cfg

if TYPE_CHECKING:
    from collections.abc import Iterator, Sequence

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

    @classmethod
    def from_config(cls, config: C) -> Self:
        self = cls.__new__(cls)
        self.matcher = Matcher.from_scopes(config.scope)
        return self

    def run(self, roots: RootsMut) -> Iterator[Root]:
        msg = f"{type(self).__name__}.{self.run.__name__}() is not yet implemented"
        raise NotImplementedError(msg)


class NewTree(_Base[cfg.NewTreeAction]):
    __slots__ = ("id_output",)
    id_output: IdName
    _kind = "new-tree"

    @classmethod
    def from_config(cls, config: cfg.NewTreeAction) -> Self:
        self = super().from_config(config)
        self.id_output = config.id
        return self

    def run(self, roots: RootsMut) -> Iterator[Root]:
        matcher = self.matcher
        over = matcher.over
        defs_moved = {}

        # NOTE: 1st pass collects everything that moves
        for root in roots:
            if matcher.id.matches(root.id):
                if over == "descendants":
                    defs_moved.update(
                        (def_name, root.pop(def_name))
                        for def_name in self._over_descendants_find(root)
                    )

                else:
                    raise not_yet(self.kind, over)

        # NOTE: 2nd pass fixes stale refs that remain
        defs_moved_keys = defs_moved.keys()
        is_disjoint = defs_moved_keys.isdisjoint
        is_superset = defs_moved_keys.__ge__
        for root in roots:
            has_stale_refs = [
                def_name
                for def_name, defn in root.def_items()
                if (refs := defn.refs) and not is_disjoint(refs)
            ]
            if has_stale_refs:
                ref_map = into_ref_map(defs_moved, self.id_output)
                for def_name in has_stale_refs:
                    root.replace(def_name, root[def_name].inner.with_ext_refs(ref_map))

        # NOTE: Finally, create the new tree
        for def_name, defn in defs_moved.items():
            if not is_superset({ref.ref for ref in defn.refs}):
                # NOTE: Much easier to get something done by pretending this is handled for now
                # Means that `defs_moved` is finished
                msg = (
                    f"TODO: {def_name!r} has references that are not owned by {self.id_output!r}, got:\n"
                    f"{defs_moved_keys - set(ref.ref for ref in defn.refs)}"  # ruff: ignore[unnecessary-generator-set]
                )
                raise NotImplementedError(msg)
        roots.append(Root(id=self.id_output, definitions=defs_moved))

        yield from roots

    def _over_descendants_find(self, root: Root) -> set[DefName]:
        """Identify all definitions we're going to steal."""
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
                    raise not_yet(self.kind, matcher.over)
            else:
                yield root


def not_yet(kind: cfg.ActionKind, over: cfg.IterOver) -> NotImplementedError:
    msg = f"Using both (action={kind!r}, over={over!r}) is not yet implemented."
    return NotImplementedError(msg)


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
