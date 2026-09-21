"""Manual defs for partial options."""

from __future__ import annotations

from typing import TYPE_CHECKING, Generic, Literal as L

import mosaic_spec as ms
from mosaic_spec._gen.marks import _MarkOptions
from mosaic_spec._typing_compat import TypeAliasType, TypedDict, TypeVar

if TYPE_CHECKING:
    from mosaic_spec import ParamRef

_CurveT = TypeVar("_CurveT")


class InsetOptions(TypedDict, total=False):
    inset: ParamRef | float
    """Shorthand to set the same default for all four insets: **insetTop**,
    **insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it.
    """
    inset_bottom: ParamRef | float
    """Insets the bottom edge by the specified number of pixels. A positive value insets towards the top edge (reducing effective area), while a negative value insets away from the top edge (increasing it)."""
    inset_left: ParamRef | float
    """Insets the left edge by the specified number of pixels. A positive value insets towards the right edge (reducing effective area), while a negative value insets away from the right edge (increasing it)."""
    inset_right: ParamRef | float
    """Insets the right edge by the specified number of pixels. A positive value insets towards the left edge (reducing effective area), while a negative value insets away from the left edge (increasing it)."""
    inset_top: ParamRef | float
    """Insets the top edge by the specified number of pixels. A positive value insets towards the bottom edge (reducing effective area), while a negative value insets away from the bottom edge (increasing it)."""


class _Curve(TypedDict, Generic[_CurveT], total=False):
    curve: _CurveT | ParamRef
    """The curve (interpolation) method for connecting adjacent points.

    One of:
    - *basis* - a cubic basis spline (repeating the end points)
    - *basis-open* - an open cubic basis spline
    - *basis-closed* - a closed cubic basis spline
    - *bump-x* - a Bézier curve with horizontal tangents
    - *bump-y* - a Bézier curve with vertical tangents
    - *bundle* - a straightened cubic basis spline (suitable for lines only, not areas)
    - *cardinal* - a cubic cardinal spline (with one-sided differences at the ends)
    - *cardinal-open* - an open cubic cardinal spline
    - *cardinal-closed* - an closed cubic cardinal spline
    - *catmull-rom* - a cubic Catmull-Rom spline (with one-sided differences at the ends)
    - *catmull-rom-open* - an open cubic Catmull-Rom spline
    - *catmull-rom-closed* - a closed cubic Catmull-Rom spline
    - *linear* - a piecewise linear curve (*i.e.*, straight line segments)
    - *linear-closed* - a closed piecewise linear curve (*i.e.*, straight line segments)
    - *monotone-x* - a cubic spline that preserves monotonicity in *x*
    - *monotone-y* - a cubic spline that preserves monotonicity in *y*
    - *natural* - a natural cubic spline
    - *step* - a piecewise constant function where *y* changes at the midpoint of *x*
    - *step-after* - a piecewise constant function where *y* changes after *x*
    - *step-before* - a piecewise constant function where *x* changes after *y*
    """

    tension: ParamRef | float
    """The tension option only has an effect on bundle, cardinal and Catmull-Rom splines (*bundle*, *cardinal*, *cardinal-open*, *cardinal-closed*,
    *catmull-rom*, *catmull-rom-open*, and *catmull-rom-closed*). For bundle splines, it corresponds to [beta][1]; for cardinal splines, [tension][2]; for Catmull-Rom splines, [alpha][3].

    [1]: https://d3js.org/d3-shape/curve#curveBundle_beta [2]: https://d3js.org/d3-shape/curve#curveCardinal_tension [3]: https://d3js.org/d3-shape/curve#curveCatmullRom_alpha
    """


class CurveOptions(_Curve[ms.Curve]): ...


class CurveAutoOptions(_Curve[ms.Curve | L["auto"]]): ...


class StackOptions(TypedDict, total=False):
    offset: ParamRef | ms.StackOffset | None
    """After stacking, an optional **offset** can be applied to translate and scale stacks, say to produce a streamgraph; defaults to null for a zero baseline (**y** = 0 for stackY, and **x** = 0 for stackX). If the *wiggle* offset is used, the default **order** changes to *inside-out*."""
    order: ParamRef | ms.StackOrder | None
    """The order in which stacks are layered.

    One of:
    - null (default) for input order
    - a named stack order method such as *inside-out* or *sum*
    - a field name, for natural order of the corresponding values
    - a function of data, for natural order of the corresponding values
    - an array of explicit **z** values in the desired order

    If the *wiggle* **offset** is used, as for a streamgraph, the default changes to *inside-out*.
    """
    # `StackOptions` also defines `reverse`, but that's already in `_MarkOptions`
    z: ms.ChannelValue
    """The **z** channel defines the series of each value in the stack. Used when the **order** is *sum*, *appearance*, *inside-out*, or an explicit array of
    **z** values.
    """


