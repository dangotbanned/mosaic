"""Representation of `config.Scopes`.

The configuration syntax is designed for maximum flexibility, while remaining compact to write.

Here we convert that into something more optimized for the search itself.
"""

from __future__ import annotations

import typing
from collections.abc import Callable, Iterable, Iterator
from typing import Any, Final, Literal as L, TypeIs

from tools.common import prepend, select_items
from tools.ir.mlir import nodes as mlir
from tools.ir.mlir.common import inner_type_is
from tools.ir.mlir.nodes import MLIR
from tools.models.base import DefName, IdName
from tools.models.config import Child, Filter, MLIRType, NamesNodes

if typing.TYPE_CHECKING:
    from tools.ir.mlir.definition import Definition
    from tools.ir.mlir.root import Root
    from tools.models.config import Depth, Scopes

type Unused = typing.Any
# NOTE: `pyrefly` stops understanding `tuple` if this is simplified
type DefsEntries[D: MLIR = MLIR] = Iterable[tuple[DefName, Definition[D]]]
type IdMatcher = IdAlways | IdInclude | IdNotExclude
type DefsMatcher = DefsAlways | DefsIncludeNames | DefsExcludeNames | DefsIncludeNodes | DefsGeneral
type ChildMatcher = ChildAlways | ChildIncludeNodes
type FieldMatcher = AlwaysFieldNames | IncludeFieldNames

type GroupByIter[T, S] = Iterator[tuple[T, Iterator[S]]]
"""An iterator with the same shape as [`itertools.groupby`][]."""


type ChildIter[D: MLIR, S] = GroupByIter[tuple[DefName, Definition[D]], S]
"""
- On each iteration, it pulls a named `Definition` and an iterator over it's matching children.
- Each `Definition` is guaranteed to have at-least one matching child
"""

type HasFields = mlir.ClosedDict | mlir.ExtraDict | mlir.OpenDict | mlir.NamedTuple
_HAS_FIELDS: Final = mlir.ClosedDict, mlir.ExtraDict, mlir.OpenDict, mlir.NamedTuple

# HACK: Forcing `pyrefly` to not infer `0` as `int`
_ZERO: Final[L[0]] = 0  # ruff: ignore[redundant-final-literal]


# NOTE: `ty` reports `Unknown`, but `pyrefly` understands
is_inner_fields: Callable[[Definition[Any]], TypeIs[Definition[HasFields]]] = inner_type_is(
    mlir.ClosedDict, mlir.ExtraDict, mlir.OpenDict, mlir.NamedTuple
)


class Matcher:
    __slots__ = ("child", "definition", "field", "id", "ref_follow_depth")
    id: IdMatcher
    definition: DefsMatcher
    child: ChildMatcher
    field: FieldMatcher
    ref_follow_depth: Depth

    def __repr__(self) -> str:
        return f"{self.id!r} & {self.definition!r} & {self.child!r}"

    def matching_definitions(self, root: Root) -> DefsEntries:
        return self.definition.iter_defs(root)

    def matching_children(self, root: Root) -> ChildIter[MLIR, MLIR]:
        """Iterate over matching definitions with at least one matching child."""
        return self.child.iter_children(self.matching_definitions(root))

    def matching_fields(self, root: Root) -> ChildIter[HasFields, tuple[str, mlir.Field]]:
        """Iterate over matching definitions with at least one matching field."""
        return self.field.iter_children(
            ((k, v) for k, v in self.matching_definitions(root) if is_inner_fields(v))
        )

    def matches_root(self, root: Root) -> bool:
        return self.id.matches(root.id)

    @classmethod
    def from_scopes(cls, scopes: Scopes) -> Matcher:
        """Construct from a full, nested configuration object."""
        return cls._from_filters(
            scopes.include, scopes.exclude, getattr(scopes, "ref_follow_depth", _ZERO)
        )

    @classmethod
    def from_builtins(
        cls,
        *,
        # include
        include_id: frozenset[IdName] = frozenset[IdName](),
        include_definition_names: frozenset[DefName] = frozenset[DefName](),
        include_definition_nodes: frozenset[MLIRType] = frozenset[MLIRType](),
        include_child_nodes: frozenset[MLIRType] = frozenset[MLIRType](),
        # exclude
        exclude_id: frozenset[IdName] = frozenset[IdName](),
        exclude_definition_names: frozenset[DefName] = frozenset[DefName](),
        exclude_definition_nodes: frozenset[MLIRType] = frozenset[MLIRType](),
        exclude_child_nodes: frozenset[MLIRType] = frozenset[MLIRType](),
        # other
        ref_follow_depth: Depth = 0,
    ) -> Matcher:
        """Construct from keyword arguments, using only builtin types."""
        return cls._from_filters(
            Filter(
                include_id,
                NamesNodes(include_definition_names, include_definition_nodes),
                Child(include_child_nodes),
            ),
            Filter(
                exclude_id,
                NamesNodes(exclude_definition_names, exclude_definition_nodes),
                Child(exclude_child_nodes),
            ),
            ref_follow_depth=ref_follow_depth,
        )

    @classmethod
    def _from_filters(
        cls, include: Filter, exclude: Filter, ref_follow_depth: Depth = 0
    ) -> Matcher:
        self = cls.__new__(cls)
        if not (incl_id := include.id):
            self.id = IdNotExclude(exclude.id) if exclude.id else _ID_ALWAYS
        else:
            self.id = IdInclude(incl_id - exclude.id) if exclude.id else IdInclude(incl_id)
        self.definition = _into_defs_matcher(include, exclude)
        if include.child or exclude.child:
            self.child = ChildIncludeNodes(include.child, exclude.child)
        else:
            self.child = _CHILD_ALWAYS
        self.field = _into_field_matcher(include.child, exclude.child)
        self.ref_follow_depth = ref_follow_depth
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


