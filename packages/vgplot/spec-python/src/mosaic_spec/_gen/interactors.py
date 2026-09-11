# Generated: `mosaic_spec._gen.interactors`
from __future__ import annotations

from typing import TYPE_CHECKING, Literal as L

from mosaic_spec._typing_compat import Required, TypeAliasType, TypedDict

if TYPE_CHECKING:
    from collections.abc import Sequence

    from mosaic_spec._gen.params import ParamRef


class BrushStyles(TypedDict, total=False, closed=True):
    """Styles for rectangular selection brushes."""

    fill: str
    """The fill color of the brush rectangle."""
    fill_opacity: float
    """The fill opacity of the brush rectangle."""
    opacity: float
    """The overall opacity of the brush rectangle."""
    stroke: str
    """The stroke color of the brush rectangle."""
    stroke_dasharray: str
    """The stroke dash array of the brush rectangle."""
    stroke_opacity: float
    """The stroke opacity of the brush rectangle."""


class Highlight(TypedDict, total=False, closed=True):
    """A highlight interactor."""

    by: Required[ParamRef]
    """The input selection. Unselected marks are deemphasized."""
    fill: str
    """The fill color of deemphasized marks. By default the fill is unchanged."""
    fill_opacity: float
    """The fill opacity of deemphasized marks. By default the fill opacity is unchanged."""
    opacity: float
    """The overall opacity of deemphasized marks. By default the opacity is set to 0.2."""
    select: Required[L["highlight"]]
    """Highlight selected marks by deemphasizing the others."""
    stroke: str
    """The stroke color of deemphasized marks. By default the stroke is unchanged."""
    stroke_opacity: float
    """The stroke opacity of deemphasized marks. By default the stroke opacity is unchanged."""


class NearestX(TypedDict, total=False, closed=True):
    """A nearestX interactor."""

    bind: Required[ParamRef]
    """The output selection. A clause of the form `field = value` is added for the currently nearest value."""
    channels: Sequence[str]
    """The encoding channels whose domain values should be selected. For example, a setting of `['color']` selects the data value backing the color channel, whereas `['x', 'z']` selects both x and z channel domain values. If unspecified, the selected channels default to match the current pointer settings: a `nearestX` interactor selects the `['x']` channels, while a `nearest` interactor selects the `['x', 'y']` channels."""
    fields: Sequence[str]
    """The fields (database column names) to use in generated selection clause predicates. If unspecified, the fields backing the selected *channels* in the first valid prior mark definition are used by default."""
    max_radius: float
    """The maximum radius of a nearest selection (default 40). Marks with (x, y) coordinates outside this radius will not be selected as nearest points."""
    select: Required[L["nearestX"]]
    """Select values from the mark closest to the pointer *x* location."""


class NearestY(TypedDict, total=False, closed=True):
    """A nearestY interactor."""

    bind: Required[ParamRef]
    """The output selection. A clause of the form `field = value` is added for the currently nearest value."""
    channels: Sequence[str]
    """The encoding channels whose domain values should be selected. For example, a setting of `['color']` selects the data value backing the color channel, whereas `['x', 'z']` selects both x and z channel domain values. If unspecified, the selected channels default to match the current pointer settings: a `nearestX` interactor selects the `['x']` channels, while a `nearest` interactor selects the `['x', 'y']` channels."""
    fields: Sequence[str]
    """The fields (database column names) to use in generated selection clause predicates. If unspecified, the fields backing the selected *channels* in the first valid prior mark definition are used by default."""
    max_radius: float
    """The maximum radius of a nearest selection (default 40). Marks with (x, y) coordinates outside this radius will not be selected as nearest points."""
    select: Required[L["nearestY"]]
    """Select values from the mark closest to the pointer *y* location."""


