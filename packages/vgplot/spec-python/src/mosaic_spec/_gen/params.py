# NOTE: DO NOT EDIT.
# Regenerate with: pnpm generate

from __future__ import annotations

from collections.abc import Sequence
from typing import Literal

from mosaic_spec._typing_compat import Required, TypeAliasType, TypedDict
from mosaic_spec.typing import ParamRef


class ParamDate(TypedDict, total=False, closed=True):
    """A Date-valued Param definition."""

    date: Required[str]
    """The initial parameter value as an ISO date/time string to be parsed to a Date object."""
    select: Literal["value"]
    """
    The type of reactive parameter. One of:
    - `"value"` (default) for a standard `Param`
    - `"intersect"` for a `Selection` that intersects clauses (logical "and")
    - `"union"` for a `Selection` that unions clauses (logical "or")
    - `"single"` for a `Selection` that retains a single clause only
    - `"crossfilter"` for a cross-filtered intersection `Selection`
    """


ParamLiteral = TypeAliasType("ParamLiteral", str | float | bool | None)
"""Literal Param values."""


ParamValue = TypeAliasType("ParamValue", ParamLiteral | Sequence[ParamLiteral | ParamRef])
"""Valid Param values."""


class Selection(TypedDict, total=False, closed=True):
    """A Selection definition."""

    cross: bool
    """A flag for cross-filtering, where selections made in a plot filter others but not oneself (default `false`, except for `crossfilter` selections)."""
    empty: bool
    """A flag for setting an initial empty selection state. If true, a selection with no clauses corresponds to an empty selection with no records. If false, a selection with no clauses selects all values."""
    include: ParamRef | Sequence[ParamRef]
    """Upstream selections whose clauses should be included as part of this selection. Any clauses or activations published to the upstream selections will be relayed to this selection."""
    select: Required[Literal["crossfilter", "intersect", "single", "union"]]
    """
    The type of reactive parameter. One of:
    - `"value"` (default) for a standard `Param`
    - `"intersect"` for a `Selection` that intersects clauses (logical "and")
    - `"union"` for a `Selection` that unions clauses (logical "or")
    - `"single"` for a `Selection` that retains a single clause only
    - `"crossfilter"` for a cross-filtered intersection `Selection`
    """


class Param(TypedDict, total=False, closed=True):
    """A Param definition."""

    select: Literal["value"]
    """
    The type of reactive parameter. One of:
    - `"value"` (default) for a standard `Param`
    - `"intersect"` for a `Selection` that intersects clauses (logical "and")
    - `"union"` for a `Selection` that unions clauses (logical "or")
    - `"single"` for a `Selection` that retains a single clause only
    - `"crossfilter"` for a cross-filtered intersection `Selection`
    """
    value: Required[ParamValue]
    """The initial parameter value."""


ParamDefinition = TypeAliasType("ParamDefinition", ParamValue | Param | ParamDate | Selection)
"""A Param or Selection definition."""
