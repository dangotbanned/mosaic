"""Representation of `config.Scopes`.

The configuration syntax is designed for maximum flexibility, while remaining compact to write.

Here we convert that into something more optimized for the search itself.
"""

from __future__ import annotations

import itertools
import typing
from collections.abc import Callable, Iterable
from typing import Final, Literal as L, Self, final

from tools.ir.mlir import nodes as mlir
from tools.ir.mlir.nodes import MLIR
from tools.models.base import Entry, IdName

if typing.TYPE_CHECKING:
    from tools.ir.mlir.definition import Definition
    from tools.ir.mlir.root import Root
    from tools.models.config import DefName, Filter, IterOver, NamesNodes, Scopes

type Unused = typing.Any
type Incomplete = typing.Any
type DefsEntries = Iterable[Entry[Definition[MLIR]]]
type DefsMatcherFn = Callable[[Root], DefsEntries]
type IdMatcher = IdAlways | IdInclude | IdNotExclude


class Matcher:
    # NOTE: For this part, some options are:
    # 1. Treat every action as an individual. Do everything sequentially. Use the scope as-is.
    # 2. Transform `Scopes` into something to base decisions on
    #   i. Possibly in combination with others, to decide what kind of "cleanup" would be needed
    # 3. Transform `Scopes` into a "compiled" representation
    #   i. Calling the compiled version will be a single call, instead of checking 19 different conditions
    __slots__ = ("id", "matching_definitions", "over", "ref_follow_depth", "todo_child")
    id: IdMatcher
    matching_definitions: DefsMatcherFn
    todo_child: Incomplete
    over: IterOver
    ref_follow_depth: Depth

    @classmethod
    def from_scopes(cls, scopes: Scopes) -> Self:
        self = cls.__new__(cls)
        include, exclude = scopes.include, scopes.exclude
        if not (incl_id := include.id):
            self.id = IdNotExclude(exclude.id) if exclude.id else _ID_ALWAYS
        else:
            self.id = IdInclude(incl_id - exclude.id) if exclude.id else IdInclude(incl_id)

        self.matching_definitions = _into_defs_matcher(include, exclude)
        self.over = scopes.over
        self.ref_follow_depth = scopes.ref_follow_depth

        # TODO @dangotbanned: `child``
        # TODO @dangotbanned: `ref`
        return self

    def search_eager(self, root: Root) -> None:
        if self.id.matches(root.id):
            if self.over == "descendants":
                for name, node in self.matching_definitions(root):
                    # yields `node` first
                    node.inner.iter_descendants()
                    msg = f"TODO: successful match on defs ({self.over=}): {name!r}, {node.inner!r}"
                    raise NotImplementedError(msg)

            elif self.over == "children":
                for name, node in self.matching_definitions(root):
                    # does not yield `node`
                    node.inner.iter_children()
                    msg = f"TODO: successful match on defs ({self.over=}): {name!r}, {node.inner!r}"
                    raise NotImplementedError(msg)
            else:
                for name, node in self.matching_definitions(root):
                    msg = f"TODO: successful match on defs ({self.over=}): {name!r}, {node.inner!r}"
                    raise NotImplementedError(msg)


def _into_defs_matcher(include: Filter, exclude: Filter) -> DefsMatcherFn:
    """Transform scope filters into a generator function, yielding matching definitions.

    Pretty aggressively optimized, as there are cheap solutions for how I plan to use the syntax.
    """
    incl_defs = include.definition
    excl_defs = exclude.definition
    # NOTE: `frozenset` does not implement `__bool__`, and instead falls back to `__len__`.
    # So we skip straight to it
    len_incl_names, len_incl_nodes, len_excl_names, len_excl_nodes = (
        len(obj) for obj in (incl_defs.names, incl_defs.nodes, excl_defs.names, excl_defs.nodes)
    )

    match (len_incl_names, len_incl_nodes, len_excl_names, len_excl_nodes):
        case (0, 0, 0, 0):
            return _no_predicate
        case (_, 0, 0, 0):
            return _include_names(incl_defs.names)
        case (0, 0, _, 0):
            return _exclude_names(excl_defs.names)
        case (0, _, 0, _):
            return _only_types(incl_defs, excl_defs)
        case _:
            return _unoptimized(incl_defs, excl_defs)


def _no_predicate(root: Root, /) -> DefsEntries:
    return root.def_items()


def _include_names(names: frozenset[DefName], /) -> DefsMatcherFn:
    def _(root: Root) -> DefsEntries:
        return root.iter_defs_by_name(names)

    return _