class Pan(TypedDict, total=False, closed=True):
    """A pan interactor."""

    select: Required[L["pan"]]
    """Pan a plot along both the `x` and `y` scales."""
    x: ParamRef
    """The output selection for the `x` domain. A clause of the form `field BETWEEN x1 AND x2` is added for the current pan/zom interval [x1, x2]."""
    xfield: str
    """The name of the field (database column) over which the `x`-component of the pan/zoom interval should be defined. If unspecified, the `x` channel field of the first valid prior mark definition is used."""
    y: ParamRef
    """The output selection for the `y` domain. A clause of the form `field BETWEEN y1 AND y2` is added for the current pan/zom interval [y1, y2]."""
    yfield: str
    """The name of the field (database column) over which the `y`-component of the pan/zoom interval should be defined. If unspecified, the `y` channel field of the first valid prior mark definition is used."""


class PanX(TypedDict, total=False, closed=True):
    """A panX interactor."""

    select: Required[L["panX"]]
    """Pan a plot along the `x` scale only."""
    x: ParamRef
    """The output selection for the `x` domain. A clause of the form `field BETWEEN x1 AND x2` is added for the current pan/zom interval [x1, x2]."""
    xfield: str
    """The name of the field (database column) over which the `x`-component of the pan/zoom interval should be defined. If unspecified, the `x` channel field of the first valid prior mark definition is used."""
    y: ParamRef
    """The output selection for the `y` domain. A clause of the form `field BETWEEN y1 AND y2` is added for the current pan/zom interval [y1, y2]."""
    yfield: str
    """The name of the field (database column) over which the `y`-component of the pan/zoom interval should be defined. If unspecified, the `y` channel field of the first valid prior mark definition is used."""


class PanY(TypedDict, total=False, closed=True):
    """A panY interactor."""

    select: Required[L["panY"]]
    """Pan a plot along the `y` scale only."""
    x: ParamRef
    """The output selection for the `x` domain. A clause of the form `field BETWEEN x1 AND x2` is added for the current pan/zom interval [x1, x2]."""
    xfield: str
    """The name of the field (database column) over which the `x`-component of the pan/zoom interval should be defined. If unspecified, the `x` channel field of the first valid prior mark definition is used."""
    y: ParamRef
    """The output selection for the `y` domain. A clause of the form `field BETWEEN y1 AND y2` is added for the current pan/zom interval [y1, y2]."""
    yfield: str
    """The name of the field (database column) over which the `y`-component of the pan/zoom interval should be defined. If unspecified, the `y` channel field of the first valid prior mark definition is used."""


class PanZoom(TypedDict, total=False, closed=True):
    """A panZoom interactor."""

    select: Required[L["panZoom"]]
    """Pan and zoom a plot along both the `x` and `y` scales."""
    x: ParamRef
    """The output selection for the `x` domain. A clause of the form `field BETWEEN x1 AND x2` is added for the current pan/zom interval [x1, x2]."""
    xfield: str
    """The name of the field (database column) over which the `x`-component of the pan/zoom interval should be defined. If unspecified, the `x` channel field of the first valid prior mark definition is used."""
    y: ParamRef
    """The output selection for the `y` domain. A clause of the form `field BETWEEN y1 AND y2` is added for the current pan/zom interval [y1, y2]."""
    yfield: str
    """The name of the field (database column) over which the `y`-component of the pan/zoom interval should be defined. If unspecified, the `y` channel field of the first valid prior mark definition is used."""


class PanZoomX(TypedDict, total=False, closed=True):
    """A panZoomX interactor."""

    select: Required[L["panZoomX"]]
    """Pan and zoom a plot along the `x` scale only."""
    x: ParamRef
    """The output selection for the `x` domain. A clause of the form `field BETWEEN x1 AND x2` is added for the current pan/zom interval [x1, x2]."""
    xfield: str
    """The name of the field (database column) over which the `x`-component of the pan/zoom interval should be defined. If unspecified, the `x` channel field of the first valid prior mark definition is used."""
    y: ParamRef
    """The output selection for the `y` domain. A clause of the form `field BETWEEN y1 AND y2` is added for the current pan/zom interval [y1, y2]."""
    yfield: str
    """The name of the field (database column) over which the `y`-component of the pan/zoom interval should be defined. If unspecified, the `y` channel field of the first valid prior mark definition is used."""


