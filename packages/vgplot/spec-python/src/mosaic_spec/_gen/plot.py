# Generated: `mosaic_spec._gen.plot`
from __future__ import annotations

from typing import TYPE_CHECKING, Annotated as A, Any, Literal as L

from mosaic_spec._typing_compat import Required, TypedDict

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence

    from mosaic_spec._gen.css_styles import CSSStyles
    from mosaic_spec._gen.interactors import PlotInteractor
    from mosaic_spec._gen.marks import PlotMark
    from mosaic_spec._gen.params import ParamRef
    from mosaic_spec._gen.plot_legend import PlotLegend
    from mosaic_spec._gen.typing import (
        ColorScaleType,
        ColorScheme,
        ContinuousScaleType,
        DiscreteScaleType,
        Fixed,
        Interpolate,
        Interval,
        LabelArrow,
        PositionScaleType,
        ProjectionName,
    )


class Margins(TypedDict, total=False, closed=True):
    """A shorthand object notation for setting multiple margin values. The object keys are margin names (top, right, etc)."""

    bottom: ParamRef | float
    left: ParamRef | float
    right: ParamRef | float
    top: ParamRef | float


class _PlotAttributesOpen(TypedDict, total=False):
    """Plot attributes."""

    align: ParamRef | float
    """How to distribute unused space in the **range** for *point* and *band* scales. A number in [0, 1], such as:

- 0 - use the start of the range, putting unused space at the end
- 0.5 (default) - use the middle, distributing unused space evenly
- 1 use the end, putting unused space at the start

For ordinal position scales only."""
    aria_description: str | None
    """The [aria-description attribute][1] on the SVG root.

[1]: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-description"""
    aria_label: str | None
    """The [aria-label attribute][1] on the SVG root.

[1]: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-label"""
    aspect_ratio: ParamRef | bool | float | None
    """The desired aspect ratio of the *x* and *y* scales, affecting the default height. Given an aspect ratio of *dx* / *dy*, and assuming that the *x* and
*y* scales represent equivalent units (say, degrees Celsius or meters), computes a default height such that *dx* pixels along *x* represents the same variation as *dy* pixels along *y*. Note: when faceting, set the *fx* and *fy* scales' **round** option to false for an exact aspect ratio."""
    axis: L["both", "bottom", "left", "right", "top"] | ParamRef | bool | None
    """The side of the frame on which to place the implicit axis: *top* or
*bottom* for *x* or *fx*, or *left* or *right* for *y* or *fy*. The default depends on the scale:

- *x* - *bottom*
- *y* - *left*
- *fx* - *top* if there is a *bottom* *x* axis, and otherwise *bottom*
- *fy* - *right* if there is a *left* *y* axis, and otherwise *right*

If *both*, an implicit axis will be rendered on both sides of the plot (*top* and *bottom* for *x* or *fx*, or *left* and *right* for *y* or
*fy*). If null, the implicit axis is suppressed.

For position axes only."""
    clip: L["frame", "sphere"] | ParamRef | bool | None
    """The default clip for all marks."""
    color_base: ParamRef | float
    """A log scale's base; defaults to 10. Does not affect the scale's encoding, but rather the default ticks. For *log* and *diverging-log* scales only."""
    color_clamp: ParamRef | bool
    """If true, values below the domain minimum are treated as the domain minimum, and values above the domain maximum are treated as the domain maximum.

Clamping is useful for focusing on a subset of the data while ensuring that extreme values remain visible, but use caution: clamped values may need an annotation to avoid misinterpretation. Clamping typically requires setting an explicit **domain** since if the domain is inferred, no values will be outside the domain.

For continuous scales only."""
    color_constant: ParamRef | float
    """A symlog scale's constant, expressing the magnitude of the linear region around the origin; defaults to 1. For *symlog* and *diverging-symlog* scales only."""
    color_domain: Fixed | ParamRef | Sequence[Any]
    """The extent of the scale's inputs (abstract values). By default inferred from channel values. For continuous data (numbers and dates), it is typically [*min*, *max*]; it can be [*max*, *min*] to reverse the scale. For ordinal data (strings or booleans), it is an array (or iterable) of values is the desired order, defaulting to natural ascending order."""
    color_exponent: ParamRef | float
    """A power scale's exponent (*e.g.*, 0.5 for sqrt); defaults to 1 for a linear scale. For *pow* and *diverging-pow* scales only."""
    color_interpolate: Interpolate | ParamRef
    """How to interpolate color range values. For quantitative scales only. This attribute can be used to specify a color space for interpolating colors specified in the **colorRange**."""
    color_label: ParamRef | str | None
    """A textual label to show on the axis or legend; if null, show no label. By default the scale label is inferred from channel definitions, possibly with an arrow (↑, →, ↓, or ←) to indicate the direction of increasing value.

For axes and legends only."""
    color_n: ParamRef | float
    """For a *quantile* scale, the number of quantiles (creates *n* - 1 thresholds); for a *quantize* scale, the approximate number of thresholds; defaults to 5."""
    color_nice: Interval | ParamRef | bool | float
    """If true, or a tick count or interval, extend the domain to nice round values. Defaults to 1, 2 or 5 times a power of 10 for *linear* scales, and nice time intervals for *utc* and *time* scales. Pass an interval such as
*minute*, *wednesday* or *month* to specify what constitutes a nice interval.

For continuous scales only."""
    color_percent: ParamRef | bool
    """If true, shorthand for a transform suitable for percentages, mapping proportions in [0, 1] to [0, 100]."""
    color_pivot: Any | ParamRef
    """For a diverging color scale, the input value (abstract value) that divides the domain into two parts; defaults to 0 for *diverging* scales, dividing the domain into negative and positive parts; defaults to 1 for
*diverging-log* scales. By default, diverging scales are symmetric around the pivot; see the **symmetric** option."""
    color_range: Fixed | ParamRef | Sequence[Any]
    """The extent of the scale's outputs (visual values). By default inferred from the scale's **type** and **domain**. For other ordinal data, it is an array (or iterable) of output values in the same order as the **domain**."""
    color_reverse: ParamRef | bool
    """Whether to reverse the scale's encoding; equivalent to reversing either the
**domain** or **range**."""
    color_scale: ColorScaleType | ParamRef | None
    """The *color* scale type, affecting how the scale encodes abstract data, say by applying a mathematical transformation. If null, the scale is disabled.

For quantitative data (numbers), defaults to *linear*; for temporal data (dates), defaults to *utc*; for ordinal data (strings or booleans), defaults to *point* for position scales, *categorical* for color scales, and otherwise *ordinal*."""
    color_scheme: ColorScheme | ParamRef
    """If specified, shorthand for setting the **colorRange** or **colorInterpolate** option of a *color* scale."""
    color_symmetric: ParamRef | bool
    """For a diverging color scale, if true (the default), extend the domain to ensure that the lower part of the domain (below the **pivot**) is commensurate with the upper part of the domain (above the **pivot**).

A symmetric diverging color scale may not use all of its output **range**; this reduces contrast but ensures that deviations both below and above the
**pivot** are represented proportionally. Otherwise if false, the full output **range** will be used; this increases contrast but values on opposite sides of the **pivot** may not be meaningfully compared."""
    color_tick_format: ParamRef | str | None
    """How to format inputs (abstract values) for axis tick labels; one of:

- a [d3-format][1] string for numeric scales
- a [d3-time-format][2] string for temporal scales

[1]: https://d3js.org/d3-time [2]: https://d3js.org/d3-time-format"""
    color_zero: ParamRef | bool
    """Whether the **domain** must include zero. If the domain minimum is positive, it will be set to zero; otherwise if the domain maximum is negative, it will be set to zero.

For quantitative scales only."""
    facet_grid: Interval | ParamRef | Sequence[Any] | bool | str
    """Default axis grid for fx and fy scales; typically set to true to enable."""
    facet_label: ParamRef | str | None
    """Default axis label for fx and fy scales; typically set to null to disable."""
    facet_margin: ParamRef | float
    """Shorthand to set the same default for all four facet margins: marginTop, marginRight, marginBottom, and marginLeft."""
    facet_margin_bottom: ParamRef | float
    """The right facet margin; the (minimum) distance in pixels between the right edges of the inner and outer plot area."""
    facet_margin_left: ParamRef | float
    """The bottom facet margin; the (minimum) distance in pixels between the bottom edges of the inner and outer plot area."""
    facet_margin_right: ParamRef | float
    """The left facet margin; the (minimum) distance in pixels between the left edges of the inner and outer plot area."""
    facet_margin_top: ParamRef | float
    """The top facet margin; the (minimum) distance in pixels between the top edges of the inner and outer plot area."""
    fx_align: ParamRef | float
    """How to distribute unused space in the **range** for *point* and *band* scales. A number in [0, 1], such as:

- 0 - use the start of the range, putting unused space at the end
- 0.5 (default) - use the middle, distributing unused space evenly
- 1 use the end, putting unused space at the start

For ordinal position scales only."""
    fx_aria_description: ParamRef | str
    """A textual description for the axis in the accessibility tree."""
    fx_aria_label: ParamRef | str
    """A short label representing the axis in the accessibility tree."""
    fx_axis: L["both", "bottom", "top"] | ParamRef | bool | None
    """The side of the frame on which to place the implicit axis: *top* or
*bottom* for *fx*. Defaults to *top* if there is a *bottom* *x* axis, and otherwise *bottom*.

If *both*, an implicit axis will be rendered on both sides of the plot (*top* and *bottom* for *fx*). If null, the implicit axis is suppressed."""
    fx_domain: Fixed | ParamRef | Sequence[Any]
    """The extent of the scale's inputs (abstract values). By default inferred from channel values. For ordinal data (strings or booleans), it is an array (or iterable) of values is the desired order, defaulting to natural ascending order."""
    fx_font_variant: ParamRef | str
    """The font-variant attribute for axis ticks; defaults to *tabular-nums* for quantitative axes."""
    fx_grid: Interval | ParamRef | Sequence[Any] | bool | str
    """Whether to show a grid aligned with the scale's ticks. If true, show a grid with the currentColor stroke; if a string, show a grid with the specified stroke color; if an approximate number of ticks, an interval, or an array of tick values, show corresponding grid lines. See also the grid mark.

For axes only."""
    fx_inset: ParamRef | float
    """Shorthand to set the same default for all four insets: **insetTop**,
**insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it."""
    fx_inset_left: ParamRef | float
    """Insets the left edge by the specified number of pixels. A positive value insets towards the right edge (reducing effective area), while a negative value insets away from the right edge (increasing it)."""
    fx_inset_right: ParamRef | float
    """Insets the right edge by the specified number of pixels. A positive value insets towards the left edge (reducing effective area), while a negative value insets away from the left edge (increasing it)."""
    fx_label: ParamRef | str | None
    """A textual label to show on the axis or legend; if null, show no label. By default the scale label is inferred from channel definitions, possibly with an arrow (↑, →, ↓, or ←) to indicate the direction of increasing value.

For axes and legends only."""
    fx_label_anchor: L["bottom", "center", "left", "right", "top"] | ParamRef
    """Where to place the axis **label** relative to the plot's frame. For vertical position scales (*y* and *fy*), may be *top*, *bottom*, or
*center*; for horizontal position scales (*x* and *fx*), may be *left*,
*right*, or *center*. Defaults to *center* for ordinal scales (including
*fx* and *fy*), and otherwise *top* for *y*, and *right* for *x*."""
    fx_label_offset: ParamRef | float
    """The axis **label** position offset (in pixels); default depends on margins and orientation."""
    fx_line: ParamRef | bool
    """If true, draw a line along the axis; if false (default), do not."""
    fx_padding: ParamRef | float
    """For *band* scales, how much of the **range** to reserve to separate adjacent bands; defaults to 0.1 (10%). For *point* scales, the amount of inset for the first and last value as a proportion of the bandwidth; defaults to 0.5 (50%).

For ordinal position scales only."""
    fx_padding_inner: ParamRef | float
    """For a *band* scale, how much of the range to reserve to separate adjacent bands."""
    fx_padding_outer: ParamRef | float
    """For a *band* scale, how much of the range to reserve to inset first and last bands."""
    fx_range: Fixed | ParamRef | Sequence[Any]
    """The extent of the scale's outputs (visual values). By default inferred from the scale's **type** and **domain**, and the plot's dimensions. For ordinal position scales (*point* and *band*), it is typically [*min*, *max*]; it can be [*max*, *min*] to reverse the scale."""
    fx_reverse: ParamRef | bool
    """Whether to reverse the scale's encoding; equivalent to reversing either the
**domain** or **range**."""
    fx_round: ParamRef | bool
    """If true, round the output value to the nearest integer (pixel); useful for crisp edges when rendering.

For position scales only."""
    fx_tick_format: ParamRef | str | None
    """How to format inputs (abstract values) for axis tick labels; one of:

- a [d3-format][1] string for numeric scales
- a [d3-time-format][2] string for temporal scales

[1]: https://d3js.org/d3-time [2]: https://d3js.org/d3-time-format"""
    fx_tick_padding: ParamRef | float
    """The distance between an axis tick mark and its associated text label (in pixels); often defaults to 3, but may be affected by **fxTickSize** and
**fxTickRotate**."""
    fx_tick_rotate: ParamRef | float
    """The rotation angle of axis tick labels in degrees clocksize; defaults to 0."""
    fx_tick_size: ParamRef | float
    """The length of axis tick marks in pixels; negative values extend in the opposite direction. Defaults to 6 for *x* and *y* axes and *color* and
*opacity* *ramp* legends, and 0 for *fx* and *fy* axes."""
    fx_tick_spacing: ParamRef | float
    """The desired approximate spacing between adjacent axis ticks, affecting the default **ticks**; defaults to 80 pixels for *x* and *fx*, and 35 pixels for *y* and *fy*."""
    fx_ticks: Interval | ParamRef | Sequence[Any] | float
    """The desired approximate number of axis ticks, or an explicit array of tick values, or an interval such as *day* or *month*."""
    fy_align: ParamRef | float
    """How to distribute unused space in the **range** for *point* and *band* scales. A number in [0, 1], such as:

- 0 - use the start of the range, putting unused space at the end
- 0.5 (default) - use the middle, distributing unused space evenly
- 1 use the end, putting unused space at the start

For ordinal position scales only."""
    fy_aria_description: ParamRef | str
    """A textual description for the axis in the accessibility tree."""
    fy_aria_label: ParamRef | str
    """A short label representing the axis in the accessibility tree."""
    fy_axis: L["both", "left", "right"] | ParamRef | bool | None
    """The side of the frame on which to place the implicit axis: *left* or
*right* for *fy*. Defaults to *left* for an *fy* scale.

If *both*, an implicit axis will be rendered on both sides of the plot (*left* and *right* for *fy*). If null, the implicit axis is suppressed."""
    fy_domain: Fixed | ParamRef | Sequence[Any]
    """The extent of the scale's inputs (abstract values). By default inferred from channel values. For ordinal data (strings or booleans), it is an array (or iterable) of values is the desired order, defaulting to natural ascending order."""
    fy_font_variant: ParamRef | str
    """The font-variant attribute for axis ticks; defaults to *tabular-nums* for quantitative axes."""
    fy_grid: Interval | ParamRef | Sequence[Any] | bool | str
    """Whether to show a grid aligned with the scale's ticks. If true, show a grid with the currentColor stroke; if a string, show a grid with the specified stroke color; if an approximate number of ticks, an interval, or an array of tick values, show corresponding grid lines. See also the grid mark.

For axes only."""
    fy_inset: ParamRef | float
    """Shorthand to set the same default for all four insets: **insetTop**,
**insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it."""
    fy_inset_bottom: ParamRef | float
    """Insets the bottom edge by the specified number of pixels. A positive value insets towards the top edge (reducing effective area), while a negative value insets away from the top edge (increasing it)."""
    fy_inset_top: ParamRef | float
    """Insets the top edge by the specified number of pixels. A positive value insets towards the bottom edge (reducing effective area), while a negative value insets away from the bottom edge (increasing it)."""
    fy_label: ParamRef | str | None
    """A textual label to show on the axis or legend; if null, show no label. By default the scale label is inferred from channel definitions, possibly with an arrow (↑, →, ↓, or ←) to indicate the direction of increasing value.

For axes and legends only."""
    fy_label_anchor: L["bottom", "center", "left", "right", "top"] | ParamRef
    """Where to place the axis **label** relative to the plot's frame. For vertical position scales (*y* and *fy*), may be *top*, *bottom*, or
*center*; for horizontal position scales (*x* and *fx*), may be *left*,
*right*, or *center*. Defaults to *center* for ordinal scales (including
*fx* and *fy*), and otherwise *top* for *y*, and *right* for *x*."""
    fy_label_offset: ParamRef | float
    """The axis **label** position offset (in pixels); default depends on margins and orientation."""
    fy_line: ParamRef | bool
    """If true, draw a line along the axis; if false (default), do not."""
    fy_padding: ParamRef | float
    """For *band* scales, how much of the **range** to reserve to separate adjacent bands; defaults to 0.1 (10%). For *point* scales, the amount of inset for the first and last value as a proportion of the bandwidth; defaults to 0.5 (50%).

For ordinal position scales only."""
    fy_padding_inner: ParamRef | float
    """For a *band* scale, how much of the range to reserve to separate adjacent bands."""
    fy_padding_outer: ParamRef | float
    """For a *band* scale, how much of the range to reserve to inset first and last bands."""
    fy_range: Fixed | ParamRef | Sequence[Any]
    """The extent of the scale's outputs (visual values). By default inferred from the scale's **type** and **domain**, and the plot's dimensions. For ordinal position scales (*point* and *band*), it is typically [*min*, *max*]; it can be [*max*, *min*] to reverse the scale."""
    fy_reverse: ParamRef | bool
    """Whether to reverse the scale's encoding; equivalent to reversing either the
**domain** or **range**."""
    fy_round: ParamRef | bool
    """If true, round the output value to the nearest integer (pixel); useful for crisp edges when rendering.

For position scales only."""
    fy_tick_format: ParamRef | str | None
    """How to format inputs (abstract values) for axis tick labels; one of:

- a [d3-format][1] string for numeric scales
- a [d3-time-format][2] string for temporal scales

[1]: https://d3js.org/d3-time [2]: https://d3js.org/d3-time-format"""
    fy_tick_padding: ParamRef | float
    """The distance between an axis tick mark and its associated text label (in pixels); often defaults to 3, but may be affected by **fyTickSize** and
**fyTickRotate**."""
    fy_tick_rotate: ParamRef | float
    """The rotation angle of axis tick labels in degrees clocksize; defaults to 0."""
    fy_tick_size: ParamRef | float
    """The length of axis tick marks in pixels; negative values extend in the opposite direction. Defaults to 6 for *x* and *y* axes and *color* and
*opacity* *ramp* legends, and 0 for *fx* and *fy* axes."""
    fy_tick_spacing: ParamRef | float
    """The desired approximate spacing between adjacent axis ticks, affecting the default **ticks**; defaults to 80 pixels for *x* and *fx*, and 35 pixels for *y* and *fy*."""
    fy_ticks: Interval | ParamRef | Sequence[Any] | float
    """The desired approximate number of axis ticks, or an explicit array of tick values, or an interval such as *day* or *month*."""
    grid: ParamRef | bool | str
    """Whether to show a grid aligned with the scale's ticks. If true, show a grid with the currentColor stroke; if a string, show a grid with the specified stroke color; if an approximate number of ticks, an interval, or an array of tick values, show corresponding grid lines. See also the grid mark.

For axes only."""
    height: ParamRef | float
    """The outer height of the plot in pixels, including margins. The default depends on the plot's scales, and the plot's width if an aspectRatio is specified. For example, if the *y* scale is linear and there is no *fy* scale, it might be 396."""
    inset: ParamRef | float
    """Shorthand to set the same default for all four insets: **insetTop**,
**insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it."""
    length_base: ParamRef | float
    """A log scale's base; defaults to 10. Does not affect the scale's encoding, but rather the default ticks. For *log* scales only."""
    length_clamp: Any
    """If true, values below the domain minimum are treated as the domain minimum, and values above the domain maximum are treated as the domain maximum.

Clamping is useful for focusing on a subset of the data while ensuring that extreme values remain visible, but use caution: clamped values may need an annotation to avoid misinterpretation. Clamping typically requires setting an explicit **domain** since if the domain is inferred, no values will be outside the domain.

For continuous scales only."""
    length_constant: ParamRef | float
    """A symlog scale's constant, expressing the magnitude of the linear region around the origin; defaults to 1. For *symlog* scales only."""
    length_domain: Fixed | ParamRef | Sequence[Any]
    """The extent of the scale's inputs (abstract values). By default inferred from channel values. For continuous data (numbers and dates), it is typically [*min*, *max*]; it can be [*max*, *min*] to reverse the scale. For ordinal data (strings or booleans), it is an array (or iterable) of values is the desired order, defaulting to natural ascending order.

Linear scales have a default domain of [0, 1]. Log scales have a default domain of [1, 10] and cannot include zero. Radius scales have a default domain from 0 to the median first quartile of associated channels. Length have a default domain from 0 to the median median of associated channels. Opacity scales have a default domain from 0 to the maximum value of associated channels."""
    length_exponent: ParamRef | float
    """A power scale's exponent (*e.g.*, 0.5 for sqrt); defaults to 1 for a linear scale. For *pow* scales only."""
    length_nice: Interval | ParamRef | bool | float
    """If true, or a tick count or interval, extend the domain to nice round values. Defaults to 1, 2 or 5 times a power of 10 for *linear* scales, and nice time intervals for *utc* and *time* scales. Pass an interval such as
*minute*, *wednesday* or *month* to specify what constitutes a nice interval.

For continuous scales only."""
    length_percent: ParamRef | bool
    """If true, shorthand for a transform suitable for percentages, mapping proportions in [0, 1] to [0, 100]."""
    length_range: Fixed | ParamRef | Sequence[Any]
    """The extent of the scale's outputs (visual values). By default inferred from the scale's **type** and **domain**, and for position scales, the plot's dimensions. For continuous data (numbers and dates), and for ordinal position scales (*point* and *band*), it is typically [*min*, *max*]; it can be [*max*, *min*] to reverse the scale. For other ordinal data, such as for a *color* scale, it is an array (or iterable) of output values in the same order as the **domain**.

Length scales have a default range of [0, 12]."""
    length_scale: ContinuousScaleType | ParamRef | None
    """The *length* scale type, affecting how the scale encodes abstract data, say by applying a mathematical transformation. If null, the scale is disabled. The length scale defaults to *linear*, as this scale is intended for quantitative data."""
    length_zero: ParamRef | bool
    """Whether the **domain** must include zero. If the domain minimum is positive, it will be set to zero; otherwise if the domain maximum is negative, it will be set to zero.

For quantitative scales only."""
    margin: ParamRef | float
    """Shorthand to set the same default for all four margins: **marginTop**,
**marginRight**, **marginBottom**, and **marginLeft**. Otherwise, the default margins depend on the maximum margins of the plot's marks. While most marks default to zero margins (because they are drawn inside the chart area), Plot's axis marks have non-zero default margins."""
    margin_bottom: ParamRef | float
    """The bottom margin; the distance in pixels between the bottom edges of the inner and outer plot area. Defaults to the maximum bottom margin of the plot's marks."""
    margin_left: ParamRef | float
    """The left margin; the distance in pixels between the left edges of the inner and outer plot area. Defaults to the maximum left margin of the plot's marks."""
    margin_right: ParamRef | float
    """The right margin; the distance in pixels between the right edges of the inner and outer plot area. Defaults to the maximum right margin of the plot's marks."""
    margin_top: ParamRef | float
    """The top margin; the distance in pixels between the top edges of the inner and outer plot area. Defaults to the maximum top margin of the plot's marks."""
    margins: Margins
    """A shorthand object notation for setting multiple margin values. The object keys are margin names (top, right, etc)."""
    name: str
    """A unique name for the plot. The name is used by standalone legend components to to lookup the plot and access scale mappings."""
    opacity_base: ParamRef | float
    """A log scale's base; defaults to 10. Does not affect the scale's encoding, but rather the default ticks. For *log* scales only."""
    opacity_clamp: ParamRef | bool
    """If true, values below the domain minimum are treated as the domain minimum, and values above the domain maximum are treated as the domain maximum.

Clamping is useful for focusing on a subset of the data while ensuring that extreme values remain visible, but use caution: clamped values may need an annotation to avoid misinterpretation. Clamping typically requires setting an explicit **domain** since if the domain is inferred, no values will be outside the domain.

For continuous scales only."""
    opacity_constant: ParamRef | float
    """A symlog scale's constant, expressing the magnitude of the linear region around the origin; defaults to 1. For *symlog* scales only."""
    opacity_domain: Fixed | ParamRef | Sequence[Any]
    """The extent of the scale's inputs (abstract values). By default inferred from channel values. For continuous data (numbers and dates), it is typically [*min*, *max*]; it can be [*max*, *min*] to reverse the scale. For ordinal data (strings or booleans), it is an array (or iterable) of values is the desired order, defaulting to natural ascending order.

Opacity scales have a default domain from 0 to the maximum value of associated channels."""
    opacity_exponent: ParamRef | float
    """A power scale's exponent (*e.g.*, 0.5 for sqrt); defaults to 1 for a linear scale. For *pow* scales only."""
    opacity_label: ParamRef | str | None
    """A textual label to show on the axis or legend; if null, show no label. By default the scale label is inferred from channel definitions, possibly with an arrow (↑, →, ↓, or ←) to indicate the direction of increasing value.

For axes and legends only."""
    opacity_nice: Interval | ParamRef | bool | float
    """If true, or a tick count or interval, extend the domain to nice round values. Defaults to 1, 2 or 5 times a power of 10 for *linear* scales, and nice time intervals for *utc* and *time* scales. Pass an interval such as
*minute*, *wednesday* or *month* to specify what constitutes a nice interval.

For continuous scales only."""
    opacity_percent: ParamRef | bool
    """If true, shorthand for a transform suitable for percentages, mapping proportions in [0, 1] to [0, 100]."""
    opacity_range: Fixed | ParamRef | Sequence[Any]
    """The extent of the scale's outputs (visual values).

Opacity scales have a default range of [0, 1]."""
    opacity_reverse: ParamRef | bool
    """Whether to reverse the scale's encoding; equivalent to reversing either the
**domain** or **range**."""
    opacity_scale: ContinuousScaleType | ParamRef | None
    """The *opacity* scale type, affecting how the scale encodes abstract data, say by applying a mathematical transformation. If null, the scale is disabled. The opacity scale defaults to *linear*; this scales is intended for quantitative data."""
    opacity_tick_format: ParamRef | str | None
    """How to format inputs (abstract values) for axis tick labels; one of:

- a [d3-format][1] string for numeric scales
- a [d3-time-format][2] string for temporal scales

[1]: https://d3js.org/d3-time [2]: https://d3js.org/d3-time-format"""
    opacity_zero: ParamRef | bool
    """Whether the **domain** must include zero. If the domain minimum is positive, it will be set to zero; otherwise if the domain maximum is negative, it will be set to zero.

For quantitative scales only."""
    padding: ParamRef | float
    """For *band* scales, how much of the **range** to reserve to separate adjacent bands; defaults to 0.1 (10%). For *point* scales, the amount of inset for the first and last value as a proportion of the bandwidth; defaults to 0.5 (50%).

For ordinal position scales only."""
    projection_clip: L["frame"] | ParamRef | bool | float | None
    """The projection's clipping method; one of:

- *frame* or true (default) - clip to the plot's frame (including margins but not insets)
- a number - clip to a circle of the given radius in degrees centered around the origin
- null or false - do not clip

Some projections (such as [*armadillo*][1] and [*berghaus*][2]) require spherical clipping: in that case set the marks' **clip** option to
*sphere*.

[1]: https://observablehq.com/@d3/armadillo [2]: https://observablehq.com/@d3/berghaus-star"""
    projection_domain: Mapping[str, Any] | ParamRef
    """A GeoJSON object to fit to the plot's frame (minus insets); defaults to a Sphere for spherical projections (outline of the the whole globe)."""
    projection_inset: ParamRef | float
    """Shorthand to set the same default for all four projection insets. All insets typically default to zero, though not always. A positive inset reduces effective area, while a negative inset increases it."""
    projection_inset_bottom: ParamRef | float
    """Insets the bottom edge of the projection by the specified number of pixels. A positive value insets towards the top edge (reducing effective area), while a negative value insets away from the top edge (increasing it)."""
    projection_inset_left: ParamRef | float
    """Insets the left edge of the projection by the specified number of pixels. A positive value insets towards the right edge (reducing effective area), while a negative value insets away from the right edge (increasing it)."""
    projection_inset_right: ParamRef | float
    """Insets the right edge of the projection by the specified number of pixels. A positive value insets towards the left edge (reducing effective area), while a negative value insets away from the left edge (increasing it)."""
    projection_inset_top: ParamRef | float
    """Insets the top edge of the projection by the specified number of pixels. A positive value insets towards the bottom edge (reducing effective area), while a negative value insets away from the bottom edge (increasing it)."""
    projection_parallels: (
        ParamRef | tuple[A[ParamRef | float, L["y1"]], A[ParamRef | float, L["y2"]]]
    )
    """The [standard parallels][1]. For conic projections only.

[1]: https://d3js.org/d3-geo/conic#conic_parallels"""
    projection_precision: ParamRef | float
    """The projection's [sampling threshold][1].

[1]: https://d3js.org/d3-geo/projection#projection_precision"""
    projection_rotate: (
        ParamRef
        | tuple[
            A[ParamRef | float, L["x"]], A[ParamRef | float, L["y"]], A[ParamRef | float, L["z"]]
        ]
    )
    """A rotation of the sphere before projection; defaults to [0, 0, 0]. Specified as Euler angles λ (yaw, or reference longitude), φ (pitch, or reference latitude), and optionally γ (roll), in degrees."""
    projection_type: ParamRef | ProjectionName | None
    """The desired projection; one of:

- a named built-in projection such as *albers-usa*
- null, for no projection

Named projections are scaled and translated to fit the **domain** to the plot's frame (minus insets)."""
    r_base: ParamRef | float
    """A log scale's base; defaults to 10. Does not affect the scale's encoding, but rather the default ticks. For *log* scales only."""
    r_clamp: Any
    """If true, values below the domain minimum are treated as the domain minimum, and values above the domain maximum are treated as the domain maximum.

Clamping is useful for focusing on a subset of the data while ensuring that extreme values remain visible, but use caution: clamped values may need an annotation to avoid misinterpretation. Clamping typically requires setting an explicit **domain** since if the domain is inferred, no values will be outside the domain.

For continuous scales only."""
    r_constant: ParamRef | float
    """A symlog scale's constant, expressing the magnitude of the linear region around the origin; defaults to 1. For *symlog* scales only."""
    r_domain: Fixed | ParamRef | Sequence[Any]
    """The extent of the scale's inputs (abstract values). By default inferred from channel values. For continuous data (numbers and dates), it is typically [*min*, *max*]; it can be [*max*, *min*] to reverse the scale. For ordinal data (strings or booleans), it is an array (or iterable) of values is the desired order, defaulting to natural ascending order.

Radius scales have a default domain from 0 to the median first quartile of associated channels."""
    r_exponent: ParamRef | float
    """A power scale's exponent (*e.g.*, 0.5 for sqrt); defaults to 1 for a linear scale. For *pow* scales only."""
    r_label: ParamRef | str | None
    """A textual label to show on the axis or legend; if null, show no label. By default the scale label is inferred from channel definitions, possibly with an arrow (↑, →, ↓, or ←) to indicate the direction of increasing value."""
    r_nice: Interval | ParamRef | bool | float
    """If true, or a tick count or interval, extend the domain to nice round values. Defaults to 1, 2 or 5 times a power of 10 for *linear* scales, and nice time intervals for *utc* and *time* scales. Pass an interval such as
*minute*, *wednesday* or *month* to specify what constitutes a nice interval.

For continuous scales only."""
    r_percent: ParamRef | bool
    """If true, shorthand for a transform suitable for percentages, mapping proportions in [0, 1] to [0, 100]."""
    r_range: Fixed | ParamRef | Sequence[Any]
    """The extent of the scale's outputs (visual values). By default inferred from the scale's **type** and **domain**, and for position scales, the plot's dimensions. For continuous data (numbers and dates), and for ordinal position scales (*point* and *band*), it is typically [*min*, *max*]; it can be [*max*, *min*] to reverse the scale. For other ordinal data, such as for a *color* scale, it is an array (or iterable) of output values in the same order as the **domain**.

Radius scales have a default range of [0, 3]."""
    r_scale: ContinuousScaleType | ParamRef | None
    """The *r* (radius) scale type, affecting how the scale encodes abstract data, say by applying a mathematical transformation. If null, the scale is disabled. The radius scale defaults to *sqrt*; this scale is intended for quantitative data."""
    r_zero: ParamRef | bool
    """Whether the **domain** must include zero. If the domain minimum is positive, it will be set to zero; otherwise if the domain maximum is negative, it will be set to zero.

For quantitative scales only."""
    style: CSSStyles | ParamRef | str | None
    """Custom styles to override Plot's defaults. Styles may be specified either as a string of inline styles (*e.g.*, `"color: red;"`, in the same fashion as assigning [*element*.style][1]) or an object of properties (*e.g.*, `{color: "red"}`, in the same fashion as assigning [*element*.style properties][2]). Note that unitless numbers ([quirky lengths][3]) such as `{padding: 20}` may not supported by some browsers; you should instead specify a string with units such as `{padding: "20px"}`. By default, the returned plot has a max-width of 100%, and the system-ui font. Plot's marks and axes default to [currentColor][4], meaning that they will inherit the surrounding content's color.

[1]: https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style [2]: https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleDeclaration [3]: https://www.w3.org/TR/css-values-4/#deprecated-quirky-length [4]: https://developer.mozilla.org/en-US/docs/Web/CSS/color_value#currentcolor_keyword"""
    symbol_domain: Fixed | ParamRef | Sequence[Any]
    """The extent of the scale's inputs (abstract values). By default inferred from channel values. As symbol scales are discrete, the domain is an array (or iterable) of values is the desired order, defaulting to natural ascending order."""
    symbol_range: Fixed | ParamRef | Sequence[Any]
    """The extent of the scale's outputs (visual values). By default inferred from the scale's **type** and **domain**, and for position scales, the plot's dimensions. For continuous data (numbers and dates), and for ordinal position scales (*point* and *band*), it is typically [*min*, *max*]; it can be [*max*, *min*] to reverse the scale. For other ordinal data, such as for a *color* scale, it is an array (or iterable) of output values in the same order as the **domain**.

Symbol scales have a default range of categorical symbols; the choice of symbols depends on whether the associated dot mark is filled or stroked."""
    symbol_scale: DiscreteScaleType | ParamRef | None
    """The *symbol* scale type, affecting how the scale encodes abstract data, say by applying a mathematical transformation. If null, the scale is disabled. Defaults to an *ordinal* scale type."""
    width: ParamRef | float
    """The outer width of the plot in pixels, including margins. Defaults to 640. On Observable, this can be set to the built-in [width][1] for full-width responsive plots. Note: the default style has a max-width of 100%; the plot will automatically shrink to fit even when a fixed width is specified.

[1]: https://github.com/observablehq/stdlib/blob/main/README.md#width"""
    x_align: ParamRef | float
    """How to distribute unused space in the **range** for *point* and *band* scales. A number in [0, 1], such as:

- 0 - use the start of the range, putting unused space at the end
- 0.5 (default) - use the middle, distributing unused space evenly
- 1 use the end, putting unused space at the start

For ordinal position scales only."""
    x_aria_description: ParamRef | str
    """A textual description for the axis in the accessibility tree."""
    x_aria_label: ParamRef | str
    """A short label representing the axis in the accessibility tree."""
    x_axis: L["both", "bottom", "top"] | ParamRef | bool | None
    """The side of the frame on which to place the implicit axis: *top* or
*bottom* for *x*. Defaults to *bottom* for an *x* scale.

If *both*, an implicit axis will be rendered on both sides of the plot (*top* and *bottom* for *x*). If null, the implicit axis is suppressed."""
    x_base: ParamRef | float
    """A log scale's base; defaults to 10. Does not affect the scale's encoding, but rather the default ticks. For *log* scales only."""
    x_clamp: ParamRef | bool
    """If true, values below the domain minimum are treated as the domain minimum, and values above the domain maximum are treated as the domain maximum.

Clamping is useful for focusing on a subset of the data while ensuring that extreme values remain visible, but use caution: clamped values may need an annotation to avoid misinterpretation. Clamping typically requires setting an explicit **domain** since if the domain is inferred, no values will be outside the domain.

For continuous scales only."""
    x_constant: ParamRef | float
    """A symlog scale's constant, expressing the magnitude of the linear region around the origin; defaults to 1. For *symlog* scales only."""
    x_domain: Fixed | ParamRef | Sequence[Any]
    """The extent of the scale's inputs (abstract values). By default inferred from channel values. For continuous data (numbers and dates), it is typically [*min*, *max*]; it can be [*max*, *min*] to reverse the scale. For ordinal data (strings or booleans), it is an array (or iterable) of values is the desired order, defaulting to natural ascending order.

Linear scales have a default domain of [0, 1]. Log scales have a default domain of [1, 10] and cannot include zero. Radius scales have a default domain from 0 to the median first quartile of associated channels. Length have a default domain from 0 to the median median of associated channels. Opacity scales have a default domain from 0 to the maximum value of associated channels."""
    x_exponent: ParamRef | float
    """A power scale's exponent (*e.g.*, 0.5 for sqrt); defaults to 1 for a linear scale. For *pow* scales only."""
    x_font_variant: ParamRef | str
    """The font-variant attribute for axis ticks; defaults to *tabular-nums* for quantitative axes."""
    x_grid: Interval | ParamRef | Sequence[Any] | bool | str
    """Whether to show a grid aligned with the scale's ticks. If true, show a grid with the currentColor stroke; if a string, show a grid with the specified stroke color; if an approximate number of ticks, an interval, or an array of tick values, show corresponding grid lines. See also the grid mark.

For axes only."""
    x_inset: ParamRef | float
    """Shorthand to set the same default for all four insets: **insetTop**,
**insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it."""
    x_inset_left: ParamRef | float
    """Insets the left edge by the specified number of pixels. A positive value insets towards the right edge (reducing effective area), while a negative value insets away from the right edge (increasing it)."""
    x_inset_right: ParamRef | float
    """Insets the right edge by the specified number of pixels. A positive value insets towards the left edge (reducing effective area), while a negative value insets away from the left edge (increasing it)."""
    x_label: ParamRef | str | None
    """A textual label to show on the axis or legend; if null, show no label. By default the scale label is inferred from channel definitions, possibly with an arrow (↑, →, ↓, or ←) to indicate the direction of increasing value.

For axes and legends only."""
    x_label_anchor: L["bottom", "center", "left", "right", "top"] | ParamRef
    """Where to place the axis **label** relative to the plot's frame. For vertical position scales (*y* and *fy*), may be *top*, *bottom*, or
*center*; for horizontal position scales (*x* and *fx*), may be *left*,
*right*, or *center*. Defaults to *center* for ordinal scales (including
*fx* and *fy*), and otherwise *top* for *y*, and *right* for *x*."""
    x_label_arrow: LabelArrow | ParamRef
    """Whether to apply a directional arrow such as → or ↑ to the x-axis scale label. If *auto* (the default), the presence of the arrow depends on whether the scale is ordinal."""
    x_label_offset: ParamRef | float
    """The axis **label** position offset (in pixels); default depends on margins and orientation."""
    x_line: ParamRef | bool
    """If true, draw a line along the axis; if false (default), do not."""
    x_nice: Interval | ParamRef | bool | float
    """If true, or a tick count or interval, extend the domain to nice round values. Defaults to 1, 2 or 5 times a power of 10 for *linear* scales, and nice time intervals for *utc* and *time* scales. Pass an interval such as
*minute*, *wednesday* or *month* to specify what constitutes a nice interval.

For continuous scales only."""
    x_padding: ParamRef | float
    """For *band* scales, how much of the **range** to reserve to separate adjacent bands; defaults to 0.1 (10%). For *point* scales, the amount of inset for the first and last value as a proportion of the bandwidth; defaults to 0.5 (50%).

For ordinal position scales only."""
    x_padding_inner: ParamRef | float
    """For a *band* scale, how much of the range to reserve to separate adjacent bands."""
    x_padding_outer: ParamRef | float
    """For a *band* scale, how much of the range to reserve to inset first and last bands."""
    x_percent: ParamRef | bool
    """If true, shorthand for a transform suitable for percentages, mapping proportions in [0, 1] to [0, 100]."""
    x_range: Fixed | ParamRef | Sequence[Any]
    """The extent of the scale's outputs (visual values). By default inferred from the scale's **type** and **domain**, and for position scales, the plot's dimensions. For continuous data (numbers and dates), and for ordinal position scales (*point* and *band*), it is typically [*min*, *max*]; it can be [*max*, *min*] to reverse the scale."""
    x_reverse: ParamRef | bool
    """Whether to reverse the scale's encoding; equivalent to reversing either the
**domain** or **range**."""
    x_round: ParamRef | bool
    """If true, round the output value to the nearest integer (pixel); useful for crisp edges when rendering.

For position scales only."""
    x_scale: ParamRef | PositionScaleType | None
    """The *x* scale type, affecting how the scale encodes abstract data, say by applying a mathematical transformation. If null, the scale is disabled.

For quantitative data (numbers), defaults to *linear*; for temporal data (dates), defaults to *utc*; for ordinal data (strings or booleans), defaults to *point* for position scales, *categorical* for color scales, and otherwise *ordinal*. However, the radius scale defaults to *sqrt*, and the length and opacity scales default to *linear*; these scales are intended for quantitative data. The plot's marks may also impose a scale type; for example, the barY mark requires that *x* is a *band* scale."""
    x_tick_format: ParamRef | str | None
    """How to format inputs (abstract values) for axis tick labels; one of:

- a [d3-format][1] string for numeric scales
- a [d3-time-format][2] string for temporal scales

[1]: https://d3js.org/d3-time [2]: https://d3js.org/d3-time-format"""
    x_tick_padding: ParamRef | float
    """The distance between an axis tick mark and its associated text label (in pixels); often defaults to 3, but may be affected by **xTickSize** and
**xTickRotate**."""
    x_tick_rotate: ParamRef | float
    """The rotation angle of axis tick labels in degrees clocksize; defaults to 0."""
    x_tick_size: ParamRef | float
    """The length of axis tick marks in pixels; negative values extend in the opposite direction. Defaults to 6 for *x* and *y* axes and *color* and
*opacity* *ramp* legends, and 0 for *fx* and *fy* axes."""
    x_tick_spacing: ParamRef | float
    """The desired approximate spacing between adjacent axis ticks, affecting the default **ticks**; defaults to 80 pixels for *x* and *fx*, and 35 pixels for *y* and *fy*."""
    x_ticks: Interval | ParamRef | Sequence[Any] | float
    """The desired approximate number of axis ticks, or an explicit array of tick values, or an interval such as *day* or *month*."""
    x_zero: ParamRef | bool
    """Whether the **domain** must include zero. If the domain minimum is positive, it will be set to zero; otherwise if the domain maximum is negative, it will be set to zero.

For quantitative scales only."""
    xy_domain: Fixed | ParamRef | Sequence[Any]
    """Set the *x* and *y* scale domains."""
    y_align: ParamRef | float
    """How to distribute unused space in the **range** for *point* and *band* scales. A number in [0, 1], such as:

- 0 - use the start of the range, putting unused space at the end
- 0.5 (default) - use the middle, distributing unused space evenly
- 1 use the end, putting unused space at the start

For ordinal position scales only."""
    y_aria_description: ParamRef | str
    """A textual description for the axis in the accessibility tree."""
    y_aria_label: ParamRef | str
    """A short label representing the axis in the accessibility tree."""
    y_axis: L["both", "left", "right"] | ParamRef | bool | None
    """The side of the frame on which to place the implicit axis: *left* or
*right* for *y*. Defaults to *left* for a *y* scale.

If *both*, an implicit axis will be rendered on both sides of the plot (*left* and *right* for *y*). If null, the implicit axis is suppressed."""
    y_base: ParamRef | float
    """A log scale's base; defaults to 10. Does not affect the scale's encoding, but rather the default ticks. For *log* scales only."""
    y_clamp: ParamRef | bool
    """If true, values below the domain minimum are treated as the domain minimum, and values above the domain maximum are treated as the domain maximum.

Clamping is useful for focusing on a subset of the data while ensuring that extreme values remain visible, but use caution: clamped values may need an annotation to avoid misinterpretation. Clamping typically requires setting an explicit **domain** since if the domain is inferred, no values will be outside the domain.

For continuous scales only."""
    y_constant: ParamRef | float
    """A symlog scale's constant, expressing the magnitude of the linear region around the origin; defaults to 1. For *symlog* scales only."""
    y_domain: Fixed | ParamRef | Sequence[Any]
    """The extent of the scale's inputs (abstract values). By default inferred from channel values. For continuous data (numbers and dates), it is typically [*min*, *max*]; it can be [*max*, *min*] to reverse the scale. For ordinal data (strings or booleans), it is an array (or iterable) of values is the desired order, defaulting to natural ascending order.

Linear scales have a default domain of [0, 1]. Log scales have a default domain of [1, 10] and cannot include zero."""
    y_exponent: ParamRef | float
    """A power scale's exponent (*e.g.*, 0.5 for sqrt); defaults to 1 for a linear scale. For *pow* scales only."""
    y_font_variant: ParamRef | str
    """The font-variant attribute for axis ticks; defaults to *tabular-nums* for quantitative axes."""
    y_grid: Interval | ParamRef | Sequence[Any] | bool | str
    """Whether to show a grid aligned with the scale's ticks. If true, show a grid with the currentColor stroke; if a string, show a grid with the specified stroke color; if an approximate number of ticks, an interval, or an array of tick values, show corresponding grid lines. See also the grid mark.

For axes only."""
    y_inset: ParamRef | float
    """Shorthand to set the same default for all four insets: **insetTop**,
**insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it."""
    y_inset_bottom: ParamRef | float
    """Insets the bottom edge by the specified number of pixels. A positive value insets towards the top edge (reducing effective area), while a negative value insets away from the top edge (increasing it)."""
    y_inset_top: ParamRef | float
    """Insets the top edge by the specified number of pixels. A positive value insets towards the bottom edge (reducing effective area), while a negative value insets away from the bottom edge (increasing it)."""
    y_label: ParamRef | str | None
    """A textual label to show on the axis or legend; if null, show no label. By default the scale label is inferred from channel definitions, possibly with an arrow (↑, →, ↓, or ←) to indicate the direction of increasing value.

For axes and legends only."""
    y_label_anchor: L["bottom", "center", "left", "right", "top"] | ParamRef
    """Where to place the axis **label** relative to the plot's frame. For vertical position scales (*y* and *fy*), may be *top*, *bottom*, or
*center*; for horizontal position scales (*x* and *fx*), may be *left*,
*right*, or *center*. Defaults to *center* for ordinal scales (including
*fx* and *fy*), and otherwise *top* for *y*, and *right* for *x*."""
    y_label_arrow: LabelArrow | ParamRef
    """Whether to apply a directional arrow such as → or ↑ to the x-axis scale label. If *auto* (the default), the presence of the arrow depends on whether the scale is ordinal."""
    y_label_offset: ParamRef | float
    """The axis **label** position offset (in pixels); default depends on margins and orientation."""
    y_line: ParamRef | bool
    """If true, draw a line along the axis; if false (default), do not."""
    y_nice: Interval | ParamRef | bool | float
    """If true, or a tick count or interval, extend the domain to nice round values. Defaults to 1, 2 or 5 times a power of 10 for *linear* scales, and nice time intervals for *utc* and *time* scales. Pass an interval such as
*minute*, *wednesday* or *month* to specify what constitutes a nice interval.

For continuous scales only."""
    y_padding: ParamRef | float
    """For *band* scales, how much of the **range** to reserve to separate adjacent bands; defaults to 0.1 (10%). For *point* scales, the amount of inset for the first and last value as a proportion of the bandwidth; defaults to 0.5 (50%).

For ordinal position scales only."""
    y_padding_inner: ParamRef | float
    """For a *band* scale, how much of the range to reserve to separate adjacent bands."""
    y_padding_outer: ParamRef | float
    """For a *band* scale, how much of the range to reserve to inset first and last bands."""
    y_percent: ParamRef | bool
    """If true, shorthand for a transform suitable for percentages, mapping proportions in [0, 1] to [0, 100]."""
    y_range: Fixed | ParamRef | Sequence[Any]
    """The extent of the scale's outputs (visual values). By default inferred from the scale's **type** and **domain**, and for position scales, the plot's dimensions. For continuous data (numbers and dates), and for ordinal position scales (*point* and *band*), it is typically [*min*,
*max*]; it can be [*max*, *min*] to reverse the scale."""
    y_reverse: ParamRef | bool
    """Whether to reverse the scale's encoding; equivalent to reversing either the
**domain** or **range**. Note that by default, when the *y* scale is continuous, the *max* value points to the top of the screen, whereas ordinal values are ranked from top to bottom."""
    y_round: ParamRef | bool
    """If true, round the output value to the nearest integer (pixel); useful for crisp edges when rendering.

For position scales only."""
    y_scale: ParamRef | PositionScaleType | None
    """The *y* scale type, affecting how the scale encodes abstract data, say by applying a mathematical transformation. If null, the scale is disabled.

For quantitative data (numbers), defaults to *linear*; for temporal data (dates), defaults to *utc*; for ordinal data (strings or booleans), defaults to *point* for position scales,  The plot's marks may also impose a scale type; for example, the barY mark requires that *x* is a *band* scale."""
    y_tick_format: ParamRef | str | None
    """How to format inputs (abstract values) for axis tick labels; one of:

- a [d3-format][1] string for numeric scales
- a [d3-time-format][2] string for temporal scales

[1]: https://d3js.org/d3-time [2]: https://d3js.org/d3-time-format"""
    y_tick_padding: ParamRef | float
    """The distance between an axis tick mark and its associated text label (in pixels); often defaults to 3, but may be affected by **yTickSize** and
**yTickRotate**."""
    y_tick_rotate: ParamRef | float
    """The rotation angle of axis tick labels in degrees clocksize; defaults to 0."""
    y_tick_size: ParamRef | float
    """The length of axis tick marks in pixels; negative values extend in the opposite direction. Defaults to 6 for *x* and *y* axes and *color* and
*opacity* *ramp* legends, and 0 for *fx* and *fy* axes."""
    y_tick_spacing: ParamRef | float
    """The desired approximate spacing between adjacent axis ticks, affecting the default **ticks**; defaults to 80 pixels for *x* and *fx*, and 35 pixels for *y* and *fy*."""
    y_ticks: Interval | ParamRef | Sequence[Any] | float
    """The desired approximate number of axis ticks, or an explicit array of tick values, or an interval such as *day* or *month*."""
    y_zero: ParamRef | bool
    """Whether the **domain** must include zero. If the domain minimum is positive, it will be set to zero; otherwise if the domain maximum is negative, it will be set to zero.

For quantitative scales only."""


class PlotAttributes(_PlotAttributesOpen, closed=True): ...


class _PlotOpen(_PlotAttributesOpen):
    """A plot component."""

    plot: Required[Sequence[PlotInteractor | PlotLegend | PlotMark]]
    """An array of plot marks, interactors, or legends. Marks are graphical elements that make up plot layers. Unless otherwise configured, interactors will use the nearest previous mark as a basis for which data fields to select."""


class Plot(_PlotOpen, closed=True): ...


__all__ = ("Margins", "Plot", "PlotAttributes")
