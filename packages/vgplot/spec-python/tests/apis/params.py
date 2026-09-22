"""A typing-first counterpart to `params.py`.

Mostly doing as a learning/experimental exercise.

If this were the direction to go in, it could be (at least partially) generated from the spec.

## Notes/Changes
- `Protocol`s mostly aligned with `Param.ts` interfaces
- `ParamTemporal` is equivalent to `ParamDate`
    - but unparsing is on demand
- `selection` is gone
    - You can get the same API by creating a module named `selection`,
      and aliasing the classmethods

## Planned
- Implement the protocols
- Experiment with simpler ways to handle parameter names
    - [`inspect.currentframe`] is heavy machinery and can cause reference cycles

[`inspect.currentframe`]: https://docs.python.org/3/library/inspect.html#the-interpreter-stack
"""

from __future__ import annotations

# pyright: reportUnusedVariable=false
import datetime as dt
from collections.abc import Collection
from typing import TYPE_CHECKING, Final, Generic, Literal as L, NewType, final, overload

import mosaic_spec as ms
from mosaic_spec import ParamLiteral as Lit, ParamRef as Ref
from mosaic_spec._typing_compat import Protocol, Self, TypeAliasType, TypedDict, TypeVar, Unpack

if TYPE_CHECKING:
    from tests.apis.data import ParamSource
    from tests.apis.inputs import Menu, MenuOptions

Temporal = TypeAliasType("Temporal", dt.date | dt.datetime | dt.time)

_TP_LIT: Final = (int, str, float, type(None))
ISO_8601 = NewType("ISO_8601", str)


class CanRef(Protocol):
    __slots__ = ()

    def __repr__(self) -> Ref: ...
    def ref(self) -> Ref: ...


class ParamBase(CanRef, Protocol):
    """Base properties shared by Param definitions."""

    __slots__ = ("name",)

    name: str
    """The name of the parameter."""

    def __repr__(self) -> Ref:
        """Interpolate the parameter in a query."""
        return Ref(f"${self.name}")

    def ref(self) -> Ref:
        # NOTE: `ParamRef` should not be a user-facing concept
        # - parameters become references when you refer to them
        return Ref(f"${self.name}")

    def to_dict(self) -> ms.Params: ...


_ValueT = TypeVar("_ValueT", covariant=True)


class _ParamValue(ParamBase, Generic[_ValueT]):
    """A Param that wraps a value."""

    __slots__ = ("value",)
    value: _ValueT
    """The initial parameter value."""

    def __init__(self, name: str, value: _ValueT) -> None:
        self.name = name
        self.value = value


# TODO @dangotbanned: De-dup with `@dataclass(frozen=True, slots=True, repr=False)`
@final
class Param(_ParamValue[Lit]):
    """A Param definition."""

    __slots__ = ()

    def to_dict(self) -> ms.Params:
        return {self.name: self.value}

    @property
    def _source(self) -> Ref:
        return self.ref()

    def source(
        self, filter_by: ParamDef | None = None, *, optimize: L[False] | None = None
    ) -> ParamSource:
        """Create an input data specification for a plot mark."""
        from tests.apis.data import ParamSource

        return ParamSource(self, filter_by, optimize=optimize)

    def menu(
        self, into: L["bind", "filter_by"] = "bind", /, **options: Unpack[MenuOptions]
    ) -> Menu:
        """Create a menu input widget, passing this param `into` either `bind` or `filter_by`.

        >>> unit = p.Unit(10)
        >>> unit.menu(options=[1, 2, 5, 10, 25, 50, 100])
        Menu({'options': [1, 2, 5, 10, 25, 50, 100], 'bind': $Unit}

        >>> p.predicate(False).menu("filter_by", options=[False, True])
        Menu({'options': [False, True], 'filter_by': $predicate}
        """
        from tests.apis.inputs import Menu

        options[into] = self
        return Menu(**options)


# TODO @dangotbanned: De-dup with `@dataclass(frozen=True, slots=True, repr=False)`
@final
class ParamArray(_ParamValue[tuple["Lit | ParamDef", ...]]):
    """An Array-valued Param definition."""

    __slots__ = ()

    def to_dict(self) -> ms.Params:
        param_defs = {}
        values = []
        for value in self.value:
            if isinstance(value, _TP_PARAM_DEF):
                param_defs.update(value.to_dict())
                v = value.ref()
            else:
                v = value
            values.append(v)
        param_defs[self.name] = values
        return param_defs


_TemporalT = TypeVar("_TemporalT", bound=Temporal, covariant=True)


# TODO @dangotbanned: De-dup with `@dataclass(frozen=True, slots=True, repr=False)`
@final
class ParamTemporal(_ParamValue[_TemporalT]):
    """A Temporal-valued Param definition."""

    __slots__ = ()

    def to_dict(self) -> dict[str, ms.ParamDate]:
        # TODO @dangotbanned: Raise a ty issue?
        # all 3 signatures allow 0-args, return type is the same
        date = ISO_8601(self.value.isoformat())  # ty: ignore[invalid-argument-type]
        return {self.name: {"date": date}}


class _CrossEmptyOpen(TypedDict, total=False):
    cross: bool
    """A flag for cross-filtering, where selections made in a plot filter others but not oneself.

    (default `False`, except for `crossfilter` selections).
    """

    empty: bool
    """A flag for setting an initial empty selection state.

    - If `True`, a selection with no clauses corresponds to an empty selection with no records.
    - If `False`, a selection with no clauses selects all values.
    """


