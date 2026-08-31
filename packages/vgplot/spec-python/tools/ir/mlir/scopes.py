"""Representation of `config.Scopes`.

The configuration syntax is designed for maximum flexibility, while remaining compact to write.

Here we convert that into something more optimized for the search itself.
"""

from __future__ import annotations

import typing
from collections.abc import Callable, Iterable, Iterator
from itertools import chain
from typing import Final, Literal as L

from tools.ir.mlir import nodes as mlir
from tools.ir.mlir.nodes import MLIR
from tools.models.base import DefName, Entry, IdName

if typing.TYPE_CHECKING:
    from tools.ir.mlir.definition import Definition
    from tools.ir.mlir.root import Root
    from tools.models.config import Depth, Filter, NamesNodes, Nodes, Scopes

type Unused = typing.Any
type Incomplete = typing.Any
type DefsEntries = Iterable[Entry[Definition[MLIR]]]
type IdMatcher = IdAlways | IdInclude | IdNotExclude
type DefsMatcher = DefsAlways | DefsIncludeNames | DefsExcludeNames | DefsIncludeNodes | DefsGeneral
type ChildMatcher = ChildAlways | ChildIncludeNodes

type GroupByIter[T, S] = Iterator[tuple[T, Iterator[S]]]
"""An iterator with the same shape as [`itertools.groupby`][].

- On each iteration, it pulls a named `Definition` and an iterator over it's matching children.
- Each `Definition` is guaranteed to have at-least one matching child
"""

# HACK: Forcing `pyrefly` to not infer `0` as `int`
_ZERO: Final[L[0]] = 0  # ruff: ignore[redundant-final-literal]


class Matcher:
    # NOTE: For this part, some options are:
    # 1. Treat every action as an individual. Do everything sequentially. Use the scope as-is.
    # 2. Transform `Scopes` into something to base decisions on
    #   i. Possibly in combination with others, to decide what kind of "cleanup" would be needed
    # 3. Transform `Scopes` into a "compiled" representation
    #   i. Calling the compiled version will be a single call, instead of checking 19 different conditions
    __slots__ = ("child", "definition", "id", "ref_follow_depth")
    id: IdMatcher
    definition: DefsMatcher
    child: ChildMatcher
    ref_follow_depth: Depth

    def __repr__(self) -> str:
        return f"{self.id!r} & {self.definition!r} & {self.child!r}"

    def matching_definitions(self, root: Root) -> DefsEntries:
        return self.definition.iter_defs(root)

    def matching_children(self, root: Root) -> GroupByIter[Entry[Definition[MLIR]], MLIR]:
        return self.child.iter_children(self.matching_definitions(root))

    def matching_descendants(self, root: Root) -> Incomplete:
        msg = "TODO @dangotbanned: Move things from `actions.py` to here"
        raise NotImplementedError(msg)

    @classmethod
    def from_scopes(cls, scopes: Scopes) -> Matcher:
        self = cls.__new__(cls)
        include, exclude = scopes.include, scopes.exclude
        if not (incl_id := include.id):
            self.id = IdNotExclude(exclude.id) if exclude.id else _ID_ALWAYS
        else:
            self.id = IdInclude(incl_id - exclude.id) if exclude.id else IdInclude(incl_id)

        self.definition = _into_defs_matcher(include, exclude)
        self.ref_follow_depth = getattr(scopes, "ref_follow_depth", _ZERO)

        if include.child or exclude.child:
            self.child = ChildIncludeNodes(include.child, exclude.child)
        else:
            self.child = _CHILD_ALWAYS

        return self


def _into_defs_matcher(include: Filter, exclude: Filter) -> DefsMatcher:
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
            return _DEFS_ALWAYS
        case (_, 0, 0, 0):
            return DefsIncludeNames(incl_defs.names)
        case (0, 0, _, 0):
            return DefsExcludeNames(excl_defs.names)
        case (0, _, 0, _):
            return DefsIncludeNodes(incl_defs, excl_defs)
        case _:
            return DefsGeneral(incl_defs, excl_defs)


def _ordered_args(iterable: Iterable[str], /) -> str:
    """Display as a variadic argument list."""
    items = sorted(iterable)
    if len(items) == 1:
        return f"({items[0]!r})"
    if items:
        return f"{tuple(items)!r}"
    return "()"


class ChildAlways:
    __slots__ = ()

    def __repr__(self) -> str:
        return "child.always()"

    def iter_children(self, entries: DefsEntries, /) -> GroupByIter[Entry[Definition[MLIR]], MLIR]:
        for name, node in entries:
            it = node.inner.iter_children()
            if first := next(it, None):
                yield (name, node), chain((first,), it)


