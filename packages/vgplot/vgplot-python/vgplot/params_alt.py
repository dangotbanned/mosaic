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

import datetime as dt
from collections.abc import Collection, Sequence
from typing import (
    TYPE_CHECKING,
    Final,
    Generic,
    Literal,
    Protocol,
    TypeAlias,
    TypedDict,
    TypeVar,
    final,
    overload,
)

if TYPE_CHECKING:
    from typing_extensions import Self, Unpack


Name: TypeAlias = str
"""`{name}`"""

Ref: TypeAlias = str
"""`${name}`"""

Select: TypeAlias = Literal["crossfilter", "intersect", "single", "union"]
"""The type of reactive parameter.

One of:
- `"intersect"` for a `Selection` that intersects clauses (logical "and")
- `"union"` for a `Selection` that unions clauses (logical "or")
- `"single"` for a `Selection` that retains a single clause only
- `"crossfilter"` for a cross-filtered intersection `Selection`
"""

_SelectT = TypeVar("_SelectT", bound=Select | Literal["value"])


# TODO @dangotbanned: If keeping the protocol, make `name` an attribute
# TODO @dangotbanned: Add `{crossfilter, intersect, single, union}` methods, e.g.
#   `def union(self, *extra_include: ParamDef, **kwds: Unpack[_SelectionOptsBase]) -> Selection: ...`
# TODO @dangotbanned: Add `to_dict`, `to_json`
class ParamBase(Protocol[_SelectT]):
    """Base properties shared by Param definitions."""

    __slots__ = ()

    select: _SelectT
    """The type of reactive parameter."""

    @property
    def name(self) -> Name:
        """The name of the parameter."""
        ...

    def __repr__(self) -> Ref:
        """Interpolate the parameter in a query."""
        return f"${self.name}"

    def to_param_ref(self) -> ParamRef:
        return ParamRef(self.name)


NumericLit: TypeAlias = int | float
TemporalLit: TypeAlias = dt.date | dt.datetime | dt.time
ParamLit: TypeAlias = str | NumericLit | bool | None
"""Literal Param values."""

NonNestedLit: TypeAlias = ParamLit | TemporalLit

_TemporalT = TypeVar("_TemporalT", bound=TemporalLit, covariant=True)
ISO_8601: TypeAlias = str


# TODO @dangotbanned: De-dup with `@dataclass(frozen=True, slots=True, repr=False)`
@final
class Param(ParamBase[Literal["value"]]):
    """A Param definition."""

    __slots__ = ("_name", "_value")
    select = "value"

    @property
    def name(self) -> Name:
        return self._name

    @property
    def value(self) -> ParamLit:
        """The initial parameter value."""
        return self._value

    def __init__(self, name: Name, value: ParamLit) -> None:
        self._name: Name = name
        self._value: ParamLit = value


# TODO @dangotbanned: De-dup with `@dataclass(frozen=True, slots=True, repr=False)`
# TODO @dangotbanned: Use a tuple for internal storage, so it stays hashable
#  - accept Sequence on entry
#  - convert to list (if needed) for json
@final
class ParamArray(ParamBase[Literal["value"]]):
    __slots__ = ("_name", "_value")
    select = "value"

    @property
    def name(self) -> Name:
        return self._name

    @property
    def value(self) -> Sequence[ParamLit | ParamRef]:
        """The initial parameter values."""
        return self._value

    def __init__(self, name: Name, value: Sequence[ParamLit | ParamRef]) -> None:
        self._name: Name = name
        self._value: Sequence[ParamLit | ParamRef] = value


# TODO @dangotbanned: De-dup with `@dataclass(frozen=True, slots=True, repr=False)`
@final
class ParamTemporal(ParamBase[Literal["value"]], Generic[_TemporalT]):
    """A Temporal-valued Param definition."""

    __slots__ = ("_name", "_value")
    select = "value"

    @property
    def name(self) -> Name:
        return self._name

    @property
    def value(self) -> _TemporalT:
        """The initial parameter value."""
        return self._value

    def __init__(self, name: Name, value: _TemporalT) -> None:
        self._name: Name = name
        self._value: _TemporalT = value

    @property
    def date(self) -> ISO_8601:
        """Convert to an ISO date/time string to be parsed to a Date object."""
        # TODO @dangotbanned: Raise a ty issue?
        # all 3 signatures allow 0-args, return type is the same
        return self.value.isoformat()  # ty: ignore[invalid-argument-type]


class _SelectionOptsBase(TypedDict, total=False):
    cross: bool
    """A flag for cross-filtering, where selections made in a plot filter others but not oneself.

    (default `False`, except for `crossfilter` selections).
    """

    empty: bool
    """A flag for setting an initial empty selection state.

    - If `True`, a selection with no clauses corresponds to an empty selection with no records.
    - If `False`, a selection with no clauses selects all values.
    """


class SelectionOpts(_SelectionOptsBase, total=False):
    # NOTE: user-facing version with permissive include
    include: IntoParamRef | Collection[IntoParamRef]
    """Upstream selections whose clauses should be included as part of this selection.

    Any clauses or activations published to the upstream selections will be relayed to this selection.
    """


