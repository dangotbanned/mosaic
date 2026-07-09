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
from typing import (
    TYPE_CHECKING,
    Final,
    Literal,
    Protocol,
    TypeAlias,
    TypedDict,
    TypeVar,
    final,
    overload,
)

if TYPE_CHECKING:
    from collections.abc import Collection, Sequence

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


class ParamBase(Protocol[_SelectT]):
    """Base properties shared by Param definitions."""

    select: _SelectT
    """The type of reactive parameter."""

    @property
    def name(self) -> Name:
        """The name of the parameter."""
        ...

    def __repr__(self) -> Ref:
        """Interpolate the parameter in a query."""
        return f"${self.name}"


NumericLit: TypeAlias = int | float
TemporalLit: TypeAlias = dt.date | dt.datetime | dt.time
ParamLit: TypeAlias = str | NumericLit | bool | None
"""Literal Param values."""

NonNestedLit: TypeAlias = ParamLit | TemporalLit

_T = TypeVar("_T", bound=TemporalLit, covariant=True)
ISO_8601: TypeAlias = str


class Param(ParamBase[Literal["value"]], Protocol):
    """A Param definition."""

    select = "value"

    @property
    def value(self) -> ParamLit:
        """The initial parameter value."""


class ParamArray(ParamBase[Literal["value"]], Protocol):
    select = "value"

    @property
    def value(self) -> Sequence[ParamLit | ParamRef]:
        """The initial parameter values."""
        ...


class ParamTemporal(ParamBase[Literal["value"]], Protocol[_T]):
    """A Temporal-valued Param definition."""

    select = "value"

    @property
    def value(self) -> _T:
        """The initial parameter value."""
        ...

    @property
    def date(self) -> ISO_8601:
        """Convert to an ISO date/time string to be parsed to a Date object."""
        return self.value.isoformat()


class _SelectionOpts(TypedDict, total=False):
    cross: bool
    """A flag for cross-filtering, where selections made in a plot filter others but not oneself.

    (default `False`, except for `crossfilter` selections).
    """

    empty: bool
    """A flag for setting an initial empty selection state.

    - If `True`, a selection with no clauses corresponds to an empty selection with no records.
    - If `False`, a selection with no clauses selects all values.
    """

    include: IntoParamRef | Collection[IntoParamRef]
    """Upstream selections whose clauses should be included as part of this selection.

    Any clauses or activations published to the upstream selections will be relayed to this selection.
    """


class Selection(ParamBase[Select], Protocol):
    select: Select
    """The type of reactive parameter."""

    cross: bool
    """A flag for cross-filtering, where selections made in a plot filter others but not oneself.

    (default `False`, except for `crossfilter` selections).
    """

    empty: bool
    """A flag for setting an initial empty selection state.

    - If `True`, a selection with no clauses corresponds to an empty selection with no records.
    - If `False`, a selection with no clauses selects all values.
    """

    include: Sequence[ParamRef]
    """Upstream selections whose clauses should be included as part of this selection.

    Any clauses or activations published to the upstream selections will be relayed to this selection.
    """

    @property
    def name(self) -> Name: ...

    def __repr__(self) -> Ref:
        msg = "TODO @dangotbanned: figure out naming for these guys"
        raise NotImplementedError(msg)

    @classmethod
    def _from_options(cls, select: Select, /, kwds: _SelectionOpts) -> Self:
        """Normalize `include`."""
        ...

    @classmethod
    def intersect(cls, **kwds: Unpack[_SelectionOpts]) -> Self:
        return cls._from_options("intersect", kwds)

    @classmethod
    def crossfilter(cls, **kwds: Unpack[_SelectionOpts]) -> Self:
        return cls._from_options("crossfilter", kwds)

    @classmethod
    def union(cls, **kwds: Unpack[_SelectionOpts]) -> Self:
        return cls._from_options("union", kwds)

    @classmethod
    def single(cls, **kwds: Unpack[_SelectionOpts]) -> Self:
        return cls._from_options("single", kwds)


ParamDef: TypeAlias = Param | ParamArray | ParamTemporal[TemporalLit] | Selection
"""A Param or Selection definition."""


Params: TypeAlias = dict[str, ParamDef]
"""Top-level Param and Selection definitions."""


def sql(expr: str) -> str:
    return expr


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

    @overload
    def __call__(self, value: ParamLit = None, /) -> Param: ...
    @overload
    def __call__(self, value: TemporalLit, /) -> ParamTemporal[TemporalLit]: ...
    @overload
    def __call__(self, value: Sequence[ParamLit | ParamRef], /) -> ParamArray: ...
    def __call__(
        self, value: NonNestedLit | Sequence[ParamLit | ParamRef] = None, /
    ) -> Param | ParamArray | ParamTemporal[TemporalLit]:
        """Initialize a param with a value."""
        raise NotImplementedError


IntoParamRef: TypeAlias = ParamDef | ParamRef
"""Anything that can be resolved into a `ParamRef`."""


class _ParamBuilder:
    def __getattr__(self, name: Name) -> ParamRef:
        """Create a `Param`/`ParamRef`."""
        raise NotImplementedError


p = _ParamBuilder()
"""Create a `Param`/`ParamRef`."""


# ruff: noqa: F841
def ctx() -> None:
    point = p.point(dt.date(2013, 5, 13))

    y = sql(
        f"Close / (SELECT max(Close) FROM stocks WHERE Symbol = source.Symbol AND Date = {p.point})"
    )
