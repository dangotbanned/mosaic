"""Representation of `config.Scopes`.

The configuration syntax is designed for maximum flexibility, while remaining compact to write.

Here we convert that into something more optimized for the search itself.
"""

from __future__ import annotations

import typing
from collections.abc import Callable, Iterable
from typing import Literal as L, Self

from tools.models.base import Entry
from tools.models.config import Depth, Filter, IdName, MLIRType, NamesNodes, Scopes

if typing.TYPE_CHECKING:
    from tools.models import mlir

type Unused = typing.Any
type Incomplete = typing.Any
type Predicate[T = object, R = bool] = Callable[[T], R]
type DefsEntries = Iterable[Entry[mlir.MLIR]]
type DefsMatcherFn = Callable[[mlir.Root], DefsEntries]


class Matcher:
    # NOTE: For this part, some options are:
    # 1. Treat every action as an individual. Do everything sequentially. Use the scope as-is.
    # 2. Transform `Scopes` into something to base decisions on
    #   i. Possibly in combination with others, to decide what kind of "cleanup" would be needed
    # 3. Transform `Scopes` into a "compiled" representation
    #   i. Calling the compiled version will be a single call, instead of checking 19 different conditions
    __slots__ = ("descend", "matches_id", "matching_definitions", "ref_follow_depth", "todo_child")
    matches_id: Predicate[IdName]
    matching_definitions: DefsMatcherFn
    todo_child: Incomplete
    descend: bool
    ref_follow_depth: Depth

    @classmethod
    def from_scopes(cls, scopes: Scopes) -> Self:
        self = cls.__new__(cls)
        include, exclude = scopes.include, scopes.exclude
        self.matches_id = _into_id_matcher(include, exclude)
        self.matching_definitions = _into_defs_matcher(include, exclude)
        self.descend = scopes.descend
        self.ref_follow_depth = scopes.ref_follow_depth

        # TODO @dangotbanned: `child``
        # TODO @dangotbanned: `ref`
        return self

    def search_eager(self, root: mlir.Root) -> None:
        if self.matches_id(root.id):
            if self.descend:
                for name, node in self.matching_definitions(root):
                    # yields `node` first
                    node.iter_descendants()
                    msg = f"TODO: successful match on defs (descend=True): {name!r}, {node!r}"
                    raise NotImplementedError(msg)

            else:
                for name, node in self.matching_definitions(root):
                    # does not yield `node`
                    node.iter_children()
                    msg = f"TODO: successful match on defs: {name!r}, {node!r}"
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
            return _no_predicate(incl_defs, excl_defs)
        case (1, 0, 0, 0):
            return _include_name_1(incl_defs, excl_defs)
        case (_, 0, 0, 0):
            return _include_names(incl_defs, excl_defs)
        case (0, 0, _, 0):
            return _exclude_names(incl_defs, excl_defs)
        case (0, _, 0, _):
            return _only_types(incl_defs, excl_defs)
        case _:
            return _unoptimized(incl_defs, excl_defs)


def _no_predicate(__: Unused, ___: Unused, /) -> DefsMatcherFn:
    def _(root: mlir.Root) -> DefsEntries:
        return root.definitions.items()

    return _


def _include_name_1(incl_defs: NamesNodes, __: Unused, /) -> DefsMatcherFn:
    name = next(iter(incl_defs.names))

    def _(root: mlir.Root) -> DefsEntries:
        yield name, root.definitions[name]

    return _


def _include_names(incl_defs: NamesNodes, __: Unused, /) -> DefsMatcherFn:
    names = incl_defs.names

    def _(root: mlir.Root) -> DefsEntries:
        defs = root.definitions
        total = len(defs)
        if (len(names) / total) < 0.1:
            for name in names:
                yield name, defs[name]
        else:
            for name, node in defs.items():
                if name in names:
                    yield name, node

    return _


def _exclude_names(__: Unused, excl_defs: NamesNodes, /) -> DefsMatcherFn:
    names = excl_defs.names

    def _(root: mlir.Root) -> DefsEntries:
        for name, node in root.definitions.items():
            if name not in names:
                yield name, node

    return _


def _only_types(incl_defs: NamesNodes, excl_defs: NamesNodes, /) -> DefsMatcherFn:
    types = _convert_nodes((incl_defs.nodes or _MLIR_TYPES).difference(excl_defs.nodes))

    def _(root: mlir.Root) -> DefsEntries:
        for name, node in root.definitions.items():
            if isinstance(node, types):
                yield name, node

    return _


def _unoptimized(incl_defs: NamesNodes, excl_defs: NamesNodes, /) -> DefsMatcherFn:
    types = _convert_nodes((incl_defs.nodes or _MLIR_TYPES).difference(excl_defs.nodes))

    def _(root: mlir.Root) -> DefsEntries:
        names = set(root.definitions.keys())
        if incl_defs.names:
            names.intersection_update(incl_defs.names)
        if excl_defs.names:
            names.difference_update(excl_defs.names)
        for name, node in root.definitions.items():
            if name in names and isinstance(node, types):
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


def _convert_nodes(nodes: Iterable[MLIRType], /) -> tuple[type[mlir.MLIR], ...]:
    from tools.models import mlir

    return tuple[type[mlir.MLIR], ...](getattr(mlir, name) for name in nodes)


def _into_id_matcher(include: Filter, exclude: Filter) -> Predicate[IdName]:
    if incl_id := include.id:
        if excl_id := exclude.id:
            return _included_not_excluded(incl_id, excl_id)
        return incl_id.__contains__
    if excl_id := exclude.id:
        return _not_excluded(excl_id)
    return _always


def _always(_: Unused, /) -> L[True]:
    return True


def _included_not_excluded[T](include: frozenset[T], exclude: frozenset[T], /) -> Predicate[T]:
    in_include = include.__contains__
    in_exclude = exclude.__contains__

    def matches(obj: T, /) -> bool:
        return in_include(obj) and not in_exclude(obj)

    return matches


def _not_excluded[T](exclude: frozenset[T], /) -> Predicate[T]:
    in_exclude = exclude.__contains__

    def matches(obj: T, /) -> bool:
        return not in_exclude(obj)

    return matches
