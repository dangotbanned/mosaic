# Generated: `mosaic_spec._gen.plot_legend`
from __future__ import annotations

from typing import TYPE_CHECKING, Literal as L

from mosaic_spec._typing_compat import Required, TypedDict

if TYPE_CHECKING:
    from mosaic_spec._gen.params import ParamRef


class _LegendOpen(TypedDict, total=False):
    """A legend defined as a top-level spec component."""

    bind: ParamRef
    """The output selection. If specified, the legend is interactive, using a `toggle` interaction for discrete legends or an `intervalX` interaction for continuous legends."""
    columns: float
    """The number of columns to use to layout a discrete legend."""
    field: str
    """The data field over which to generate output selection clauses. If unspecified, a matching field is retrieved from existing plot marks."""
    height: float
    """The height of a continuous legend, in pixels."""
    label: str
    """The legend label."""
    legend: Required[L["color", "opacity", "symbol"]]
    """A legend of the given type. The valid types are `"color"`, `"opacity"`, and `"symbol"`."""
    margin_bottom: float
    """The bottom margin of the legend component, in pixels."""
    margin_left: float
    """The left margin of the legend component, in pixels."""
    margin_right: float
    """The right margin of the legend component, in pixels."""
    margin_top: float
    """The top margin of the legend component, in pixels."""
    plot: Required[str]
    """The name of the plot this legend applies to. A plot must include a `name` attribute to be referenced."""
    tick_size: float
    """The size of legend ticks in a continuous legend, in pixels."""
    width: float
    """The width of a continuous legend, in pixels."""


class PlotLegend(TypedDict, total=False, closed=True):
    """A legend defined as an entry within a plot."""

    bind: ParamRef
    """The output selection. If specified, the legend is interactive, using a `toggle` interaction for discrete legends or an `intervalX` interaction for continuous legends."""
    columns: float
    """The number of columns to use to layout a discrete legend."""
    field: str
    """The data field over which to generate output selection clauses. If unspecified, a matching field is retrieved from existing plot marks."""
    height: float
    """The height of a continuous legend, in pixels."""
    label: str
    """The legend label."""
    legend: Required[L["color", "opacity", "symbol"]]
    """A legend of the given type. The valid types are `"color"`, `"opacity"`, and `"symbol"`."""
    margin_bottom: float
    """The bottom margin of the legend component, in pixels."""
    margin_left: float
    """The left margin of the legend component, in pixels."""
    margin_right: float
    """The right margin of the legend component, in pixels."""
    margin_top: float
    """The top margin of the legend component, in pixels."""
    tick_size: float
    """The size of legend ticks in a continuous legend, in pixels."""
    width: float
    """The width of a continuous legend, in pixels."""


class Legend(_LegendOpen, total=False, closed=True): ...


__all__ = ("Legend", "PlotLegend")