class PanZoomY(TypedDict, total=False, closed=True):
    """A panZoomY interactor."""

    select: Required[L["panZoomY"]]
    """Pan and zoom a plot along the `y` scale only."""
    x: ParamRef
    """The output selection for the `x` domain. A clause of the form `field BETWEEN x1 AND x2` is added for the current pan/zom interval [x1, x2]."""
    xfield: str
    """The name of the field (database column) over which the `x`-component of the pan/zoom interval should be defined. If unspecified, the `x` channel field of the first valid prior mark definition is used."""
    y: ParamRef
    """The output selection for the `y` domain. A clause of the form `field BETWEEN y1 AND y2` is added for the current pan/zom interval [y1, y2]."""
    yfield: str
    """The name of the field (database column) over which the `y`-component of the pan/zoom interval should be defined. If unspecified, the `y` channel field of the first valid prior mark definition is used."""


class Toggle(TypedDict, total=False, closed=True):
    """A toggle interactor."""

    bind: Required[ParamRef]
    """The output selection. A clause of the form `(field = value1) OR (field = value2) ...` is added for the currently selected values."""
    channels: Required[Sequence[str]]
    """The encoding channels over which to select values. For a selected mark, selection clauses will cover the backing data fields for each channel."""
    peers: bool
    """A flag indicating if peer (sibling) marks are excluded when cross-filtering (default `true`). If set, peer marks will not be filtered by this interactor's selection in cross-filtering setups."""
    select: Required[L["toggle"]]
    """Select individual values."""


class ToggleColor(TypedDict, total=False, closed=True):
    """A toggleColor interactor."""

    bind: Required[ParamRef]
    """The output selection. A clause of the form `(field = value1) OR (field = value2) ...` is added for the currently selected values."""
    peers: bool
    """A flag indicating if peer (sibling) marks are excluded when cross-filtering (default `true`). If set, peer marks will not be filtered by this interactor's selection in cross-filtering setups."""
    select: Required[L["toggleColor"]]
    """Select individual values in the `color` scale domain. Clicking or touching a mark toggles its selection status."""


class ToggleX(TypedDict, total=False, closed=True):
    """A toggleX interactor."""

    bind: Required[ParamRef]
    """The output selection. A clause of the form `(field = value1) OR (field = value2) ...` is added for the currently selected values."""
    peers: bool
    """A flag indicating if peer (sibling) marks are excluded when cross-filtering (default `true`). If set, peer marks will not be filtered by this interactor's selection in cross-filtering setups."""
    select: Required[L["toggleX"]]
    """Select individual values in the `x` scale domain. Clicking or touching a mark toggles its selection status."""


class ToggleY(TypedDict, total=False, closed=True):
    """A toggleY interactor."""

    bind: Required[ParamRef]
    """The output selection. A clause of the form `(field = value1) OR (field = value2) ...` is added for the currently selected values."""
    peers: bool
    """A flag indicating if peer (sibling) marks are excluded when cross-filtering (default `true`). If set, peer marks will not be filtered by this interactor's selection in cross-filtering setups."""
    select: Required[L["toggleY"]]
    """Select individual values in the `y` scale domain. Clicking or touching a mark toggles its selection status."""


class IntervalX(TypedDict, total=False, closed=True):
    """An intervalX interactor."""

    bind: Required[ParamRef]
    """The output selection. A clause of the form `field BETWEEN lo AND hi` is added for the currently selected interval [lo, hi]."""
    brush: BrushStyles
    """CSS styles for the brush (SVG `rect`) element."""
    field: str
    """The name of the field (database column) over which the interval selection should be defined. If unspecified, the  channel field of the first valid prior mark definition is used."""
    peers: bool
    """A flag indicating if peer (sibling) marks are excluded when cross-filtering (default `true`). If set, peer marks will not be filtered by this interactor's selection in cross-filtering setups."""
    pixel_size: float
    """The size of an interactive pixel (default `1`). Larger pixel sizes reduce the brush resolution, which can reduce the size of pre-aggregated materialized views."""
    select: Required[L["intervalX"]]
    """Select a continuous 1D interval selection over the `x` scale domain."""


