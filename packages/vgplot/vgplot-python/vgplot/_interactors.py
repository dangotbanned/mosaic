"""A manual example of translating `spec/interactors` to [`TypedDict`]s.

## This is not a new idea
- In ([vega/altair#3536]) I did a (crude) heuristic-based translation for part of the [vega-lite schema]
    - The expressiveness of JSON schema made this task difficult
- I've found an active project [`ts2python`] that looks like a better direction
    - Python's type system is less expressive than TypeScript's (for now [PEP 827 - Type Manipulation])
    - But [`TypedDict`] can:
        - model optionality, [openness] and mutability
        - use [multiple inheritance]
        - define type parameters
        - use a [functional syntax] to **define keys that are not valid Python identifiers**

## Notes
- [`BrushStyles`][] and [`Highlight`][] demo translating `.ts` comments -> `.py` docstrings
    - Not doing that for everything
    - Need to give an example because Ruff doesn't format them
- A [`TypedDict`] can also be used with [`Unpack` for keyword arguments]

[`TypedDict`]: https://typing.python.org/en/latest/spec/typeddict.html
[`Unpack` for keyword arguments]: https://typing.python.org/en/latest/spec/callables.html#unpack-for-keyword-arguments
[vega/altair#3536]: https://github.com/vega/altair/pull/3536
[vega-lite schema]: https://github.com/vega/schema/tree/master/vega-lite
[`ts2python`]: https://github.com/jecki/ts2python
[PEP 827 - Type Manipulation]: https://peps.python.org/pep-0827/
[multiple inheritance]: https://typing.python.org/en/latest/spec/typeddict.html#multiple-inheritance
[openness]: https://typing.python.org/en/latest/spec/typeddict.html#openness
[functional syntax]: https://typing.python.org/en/latest/spec/typeddict.html#functional-syntax
"""

from __future__ import annotations

# ruff: noqa: N817
from typing import TYPE_CHECKING, Any, TypeAlias, TypedDict
from typing import Literal as L

if TYPE_CHECKING:
    from collections.abc import Sequence

    from typing_extensions import NotRequired, Required

ParamRef: TypeAlias = Any
"""Placeholder as I should probably move this idea to another branch."""


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


# fmt: off
# NOTE: Common fields, these *can* have docstrings attatch which should propagate to children
class _Bind(TypedDict):
    bind: Required[ParamRef]
class _Brush(TypedDict):
    brush: NotRequired[BrushStyles]
class _Peers(TypedDict):
    peers: NotRequired[bool]
class _Channels(TypedDict):
    channels: Required[Sequence[str]]
class _XYField(TypedDict):
    xfield: NotRequired[str]
    yfield: NotRequired[str]
class _PixelSize(TypedDict):
    pixel_size: NotRequired[float]
# fmt: on


class Interval1DOptions(_Bind, _Peers, _Brush, _PixelSize, total=False):
    field: str


# NOTE: https://typing.python.org/en/latest/spec/typeddict.html#class-based-syntax
# > `total`: a boolean literal ... indicating whether all items are required
# > (`True`, the default) or non-required (`False`).
# > This affects only items defined in this class, not in any base classes,
# > and it does not affect any items that use an explicit `Required[]`` or `NotRequired[]` qualifier.
class IntervalX(Interval1DOptions):
    select: L["intervalX"]


class IntervalY(Interval1DOptions):
    select: L["intervalY"]


class Interval2DOptions(_Bind, _Peers, _Brush, _XYField, _PixelSize): ...


class IntervalXY(Interval2DOptions):
    select: L["intervalXY"]


class NearestOptions(_Bind, total=False):
    channels: Sequence[str]
    fields: Sequence[str]
    max_radius: float


class Nearest(NearestOptions):
    select: L["nearest"]


class NearestX(NearestOptions):
    select: L["nearestX"]


class NearestY(NearestOptions):
    select: L["nearestY"]


class PanZoomOptions(_XYField, TypedDict, total=False):
    x: ParamRef
    y: ParamRef


class Pan(PanZoomOptions):
    select: L["pan"]


class PanX(PanZoomOptions):
    select: L["panX"]


class PanY(PanZoomOptions):
    select: L["panY"]


class PanZoom(PanZoomOptions):
    select: L["panZoom"]


class PanZoomX(PanZoomOptions):
    select: L["panZoomX"]


class PanZoomY(PanZoomOptions):
    select: L["panZoomY"]


class RegionOptions(_Bind, _Peers, _Brush, _Channels): ...


class Region(RegionOptions):
    select: L["region"]


class ToggleOptions(_Bind, _Peers): ...


class Toggle(ToggleOptions, _Channels):
    select: L["toggle"]


class ToggleX(ToggleOptions):
    select: L["toggleX"]


class ToggleY(ToggleOptions):
    select: L["toggleY"]


class ToggleZ(ToggleOptions):
    select: L["toggleZ"]


class ToggleColor(ToggleOptions):
    select: L["toggleColor"]


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