class _CrossEmpty(_CrossEmptyOpen, closed=True): ...


# NOTE: user-facing version with permissive include
class SelectionOpts(_CrossEmptyOpen, total=False, closed=True):
    include: ParamDef | Collection[ParamDef]
    """Upstream selections whose clauses should be included as part of this selection.

    Any clauses or activations published to the upstream selections will be relayed to this selection.
    """


Select = L["crossfilter", "intersect", "single", "union"]
"""The type of reactive parameter."""


# TODO @dangotbanned: De-dup with `@dataclass(frozen=True, slots=True, repr=False)`
@final
class Selection(ParamBase):
    """A Selection definition."""

    __slots__ = ("include", "kwds", "select")
    select: Select
    """The type of reactive parameter."""

    kwds: _CrossEmpty
    include: tuple[ParamDef, ...]

    def __init__(
        self, name: str, select: Select, /, kwds: _CrossEmpty, include: tuple[ParamDef, ...] = ()
    ) -> None:
        self.select = select
        self.kwds = kwds
        self.name = name
        self.include = include

    @classmethod
    def _from_options(cls, name: str, select: Select, /, kwds: SelectionOpts) -> Self:
        opts: _CrossEmpty = {}
        if (cross := kwds.get("cross")) is not None:
            opts["cross"] = cross
        if (empty := kwds.get("empty")) is not None:
            opts["empty"] = empty
        if include := kwds.get("include"):
            incl = (include,) if not isinstance(include, Collection) else tuple(include)
            return cls(name, select, opts, incl)
        return cls(name, select, opts)

    def to_dict(self) -> ms.Params:
        self_dict: ms.Selection = {"select": self.select, **self.kwds}
        if include := self.include:
            param_defs = {}
            param_refs = []
            for param in include:
                param_defs.update(param.to_dict())
                param_refs.append(param.ref())
            self_dict["include"] = param_refs
            param_defs[self.name] = self_dict
            return param_defs
        return {self.name: self_dict}

    def menu(
        self, into: L["bind", "filter_by"] = "bind", /, **options: Unpack[MenuOptions]
    ) -> Menu:
        """Create a menu input widget, passing this selection `into` either `bind` or `filter_by`.

        >>> p.query.cross().menu(column="partial_t", label="Partial t")
        Menu({'column': 'partial_t', 'label': 'Partial t', 'bind': $query}
        """
        from tests.apis.inputs import Menu

        options[into] = self
        return Menu(**options)


ParamDef = TypeAliasType("ParamDef", Param | ParamArray | ParamTemporal[Temporal] | Selection)
"""A Param or Selection definition."""

_TP_PARAM_DEF: Final = Param, ParamArray, ParamTemporal, Selection


@final
class _ParamBuilder:
    """A partially initialized param.

    To create a parameter, call with an optional default value.

    To create a selection, call either `single`, `union`, `cross` or `intersect` methods.
    """

    __slots__ = ("_name",)

    def __init__(self, name: str, /) -> None:
        self._name: Final[str] = name

    @overload
    def __call__(self, value: Lit = None, /) -> Param: ...
    @overload
    def __call__(self, value: _TemporalT, /) -> ParamTemporal[_TemporalT]: ...
    @overload
    def __call__(self, value: Collection[Lit | ParamDef], /) -> ParamArray: ...
    def __call__(
        self, value: Lit | _TemporalT | Collection[Lit | ParamDef] = None, /
    ) -> Param | ParamArray | ParamTemporal[_TemporalT]:
        """Initialize a param with a value."""
        name = self._name
        if not isinstance(value, _TP_LIT):
            if not isinstance(value, (dt.date, dt.datetime, dt.time)):
                return ParamArray(name, tuple(value))
            if isinstance(value, Collection):
                raise TypeError

            return ParamTemporal(name, value)
        return Param(name, value)

    def single(self, **kwds: Unpack[SelectionOpts]) -> Selection:
        return Selection._from_options(self._name, "single", kwds)

    def cross(self, **kwds: Unpack[SelectionOpts]) -> Selection:
        return Selection._from_options(self._name, "crossfilter", kwds)

    def union(self, **kwds: Unpack[SelectionOpts]) -> Selection:
        return Selection._from_options(self._name, "union", kwds)

    def intersect(self, **kwds: Unpack[SelectionOpts]) -> Selection:
        return Selection._from_options(self._name, "intersect", kwds)


@final
class _P:
    __slots__ = ()

    def __getattr__(self, name: str) -> _ParamBuilder:
        return _ParamBuilder(name)


p: Final = _P()
"""Create a `Param` or `Selection`."""


def sql(expr: str) -> str:
    return expr


# ruff: noqa: F841
def ctx() -> None:
    point = p.point(dt.date(2013, 5, 13))

    y = sql(
        f"Close / (SELECT max(Close) FROM stocks WHERE Symbol = source.Symbol AND Date = {p.point})"  # ruff: ignore[hardcoded-sql-expression]
    )

    array_1 = p.array_1((1, 2, 3))
    time_1 = p.time(dt.time(12, 30))
    date_1 = p.date(dt.date(1970, 1, 2))
    datetime_1 = p.datetime(dt.datetime(1970, 1, 2, 12, 30))

    # NOTE: `athletes.py` example
    category = p.category.intersect()
    query = p.query.intersect(include=category)
    hover = p.hover.intersect(empty=True)

    param_sel_2 = p.union.union(empty=False, include=[time_1, date_1])
    param_sel_5 = p.single.single(cross=True, include=p.date(dt.date(1970, 1, 2)))
