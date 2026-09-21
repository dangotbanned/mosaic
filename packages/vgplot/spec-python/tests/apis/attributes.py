"""Experimenting with hierarchical attribute surface.

## Notes
- Approximately [the inverse of this](https://github.com/dangotbanned/mosaic/blob/155f94933710e3707d15f181ac24bdb583215fa4/packages/vgplot/plot/src/plot-attributes.js#L1-L212)
    - Need to define a mapping like that
- Related to [roadmap.md#unflatten-the-spec]

[the inverse of this]: https://github.com/dangotbanned/mosaic/blob/155f94933710e3707d15f181ac24bdb583215fa4/packages/vgplot/plot/src/plot-attributes.js#L1-L212
[roadmap.md#unflatten-the-spec]: https://github.com/dangotbanned/mosaic/blob/155f94933710e3707d15f181ac24bdb583215fa4/packages/vgplot/spec-python/docs/roadmap.md#L65-L106
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Generic, Literal as L

from mosaic_spec import ColorScaleType, ContinuousScaleType, DiscreteScaleType, PositionScaleType
from mosaic_spec._typing_compat import TypedDict, TypeVar

if TYPE_CHECKING:
    from collections.abc import Sequence

    import mosaic_spec as ms
    from mosaic_spec import Fixed, Interval, LabelArrow, ParamRef


ScaleT = TypeVar("ScaleT")
AxisT = TypeVar("AxisT")


# NOTE: super minimal
class _Align(TypedDict, total=False):
    align: ParamRef | float
    """How to distribute unused space in the **range** for *point* and *band* scales. A number in [0, 1], such as:

    - 0 - use the start of the range, putting unused space at the end
    - 0.5 (default) - use the middle, distributing unused space evenly
    - 1 use the end, putting unused space at the start

    For ordinal position scales only.
    """


class _Axis(TypedDict, Generic[AxisT], total=False):
    axis: AxisT | ParamRef | bool | None


class _DomainRange(TypedDict, total=False):
    domain: Fixed | ParamRef | Sequence[Any]
    range: Fixed | ParamRef | Sequence[Any]


class _Scale(TypedDict, Generic[ScaleT], total=False):
    scale: ScaleT | ParamRef | None


class _Grid(TypedDict, total=False):
    grid: Interval | ParamRef | Sequence[Any] | bool | str
    """Whether to show a grid aligned with the scale's ticks.

    - If true, show a grid with the currentColor stroke
    - If a string, show a grid with the specified stroke color
    - If an approximate number of ticks, an interval, or an array of tick values,
      show corresponding grid lines.

    See also the grid mark.
    """


class _Label(TypedDict, total=False):
    label: ParamRef | str | None
    """A textual label to show on the axis or legend.

    If null, show no label.
    By default the scale label is inferred from channel definitions,
    possibly with an arrow (↑, →, ↓, or ←) to indicate the direction of increasing value.
    """


class _ReverseTickFormat(TypedDict, total=False):
    reverse: ParamRef | bool
    """Whether to reverse the scale's encoding.

    Equivalent to reversing either the **domain** or **range**.
    """
    tick_format: ParamRef | str | None
    """How to format inputs (abstract values) for axis tick labels.

    One of:
    - a [d3-format][1] string for numeric scales
    - a [d3-time-format][2] string for temporal scales

    [1]: https://d3js.org/d3-time
    [2]: https://d3js.org/d3-time-format
    """


# NOTE: more specialized
class _BaseClampConstantExponentNicePercentZero(TypedDict, total=False):
    base: ParamRef | float
    clamp: ParamRef | bool
    constant: ParamRef | float
    exponent: ParamRef | float
    nice: ms.Interval | ms.ParamRef | bool | float
    percent: ParamRef | bool
    zero: ParamRef | bool
    """Whether the **domain** must include zero.

    - If the domain minimum is positive, it will be set to zero
    - otherwise if the domain maximum is negative, it will be set to zero
    """


class _ColorContinuous(
    _BaseClampConstantExponentNicePercentZero, _DomainRange, _Label, _Scale[ScaleT], total=False
): ...


class _AxisX(_Axis[L["both", "bottom", "top"]], total=False):
    inset_left: ParamRef | float
    inset_right: ParamRef | float


class _AxisY(_Axis[L["both", "left", "right"]], total=False):
    inset_bottom: ParamRef | float
    inset_top: ParamRef | float


class _Position(_Align, _DomainRange, _Grid, _Label, _ReverseTickFormat, total=False):
    aria_description: ParamRef | str
    """A textual description for the axis in the accessibility tree."""
    aria_label: ParamRef | str
    """A short label representing the axis in the accessibility tree."""
    font_variant: ParamRef | str
    inset: ParamRef | float
    label_anchor: L["bottom", "center", "left", "right", "top"] | ParamRef
    label_offset: ParamRef | float
    line: ParamRef | bool
    padding: ParamRef | float
    padding_inner: ParamRef | float
    padding_outer: ParamRef | float
    round: ParamRef | bool
    tick_padding: ParamRef | float
    tick_rotate: ParamRef | float
    tick_size: ParamRef | float
    tick_spacing: ParamRef | float
    ticks: Interval | ParamRef | Sequence[Any] | float
    """The desired approximate number of axis ticks, or an explicit array of tick values, or an interval such as *day* or *month*."""


class _XY(
    _Position, _BaseClampConstantExponentNicePercentZero, _Scale[PositionScaleType], total=False
):
    label_arrow: LabelArrow | ParamRef
    """Whether to apply a directional arrow such as → or ↑ to the axis scale label.

    If *auto* (the default), the presence of the arrow depends on whether the scale is ordinal.
    """


# NOTE: Concrete attributes
class Fx(_Position, _AxisX, total=False, closed=True): ...


class Fy(_Position, _AxisY, closed=True): ...


class X(_XY, _AxisX, total=False, closed=True): ...


class Y(_XY, _AxisY, total=False, closed=True): ...


class Length(_ColorContinuous[ContinuousScaleType], closed=True): ...


class R(_ColorContinuous[ContinuousScaleType], closed=True): ...


class Symbol(_DomainRange, _Scale[DiscreteScaleType], closed=True): ...


class Color(_ColorContinuous[ColorScaleType], _ReverseTickFormat, total=False, closed=True):
    interpolate: ms.Interpolate | ParamRef
    n: ParamRef | float
    pivot: Any | ParamRef
    scheme: ms.ColorScheme | ParamRef
    symmetric: ParamRef | bool


class Opacity(_ColorContinuous[ContinuousScaleType], _ReverseTickFormat, closed=True): ...


class Facet(_Grid, _Label, total=False, closed=True):
    margin: ParamRef | float | ms.Margins  # `facet_margin`, `facet_margin_*`
    """Set the same default (`ParamRef | float`) or multiple defaults (`ms.Margins`) for margins."""


# NOTE: Top-level, can be inhereted by `Plot`, `PlotAttributes`
class _PlotOptions(_Align, _Axis[L["both", "bottom", "left", "right", "top"]], total=False):
    aria_description: str | None
    """The [aria-description attribute][1] on the SVG root.

    [1]: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-description
    """
    aria_label: str | None
    """The [aria-label attribute][1] on the SVG root.

    [1]: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-label
    """
    aspect_ratio: ParamRef | bool | float | None
    clip: L["frame", "sphere"] | ParamRef | bool | None
    color: Color
    facet: Facet
    fx: Fx
    fy: Fy
    grid: ParamRef | bool | str
    height: ParamRef | float
    inset: ParamRef | float
    length: Length
    margin: ParamRef | float | ms.Margins  # `margin`, `margin_*`, `margins`
    """Set the same deafult (`ParamRef | float`) or multiple defaults (`ms.Margins`) for margins."""

    name: str
    """A unique name for the plot.

    The name is used by standalone legend components to to lookup the plot and access scale mappings.
    """
    opacity: Opacity
    r: R
    style: ms.CSSStyles | ParamRef | None
    symbol: Symbol
    width: ParamRef | float
    x: X
    y: Y
    xy_domain: Fixed | ParamRef | Sequence[Any]
    """Set the *x* and *y* scale domains."""


# NOTE: Concrete, can be used in `SpecHead`
class PlotAttributes(_PlotOptions, closed=True): ...