def _into_field_matcher(include: Child, exclude: Child, /) -> FieldMatcher:
    incl, excl = include.field_names, exclude.field_names
    match (len(incl), len(excl)):
        case (0, 0):
            return _FIELD_ALWAYS
        case (_, 0):
            return IncludeFieldNames(incl)
        case (0, _):
            msg = f"`exclude.nodes.field_names` is not yet implemented, got: {excl!r}"
            raise NotImplementedError(msg)
        case _:
            return IncludeFieldNames(incl - excl)


def _ordered_args(iterable: Iterable[str], /) -> str:
    """Display as a variadic argument list."""
    items = sorted(iterable)
    if len(items) == 1:
        return f"({items[0]!r})"
    if items:
        return f"{tuple(items)!r}"
    return "()"


class _BaseChild[D: MLIR, C]:
    __slots__ = ()

    def _into_iter(self, parent: D, /) -> Iterator[C]:
        raise NotImplementedError

    def iter_children(self, entries: DefsEntries[D], /) -> ChildIter[D, C]:
        for name, defn in entries:
            children = self._into_iter(defn.inner)
            if first := next(children, None):
                yield (name, defn), prepend(first, children)


class ChildAlways(_BaseChild[MLIR, MLIR]):
    __slots__ = ()

    def __repr__(self) -> str:
        return "child.always()"

    def _into_iter(self, parent: MLIR, /) -> Iterator[MLIR]:
        return parent.iter_children()


class ChildIncludeNodes(_BaseChild[MLIR, MLIR]):
    __slots__ = ("types",)

    def __repr__(self) -> str:
        return f"child.node.is_in{_ordered_args(tp.__name__ for tp in self.types)}"

    def __init__(self, incl: Child, excl: Child, /) -> None:
        self.types: tuple[type[MLIR], ...] = _convert_nodes(incl, excl)

    def _into_iter(self, parent: MLIR, /) -> Iterator[MLIR]:
        types = self.types
        return (child for child in parent.iter_children() if isinstance(child, types))


class AlwaysFieldNames(_BaseChild[HasFields, tuple[str, mlir.Field]]):
    __slots__ = ()

    def __repr__(self) -> str:
        return "field_names.always()"

    def _into_iter(self, parent: HasFields, /) -> Iterator[tuple[str, mlir.Field]]:
        return parent.iter_fields_items()


class IncludeFieldNames(_BaseChild[HasFields, tuple[str, mlir.Field]]):
    __slots__ = ("names",)
    names: frozenset[str]

    def __repr__(self) -> str:
        return f"field_names.is_in{_ordered_args(self.names)}"

    def __init__(self, names: frozenset[str], /) -> None:
        self.names = names

    def _into_iter(self, parent: HasFields, /) -> Iterator[tuple[str, mlir.Field]]:
        return select_items(parent.fields, self.names, allow_missing=True)


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


def _convert_nodes(incl: NamesNodes | Child, excl: NamesNodes | Child, /) -> tuple[type[MLIR], ...]:
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
_FIELD_ALWAYS: Final = AlwaysFieldNames()