def _exclude_names(names: frozenset[DefName], /) -> DefsMatcherFn:
    in_exclude = names.__contains__

    def _(root: Root) -> DefsEntries:
        yield from ((name, node) for name, node in root.def_items() if not in_exclude(name))

    return _


def _only_types(incl_defs: NamesNodes, excl_defs: NamesNodes, /) -> DefsMatcherFn:
    types = _convert_nodes(incl_defs, excl_defs)

    def _(root: Root) -> DefsEntries:
        yield from (
            (name, node) for name, node in root.def_items() if isinstance(node.inner, types)
        )

    return _


def _unoptimized(incl_defs: NamesNodes, excl_defs: NamesNodes, /) -> DefsMatcherFn:
    types = _convert_nodes(incl_defs, excl_defs)

    def _(root: Root) -> DefsEntries:
        names = root.def_names()
        if incl_defs.names:
            names = names & incl_defs.names
        if excl_defs.names:
            names = names - excl_defs.names
        include_name = names.__contains__
        for name, node in root.def_items():
            if include_name(name) and isinstance(node.inner, types):
                yield name, node

    return _


_MLIR_TYPES = frozenset(
    (
        "ClosedDict",
        "EmptyTuple",
        "ExtReference",
        "ExtraDict",
        "Field",
        "HomogeneousTuple",
        "Literal",
        "NamedTuple",
        "OpenDict",
        "PyBool",
        "PyFloat",
        "PyInt",
        "PyNone",
        "PyStr",
        "Reference",
        "Sequence",
        "Union",
        "Unknown",
        "VariantHomogeneousTuple",
    )
)


def _convert_nodes(incl_defs: NamesNodes, excl_defs: NamesNodes, /) -> tuple[type[MLIR], ...]:
    nodes = (incl_defs.nodes or _MLIR_TYPES).difference(excl_defs.nodes)
    return tuple[type[MLIR], ...](getattr(mlir, name) for name in nodes)


class IdInclude:
    __slots__ = ("names",)

    def __init__(self, names: frozenset[IdName], /) -> None:
        self.names: frozenset[IdName] = names

    def matches(self, name: IdName, /) -> bool:
        return self.names.__contains__(name)


class IdNotExclude:
    __slots__ = ("_in_exclude", "names")

    def __init__(self, names: frozenset[IdName], /) -> None:
        self.names: frozenset[IdName] = names
        self._in_exclude: Callable[[IdName], bool] = self.names.__contains__

    def matches(self, name: IdName, /) -> bool:
        return not self._in_exclude(name)


class IdAlways:
    __slots__ = ()

    def matches(self, _: Unused, /) -> L[True]:
        return True


_ID_ALWAYS: Final = IdAlways()


type DepthOp = L[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
type DepthNoOp = L[0]
"""This case **must** be narrowed from before starting iteration."""

type Depth = DepthNoOp | DepthOp


class _DepthExceeded(BaseException):
    @staticmethod
    def _from_ref_follower(obj: _RefFollower) -> _DepthExceeded:
        msg = f"Reached depth limit {obj.depth_limit!r} for definition {obj._owner!r}"
        return _DepthExceeded(msg)


_NO_ERROR = None
_RE_RAISE = False
_SUPPRESS = True


@final
class _RefFollower:
    """(Partial) Impl for `scopes.ref_follow_depth`.

    ## Notes
    - Context manager that nopes-out after going through `depth_limit` refs
        - Non re-entrant
        - One per-definition
        - `depth_limit` is local to `Scopes`
        - `depth_current` is local to here
    - Needs (indirect) access to `Root.definitions`
    """

    # NOTE: https://docs.python.org/3/reference/compound_stmts.html#the-with-statement
    __slots__ = ("_count_next", "_owner", "depth_current", "depth_limit")

    depth_limit: Final[DepthOp]

    def __init__(self, depth_limit: DepthOp, owner: DefName, /) -> None:
        self.depth_limit = depth_limit
        self._count_next: Callable[[], int] = itertools.count().__next__
        self._owner: DefName = owner

    def _increment(self) -> None:
        # Call from the *actual* following method of this class
        if self._count_next() > self.depth_limit:
            # "Catch" in `__exit__`
            raise _DepthExceeded._from_ref_follower(self)

    def follow(self, *args: Incomplete) -> Incomplete:
        self._increment()
        msg = "TODO @dangotbanned: Figure out the iteration side, then come back to this part"
        raise NotImplementedError(msg)

    def __enter__(self) -> _RefFollower:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: object,
        /,
    ) -> bool | None:
        if exc_type is None:
            return _NO_ERROR
        if exc_type is not _DepthExceeded:
            return _RE_RAISE
        return _SUPPRESS