class ChildIncludeNodes:
    __slots__ = ("types",)

    def __repr__(self) -> str:
        return f"child.node.is_in{_ordered_args(tp.__name__ for tp in self.types)}"

    def __init__(self, incl: Nodes, excl: Nodes, /) -> None:
        self.types: tuple[type[MLIR], ...] = _convert_nodes(incl, excl)

    def iter_children(self, entries: DefsEntries, /) -> GroupByIter[Entry[Definition[MLIR]], MLIR]:
        types = self.types
        for name, node in entries:
            it = (child for child in node.inner.iter_children() if isinstance(child, types))
            if first := next(it, None):
                yield (name, node), chain((first,), it)


class DefsAlways:
    __slots__ = ()

    def __repr__(self) -> str:
        return "definition.always()"

    def iter_defs(self, root: Root, /) -> DefsEntries:
        return root.def_items()


class DefsIncludeNames:
    __slots__ = ("names",)

    def __repr__(self) -> str:
        return f"definition.name.is_in{_ordered_args(self.names)}"

    def __init__(self, names: frozenset[DefName], /) -> None:
        self.names: frozenset[DefName] = names

    def iter_defs(self, root: Root, /) -> DefsEntries:
        return root.iter_defs_by_name(self.names)


class DefsExcludeNames:
    __slots__ = ("_in_exclude", "names")

    def __repr__(self) -> str:
        return f"definition.name.is_not_in{_ordered_args(self.names)}"

    def __init__(self, names: frozenset[DefName], /) -> None:
        self.names: frozenset[DefName] = names
        self._in_exclude: Callable[[DefName], bool] = self.names.__contains__

    def iter_defs(self, root: Root, /) -> DefsEntries:
        in_exclude = self._in_exclude
        yield from ((name, node) for name, node in root.def_items() if not in_exclude(name))


class DefsIncludeNodes:
    __slots__ = ("types",)

    def __repr__(self) -> str:
        return f"definition.node.is_in{_ordered_args(tp.__name__ for tp in self.types)}"

    def __init__(self, incl_defs: NamesNodes, excl_defs: NamesNodes, /) -> None:
        self.types: tuple[type[MLIR], ...] = _convert_nodes(incl_defs, excl_defs)

    def iter_defs(self, root: Root, /) -> DefsEntries:
        types = self.types
        yield from (
            (name, node) for name, node in root.def_items() if isinstance(node.inner, types)
        )


class DefsGeneral:
    __slots__ = ("exclude_names", "include_names", "types")

    def __repr__(self) -> str:
        s = f"node.is_in{_ordered_args(tp.__name__ for tp in self.types)}"
        if include := self.include_names:
            s = f"{s} & name.is_in{_ordered_args(include)}"
        if exclude := self.exclude_names:
            s = f"{s} & name.is_not_in{_ordered_args(exclude)}"
        return f"definition.({s})"

    def __init__(self, incl_defs: NamesNodes, excl_defs: NamesNodes, /) -> None:
        self.types: tuple[type[MLIR], ...] = _convert_nodes(incl_defs, excl_defs)
        self.include_names: frozenset[DefName] = incl_defs.names
        self.exclude_names: frozenset[DefName] = excl_defs.names

    def iter_defs(self, root: Root, /) -> DefsEntries:
        names = root.def_names()
        if self.include_names:
            names = names & self.include_names
        if self.exclude_names:
            names = names - self.exclude_names
        types = self.types
        for name, node in root.iter_defs_by_name(names):
            if isinstance(node.inner, types):
                yield name, node


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


def _convert_nodes(incl: NamesNodes | Nodes, excl: NamesNodes | Nodes, /) -> tuple[type[MLIR], ...]:
    nodes = (incl.nodes or _MLIR_TYPES).difference(excl.nodes)
    return tuple[type[MLIR], ...](getattr(mlir, name) for name in nodes)


class IdInclude:
    __slots__ = ("names",)

    def __repr__(self) -> str:
        return f"id.is_in{_ordered_args(self.names)}"

    def __init__(self, names: frozenset[IdName], /) -> None:
        self.names: frozenset[IdName] = names

    def matches(self, name: IdName, /) -> bool:
        return self.names.__contains__(name)


class IdNotExclude:
    __slots__ = ("_in_exclude", "names")

    def __repr__(self) -> str:
        return f"id.is_not_in{_ordered_args(self.names)}"

    def __init__(self, names: frozenset[IdName], /) -> None:
        self.names: frozenset[IdName] = names
        self._in_exclude: Callable[[IdName], bool] = self.names.__contains__

    def matches(self, name: IdName, /) -> bool:
        return not self._in_exclude(name)


class IdAlways:
    __slots__ = ()

    def __repr__(self) -> str:
        return "id.always()"

    def matches(self, _: Unused, /) -> L[True]:
        return True


_ID_ALWAYS: Final = IdAlways()
_DEFS_ALWAYS: Final = DefsAlways()
_CHILD_ALWAYS: Final = ChildAlways()
