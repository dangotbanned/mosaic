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
from typing import TYPE_CHECKING, Literal, Protocol, TypeAlias, TypedDict, TypeVar

if TYPE_CHECKING:
    from collections.abc import Collection, Sequence

    from typing_extensions import Self, Unpack


ParamRef: TypeAlias = str
"""`$${string}`."""

_Select: TypeAlias = Literal["crossfilter", "intersect", "single", "union"]
"""The type of reactive parameter.

One of:
- `"intersect"` for a `Selection` that intersects clauses (logical "and")
- `"union"` for a `Selection` that unions clauses (logical "or")
- `"single"` for a `Selection` that retains a single clause only
- `"crossfilter"` for a cross-filtered intersection `Selection`
"""

Select: TypeAlias = Literal["value"] | _Select


class ParamBase(Protocol):
    """Base properties shared by Param definitions."""

    select: Select
    """The type of reactive parameter."""

    @property
    def name(self) -> ParamRef:
        """Either `"name"` or `"$name"`.

        Help me!
        """
        ...


NumericLiteral: TypeAlias = int | float
TemporalLiteral: TypeAlias = dt.date | dt.datetime | dt.time
ParamLiteral: TypeAlias = str | NumericLiteral | bool | None
"""Literal Param values."""


class Param(ParamBase, Protocol):
    """A Param definition."""

    @property
    def value(self) -> ParamLiteral:
        """The initial parameter value."""


class ParamArray(ParamBase, Protocol):
    @property
    def value(self) -> Sequence[ParamLiteral | ParamRef]:
        """The initial parameter values."""
        ...


_T = TypeVar("_T", bound=TemporalLiteral, covariant=True)
ISO_8601: TypeAlias = str


class ParamTemporal(ParamBase, Protocol[_T]):
    """A Temporal-valued Param definition."""

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


class Selection(Protocol):
    select: _Select
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
    def name(self) -> ParamRef: ...

    @classmethod
    def _from_options(cls, select: _Select, /, kwds: _SelectionOpts) -> Self:
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


ParamDef: TypeAlias = Param | ParamArray | ParamTemporal[TemporalLiteral] | Selection
"""A Param or Selection definition."""

IntoParamRef: TypeAlias = ParamDef | ParamRef
"""Anything that can be resolved into a `ParamRef`."""

Params: TypeAlias = dict[str, ParamDef]
"""Top-level Param and Selection definitions."""
