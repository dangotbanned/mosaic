# Generated: `mosaic_spec._gen.plot_from`
from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from mosaic_spec._typing_compat import Required, TypeAliasType, TypedDict

if TYPE_CHECKING:
    from mosaic_spec._gen.params import ParamRef

PlotDataInline = TypeAliasType("PlotDataInline", Sequence[Any])
"""An array of inline data values to visualize. As this data does not come from a database, it can not be filtered by interactive selections."""


class PlotFrom(TypedDict, total=False, closed=True):
    """Input data specification for a plot mark."""

    filter_by: ParamRef
    """A selection that filters the mark data."""
    optimize: bool
    """A flag (default `true`) to enable any mark-specific query optimizations. If `false`, optimizations are disabled to aid testing and debugging."""
    source: Required[ParamRef | str]
    """The name of the backing data table."""


PlotMarkData = TypeAliasType("PlotMarkData", PlotDataInline | PlotFrom)
"""Input data for a marks"""


__all__ = ("PlotDataInline", "PlotFrom", "PlotMarkData")
