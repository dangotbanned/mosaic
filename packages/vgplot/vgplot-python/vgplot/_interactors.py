"""A manual example of translating `spec/interactors` to [`TypedDict`]s.

[`TypedDict`]: https://typing.python.org/en/latest/spec/typeddict.html
[`Unpack` for keyword arguments]: https://typing.python.org/en/latest/spec/callables.html#unpack-for-keyword-arguments

## Notes
- [`BrushStyles`][] and [`Highlight`][] demo translating `.ts` comments -> `.py` docstrings
    - Not doing that for everything
    - Need to give an example because Ruff doesn't format them
- A [`TypedDict`] can also be used with [`Unpack` for keyword arguments]
"""

from __future__ import annotations

# ruff: noqa: N817
from typing import TYPE_CHECKING, Any, TypeAlias, TypedDict
from typing import Literal as L

if TYPE_CHECKING:
    from collections.abc import Sequence

    from typing_extensions import Required

Incomplete: TypeAlias = Any
ParamRef: TypeAlias = Incomplete


# NOTE: One-line docstring
class BrushStyles(TypedDict, total=False):
    opacity: float
    """The overall opacity of the brush rectangle."""
    fill_opacity: float
    """The fill opacity of the brush rectangle."""
    stroke_opacity: float
    """The stroke opacity of the brush rectangle."""
    fill: str
    """The fill color of the brush rectangle."""
    stroke: str
    """The stroke color of the brush rectangle."""
    stroke_dasharray: str
    """ The stroke dash array of the brush rectangle."""


# NOTE: After first sentence, split it up
class Highlight(TypedDict, total=False):
    select: Required[L["highlight"]]
    """Highlight selected marks by deemphasizing the others."""
    by: Required[ParamRef]
    """The input selection.

    Unselected marks are deemphasized.
    """
    opacity: float
    """The overall opacity of deemphasized marks.

    By default the opacity is set to 0.2.
    """
    fillOpacity: float
    """The fill opacity of deemphasized marks.

    By default the fill opacity is unchanged.
    """
    strokeOpacity: float
    """The stroke opacity of deemphasized marks.

    By default the stroke opacity is unchanged.
    """
    fill: str
    """The fill color of deemphasized marks.

    By default the fill is unchanged.
    """
    stroke: str
    """The stroke color of deemphasized marks.

    By default the stroke is unchanged."""


class Interval1DOptions(TypedDict, total=False):
    bind: Required[ParamRef]
    field: str
    pixel_size: float
    peers: bool
    brush: BrushStyles


# TODO @dangotbanned: Double-check the spec if `Required` is implicit
# when inheriting from a `total=False` and not redfining it
class IntervalX(Interval1DOptions):
    select: Required[L["intervalX"]]


class IntervalY(Interval1DOptions):
    select: Required[L["intervalY"]]


class Interval2DOptions(TypedDict, total=False):
    bind: Required[ParamRef]
    xfield: str
    yfield: str
    pixel_size: float
    peers: bool
    brush: BrushStyles


class IntervalXY(Interval2DOptions):
    select: Required[L["intervalXY"]]


class NearestOptions(TypedDict, total=False):
    bind: Required[ParamRef]
    channels: Sequence[str]
    fields: Sequence[str]
    max_radius: float


class Nearest(NearestOptions):
    select: Required[L["nearest"]]


class NearestX(NearestOptions):
    select: Required[L["nearestX"]]


class NearestY(NearestOptions):
    select: Required[L["nearestY"]]


class PanZoomOptions(TypedDict, total=False):
    x: ParamRef
    y: ParamRef
    xfield: str
    yfield: str


class Pan(PanZoomOptions):
    select: Required[L["pan"]]


class PanX(PanZoomOptions):
    select: Required[L["panX"]]


class PanY(PanZoomOptions):
    select: Required[L["panY"]]


class PanZoom(PanZoomOptions):
    select: Required[L["panZoom"]]


class PanZoomX(PanZoomOptions):
    select: Required[L["panZoomX"]]


class PanZoomY(PanZoomOptions):
    select: Required[L["panZoomY"]]


class RegionOptions(TypedDict, total=False):
    bind: Required[ParamRef]
    channels: Required[Sequence[str]]
    peers: bool
    brush: BrushStyles


class Region(RegionOptions):
    select: Required[L["region"]]


class ToggleOptions(TypedDict, total=False):
    bind: Required[ParamRef]
    peers: bool


class Toggle(ToggleOptions):
    select: Required[L["toggle"]]
    channels: Required[Sequence[str]]


class ToggleX(ToggleOptions):
    select: Required[L["toggleX"]]


class ToggleY(ToggleOptions):
    select: Required[L["toggleY"]]


class ToggleZ(ToggleOptions):
    select: Required[L["toggleZ"]]


class ToggleColor(ToggleOptions):
    select: Required[L["toggleColor"]]


PlotInteractor: TypeAlias = (
    Highlight
    | IntervalX
    | IntervalY
    | IntervalXY
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
    | ToggleX
    | ToggleY
    | ToggleColor
)
"""A plot interactor entry."""
