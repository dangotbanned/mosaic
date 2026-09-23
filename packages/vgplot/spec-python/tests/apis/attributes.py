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
    from mosaic_spec import Fixed, Interval, LabelArrow
    from tests.apis.params import ParamDef


ScaleT = TypeVar("ScaleT")
AxisT = TypeVar("AxisT")


class Margins(TypedDict, total=False, closed=True):
    """Set multiple margin values."""

    bottom: ParamDef | float
    left: ParamDef | float
    right: ParamDef | float
    top: ParamDef | float


# NOTE: super minimal
class _Align(TypedDict, total=False):
    align: ParamDef | float
    """How to distribute unused space in the **range** for *point* and *band* scales. A number in [0, 1], such as:

    - 0 - use the start of the range, putting unused space at the end
    - 0.5 (default) - use the middle, distributing unused space evenly
    - 1 use the end, putting unused space at the start

    For ordinal position scales only.
    """


class _Axis(TypedDict, Generic[AxisT], total=False):
    axis: AxisT | ParamDef | bool | None


class _DomainRange(TypedDict, total=False):
    domain: Fixed | ParamDef | Sequence[Any]
    range: Fixed | ParamDef | Sequence[Any]


class _Scale(TypedDict, Generic[ScaleT], total=False):
    scale: ScaleT | ParamDef | None


class _Grid(TypedDict, total=False):
    grid: Interval | ParamDef | Sequence[Any] | bool | str
    """Whether to show a grid aligned with the scale's ticks.

    - If true, show a grid with the currentColor stroke
    - If a string, show a grid with the specified stroke color
    - If an approximate number of ticks, an interval, or an array of tick values,
      show corresponding grid lines.

    See also the grid mark.
    """


class _Label(TypedDict, total=False):
    label: ParamDef | str | None
    """A textual label to show on the axis or legend.

    If null, show no label.
    By default the scale label is inferred from channel definitions,
    possibly with an arrow (↑, →, ↓, or ←) to indicate the direction of increasing value.
    """


class _ReverseTickFormat(TypedDict, total=False):
    reverse: ParamDef | bool
    """Whether to reverse the scale's encoding.

    Equivalent to reversing either the **domain** or **range**.
    """
    tick_format: ParamDef | str | None
    """How to format inputs (abstract values) for axis tick labels.

    One of:
    - a [d3-format][1] string for numeric scales
    - a [d3-time-format][2] string for temporal scales

    [1]: https://d3js.org/d3-time
    [2]: https://d3js.org/d3-time-format
    """


# NOTE: more specialized
class _BaseClampConstantExponentNicePercentZero(TypedDict, total=False):
    base: ParamDef | float
    clamp: ParamDef | bool
    constant: ParamDef | float
    exponent: ParamDef | float
    nice: ms.Interval | ParamDef | bool | float
    percent: ParamDef | bool
    zero: ParamDef | bool
    """Whether the **domain** must include zero.

    - If the domain minimum is positive, it will be set to zero
    - otherwise if the domain maximum is negative, it will be set to zero
    """


class _ColorContinuous(
    _BaseClampConstantExponentNicePercentZero, _DomainRange, _Label, _Scale[ScaleT], total=False
): ...


class _AxisX(_Axis[L["both", "bottom", "top"]], total=False):
    inset_left: ParamDef | float
    inset_right: ParamDef | float


class _AxisY(_Axis[L["both", "left", "right"]], total=False):
    inset_bottom: ParamDef | float
    inset_top: ParamDef | float


class _Position(_Align, _DomainRange, _Grid, _Label, _ReverseTickFormat, total=False):
    aria_description: ParamDef | str
    """A textual description for the axis in the accessibility tree."""
    aria_label: ParamDef | str
    """A short label representing the axis in the accessibility tree."""
    font_variant: ParamDef | str
    inset: ParamDef | float
    label_anchor: L["bottom", "center", "left", "right", "top"] | ParamDef
    label_offset: ParamDef | float
    line: ParamDef | bool
    padding: ParamDef | float
    padding_inner: ParamDef | float
    padding_outer: ParamDef | float
    round: ParamDef | bool
    tick_padding: ParamDef | float
    tick_rotate: ParamDef | float
    tick_size: ParamDef | float
    tick_spacing: ParamDef | float
    ticks: Interval | ParamDef | Sequence[Any] | float
    """The desired approximate number of axis ticks, or an explicit array of tick values, or an interval such as *day* or *month*."""


class _XY(
    _Position, _BaseClampConstantExponentNicePercentZero, _Scale[PositionScaleType], total=False
):
    label_arrow: LabelArrow | ParamDef
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
    interpolate: ms.Interpolate | ParamDef
    n: ParamDef | float
    pivot: Any | ParamDef
    scheme: ms.ColorScheme | ParamDef
    symmetric: ParamDef | bool


class Opacity(_ColorContinuous[ContinuousScaleType], _ReverseTickFormat, closed=True): ...


class Facet(_Grid, _Label, total=False, closed=True):
    margin: ParamDef | float | Margins  # `facet_margin`, `facet_margin_*`
    """Set the same default (`ParamDef | float`) or multiple defaults (`Margins`) for margins."""


class PlotAttributes(
    _Align, _Axis[L["both", "bottom", "left", "right", "top"]], total=False, closed=True
):
    """*Attributes* are plot-level settings.

    They are represented in a style closer to [Observable Plot](https://observablehq.github.io/plot/api#options).

    For example, `width` and `height` are available at the plot-level, but scale settings are grouped together.
    """

    aria_description: str | None
    """The [aria-description attribute][1] on the SVG root.

    [1]: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-description
    """
    aria_label: str | None
    """The [aria-label attribute][1] on the SVG root.

    [1]: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-label
    """
    aspect_ratio: ParamDef | bool | float | None
    clip: L["frame", "sphere"] | ParamDef | bool | None
    color: Color
    facet: Facet
    fx: Fx
    fy: Fy
    grid: ParamDef | bool | str
    height: ParamDef | float
    inset: ParamDef | float
    length: Length
    margin: ParamDef | float | Margins  # `margin`, `margin_*`, `margins`
    """Set the same deafult (`ParamDef | float`) or multiple defaults (`Margins`) for margins."""

    name: str
    """A unique name for the plot.

    The name is used by standalone legend components to to lookup the plot and access scale mappings.
    """
    opacity: Opacity
    r: R
    style: ms.CSSStyles | ParamDef | None
    symbol: Symbol
    width: ParamDef | float
    x: X
    y: Y
    xy_domain: Fixed | ParamDef | Sequence[Any]
    """Set the *x* and *y* scale domains."""