class _SelectionOpts(_SelectionOptsBase, total=False):
    # NOTE: internal version with normalized include
    include: Sequence[ParamRef]
    """Upstream selections whose clauses should be included as part of this selection.

    Any clauses or activations published to the upstream selections will be relayed to this selection.
    """


# TODO @dangotbanned: Need something ergonomic for naming
# TODO @dangotbanned: De-dup with `@dataclass(frozen=True, slots=True, repr=False)`
@final
class Selection(ParamBase[Select]):
    __slots__ = ("_name", "opts", "select")
    select: Select
    """The type of reactive parameter."""

    opts: _SelectionOpts

    @property
    def name(self) -> Name:
        msg = "TODO @dangotbanned: figure out naming for these guys"
        raise NotImplementedError(msg)

    def __init__(self, select: Select, /, kwds: _SelectionOpts) -> None:
        self.select = select
        self.opts = kwds

    @classmethod
    def _from_options(cls, select: Select, /, kwds: SelectionOpts) -> Self:
        opts: _SelectionOpts = {}
        if (cross := kwds.get("cross")) is not None:
            opts["cross"] = cross
        if (empty := kwds.get("empty")) is not None:
            opts["empty"] = empty
        if include := kwds.get("include"):
            opts["include"] = (
                (include.to_param_ref(),)
                if not isinstance(include, Collection)
                else tuple(param.to_param_ref() for param in include)
            )
        return cls(select, opts)

    @classmethod
    def intersect(cls, **kwds: Unpack[SelectionOpts]) -> Self:
        return cls._from_options("intersect", kwds)

    @classmethod
    def crossfilter(cls, **kwds: Unpack[SelectionOpts]) -> Self:
        return cls._from_options("crossfilter", kwds)

    @classmethod
    def union(cls, **kwds: Unpack[SelectionOpts]) -> Self:
        return cls._from_options("union", kwds)

    @classmethod
    def single(cls, **kwds: Unpack[SelectionOpts]) -> Self:
        return cls._from_options("single", kwds)


ParamDef: TypeAlias = Param | ParamArray | ParamTemporal[TemporalLit] | Selection
"""A Param or Selection definition."""


Params: TypeAlias = dict[str, ParamDef]
"""Top-level Param and Selection definitions."""


def sql(expr: str) -> str:
    return expr


# TODO @dangotbanned: Consider replacing this level
# - if we need to store a ref, use the `name`
# - if this is a mid-builder step, return a callable Protocol from __getattr__
#   - that protocol will be incompatible with the `ParamDef`
# - if we want to reference a parameter, the parameter will support converting as needed
@final
class ParamRef:
    """A reference to a parameter."""

    __slots__ = ("_name",)

    def __init__(self, name: Name, /) -> None:
        self._name: Final[Name] = name

    def __eq__(self, other: object) -> bool:
        if type(other) is ParamRef:
            return other._name == self._name
        return NotImplemented

    def __hash__(self) -> int:
        return hash((ParamRef, self._name))

    def __repr__(self) -> Ref:
        return f"${self._name}"

    def to_param_ref(self) -> ParamRef:
        return self

    @overload
    def __call__(self, value: ParamLit = None, /) -> Param: ...
    @overload
    def __call__(self, value: _TemporalT, /) -> ParamTemporal[_TemporalT]: ...
    @overload
    def __call__(self, value: Sequence[ParamLit | ParamRef], /) -> ParamArray: ...
    def __call__(
        self, value: ParamLit | _TemporalT | Sequence[ParamLit | ParamRef] = None, /
    ) -> Param | ParamArray | ParamTemporal[_TemporalT]:
        """Initialize a param with a value."""
        name = self._name
        if isinstance(value, Sequence):
            if not isinstance(value, str):
                return ParamArray(name, value)  # ty: ignore[invalid-argument-type]
        elif isinstance(value, (dt.date, dt.datetime, dt.time)):
            return ParamTemporal(name, value)
        return Param(name, value)


IntoParamRef: TypeAlias = ParamDef | ParamRef
"""Anything that can be resolved into a `ParamRef`."""


class _ParamBuilder:
    def __getattr__(self, name: Name) -> ParamRef:
        """Create a `Param`/`ParamRef`."""
        return ParamRef(name)


p = _ParamBuilder()
"""Create a `Param`/`ParamRef`."""


# ruff: noqa: F841
def ctx() -> None:
    point = p.point(dt.date(2013, 5, 13))

    y = sql(
        f"Close / (SELECT max(Close) FROM stocks WHERE Symbol = source.Symbol AND Date = {p.point})"
    )
    selection = Selection

    array_1 = p.array_1((1, 2, 3))
    time_1 = p.time(dt.time(12, 30))
    date_1 = p.date(dt.date(1970, 1, 2))
    datetime_1 = p.datetime(dt.datetime(1970, 1, 2, 12, 30))

    param_sel_1 = selection.intersect()
    param_sel_2 = selection.union(empty=False, include=[time_1, date_1])
    param_sel_3 = selection.crossfilter(include=p.lit_1(1))
    param_sel_4 = selection.crossfilter(include=(array_1, datetime_1))
    param_sel_5 = selection.single(cross=True, include=p.date(dt.date(1970, 1, 2)))
