# Generated: `mosaic_spec._gen.params`
from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Literal as L

from mosaic_spec._typing_compat import Required, TypeAliasType, TypedDict


class ParamDate(TypedDict, total=False, closed=True):
    """A Date-valued Param definition."""

    date: Required[str]
    """The initial parameter value as an ISO date/time string to be parsed to a Date object."""
    select: L["value"]
    """The type of reactive parameter. One of:
    - `"value"` (default) for a standard `Param`
    - `"intersect"` for a `Selection` that intersects clauses (logical "and")
    - `"union"` for a `Selection` that unions clauses (logical "or")
    - `"single"` for a `Selection` that retains a single clause only
    - `"crossfilter"` for a cross-filtered intersection `Selection`
    """


ParamLiteral = TypeAliasType("ParamLiteral", bool | float | str | None)
"""Literal Param values."""
ParamRef = TypeAliasType("ParamRef", str)
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
    select: Required[L["crossfilter", "intersect", "single", "union"]]
    """The type of reactive parameter. One of:
    - `"value"` (default) for a standard `Param`
    - `"intersect"` for a `Selection` that intersects clauses (logical "and")
    - `"union"` for a `Selection` that unions clauses (logical "or")
    - `"single"` for a `Selection` that retains a single clause only
    - `"crossfilter"` for a cross-filtered intersection `Selection`
    """


class Param(TypedDict, total=False, closed=True):
    """A Param definition."""

    select: L["value"]
    """The type of reactive parameter. One of:
    - `"value"` (default) for a standard `Param`
    - `"intersect"` for a `Selection` that intersects clauses (logical "and")
    - `"union"` for a `Selection` that unions clauses (logical "or")
    - `"single"` for a `Selection` that retains a single clause only
    - `"crossfilter"` for a cross-filtered intersection `Selection`
    """
    value: Required[ParamValue]
    """The initial parameter value."""


ParamDefinition = TypeAliasType("ParamDefinition", Param | ParamDate | ParamValue | Selection)
"""A Param or Selection definition."""
Params = TypeAliasType("Params", Mapping[str, ParamDefinition])
"""Top-level Param and Selection definitions."""


__all__ = (
    "Param",
    "ParamDate",
    "ParamDefinition",
    "ParamLiteral",
    "ParamRef",
    "ParamValue",
    "Params",
    "Selection",
)