class IntervalXY(TypedDict, total=False, closed=True):
    """An intervalXY interactor."""

    bind: Required[ParamRef]
    """The output selection. A clause of the form `(xfield BETWEEN x1 AND x2) AND (yfield BETWEEN y1 AND y2)` is added for the currently selected intervals."""
    brush: BrushStyles
    """CSS styles for the brush (SVG `rect`) element."""
    peers: bool
    """A flag indicating if peer (sibling) marks are excluded when cross-filtering (default `true`). If set, peer marks will not be filtered by this interactor's selection in cross-filtering setups."""
    pixel_size: float
    """The size of an interactive pixel (default `1`). Larger pixel sizes reduce the brush resolution, which can reduce the size of pre-aggregated materialized views."""
    select: Required[L["intervalXY"]]
    """Select a continuous 2D interval selection over the `x` and `y` scale domains."""
    xfield: str
    """The name of the field (database column) over which the `x`-component of the interval selection should be defined. If unspecified, the `x` channel field of the first valid prior mark definition is used."""
    yfield: str
    """The name of the field (database column) over which the `y`-component of the interval selection should be defined. If unspecified, the `y` channel field of the first valid prior mark definition is used."""


class IntervalY(TypedDict, total=False, closed=True):
    """An intervalY interactor."""

    bind: Required[ParamRef]
    """The output selection. A clause of the form `field BETWEEN lo AND hi` is added for the currently selected interval [lo, hi]."""
    brush: BrushStyles
    """CSS styles for the brush (SVG `rect`) element."""
    field: str
    """The name of the field (database column) over which the interval selection should be defined. If unspecified, the  channel field of the first valid prior mark definition is used."""
    peers: bool
    """A flag indicating if peer (sibling) marks are excluded when cross-filtering (default `true`). If set, peer marks will not be filtered by this interactor's selection in cross-filtering setups."""
    pixel_size: float
    """The size of an interactive pixel (default `1`). Larger pixel sizes reduce the brush resolution, which can reduce the size of pre-aggregated materialized views."""
    select: Required[L["intervalY"]]
    """Select a continuous 1D interval selection over the `y` scale domain."""


class Region(TypedDict, total=False, closed=True):
    """A rectangular region interactor."""

    bind: Required[ParamRef]
    """The output selection. A clause of the form `(field = value1) OR (field = value2) ...` is added for the currently selected values."""
    brush: BrushStyles
    """CSS styles for the brush (SVG `rect`) element."""
    channels: Required[Sequence[str]]
    """The encoding channels over which to select values. For a selected mark, selection clauses will cover the backing data fields for each channel."""
    peers: bool
    """A flag indicating if peer (sibling) marks are excluded when cross-filtering (default `true`). If set, peer marks will not be filtered by this interactor's selection in cross-filtering setups."""
    select: Required[L["region"]]
    """Select aspects of individual marks within a 2D range."""


PlotInteractor = TypeAliasType(
    "PlotInteractor",
    Highlight
    | IntervalX
    | IntervalXY
    | IntervalY
    | NearestX
    | NearestY
    | Pan
    | PanX
    | PanY
    | PanZoom
    | PanZoomX
    | PanZoomY
    | Region
    | Toggle
    | ToggleColor
    | ToggleX
    | ToggleY,
)
"""A plot interactor entry."""


__all__ = (
    "BrushStyles",
    "Highlight",
    "IntervalX",
    "IntervalXY",
    "IntervalY",
    "NearestX",
    "NearestY",
    "Pan",
    "PanX",
    "PanY",
    "PanZoom",
    "PanZoomX",
    "PanZoomY",
    "PlotInteractor",
    "Region",
    "Toggle",
    "ToggleColor",
    "ToggleX",
    "ToggleY",
)