class RectCornerOptions(TypedDict, total=False):
    rx: ParamRef | float | str
    """The rounded corner [*x*-radius][1], either in pixels or as a percentage of the rect width. If **rx** is not specified, it defaults to **ry** if present, and otherwise draws square corners.

    [1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/rx
    """
    ry: ParamRef | float | str
    """The rounded corner [*y*-radius][1], either in pixels or as a percentage of the rect height. If **ry** is not specified, it defaults to **rx** if present, and otherwise draws square corners.

    [1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/ry
    """


_RectXT = TypeVar("_RectXT", ms.ChannelValueSpec, ms.ChannelValueIntervalSpec)
_RectYT = TypeVar("_RectYT", ms.ChannelValueSpec, ms.ChannelValueIntervalSpec)


class _RectOptions(
    _MarkOptions,
    InsetOptions,
    RectCornerOptions,
    StackOptions,
    Generic[_RectXT, _RectYT],
    total=False,
    closed=True,
):
    """Options for marks that render rectangles, including bar, cell, and rect."""

    x: _RectXT
    """The horizontal position (or length/width) channel, typically bound to the
    *x* scale.

    If an **interval** is specified, then **x1** and **x2** are derived from
    **x**, representing the lower and upper bound of the containing interval, respectively. For example, for a vertical bar chart of items sold by day:

    ```js Plot.rectY(sales, {x: "date", interval: "day", y2: "items"}) ```

    If *x* represents ordinal values, use a bar or cell mark instead.
    """
    x1: ms.ChannelValueSpec
    """The required primary (starting, often left) horizontal position channel, typically bound to the *x* scale. Setting this option disables the rectX mark's implicit stackX transform.

    If *x* represents ordinal values, use a bar or cell mark instead.
    """
    x2: ms.ChannelValueSpec
    """The required secondary (ending, often right) horizontal position channel, typically bound to the *x* scale. Setting this option disables the rectX mark's implicit stackX transform.

    If *x* represents ordinal values, use a bar or cell mark instead.
    """
    y: _RectYT
    """The vertical position (or length/height) channel, typically bound to the
    *y* scale.

    If an **interval** is specified, then **y1** and **y2** are derived from
    **y**, representing the lower and upper bound of the containing interval, respectively. For example, for a horizontal bar chart of items sold by day:

    ```js Plot.rectX(sales, {y: "date", interval: "day", x2: "items"}) ```

    If *y* represents ordinal values, use a bar or cell mark instead.
    """
    y1: ms.ChannelValueSpec
    """The required primary (starting, often bottom) vertical position channel, typically bound to the *y* scale. Setting this option disables the rectY mark's implicit stackY transform.

    If *y* represents ordinal values, use a bar or cell mark instead.
    """
    y2: ms.ChannelValueSpec
    """The required secondary (ending, often top) vertical position channel, typically bound to the *y* scale. Setting this option disables the rectY mark's implicit stackY transform.

    If *y* represents ordinal values, use a bar or cell mark instead.
    """
    interval: ms.Interval | ParamRef
    """How to convert a continuous value (**x** for rectY, **y** for rectX, or both for rect) into an interval (**x1** and **x2** for rectY, or **y1** and
    **y2** for rectX, or both for rect); one of:

    - a named time interval such as *day* (for date intervals)
    - a number (for number intervals), defining intervals at integer multiples of *n*

    Setting this option disables the implicit stack transform (stackX for rectX, or stackY for rectY).
    """


# NOTE: Defines everything except `mark` and `data`
RectOptions = TypeAliasType(
    "RectOptions", _RectOptions[ms.ChannelValueIntervalSpec, ms.ChannelValueIntervalSpec]
)
RectXOptions = TypeAliasType(
    "RectXOptions", _RectOptions[ms.ChannelValueSpec, ms.ChannelValueIntervalSpec]
)
RectYOptions = TypeAliasType(
    "RectYOptions", _RectOptions[ms.ChannelValueIntervalSpec, ms.ChannelValueSpec]
)
