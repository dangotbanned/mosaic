# Generated: `mosaic_spec._gen.marks`
from __future__ import annotations

from collections.abc import Mapping
from collections.abc import Sequence
from mosaic_spec._gen.expression import AggregateExpression
from mosaic_spec._gen.expression import SQLExpression
from mosaic_spec._gen.params import ParamRef
from mosaic_spec._gen.plot_from import PlotMarkData
from mosaic_spec._gen.transform import Transform
from mosaic_spec._gen.typing import ChannelDomainValue
from mosaic_spec._gen.typing import ChannelName
from mosaic_spec._gen.typing import Curve
from mosaic_spec._gen.typing import FrameAnchor
from mosaic_spec._gen.typing import GridInterpolate
from mosaic_spec._gen.typing import Interval
from mosaic_spec._gen.typing import MarkerName
from mosaic_spec._gen.typing import Reducer
from mosaic_spec._gen.typing import ScaleName
from mosaic_spec._gen.typing import SelectFilter
from mosaic_spec._gen.typing import StackOffset
from mosaic_spec._gen.typing import StackOrder
from mosaic_spec._gen.typing import SymbolType
from mosaic_spec._gen.typing import TipPointer
from mosaic_spec._gen.typing import VectorShape
from mosaic_spec._typing_compat import Required
from mosaic_spec._typing_compat import TypeAliasType
from mosaic_spec._typing_compat import TypedDict
from typing import Annotated as A
from typing import Any
from typing import Literal as L

class ChannelDomainValueSpec1(TypedDict,total=False,closed=True):
    """How to derive a scale's domain from a channel's values."""
    limit: float | tuple[A[float, L['lo']],A[float, L['hi']]]
    '''If a positive number, limit the domain to the first *n* sorted values. If a negative number, limit the domain to the last *-n* sorted values. Hence, a positive **limit** with **reverse** true will return the top *n* values in descending order.

If an array [*lo*, *hi*], slices the sorted domain from *lo* (inclusive) to
*hi* (exclusive). As with [*array*.slice][1], if either *lo* or *hi* are negative, it indicates an offset from the end of the array; if *lo* is undefined it defaults to 0, and if *hi* is undefined it defaults to Infinity.

Note: limiting the imputed domain of one scale, say *x*, does not affect the imputed domain of another scale, say *y*; each scale domain is imputed independently.

[1]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice'''
    order: L['ascending','descending',None]
    '''How to order reduced values.'''
    reduce: None | Reducer | bool
    '''How to produce a singular value (for subsequent sorting) from aggregated channel values; one of:

- true (default) - alias for *max*
- false or null - disabled; don't impute the scale domain
- a named reducer implementation such as *count* or *sum*
- a function that takes an array of values and returns the reduced value
- an object that implements the *reduceIndex* method'''
    reverse: bool
    '''If true, reverse the order after sorting.'''
    value: Required[ChannelDomainValue]
ChannelValue = TypeAliasType('ChannelValue', AggregateExpression | None | SQLExpression | Sequence[Any] | Transform | bool | float | str)
'''A channel's values may be expressed as:

- a field name, to extract the corresponding value for each datum
- an iterable of values, typically of the same length as the data
- a channel transform or SQL expression
- a constant number or boolean
- null to represent no value'''
class Format(TypedDict,total=False,closed=True):
    """How channel values are formatted for display. If a format is a string, it is interpreted as a (UTC) time format for temporal channels, and otherwise a number format."""
    aria_label: ParamRef | bool | str
    fill: ParamRef | bool | str
    fill_opacity: ParamRef | bool | str
    font_size: ParamRef | bool | str
    fx: ParamRef | bool | str
    fy: ParamRef | bool | str
    geometry: ParamRef | bool | str
    height: ParamRef | bool | str
    href: ParamRef | bool | str
    length: ParamRef | bool | str
    opacity: ParamRef | bool | str
    path: ParamRef | bool | str
    r: ParamRef | bool | str
    rotate: ParamRef | bool | str
    src: ParamRef | bool | str
    stroke: ParamRef | bool | str
    stroke_opacity: ParamRef | bool | str
    stroke_width: ParamRef | bool | str
    symbol: ParamRef | bool | str
    text: ParamRef | bool | str
    title: ParamRef | bool | str
    weight: ParamRef | bool | str
    width: ParamRef | bool | str
    x: ParamRef | bool | str
    x1: ParamRef | bool | str
    x2: ParamRef | bool | str
    y: ParamRef | bool | str
    y1: ParamRef | bool | str
    y2: ParamRef | bool | str
    z: ParamRef | bool | str
class SortOrder1(TypedDict,total=False,closed=True):
    """How to order values; one of:

- a function for comparing data, returning a signed number
- a channel value definition for sorting given values in ascending order
- a {value, order} object for sorting given values
- a {channel, order} object for sorting the named channel's values"""
    channel: ChannelName | L['-ariaLabel','-fill','-fillOpacity','-fontSize','-fx','-fy','-geometry','-height','-href','-length','-opacity','-path','-r','-rotate','-src','-stroke','-strokeOpacity','-strokeWidth','-symbol','-text','-title','-weight','-width','-x','-x1','-x2','-y','-y1','-y2','-z']
    order: L['ascending','descending']
ChannelDomainValueSpec = TypeAliasType('ChannelDomainValueSpec', ChannelDomainValue | ChannelDomainValueSpec1)
'''How to derive a scale's domain from a channel's values.'''
class ChannelValueIntervalSpec1(TypedDict,total=False,closed=True):
    """In some contexts, when specifying a mark channel's value, you can provide a {value, interval} object to specify an associated interval."""
    interval: Required[Interval]
    value: Required[ChannelValue]
class ChannelValueSpec1(TypedDict,total=False,closed=True):
    """When specifying a mark channel's value, you can provide a {value, scale} object to override the scale that would normally be associated with the channel."""
    label: str
    scale: L['auto'] | None | ScaleName | bool
    value: Required[ChannelValue]
class SortOrder2(TypedDict,total=False,closed=True):
    """How to order values; one of:

- a function for comparing data, returning a signed number
- a channel value definition for sorting given values in ascending order
- a {value, order} object for sorting given values
- a {channel, order} object for sorting the named channel's values"""
    order: L['ascending','descending']
    value: ChannelValue
class ChannelDomainSort(TypedDict,total=False,closed=True):
    """How to impute scale domains from channel values."""
    color: ChannelDomainValueSpec
    fx: ChannelDomainValueSpec
    fy: ChannelDomainValueSpec
    length: ChannelDomainValueSpec
    limit: float | tuple[A[float, L['lo']],A[float, L['hi']]]
    '''If a positive number, limit the domain to the first *n* sorted values. If a negative number, limit the domain to the last *-n* sorted values. Hence, a positive **limit** with **reverse** true will return the top *n* values in descending order.

If an array [*lo*, *hi*], slices the sorted domain from *lo* (inclusive) to
*hi* (exclusive). As with [*array*.slice][1], if either *lo* or *hi* are negative, it indicates an offset from the end of the array; if *lo* is undefined it defaults to 0, and if *hi* is undefined it defaults to Infinity.

Note: limiting the imputed domain of one scale, say *x*, does not affect the imputed domain of another scale, say *y*; each scale domain is imputed independently.

[1]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice'''
    opacity: ChannelDomainValueSpec
    order: L['ascending','descending',None]
    '''How to order reduced values.'''
    r: ChannelDomainValueSpec
    reduce: None | Reducer | bool
    '''How to produce a singular value (for subsequent sorting) from aggregated channel values; one of:

- true (default) - alias for *max*
- false or null - disabled; don't impute the scale domain
- a named reducer implementation such as *count* or *sum*
- a function that takes an array of values and returns the reduced value
- an object that implements the *reduceIndex* method'''
    reverse: bool
    '''If true, reverse the order after sorting.'''
    symbol: ChannelDomainValueSpec
    x: ChannelDomainValueSpec
    y: ChannelDomainValueSpec
ChannelValueSpec = TypeAliasType('ChannelValueSpec', ChannelValue | ChannelValueSpec1)
'''When specifying a mark channel's value, you can provide a {value, scale} object to override the scale that would normally be associated with the channel.'''
SortOrder = TypeAliasType('SortOrder', ChannelValue | SortOrder1 | SortOrder2)
'''How to order values; one of:

- a function for comparing data, returning a signed number
- a channel value definition for sorting given values in ascending order
- a {value, order} object for sorting given values
- a {channel, order} object for sorting the named channel's values'''
ChannelValueIntervalSpec = TypeAliasType('ChannelValueIntervalSpec', ChannelValueIntervalSpec1 | ChannelValueSpec)
'''In some contexts, when specifying a mark channel's value, you can provide a {value, interval} object to specify an associated interval.'''
class Tip(TypedDict,total=False,closed=True):
    """Whether to generate a tooltip for this mark, and any tip options."""
    anchor: FrameAnchor | ParamRef
    '''The tip anchor specifies how to orient the tip box relative to its anchor position; it refers to the part of the tip box that is attached to the anchor point. For example, the *top-left* anchor places the top-left corner of tip box near the anchor position, hence placing the tip box below and to the right of the anchor position.'''
    font_family: ParamRef | str
    '''The [font-family][1]; a constant; defaults to the plot's font family, which is typically [*system-ui*][2].

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-family [2]: https://drafts.csswg.org/css-fonts-4/#valdef-font-family-system-ui'''
    font_size: ChannelValue | ParamRef
    '''The [font size][1] in pixels; either a constant or a channel; defaults to the plot's font size, which is typically 10. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-size'''
    font_style: ParamRef | str
    '''The [font style][1]; a constant; defaults to the plot's font style, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-style'''
    font_variant: ParamRef | str
    '''The [font variant][1]; a constant; if the **text** channel contains numbers or dates, defaults to *tabular-nums* to facilitate comparing numbers; otherwise defaults to the plot's font style, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant'''
    font_weight: ParamRef | float | str
    '''The [font weight][1]; a constant; defaults to the plot's font weight, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight'''
    format: Format
    '''How channel values are formatted for display. If a format is a string, it is interpreted as a (UTC) time format for temporal channels, and otherwise a number format.'''
    frame_anchor: FrameAnchor | ParamRef
    '''The frame anchor specifies defaults for **x** and **y** based on the plot's frame; it may be one of the four sides (*top*, *right*, *bottom*, *left*), one of the four corners (*top-left*, *top-right*, *bottom-right*,
*bottom-left*), or the *middle* of the frame. For example, for tips distributed horizontally at the top of the frame:

```js Plot.tip(data, {x: "date", frameAnchor: "top"}) ```'''
    line_height: ParamRef | float
    '''The line height in ems; defaults to 1. The line height affects the (typically vertical) separation between adjacent baselines of text, as well as the separation between the text and its anchor point.'''
    line_width: ParamRef | float
    '''The line width in ems (e.g., 10 for about 20 characters); defaults to infinity, disabling wrapping and clipping.

If **textOverflow** is null, lines will be wrapped at the specified length. If a line is split at a soft hyphen (\xad), a hyphen (-) will be displayed at the end of the line. If **textOverflow** is not null, lines will be clipped according to the given strategy.'''
    monospace: ParamRef | bool
    '''If true, changes the default **fontFamily** to *monospace*, and uses simplified monospaced text metrics calculations.'''
    path_filter: ParamRef | str
    '''The image filter for the tip's box; defaults to a drop shadow.'''
    pointer: TipPointer
    pointer_size: ParamRef | float
    '''The size of the tip's pointer in pixels; defaults to 12.'''
    preferred_anchor: FrameAnchor | None | ParamRef
    '''If an explicit tip anchor is not specified, an anchor is chosen automatically such that the tip fits within the plot's frame; if the preferred anchor fits, it is chosen.'''
    text_anchor: L['end','middle','start'] | ParamRef
    '''The [text anchor][1] controls how text is aligned (typically horizontally) relative to its anchor point; it is one of *start*, *end*, or *middle*. If the frame anchor is *left*, *top-left*, or *bottom-left*, the default text anchor is *start*; if the frame anchor is *right*, *top-right*, or
*bottom-right*, the default is *end*; otherwise it is *middle*.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/text-anchor'''
    text_overflow: L['clip','clip-end','clip-start','ellipsis','ellipsis-end','ellipsis-middle','ellipsis-start'] | None | ParamRef
    '''How truncate (or wrap) lines of text longer than the given **lineWidth**; one of:

- null (default) - preserve overflowing characters (and wrap if needed)
- *clip* or *clip-end* - remove characters from the end
- *clip-start* - remove characters from the start
- *ellipsis* or *ellipsis-end* - replace characters from the end with an ellipsis (…)
- *ellipsis-start* - replace characters from the start with an ellipsis (…)
- *ellipsis-middle* - replace characters from the middle with an ellipsis (…)

If no **title** was specified, if text requires truncation, a title containing the non-truncated text will be implicitly added.'''
    text_padding: ParamRef | float
    '''The padding around the text in pixels; defaults to 8.'''
    x: ChannelValueSpec
    '''The horizontal position channel specifying the tip's anchor, typically bound to the *x* scale.'''
    x1: ChannelValueSpec
    '''The starting horizontal position channel specifying the tip's anchor, typically bound to the *x* scale.'''
    x2: ChannelValueSpec
    '''The ending horizontal position channel specifying the tip's anchor, typically bound to the *x* scale.'''
    y: ChannelValueSpec
    '''The vertical position channel specifying the tip's anchor, typically bound to the *y* scale.'''
    y1: ChannelValueSpec
    '''The starting vertical position channel specifying the tip's anchor, typically bound to the *y* scale.'''
    y2: ChannelValueSpec
    '''The ending vertical position channel specifying the tip's anchor, typically bound to the *y* scale.'''
class MarkOptions(TypedDict,total=False):
    """Shared options for all marks."""
    aria_description: ParamRef | str
    '''The [aria-description][1]; a constant textual description.

[1]: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-description'''
    aria_hidden: ParamRef | str
    '''The [aria-hidden][1] state; a constant indicating whether the element is exposed to an accessibility API.

[1]: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-hidden'''
    aria_label: ChannelValue
    '''The [aria-label][1]; a channel specifying short textual labels representing the value in the accessibility tree.

[1]: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-label'''
    channels: Mapping[str, str]
    '''Additional named channels, for example to include in a tooltip. Consists of (channel name, data field name) key-value pairs.'''
    clip: L['frame','sphere'] | None | ParamRef | bool
    '''How to clip the mark; one of:

- *frame* or true - clip to the plot's frame (inner area)
- *sphere* - clip to the projected sphere (*e.g.*, front hemisphere)
- null or false - do not clip

The *sphere* clip option requires a geographic projection.'''
    dx: ParamRef | float
    '''The horizontal offset in pixels; a constant option. On low-density screens, an additional 0.5px offset may be applied for crisp edges.'''
    dy: ParamRef | float
    '''The vertical offset in pixels; a constant option. On low-density screens, an additional 0.5px offset may be applied for crisp edges.'''
    facet: L['auto','exclude','include','super'] | None | ParamRef | bool
    '''Whether to enable or disable faceting; one of:

- *auto* (default) - automatically determine if this mark should be faceted
- *include* (or true) - draw the subset of the mark's data in the current facet
- *exclude* - draw the subset of the mark's data *not* in the current facet
- *super* - draw this mark in a single frame that covers all facets
- null (or false) - repeat this mark's data across all facets (*i.e.*, no faceting)

When a mark uses *super* faceting, it is not allowed to use position scales (*x*, *y*, *fx*, or *fy*); *super* faceting is intended for decorations, such as labels and legends.

When top-level faceting is used, the default *auto* setting is equivalent to *include* when the mark data is strictly equal to the top-level facet data; otherwise it is equivalent to null. When the *include* or *exclude* facet mode is chosen, the mark data must be parallel to the top-level facet data: the data must have the same length and order. If the data are not parallel, then the wrong data may be shown in each facet. The default
*auto* therefore requires strict equality (`===`) for safety, and using the facet data as mark data is recommended when using the *exclude* facet mode. (To construct parallel data safely, consider using [*array*.map][1] on the facet data.)

When mark-level faceting is used, the default *auto* setting is equivalent to *include*: the mark will be faceted if either the **fx** or **fy** channel option (or both) is specified. The null or false option will disable faceting, while *exclude* draws the subset of the mark's data *not* in the current facet.

[1]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map'''
    facet_anchor: L['bottom','bottom-empty','bottom-left','bottom-right','empty','left','left-empty','right','right-empty','top','top-empty','top-left','top-right'] | None | ParamRef
    '''How to place the mark with respect to facets; one of:

- null (default for most marks) - display the mark in each non-empty facet
- *top*, *right*, *bottom*, or *left* - display the mark only in facets on   the given side
- *top-empty*, *right-empty*, *bottom-empty*, or *left-empty* (default for   axis marks) - display the mark only in facets that have empty space on   the given side: either the margin, or an empty facet
- *empty* - display the mark in empty facets only'''
    fill: ChannelValueSpec | ParamRef
    '''The [fill][1]; a constant CSS color string, or a channel typically bound to the *color* scale. If all channel values are valid CSS colors, by default the channel will not be bound to the *color* scale, interpreting the colors literally.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/fill'''
    fill_opacity: ChannelValueSpec | ParamRef
    '''The [fill-opacity][1]; a constant number between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/fill-opacity'''
    filter: ChannelValue
    '''Applies a transform to filter the mark's index according to the given channel values; only truthy values are retained.

Note that filtering only affects the rendered mark index, not the associated channel values, and has no effect on imputed scale domains.'''
    fx: ChannelValue
    '''The horizontal facet position channel, for mark-level faceting, bound to the *fx* scale.'''
    fy: ChannelValue
    '''The vertical facet position channel, for mark-level faceting, bound to the
*fy* scale.'''
    href: ChannelValue
    '''The [href][1]; a channel specifying URLs for clickable links. May be used in conjunction with the **target** option to open links in another window.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/href'''
    image_filter: ParamRef | str
    '''A CSS [filter][1]; a constant string used to adjust the rendering of images, such as *blur(5px)*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/filter'''
    margin: ParamRef | float
    '''Shorthand to set the same default for all four mark margins: **marginTop**,
**marginRight**, **marginBottom**, and **marginLeft**; typically defaults to 0, except for axis marks.'''
    margin_bottom: ParamRef | float
    '''The mark's bottom margin; the minimum distance in pixels between the bottom edges of the inner and outer plot area.'''
    margin_left: ParamRef | float
    '''The mark's left margin; the minimum distance in pixels between the left edges of the inner and outer plot area.'''
    margin_right: ParamRef | float
    '''The mark's right margin; the minimum distance in pixels between the right edges of the mark's inner and outer plot area.'''
    margin_top: ParamRef | float
    '''The mark's top margin; the minimum distance in pixels between the top edges of the inner and outer plot area.'''
    mix_blend_mode: ParamRef | str
    '''The [mix-blend-mode][1]; a constant string specifying how to blend content such as *multiply*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/mix-blend-mode'''
    paint_order: ParamRef | str
    '''The [paint-order][1]; a constant string specifying the order in which the
**fill**, **stroke**, and any markers are drawn; defaults to *normal*, which draws the fill, then stroke, then markers; defaults to *stroke* for the text mark to create a “halo” around text to improve legibility.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/paint-order'''
    pointer_events: ParamRef | str
    '''The [pointer-events][1] property; a constant string such as *none*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/pointer-events'''
    reverse: ParamRef | bool
    '''Applies a transform to reverse the order of the mark's index, say for reverse input order.'''
    select: SelectFilter
    '''Applies a filter transform after data is loaded to highlight selected values only. For example, `first` and `last` select the first or last values of series only (using the *z* channel to separate series). Meanwhile, `nearestX` and `nearestY` select the point nearest to the pointer along the *x* or *y* channel dimension. Unlike Mosaic selections, a mark level *select* is internal to the mark only, and does not populate a param or selection value to be shared across clients.

Note that filtering only affects the rendered mark index, not the associated channel values, and has no effect on imputed scale domains.'''
    shape_rendering: ParamRef | str
    '''The [shape-rendering][1]; a constant string such as *crispEdges*.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/shape-rendering'''
    sort: ChannelDomainSort | SortOrder
    '''Either applies a transform to sort the mark's index by the specified channel values, or imputes ordinal scale domains from this mark's channels.

When imputing ordinal scale domains from channel values, the **sort** option is an object whose keys are ordinal scale names such as *x* or *fx*, and whose values are channel names such as *y*, *y1*, or *y2*. For example, to impute the *y* scale's domain from the associated *x* channel values in ascending order:

```js sort: {y: "x"} ```

For different sort options for different scales, replace the channel name with a *value* object and per-scale options:

```js sort: {y: {value: "-x"}} ```

When sorting the mark's index, the **sort** option is instead one of:

- a channel value definition for sorting given values in ascending order
- a {value, order} object for sorting given values
- a {channel, order} object for sorting the named channel's values'''
    stroke: ChannelValueSpec | ParamRef
    '''The [stroke][1]; a constant CSS color string, or a channel typically bound to the *color* scale. If all channel values are valid CSS colors, by default the channel will not be bound to the *color* scale, interpreting the colors literally.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/stroke'''
    stroke_dasharray: ParamRef | float | str
    '''The [stroke-dasharray][1]; a constant number indicating the length in pixels of alternating dashes and gaps, or a constant string of numbers separated by spaces or commas (_e.g._, *10 2* for dashes of 10 pixels separated by gaps of 2 pixels), or *none* (the default) for no dashing

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/stroke-dasharray'''
    stroke_dashoffset: ParamRef | float | str
    '''The [stroke-dashoffset][1]; a constant indicating the offset in pixels of the first dash along the stroke; defaults to zero.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/stroke-dashoffset'''
    stroke_linecap: ParamRef | str
    '''The [stroke-linecap][1]; a constant specifying how to cap stroked paths, such as *butt*, *round*, or *square*.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/stroke-linecap'''
    stroke_linejoin: ParamRef | str
    '''The [stroke-linejoin][1]; a constant specifying how to join stroked paths, such as *bevel*, *miter*, *miter-clip*, or *round*.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/stroke-linejoin'''
    stroke_miterlimit: ParamRef | float
    '''The [stroke-miterlimit][1]; a constant number specifying how to limit the length of *miter* joins on stroked paths.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/stroke-miterlimit'''
    stroke_opacity: ChannelValueSpec
    '''The [stroke-opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/stroke-opacity'''
    stroke_width: ChannelValueSpec
    '''The [stroke-width][1]; a constant number in pixels, or a channel.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/stroke-width'''
    target: ParamRef | str
    '''The [target][1]; a constant string specifying the target window (_e.g._,
*_blank*) for clickable links; used in conjunction with the **href** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/target'''
    tip: ParamRef | Tip | TipPointer | bool
    '''Whether to generate a tooltip for this mark, and any tip options.'''
    title: ChannelValue
    '''The title; a channel specifying accessible, short textual descriptions as strings (possibly with newlines). If the tip option is specified, the title will be displayed with an interactive tooltip instead of using the SVG [title element][1].

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Element/title'''
class _AreaOpen(MarkOptions,total=False):
    """The area mark."""
    curve: Curve | ParamRef
    '''The curve (interpolation) method for connecting adjacent points. One of:

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
- *step-before* - a piecewise constant function where *x* changes after *y*'''
    mark: Required[L['area']]
    '''An area mark. The area mark is rarely used directly; it is only needed when the baseline and topline have neither *x* nor *y* values in common. Use areaY for a horizontal orientation where the baseline and topline share *x* values, or areaX for a vertical orientation where the baseline and topline share *y* values.'''
    offset: None | ParamRef | StackOffset
    '''After stacking, an optional **offset** can be applied to translate and scale stacks, say to produce a streamgraph; defaults to null for a zero baseline (**y** = 0 for stackY, and **x** = 0 for stackX). If the *wiggle* offset is used, the default **order** changes to *inside-out*.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    order: None | ParamRef | StackOrder
    '''The order in which stacks are layered; one of:

- null (default) for input order
- a named stack order method such as *inside-out* or *sum*
- a field name, for natural order of the corresponding values
- a function of data, for natural order of the corresponding values
- an array of explicit **z** values in the desired order

If the *wiggle* **offset** is used, as for a streamgraph, the default changes to *inside-out*.'''
    tension: ParamRef | float
    '''The tension option only has an effect on bundle, cardinal and Catmull-Rom splines (*bundle*, *cardinal*, *cardinal-open*, *cardinal-closed*,
*catmull-rom*, *catmull-rom-open*, and *catmull-rom-closed*). For bundle splines, it corresponds to [beta][1]; for cardinal splines, [tension][2]; for Catmull-Rom splines, [alpha][3].

[1]: https://d3js.org/d3-shape/curve#curveBundle_beta [2]: https://d3js.org/d3-shape/curve#curveCardinal_tension [3]: https://d3js.org/d3-shape/curve#curveCatmullRom_alpha'''
    x1: ChannelValueSpec
    '''The required primary (starting, often left) horizontal position channel, representing the area's baseline, typically bound to the *x* scale. For areaX, setting this option disables the implicit stackX transform.'''
    x2: ChannelValueSpec
    '''The optional secondary (ending, often right) horizontal position channel, representing the area's topline, typically bound to the *x* scale; if not specified, **x1** is used. For areaX, setting this option disables the implicit stackX transform.'''
    y1: ChannelValueSpec
    '''The required primary (starting, often bottom) vertical position channel, representing the area's baseline, typically bound to the *y* scale. For areaY, setting this option disables the implicit stackY transform.'''
    y2: ChannelValueSpec
    '''The optional secondary (ending, often top) vertical position channel, representing the area's topline, typically bound to the *y* scale; if not specified, **y1** is used. For areaY, setting this option disables the implicit stackY transform.'''
    z: ChannelValue
    '''An optional ordinal channel for grouping data into (possibly stacked) series to be drawn as separate areas; defaults to **fill** if a channel, or
**stroke** if a channel.'''
class _AreaXOpen(MarkOptions,total=False):
    """The areaX mark."""
    curve: Curve | ParamRef
    '''The curve (interpolation) method for connecting adjacent points. One of:

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
- *step-before* - a piecewise constant function where *x* changes after *y*'''
    mark: Required[L['areaX']]
    '''A vertically-oriented area mark, where the baseline and topline share
**y** values, as in a time-series area chart where time goes up↑.

If neither **x1** nor **x2** is specified, an implicit stackX transform is applied and **x** defaults to the identity function, assuming that *data* = [*x₀*, *x₁*, *x₂*, …]. Otherwise, if only one of **x1** or **x2** is specified, the other defaults to **x**, which defaults to zero.

If an **interval** is specified, **y** values are binned accordingly, allowing zeroes for empty bins instead of interpolating across gaps. This is recommended to “regularize” sampled data; for example, if your data represents timestamped observations and you expect one observation per day, use *day* as the **interval**.

Variable aesthetic channels are supported: if the **fill** is defined as a channel, the area will be broken into contiguous overlapping sections when the fill color changes; the fill color will apply to the interval spanning the current data point and the following data point. This behavior also applies to the **fillOpacity**, **stroke**, **strokeOpacity**,
**strokeWidth**, **opacity**, **href**, **title**, and **ariaLabel** channels. When any of these channels are used, setting an explicit **z** channel (possibly to null) is strongly recommended.'''
    offset: None | ParamRef | StackOffset
    '''After stacking, an optional **offset** can be applied to translate and scale stacks, say to produce a streamgraph; defaults to null for a zero baseline (**y** = 0 for stackY, and **x** = 0 for stackX). If the *wiggle* offset is used, the default **order** changes to *inside-out*.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    order: None | ParamRef | StackOrder
    '''The order in which stacks are layered; one of:

- null (default) for input order
- a named stack order method such as *inside-out* or *sum*
- a field name, for natural order of the corresponding values
- a function of data, for natural order of the corresponding values
- an array of explicit **z** values in the desired order

If the *wiggle* **offset** is used, as for a streamgraph, the default changes to *inside-out*.'''
    tension: ParamRef | float
    '''The tension option only has an effect on bundle, cardinal and Catmull-Rom splines (*bundle*, *cardinal*, *cardinal-open*, *cardinal-closed*,
*catmull-rom*, *catmull-rom-open*, and *catmull-rom-closed*). For bundle splines, it corresponds to [beta][1]; for cardinal splines, [tension][2]; for Catmull-Rom splines, [alpha][3].

[1]: https://d3js.org/d3-shape/curve#curveBundle_beta [2]: https://d3js.org/d3-shape/curve#curveCardinal_tension [3]: https://d3js.org/d3-shape/curve#curveCatmullRom_alpha'''
    x: ChannelValueSpec
    '''The horizontal position (or length) channel, typically bound to the *x* scale.

If neither **x1** nor **x2** is specified, an implicit stackX transform is applied and **x** defaults to the identity function, assuming that *data* = [*x₀*, *x₁*, *x₂*, …]. Otherwise, if only one of **x1** or **x2** is specified, the other defaults to **x**, which defaults to zero.'''
    x1: ChannelValueSpec
    '''The required primary (starting, often left) horizontal position channel, representing the area's baseline, typically bound to the *x* scale. For areaX, setting this option disables the implicit stackX transform.'''
    x2: ChannelValueSpec
    '''The optional secondary (ending, often right) horizontal position channel, representing the area's topline, typically bound to the *x* scale; if not specified, **x1** is used. For areaX, setting this option disables the implicit stackX transform.'''
    y: ChannelValueSpec
    '''The vertical position channel, typically bound to the *y* scale; defaults to the zero-based index of the data [0, 1, 2, …].'''
    z: ChannelValue
    '''An optional ordinal channel for grouping data into (possibly stacked) series to be drawn as separate areas; defaults to **fill** if a channel, or
**stroke** if a channel.'''
class _AreaYOpen(MarkOptions,total=False):
    """The areaY mark."""
    curve: Curve | ParamRef
    '''The curve (interpolation) method for connecting adjacent points. One of:

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
- *step-before* - a piecewise constant function where *x* changes after *y*'''
    mark: Required[L['areaY']]
    '''A horizontally-oriented area mark, where the baseline and topline share
**x** values, as in a time-series area chart where time goes right→.

If neither **y1** nor **y2** is specified, an implicit stackY transform is applied and **y** defaults to the identity function, assuming that *data* = [*y₀*, *y₁*, *y₂*, …]. Otherwise, if only one of **y1** or **y2** is specified, the other defaults to **y**, which defaults to zero.

If an **interval** is specified, **x** values are binned accordingly, allowing zeroes for empty bins instead of interpolating across gaps. This is recommended to “regularize” sampled data; for example, if your data represents timestamped observations and you expect one observation per day, use *day* as the **interval**.

Variable aesthetic channels are supported: if the **fill** is defined as a channel, the area will be broken into contiguous overlapping sections when the fill color changes; the fill color will apply to the interval spanning the current data point and the following data point. This behavior also applies to the **fillOpacity**, **stroke**, **strokeOpacity**,
**strokeWidth**, **opacity**, **href**, **title**, and **ariaLabel** channels. When any of these channels are used, setting an explicit **z** channel (possibly to null) is strongly recommended.'''
    offset: None | ParamRef | StackOffset
    '''After stacking, an optional **offset** can be applied to translate and scale stacks, say to produce a streamgraph; defaults to null for a zero baseline (**y** = 0 for stackY, and **x** = 0 for stackX). If the *wiggle* offset is used, the default **order** changes to *inside-out*.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    order: None | ParamRef | StackOrder
    '''The order in which stacks are layered; one of:

- null (default) for input order
- a named stack order method such as *inside-out* or *sum*
- a field name, for natural order of the corresponding values
- a function of data, for natural order of the corresponding values
- an array of explicit **z** values in the desired order

If the *wiggle* **offset** is used, as for a streamgraph, the default changes to *inside-out*.'''
    tension: ParamRef | float
    '''The tension option only has an effect on bundle, cardinal and Catmull-Rom splines (*bundle*, *cardinal*, *cardinal-open*, *cardinal-closed*,
*catmull-rom*, *catmull-rom-open*, and *catmull-rom-closed*). For bundle splines, it corresponds to [beta][1]; for cardinal splines, [tension][2]; for Catmull-Rom splines, [alpha][3].

[1]: https://d3js.org/d3-shape/curve#curveBundle_beta [2]: https://d3js.org/d3-shape/curve#curveCardinal_tension [3]: https://d3js.org/d3-shape/curve#curveCatmullRom_alpha'''
    x: ChannelValueSpec
    '''The horizontal position channel, typically bound to the *x* scale; defaults to the zero-based index of the data [0, 1, 2, …].'''
    y: ChannelValueSpec
    '''The vertical position (or length) channel, typically bound to the *y* scale.

If neither **y1** nor **y2** is specified, an implicit stackY transform is applied and **y** defaults to the identity function, assuming that *data* = [*y₀*, *y₁*, *y₂*, …]. Otherwise, if only one of **y1** or **y2** is specified, the other defaults to **y**, which defaults to zero.'''
    y1: ChannelValueSpec
    '''The required primary (starting, often bottom) vertical position channel, representing the area's baseline, typically bound to the *y* scale. For areaY, setting this option disables the implicit stackY transform.'''
    y2: ChannelValueSpec
    '''The optional secondary (ending, often top) vertical position channel, representing the area's topline, typically bound to the *y* scale; if not specified, **y1** is used. For areaY, setting this option disables the implicit stackY transform.'''
    z: ChannelValue
    '''An optional ordinal channel for grouping data into (possibly stacked) series to be drawn as separate areas; defaults to **fill** if a channel, or
**stroke** if a channel.'''
class _ArrowOpen(MarkOptions,total=False):
    """The arrow mark."""
    bend: ParamRef | bool | float
    '''The angle, a constant in degrees, between the straight line intersecting the arrow's two control points and the outgoing tangent direction of the arrow from the start point. The angle must be within ±90°; a positive angle will produce a clockwise curve, while a negative angle will produce a counterclockwise curve; zero (the default) will produce a straight line. Use true for 22.5°.'''
    head_angle: ParamRef | float
    '''How pointy the arrowhead is, in degrees; a constant typically between 0° and 180°, and defaults to 60°.'''
    head_length: ParamRef | float
    '''The size of the arrowhead relative to the **strokeWidth**; a constant. Assuming the default of stroke width 1.5px, this is the length of the arrowhead's side in pixels.'''
    inset: ParamRef | float
    '''Shorthand to set the same default for **insetStart** and **insetEnd**.'''
    inset_end: ParamRef | float
    '''The ending inset, a constant in pixels; defaults to 0. A positive inset shortens the arrow by moving the ending point towards the starting point, while a negative inset extends it by moving the ending point in the opposite direction. A positive ending inset may be useful if the arrow points to a dot.'''
    inset_start: ParamRef | float
    '''The starting inset, a constant in pixels; defaults to 0. A positive inset shortens the arrow by moving the starting point towards the endpoint point, while a negative inset extends it by moving the starting point in the opposite direction. A positive starting inset may be useful if the arrow emerges from a dot.'''
    mark: Required[L['arrow']]
    '''An arrow mark, drawing (possibly swoopy) arrows connecting pairs of points.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    sweep: L['+x','+y','-x','-y'] | ParamRef | float
    '''The sweep order; defaults to 1 indicating a positive (clockwise) bend angle; -1 indicates a negative (anticlockwise) bend angle; 0 effectively clears the bend angle. If set to *-x*, the bend angle is flipped when the ending point is to the left of the starting point — ensuring all arrows bulge up (down if bend is negative); if set to *-y*, the bend angle is flipped when the ending point is above the starting point — ensuring all arrows bulge right (left if bend is negative); the sign is negated for
*+x* and *+y*.'''
    x: ChannelValueSpec
    '''The horizontal position, for vertical arrows; typically bound to the *x* scale; shorthand for setting defaults for both **x1** and **x2**.'''
    x1: ChannelValueSpec
    '''The starting horizontal position; typically bound to the *x* scale; also sets a default for **x2**.'''
    x2: ChannelValueSpec
    '''The ending horizontal position; typically bound to the *x* scale; also sets a default for **x1**.'''
    y: ChannelValueSpec
    '''The vertical position, for horizontal arrows; typically bound to the *y* scale; shorthand for setting defaults for both **y1** and **y2**.'''
    y1: ChannelValueSpec
    '''The starting vertical position; typically bound to the *y* scale; also sets a default for **y2**.'''
    y2: ChannelValueSpec
    '''The ending vertical position; typically bound to the *y* scale; also sets a default for **y1**.'''
class _AxisFxOpen(MarkOptions,total=False):
    """The axisFx mark."""
    anchor: L['bottom','left','right','top'] | ParamRef
    '''The side of the frame on which to place the axis: *top* or *bottom* for horizontal axes (axisX and axisFx) and their associated vertical grids (gridX and gridFx), or *left* or *right* for vertical axes (axisY and axisFY) and their associated horizontal grids (gridY and gridFy).

The default **anchor** depends on the associated scale:

- *x* - *bottom*
- *y* - *left*
- *fx* - *top* if there is a *bottom* *x* axis, and otherwise *bottom*
- *fy* - *right* if there is a *left* *y* axis, and otherwise *right*

For grids, the **anchor** also affects the extent of grid lines when the opposite dimension is specified (**x** for gridY and **y** for gridX).'''
    color: ChannelValueSpec | ParamRef
    '''A shorthand for setting both **fill** and **stroke**; affects the stroke of tick vectors and grid rules, and the fill of tick texts and axis label texts; defaults to *currentColor*.'''
    font_family: ParamRef | str
    '''The [font-family][1]; a constant; defaults to the plot's font family, which is typically [*system-ui*][2].

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-family [2]: https://drafts.csswg.org/css-fonts-4/#valdef-font-family-system-ui'''
    font_size: ChannelValue | ParamRef
    '''The [font size][1] in pixels; either a constant or a channel; defaults to the plot's font size, which is typically 10. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-size'''
    font_style: ParamRef | str
    '''The [font style][1]; a constant; defaults to the plot's font style, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-style'''
    font_variant: ParamRef | str
    '''The [font variant][1]; a constant; if the **text** channel contains numbers or dates, defaults to *tabular-nums* to facilitate comparing numbers; otherwise defaults to the plot's font style, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant'''
    font_weight: ParamRef | float | str
    '''The [font weight][1]; a constant; defaults to the plot's font weight, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight'''
    frame_anchor: FrameAnchor | ParamRef
    '''The frame anchor specifies defaults for **x** and **y**, along with
**textAnchor** and **lineAnchor**, based on the plot's frame; it may be one of the four sides (*top*, *right*, *bottom*, *left*), one of the four corners (*top-left*, *top-right*, *bottom-right*, *bottom-left*), or the
*middle* of the frame.'''
    inset: ParamRef | float
    '''Shorthand to set the same default for all four insets: **insetTop**,
**insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it.'''
    inset_bottom: ParamRef | float
    '''Insets the bottom edge by the specified number of pixels. A positive value insets towards the top edge (reducing effective area), while a negative value insets away from the top edge (increasing it).'''
    inset_top: ParamRef | float
    '''Insets the top edge by the specified number of pixels. A positive value insets towards the bottom edge (reducing effective area), while a negative value insets away from the bottom edge (increasing it).'''
    interval: Interval | ParamRef
    '''Enforces uniformity for data at regular intervals, such as integer values or daily samples. The interval may be one of:

- a named time interval such as *day* (for date intervals)
- a number (for number intervals), defining intervals at integer multiples of *n*

This option sets the internal transform to the given interval's
*interval*.floor function. In addition, the default **domain** will align with interval boundaries.'''
    label: None | ParamRef | str
    '''A textual label to show on the axis or legend; if null, show no label. By default the scale label is inferred from channel definitions, possibly with an arrow (↑, →, ↓, or ←) to indicate the direction of increasing value.

For axes and legends only.'''
    label_anchor: L['bottom','center','left','right','top'] | ParamRef
    '''Where to place the axis **label** relative to the plot's frame. For vertical position scales (*y* and *fy*), may be *top*, *bottom*, or
*center*; for horizontal position scales (*x* and *fx*), may be *left*,
*right*, or *center*. Defaults to *center* for ordinal scales (including
*fx* and *fy*), and otherwise *top* for *y*, and *right* for *x*.'''
    label_arrow: L['auto','down','left','none','right','up',True] | None | ParamRef | bool
    '''Whether to apply a directional arrow such as → or ↑ to the scale label. If
*auto* (the default), the presence of the arrow depends on whether the scale is ordinal.'''
    label_offset: ParamRef | float
    '''The axis **label** position offset (in pixels); default depends on margins and orientation.'''
    line_anchor: L['bottom','middle','top'] | ParamRef
    '''The line anchor controls how text is aligned (typically vertically) relative to its anchor point; it is one of *top*, *bottom*, or *middle*. If the frame anchor is *top*, *top-left*, or *top-right*, the default line anchor is *top*; if the frame anchor is *bottom*, *bottom-right*, or
*bottom-left*, the default is *bottom*; otherwise it is *middle*.'''
    line_height: ParamRef | float
    '''The line height in ems; defaults to 1. The line height affects the (typically vertical) separation between adjacent baselines of text, as well as the separation between the text and its anchor point.'''
    line_width: ParamRef | float
    '''The line width in ems (e.g., 10 for about 20 characters); defaults to infinity, disabling wrapping and clipping.

If **textOverflow** is null, lines will be wrapped at the specified length. If a line is split at a soft hyphen (\xad), a hyphen (-) will be displayed at the end of the line. If **textOverflow** is not null, lines will be clipped according to the given strategy.'''
    mark: Required[L['axisFx']]
    '''An axis mark to document the visual encoding of the horizontal facet position *fx* scale, comprised of (up to) three marks: a vector for ticks, a text for tick labels, and another text for an axis label. The data defaults to the *fx* scale's domain; if desired, use one of the **ticks**,
**tickSpacing**, or **interval** options.

The **facetAnchor** and **frameAnchor** options defaults to **anchor**. The default margins likewise depend on **anchor** as follows; in order of
**marginTop**, **marginRight**, **marginBottom**, and **marginLeft**, in pixels:

- *top* - 30, 20, 0, 20
- *bottom* - 0, 20, 30, 20

For simplicity, and for consistent layout across plots, default axis margins are not affected by tick labels. If tick labels are too long, either increase the margin or shorten the labels: use the *k* SI-prefix tick format; use the
**transform** *y*-scale option to show thousands or millions; or use the
**textOverflow** and **lineWidth** options to clip.'''
    marker: L['none'] | MarkerName | None | ParamRef | bool
    '''Shorthand to set the same default for markerStart, markerMid, and markerEnd; one of:

- a marker name such as *arrow* or *circle*
- *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_end: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the ending point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_mid: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for any middle (interior) points of a line segment. If the line segment only has a start and end point, this option has no effect. One of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*
* a function - a custom marker function; see below'''
    marker_start: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the starting point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    monospace: ParamRef | bool
    '''If true, changes the default **fontFamily** to *monospace*, and uses simplified monospaced text metrics calculations.'''
    opacity: ChannelValueSpec
    '''A shorthand for setting both **fillOpacity** and **strokeOpacity**; affects the stroke opacity of tick vectors and grid rules, and the fill opacity of tick texts and axis label texts; defaults to 1 for axes and 0.1 for grids.'''
    rotate: ChannelValue | ParamRef
    '''The rotation angle in degrees clockwise; a constant or a channel; defaults to 0°. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel.'''
    text: ChannelValue
    '''The text contents channel, possibly with line breaks (\n, \r\n, or \r). If not specified, defaults to the zero-based index [0, 1, 2, …].'''
    text_anchor: L['end','middle','start'] | ParamRef
    '''The [text anchor][1] controls how text is aligned (typically horizontally) relative to its anchor point; it is one of *start*, *end*, or *middle*. If the frame anchor is *left*, *top-left*, or *bottom-left*, the default text anchor is *start*; if the frame anchor is *right*, *top-right*, or
*bottom-right*, the default is *end*; otherwise it is *middle*.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/text-anchor'''
    text_overflow: L['clip','clip-end','clip-start','ellipsis','ellipsis-end','ellipsis-middle','ellipsis-start'] | None | ParamRef
    '''How truncate (or wrap) lines of text longer than the given **lineWidth**; one of:

- null (default) - preserve overflowing characters (and wrap if needed)
- *clip* or *clip-end* - remove characters from the end
- *clip-start* - remove characters from the start
- *ellipsis* or *ellipsis-end* - replace characters from the end with an ellipsis (…)
- *ellipsis-start* - replace characters from the start with an ellipsis (…)
- *ellipsis-middle* - replace characters from the middle with an ellipsis (…)

If no **title** was specified, if text requires truncation, a title containing the non-truncated text will be implicitly added.'''
    text_stroke: ChannelValueSpec | ParamRef
    '''The tick text **stroke**, say for a *white* outline to improve legibility; defaults to null.'''
    text_stroke_opacity: ChannelValueSpec
    '''The tick text **strokeOpacity**; defaults to 1; has no effect unless **textStroke** is set.'''
    text_stroke_width: ChannelValueSpec
    '''The tick text **strokeWidth**; defaults to 4; has no effect unless **textStroke** is set.'''
    tick_format: None | ParamRef | str
    '''How to format inputs (abstract values) for axis tick labels; one of:

- a [d3-format][1] string for numeric scales
- a [d3-time-format][2] string for temporal scales

[1]: https://d3js.org/d3-time [2]: https://d3js.org/d3-time-format'''
    tick_padding: ParamRef | float
    '''The distance between an axis tick mark and its associated text label (in pixels); often defaults to 3, but may be affected by **xTickSize** and
**xTickRotate**.'''
    tick_rotate: ParamRef | float
    '''The rotation angle of axis tick labels in degrees clocksize; defaults to 0.'''
    tick_size: ParamRef | float
    '''The length of axis tick marks in pixels; negative values extend in the opposite direction. Defaults to 6 for *x* and *y* axes and *color* and
*opacity* *ramp* legends, and 0 for *fx* and *fy* axes.'''
    tick_spacing: ParamRef | float
    '''The desired approximate spacing between adjacent axis ticks, affecting the default **ticks**; defaults to 80 pixels for *x* and *fx*, and 35 pixels for *y* and *fy*.'''
    ticks: Interval | ParamRef | Sequence[Any] | float
    '''The desired approximate number of axis ticks, or an explicit array of tick values, or an interval such as *day* or *month*.'''
    x: ChannelValueSpec
    '''The horizontal position channel specifying the text's anchor point, typically bound to the *x* scale.'''
    y: ChannelValueSpec
    '''The vertical position channel specifying the text's anchor point, typically bound to the *y* scale.'''
    z: ChannelValue
    '''An optional ordinal channel for grouping data into series.'''
class _AxisFyOpen(MarkOptions,total=False):
    """The axisFy mark."""
    anchor: L['bottom','left','right','top'] | ParamRef
    '''The side of the frame on which to place the axis: *top* or *bottom* for horizontal axes (axisX and axisFx) and their associated vertical grids (gridX and gridFx), or *left* or *right* for vertical axes (axisY and axisFY) and their associated horizontal grids (gridY and gridFy).

The default **anchor** depends on the associated scale:

- *x* - *bottom*
- *y* - *left*
- *fx* - *top* if there is a *bottom* *x* axis, and otherwise *bottom*
- *fy* - *right* if there is a *left* *y* axis, and otherwise *right*

For grids, the **anchor** also affects the extent of grid lines when the opposite dimension is specified (**x** for gridY and **y** for gridX).'''
    color: ChannelValueSpec | ParamRef
    '''A shorthand for setting both **fill** and **stroke**; affects the stroke of tick vectors and grid rules, and the fill of tick texts and axis label texts; defaults to *currentColor*.'''
    font_family: ParamRef | str
    '''The [font-family][1]; a constant; defaults to the plot's font family, which is typically [*system-ui*][2].

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-family [2]: https://drafts.csswg.org/css-fonts-4/#valdef-font-family-system-ui'''
    font_size: ChannelValue | ParamRef
    '''The [font size][1] in pixels; either a constant or a channel; defaults to the plot's font size, which is typically 10. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-size'''
    font_style: ParamRef | str
    '''The [font style][1]; a constant; defaults to the plot's font style, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-style'''
    font_variant: ParamRef | str
    '''The [font variant][1]; a constant; if the **text** channel contains numbers or dates, defaults to *tabular-nums* to facilitate comparing numbers; otherwise defaults to the plot's font style, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant'''
    font_weight: ParamRef | float | str
    '''The [font weight][1]; a constant; defaults to the plot's font weight, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight'''
    frame_anchor: FrameAnchor | ParamRef
    '''The frame anchor specifies defaults for **x** and **y**, along with
**textAnchor** and **lineAnchor**, based on the plot's frame; it may be one of the four sides (*top*, *right*, *bottom*, *left*), one of the four corners (*top-left*, *top-right*, *bottom-right*, *bottom-left*), or the
*middle* of the frame.'''
    inset: ParamRef | float
    '''Shorthand to set the same default for all four insets: **insetTop**,
**insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it.'''
    inset_left: ParamRef | float
    '''Insets the left edge by the specified number of pixels. A positive value insets towards the right edge (reducing effective area), while a negative value insets away from the right edge (increasing it).'''
    inset_right: ParamRef | float
    '''Insets the right edge by the specified number of pixels. A positive value insets towards the left edge (reducing effective area), while a negative value insets away from the left edge (increasing it).'''
    interval: Interval | ParamRef
    '''Enforces uniformity for data at regular intervals, such as integer values or daily samples. The interval may be one of:

- a named time interval such as *day* (for date intervals)
- a number (for number intervals), defining intervals at integer multiples of *n*

This option sets the internal transform to the given interval's
*interval*.floor function. In addition, the default **domain** will align with interval boundaries.'''
    label: None | ParamRef | str
    '''A textual label to show on the axis or legend; if null, show no label. By default the scale label is inferred from channel definitions, possibly with an arrow (↑, →, ↓, or ←) to indicate the direction of increasing value.

For axes and legends only.'''
    label_anchor: L['bottom','center','left','right','top'] | ParamRef
    '''Where to place the axis **label** relative to the plot's frame. For vertical position scales (*y* and *fy*), may be *top*, *bottom*, or
*center*; for horizontal position scales (*x* and *fx*), may be *left*,
*right*, or *center*. Defaults to *center* for ordinal scales (including
*fx* and *fy*), and otherwise *top* for *y*, and *right* for *x*.'''
    label_arrow: L['auto','down','left','none','right','up',True] | None | ParamRef | bool
    '''Whether to apply a directional arrow such as → or ↑ to the scale label. If
*auto* (the default), the presence of the arrow depends on whether the scale is ordinal.'''
    label_offset: ParamRef | float
    '''The axis **label** position offset (in pixels); default depends on margins and orientation.'''
    line_anchor: L['bottom','middle','top'] | ParamRef
    '''The line anchor controls how text is aligned (typically vertically) relative to its anchor point; it is one of *top*, *bottom*, or *middle*. If the frame anchor is *top*, *top-left*, or *top-right*, the default line anchor is *top*; if the frame anchor is *bottom*, *bottom-right*, or
*bottom-left*, the default is *bottom*; otherwise it is *middle*.'''
    line_height: ParamRef | float
    '''The line height in ems; defaults to 1. The line height affects the (typically vertical) separation between adjacent baselines of text, as well as the separation between the text and its anchor point.'''
    line_width: ParamRef | float
    '''The line width in ems (e.g., 10 for about 20 characters); defaults to infinity, disabling wrapping and clipping.

If **textOverflow** is null, lines will be wrapped at the specified length. If a line is split at a soft hyphen (\xad), a hyphen (-) will be displayed at the end of the line. If **textOverflow** is not null, lines will be clipped according to the given strategy.'''
    mark: Required[L['axisFy']]
    '''An axis mark to document the visual encoding of the vertical facet position *fy* scale, comprised of (up to) three marks: a vector for ticks, a text for tick labels, and another text for an axis label. The data defaults to the *fy* scale's domain; if desired, use one of the **ticks**,
**tickSpacing**, or **interval** options.

The **facetAnchor** option defaults to *right-empty* if **anchor** is
*right*, and *left-empty* if **anchor** is *left*. The default margins likewise depend on **anchor** as follows; in order of **marginTop**,
**marginRight**, **marginBottom**, and **marginLeft**, in pixels:

- *right* - 20, 40, 20, 0
- *left* - 20, 0, 20, 40

For simplicity, and for consistent layout across plots, default axis margins are not affected by tick labels. If tick labels are too long, either increase the margin or shorten the labels: use the *k* SI-prefix tick format; or use the **textOverflow** and **lineWidth** options to clip.'''
    marker: L['none'] | MarkerName | None | ParamRef | bool
    '''Shorthand to set the same default for markerStart, markerMid, and markerEnd; one of:

- a marker name such as *arrow* or *circle*
- *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_end: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the ending point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_mid: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for any middle (interior) points of a line segment. If the line segment only has a start and end point, this option has no effect. One of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*
* a function - a custom marker function; see below'''
    marker_start: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the starting point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    monospace: ParamRef | bool
    '''If true, changes the default **fontFamily** to *monospace*, and uses simplified monospaced text metrics calculations.'''
    opacity: ChannelValueSpec
    '''A shorthand for setting both **fillOpacity** and **strokeOpacity**; affects the stroke opacity of tick vectors and grid rules, and the fill opacity of tick texts and axis label texts; defaults to 1 for axes and 0.1 for grids.'''
    rotate: ChannelValue | ParamRef
    '''The rotation angle in degrees clockwise; a constant or a channel; defaults to 0°. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel.'''
    text: ChannelValue
    '''The text contents channel, possibly with line breaks (\n, \r\n, or \r). If not specified, defaults to the zero-based index [0, 1, 2, …].'''
    text_anchor: L['end','middle','start'] | ParamRef
    '''The [text anchor][1] controls how text is aligned (typically horizontally) relative to its anchor point; it is one of *start*, *end*, or *middle*. If the frame anchor is *left*, *top-left*, or *bottom-left*, the default text anchor is *start*; if the frame anchor is *right*, *top-right*, or
*bottom-right*, the default is *end*; otherwise it is *middle*.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/text-anchor'''
    text_overflow: L['clip','clip-end','clip-start','ellipsis','ellipsis-end','ellipsis-middle','ellipsis-start'] | None | ParamRef
    '''How truncate (or wrap) lines of text longer than the given **lineWidth**; one of:

- null (default) - preserve overflowing characters (and wrap if needed)
- *clip* or *clip-end* - remove characters from the end
- *clip-start* - remove characters from the start
- *ellipsis* or *ellipsis-end* - replace characters from the end with an ellipsis (…)
- *ellipsis-start* - replace characters from the start with an ellipsis (…)
- *ellipsis-middle* - replace characters from the middle with an ellipsis (…)

If no **title** was specified, if text requires truncation, a title containing the non-truncated text will be implicitly added.'''
    text_stroke: ChannelValueSpec | ParamRef
    '''The tick text **stroke**, say for a *white* outline to improve legibility; defaults to null.'''
    text_stroke_opacity: ChannelValueSpec
    '''The tick text **strokeOpacity**; defaults to 1; has no effect unless **textStroke** is set.'''
    text_stroke_width: ChannelValueSpec
    '''The tick text **strokeWidth**; defaults to 4; has no effect unless **textStroke** is set.'''
    tick_format: None | ParamRef | str
    '''How to format inputs (abstract values) for axis tick labels; one of:

- a [d3-format][1] string for numeric scales
- a [d3-time-format][2] string for temporal scales

[1]: https://d3js.org/d3-time [2]: https://d3js.org/d3-time-format'''
    tick_padding: ParamRef | float
    '''The distance between an axis tick mark and its associated text label (in pixels); often defaults to 3, but may be affected by **xTickSize** and
**xTickRotate**.'''
    tick_rotate: ParamRef | float
    '''The rotation angle of axis tick labels in degrees clocksize; defaults to 0.'''
    tick_size: ParamRef | float
    '''The length of axis tick marks in pixels; negative values extend in the opposite direction. Defaults to 6 for *x* and *y* axes and *color* and
*opacity* *ramp* legends, and 0 for *fx* and *fy* axes.'''
    tick_spacing: ParamRef | float
    '''The desired approximate spacing between adjacent axis ticks, affecting the default **ticks**; defaults to 80 pixels for *x* and *fx*, and 35 pixels for *y* and *fy*.'''
    ticks: Interval | ParamRef | Sequence[Any] | float
    '''The desired approximate number of axis ticks, or an explicit array of tick values, or an interval such as *day* or *month*.'''
    x: ChannelValueSpec
    '''The horizontal position channel specifying the text's anchor point, typically bound to the *x* scale.'''
    y: ChannelValueSpec
    '''The vertical position channel specifying the text's anchor point, typically bound to the *y* scale.'''
    z: ChannelValue
    '''An optional ordinal channel for grouping data into series.'''
class _AxisXOpen(MarkOptions,total=False):
    """The axisX mark."""
    anchor: L['bottom','left','right','top'] | ParamRef
    '''The side of the frame on which to place the axis: *top* or *bottom* for horizontal axes (axisX and axisFx) and their associated vertical grids (gridX and gridFx), or *left* or *right* for vertical axes (axisY and axisFY) and their associated horizontal grids (gridY and gridFy).

The default **anchor** depends on the associated scale:

- *x* - *bottom*
- *y* - *left*
- *fx* - *top* if there is a *bottom* *x* axis, and otherwise *bottom*
- *fy* - *right* if there is a *left* *y* axis, and otherwise *right*

For grids, the **anchor** also affects the extent of grid lines when the opposite dimension is specified (**x** for gridY and **y** for gridX).'''
    color: ChannelValueSpec | ParamRef
    '''A shorthand for setting both **fill** and **stroke**; affects the stroke of tick vectors and grid rules, and the fill of tick texts and axis label texts; defaults to *currentColor*.'''
    font_family: ParamRef | str
    '''The [font-family][1]; a constant; defaults to the plot's font family, which is typically [*system-ui*][2].

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-family [2]: https://drafts.csswg.org/css-fonts-4/#valdef-font-family-system-ui'''
    font_size: ChannelValue | ParamRef
    '''The [font size][1] in pixels; either a constant or a channel; defaults to the plot's font size, which is typically 10. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-size'''
    font_style: ParamRef | str
    '''The [font style][1]; a constant; defaults to the plot's font style, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-style'''
    font_variant: ParamRef | str
    '''The [font variant][1]; a constant; if the **text** channel contains numbers or dates, defaults to *tabular-nums* to facilitate comparing numbers; otherwise defaults to the plot's font style, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant'''
    font_weight: ParamRef | float | str
    '''The [font weight][1]; a constant; defaults to the plot's font weight, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight'''
    frame_anchor: FrameAnchor | ParamRef
    '''The frame anchor specifies defaults for **x** and **y**, along with
**textAnchor** and **lineAnchor**, based on the plot's frame; it may be one of the four sides (*top*, *right*, *bottom*, *left*), one of the four corners (*top-left*, *top-right*, *bottom-right*, *bottom-left*), or the
*middle* of the frame.'''
    inset: ParamRef | float
    '''Shorthand to set the same default for all four insets: **insetTop**,
**insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it.'''
    inset_bottom: ParamRef | float
    '''Insets the bottom edge by the specified number of pixels. A positive value insets towards the top edge (reducing effective area), while a negative value insets away from the top edge (increasing it).'''
    inset_top: ParamRef | float
    '''Insets the top edge by the specified number of pixels. A positive value insets towards the bottom edge (reducing effective area), while a negative value insets away from the bottom edge (increasing it).'''
    interval: Interval | ParamRef
    '''Enforces uniformity for data at regular intervals, such as integer values or daily samples. The interval may be one of:

- a named time interval such as *day* (for date intervals)
- a number (for number intervals), defining intervals at integer multiples of *n*

This option sets the internal transform to the given interval's
*interval*.floor function. In addition, the default **domain** will align with interval boundaries.'''
    label: None | ParamRef | str
    '''A textual label to show on the axis or legend; if null, show no label. By default the scale label is inferred from channel definitions, possibly with an arrow (↑, →, ↓, or ←) to indicate the direction of increasing value.

For axes and legends only.'''
    label_anchor: L['bottom','center','left','right','top'] | ParamRef
    '''Where to place the axis **label** relative to the plot's frame. For vertical position scales (*y* and *fy*), may be *top*, *bottom*, or
*center*; for horizontal position scales (*x* and *fx*), may be *left*,
*right*, or *center*. Defaults to *center* for ordinal scales (including
*fx* and *fy*), and otherwise *top* for *y*, and *right* for *x*.'''
    label_arrow: L['auto','down','left','none','right','up',True] | None | ParamRef | bool
    '''Whether to apply a directional arrow such as → or ↑ to the scale label. If
*auto* (the default), the presence of the arrow depends on whether the scale is ordinal.'''
    label_offset: ParamRef | float
    '''The axis **label** position offset (in pixels); default depends on margins and orientation.'''
    line_anchor: L['bottom','middle','top'] | ParamRef
    '''The line anchor controls how text is aligned (typically vertically) relative to its anchor point; it is one of *top*, *bottom*, or *middle*. If the frame anchor is *top*, *top-left*, or *top-right*, the default line anchor is *top*; if the frame anchor is *bottom*, *bottom-right*, or
*bottom-left*, the default is *bottom*; otherwise it is *middle*.'''
    line_height: ParamRef | float
    '''The line height in ems; defaults to 1. The line height affects the (typically vertical) separation between adjacent baselines of text, as well as the separation between the text and its anchor point.'''
    line_width: ParamRef | float
    '''The line width in ems (e.g., 10 for about 20 characters); defaults to infinity, disabling wrapping and clipping.

If **textOverflow** is null, lines will be wrapped at the specified length. If a line is split at a soft hyphen (\xad), a hyphen (-) will be displayed at the end of the line. If **textOverflow** is not null, lines will be clipped according to the given strategy.'''
    mark: Required[L['axisX']]
    '''An axis mark to document the visual encoding of the horizontal position
*x* scale, comprised of (up to) three marks: a vector for ticks, a text for tick labels, and another text for an axis label. The data defaults to tick values sampled from the *x* scale's domain; if desired, use one of the **ticks**, **tickSpacing**, or **interval** options.

The **facetAnchor** option defaults to *bottom-empty* if **anchor** is
*bottom*, and *top-empty* if **anchor** is *top*. The default margins likewise depend on **anchor** as follows; in order of **marginTop**,
**marginRight**, **marginBottom**, and **marginLeft**, in pixels:

- *top* - 30, 20, 0, 20
- *bottom* - 0, 20, 30, 20

For simplicity, and for consistent layout across plots, default axis margins are not affected by tick labels. If tick labels are too long, either increase the margin or shorten the labels: use the *k* SI-prefix tick format; use the
**transform** *y*-scale option to show thousands or millions; or use the
**textOverflow** and **lineWidth** options to clip.'''
    marker: L['none'] | MarkerName | None | ParamRef | bool
    '''Shorthand to set the same default for markerStart, markerMid, and markerEnd; one of:

- a marker name such as *arrow* or *circle*
- *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_end: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the ending point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_mid: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for any middle (interior) points of a line segment. If the line segment only has a start and end point, this option has no effect. One of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*
* a function - a custom marker function; see below'''
    marker_start: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the starting point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    monospace: ParamRef | bool
    '''If true, changes the default **fontFamily** to *monospace*, and uses simplified monospaced text metrics calculations.'''
    opacity: ChannelValueSpec
    '''A shorthand for setting both **fillOpacity** and **strokeOpacity**; affects the stroke opacity of tick vectors and grid rules, and the fill opacity of tick texts and axis label texts; defaults to 1 for axes and 0.1 for grids.'''
    rotate: ChannelValue | ParamRef
    '''The rotation angle in degrees clockwise; a constant or a channel; defaults to 0°. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel.'''
    text: ChannelValue
    '''The text contents channel, possibly with line breaks (\n, \r\n, or \r). If not specified, defaults to the zero-based index [0, 1, 2, …].'''
    text_anchor: L['end','middle','start'] | ParamRef
    '''The [text anchor][1] controls how text is aligned (typically horizontally) relative to its anchor point; it is one of *start*, *end*, or *middle*. If the frame anchor is *left*, *top-left*, or *bottom-left*, the default text anchor is *start*; if the frame anchor is *right*, *top-right*, or
*bottom-right*, the default is *end*; otherwise it is *middle*.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/text-anchor'''
    text_overflow: L['clip','clip-end','clip-start','ellipsis','ellipsis-end','ellipsis-middle','ellipsis-start'] | None | ParamRef
    '''How truncate (or wrap) lines of text longer than the given **lineWidth**; one of:

- null (default) - preserve overflowing characters (and wrap if needed)
- *clip* or *clip-end* - remove characters from the end
- *clip-start* - remove characters from the start
- *ellipsis* or *ellipsis-end* - replace characters from the end with an ellipsis (…)
- *ellipsis-start* - replace characters from the start with an ellipsis (…)
- *ellipsis-middle* - replace characters from the middle with an ellipsis (…)

If no **title** was specified, if text requires truncation, a title containing the non-truncated text will be implicitly added.'''
    text_stroke: ChannelValueSpec | ParamRef
    '''The tick text **stroke**, say for a *white* outline to improve legibility; defaults to null.'''
    text_stroke_opacity: ChannelValueSpec
    '''The tick text **strokeOpacity**; defaults to 1; has no effect unless **textStroke** is set.'''
    text_stroke_width: ChannelValueSpec
    '''The tick text **strokeWidth**; defaults to 4; has no effect unless **textStroke** is set.'''
    tick_format: None | ParamRef | str
    '''How to format inputs (abstract values) for axis tick labels; one of:

- a [d3-format][1] string for numeric scales
- a [d3-time-format][2] string for temporal scales

[1]: https://d3js.org/d3-time [2]: https://d3js.org/d3-time-format'''
    tick_padding: ParamRef | float
    '''The distance between an axis tick mark and its associated text label (in pixels); often defaults to 3, but may be affected by **xTickSize** and
**xTickRotate**.'''
    tick_rotate: ParamRef | float
    '''The rotation angle of axis tick labels in degrees clocksize; defaults to 0.'''
    tick_size: ParamRef | float
    '''The length of axis tick marks in pixels; negative values extend in the opposite direction. Defaults to 6 for *x* and *y* axes and *color* and
*opacity* *ramp* legends, and 0 for *fx* and *fy* axes.'''
    tick_spacing: ParamRef | float
    '''The desired approximate spacing between adjacent axis ticks, affecting the default **ticks**; defaults to 80 pixels for *x* and *fx*, and 35 pixels for *y* and *fy*.'''
    ticks: Interval | ParamRef | Sequence[Any] | float
    '''The desired approximate number of axis ticks, or an explicit array of tick values, or an interval such as *day* or *month*.'''
    x: ChannelValueSpec
    '''The horizontal position channel specifying the text's anchor point, typically bound to the *x* scale.'''
    y: ChannelValueSpec
    '''The vertical position channel specifying the text's anchor point, typically bound to the *y* scale.'''
    z: ChannelValue
    '''An optional ordinal channel for grouping data into series.'''
class _AxisYOpen(MarkOptions,total=False):
    """The axisY mark."""
    anchor: L['bottom','left','right','top'] | ParamRef
    '''The side of the frame on which to place the axis: *top* or *bottom* for horizontal axes (axisX and axisFx) and their associated vertical grids (gridX and gridFx), or *left* or *right* for vertical axes (axisY and axisFY) and their associated horizontal grids (gridY and gridFy).

The default **anchor** depends on the associated scale:

- *x* - *bottom*
- *y* - *left*
- *fx* - *top* if there is a *bottom* *x* axis, and otherwise *bottom*
- *fy* - *right* if there is a *left* *y* axis, and otherwise *right*

For grids, the **anchor** also affects the extent of grid lines when the opposite dimension is specified (**x** for gridY and **y** for gridX).'''
    color: ChannelValueSpec | ParamRef
    '''A shorthand for setting both **fill** and **stroke**; affects the stroke of tick vectors and grid rules, and the fill of tick texts and axis label texts; defaults to *currentColor*.'''
    font_family: ParamRef | str
    '''The [font-family][1]; a constant; defaults to the plot's font family, which is typically [*system-ui*][2].

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-family [2]: https://drafts.csswg.org/css-fonts-4/#valdef-font-family-system-ui'''
    font_size: ChannelValue | ParamRef
    '''The [font size][1] in pixels; either a constant or a channel; defaults to the plot's font size, which is typically 10. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-size'''
    font_style: ParamRef | str
    '''The [font style][1]; a constant; defaults to the plot's font style, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-style'''
    font_variant: ParamRef | str
    '''The [font variant][1]; a constant; if the **text** channel contains numbers or dates, defaults to *tabular-nums* to facilitate comparing numbers; otherwise defaults to the plot's font style, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant'''
    font_weight: ParamRef | float | str
    '''The [font weight][1]; a constant; defaults to the plot's font weight, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight'''
    frame_anchor: FrameAnchor | ParamRef
    '''The frame anchor specifies defaults for **x** and **y**, along with
**textAnchor** and **lineAnchor**, based on the plot's frame; it may be one of the four sides (*top*, *right*, *bottom*, *left*), one of the four corners (*top-left*, *top-right*, *bottom-right*, *bottom-left*), or the
*middle* of the frame.'''
    inset: ParamRef | float
    '''Shorthand to set the same default for all four insets: **insetTop**,
**insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it.'''
    inset_left: ParamRef | float
    '''Insets the left edge by the specified number of pixels. A positive value insets towards the right edge (reducing effective area), while a negative value insets away from the right edge (increasing it).'''
    inset_right: ParamRef | float
    '''Insets the right edge by the specified number of pixels. A positive value insets towards the left edge (reducing effective area), while a negative value insets away from the left edge (increasing it).'''
    interval: Interval | ParamRef
    '''Enforces uniformity for data at regular intervals, such as integer values or daily samples. The interval may be one of:

- a named time interval such as *day* (for date intervals)
- a number (for number intervals), defining intervals at integer multiples of *n*

This option sets the internal transform to the given interval's
*interval*.floor function. In addition, the default **domain** will align with interval boundaries.'''
    label: None | ParamRef | str
    '''A textual label to show on the axis or legend; if null, show no label. By default the scale label is inferred from channel definitions, possibly with an arrow (↑, →, ↓, or ←) to indicate the direction of increasing value.

For axes and legends only.'''
    label_anchor: L['bottom','center','left','right','top'] | ParamRef
    '''Where to place the axis **label** relative to the plot's frame. For vertical position scales (*y* and *fy*), may be *top*, *bottom*, or
*center*; for horizontal position scales (*x* and *fx*), may be *left*,
*right*, or *center*. Defaults to *center* for ordinal scales (including
*fx* and *fy*), and otherwise *top* for *y*, and *right* for *x*.'''
    label_arrow: L['auto','down','left','none','right','up',True] | None | ParamRef | bool
    '''Whether to apply a directional arrow such as → or ↑ to the scale label. If
*auto* (the default), the presence of the arrow depends on whether the scale is ordinal.'''
    label_offset: ParamRef | float
    '''The axis **label** position offset (in pixels); default depends on margins and orientation.'''
    line_anchor: L['bottom','middle','top'] | ParamRef
    '''The line anchor controls how text is aligned (typically vertically) relative to its anchor point; it is one of *top*, *bottom*, or *middle*. If the frame anchor is *top*, *top-left*, or *top-right*, the default line anchor is *top*; if the frame anchor is *bottom*, *bottom-right*, or
*bottom-left*, the default is *bottom*; otherwise it is *middle*.'''
    line_height: ParamRef | float
    '''The line height in ems; defaults to 1. The line height affects the (typically vertical) separation between adjacent baselines of text, as well as the separation between the text and its anchor point.'''
    line_width: ParamRef | float
    '''The line width in ems (e.g., 10 for about 20 characters); defaults to infinity, disabling wrapping and clipping.

If **textOverflow** is null, lines will be wrapped at the specified length. If a line is split at a soft hyphen (\xad), a hyphen (-) will be displayed at the end of the line. If **textOverflow** is not null, lines will be clipped according to the given strategy.'''
    mark: Required[L['axisY']]
    '''An axis mark to document the visual encoding of the vertical position *y* scale, comprised of (up to) three marks: a vector for ticks, a text for tick labels, and another text for an axis label. The data defaults to tick values sampled from the *y* scale's domain; if desired, use one of the
**ticks**, **tickSpacing**, or **interval** options.

The **facetAnchor** option defaults to *right-empty* if **anchor** is
*right*, and *left-empty* if **anchor** is *left*. The default margins likewise depend on **anchor** as follows; in order of **marginTop**,
**marginRight**, **marginBottom**, and **marginLeft**, in pixels:

- *right* - 20, 40, 20, 0
- *left* - 20, 0, 20, 40

For simplicity, and for consistent layout across plots, default axis margins are not affected by tick labels. If tick labels are too long, either increase the margin or shorten the labels: use the *k* SI-prefix tick format; or use the **textOverflow** and **lineWidth** options to clip.'''
    marker: L['none'] | MarkerName | None | ParamRef | bool
    '''Shorthand to set the same default for markerStart, markerMid, and markerEnd; one of:

- a marker name such as *arrow* or *circle*
- *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_end: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the ending point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_mid: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for any middle (interior) points of a line segment. If the line segment only has a start and end point, this option has no effect. One of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*
* a function - a custom marker function; see below'''
    marker_start: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the starting point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    monospace: ParamRef | bool
    '''If true, changes the default **fontFamily** to *monospace*, and uses simplified monospaced text metrics calculations.'''
    opacity: ChannelValueSpec
    '''A shorthand for setting both **fillOpacity** and **strokeOpacity**; affects the stroke opacity of tick vectors and grid rules, and the fill opacity of tick texts and axis label texts; defaults to 1 for axes and 0.1 for grids.'''
    rotate: ChannelValue | ParamRef
    '''The rotation angle in degrees clockwise; a constant or a channel; defaults to 0°. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel.'''
    text: ChannelValue
    '''The text contents channel, possibly with line breaks (\n, \r\n, or \r). If not specified, defaults to the zero-based index [0, 1, 2, …].'''
    text_anchor: L['end','middle','start'] | ParamRef
    '''The [text anchor][1] controls how text is aligned (typically horizontally) relative to its anchor point; it is one of *start*, *end*, or *middle*. If the frame anchor is *left*, *top-left*, or *bottom-left*, the default text anchor is *start*; if the frame anchor is *right*, *top-right*, or
*bottom-right*, the default is *end*; otherwise it is *middle*.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/text-anchor'''
    text_overflow: L['clip','clip-end','clip-start','ellipsis','ellipsis-end','ellipsis-middle','ellipsis-start'] | None | ParamRef
    '''How truncate (or wrap) lines of text longer than the given **lineWidth**; one of:

- null (default) - preserve overflowing characters (and wrap if needed)
- *clip* or *clip-end* - remove characters from the end
- *clip-start* - remove characters from the start
- *ellipsis* or *ellipsis-end* - replace characters from the end with an ellipsis (…)
- *ellipsis-start* - replace characters from the start with an ellipsis (…)
- *ellipsis-middle* - replace characters from the middle with an ellipsis (…)

If no **title** was specified, if text requires truncation, a title containing the non-truncated text will be implicitly added.'''
    text_stroke: ChannelValueSpec | ParamRef
    '''The tick text **stroke**, say for a *white* outline to improve legibility; defaults to null.'''
    text_stroke_opacity: ChannelValueSpec
    '''The tick text **strokeOpacity**; defaults to 1; has no effect unless **textStroke** is set.'''
    text_stroke_width: ChannelValueSpec
    '''The tick text **strokeWidth**; defaults to 4; has no effect unless **textStroke** is set.'''
    tick_format: None | ParamRef | str
    '''How to format inputs (abstract values) for axis tick labels; one of:

- a [d3-format][1] string for numeric scales
- a [d3-time-format][2] string for temporal scales

[1]: https://d3js.org/d3-time [2]: https://d3js.org/d3-time-format'''
    tick_padding: ParamRef | float
    '''The distance between an axis tick mark and its associated text label (in pixels); often defaults to 3, but may be affected by **xTickSize** and
**xTickRotate**.'''
    tick_rotate: ParamRef | float
    '''The rotation angle of axis tick labels in degrees clocksize; defaults to 0.'''
    tick_size: ParamRef | float
    '''The length of axis tick marks in pixels; negative values extend in the opposite direction. Defaults to 6 for *x* and *y* axes and *color* and
*opacity* *ramp* legends, and 0 for *fx* and *fy* axes.'''
    tick_spacing: ParamRef | float
    '''The desired approximate spacing between adjacent axis ticks, affecting the default **ticks**; defaults to 80 pixels for *x* and *fx*, and 35 pixels for *y* and *fy*.'''
    ticks: Interval | ParamRef | Sequence[Any] | float
    '''The desired approximate number of axis ticks, or an explicit array of tick values, or an interval such as *day* or *month*.'''
    x: ChannelValueSpec
    '''The horizontal position channel specifying the text's anchor point, typically bound to the *x* scale.'''
    y: ChannelValueSpec
    '''The vertical position channel specifying the text's anchor point, typically bound to the *y* scale.'''
    z: ChannelValue
    '''An optional ordinal channel for grouping data into series.'''
class _BarXOpen(MarkOptions,total=False):
    """The barX mark."""
    inset: ParamRef | float
    '''Shorthand to set the same default for all four insets: **insetTop**,
**insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it.'''
    inset_bottom: ParamRef | float
    '''Insets the bottom edge by the specified number of pixels. A positive value insets towards the top edge (reducing effective area), while a negative value insets away from the top edge (increasing it).'''
    inset_left: ParamRef | float
    '''Insets the left edge by the specified number of pixels. A positive value insets towards the right edge (reducing effective area), while a negative value insets away from the right edge (increasing it).'''
    inset_right: ParamRef | float
    '''Insets the right edge by the specified number of pixels. A positive value insets towards the left edge (reducing effective area), while a negative value insets away from the left edge (increasing it).'''
    inset_top: ParamRef | float
    '''Insets the top edge by the specified number of pixels. A positive value insets towards the bottom edge (reducing effective area), while a negative value insets away from the bottom edge (increasing it).'''
    interval: Interval | ParamRef
    '''How to convert a continuous value (**x** for barX, or **y** for barY) into an interval (**x1** and **x2** for barX, or **y1** and **y2** for barY); one of:

- a named time interval such as *day* (for date intervals)
- a number (for number intervals), defining intervals at integer multiples of *n*

Setting this option disables the implicit stack transform (stackX for barX, or stackY for barY).'''
    mark: Required[L['barX']]
    '''A horizontal bar mark. The required *x* values should be quantitative or temporal, and the optional *y* values should be ordinal.

If neither **x1** nor **x2** nor **interval** is specified, an implicit stackX transform is applied and **x** defaults to the identity function, assuming that *data* = [*x₀*, *x₁*, *x₂*, …]. Otherwise if an **interval** is specified, then **x1** and **x2** are derived from **x**, representing the lower and upper bound of the containing interval, respectively. Otherwise, if only one of **x1** or **x2** is specified, the other defaults to **x**, which defaults to zero.

The optional **y** ordinal channel specifies the vertical position; it is typically bound to the *y* scale, which must be a *band* scale. If the
**y** channel is not specified, the bar will span the vertical extent of the plot's frame.

If *y* is quantitative, use the rectX mark instead. If *x* is ordinal, use the cell mark instead.'''
    offset: None | ParamRef | StackOffset
    '''After stacking, an optional **offset** can be applied to translate and scale stacks, say to produce a streamgraph; defaults to null for a zero baseline (**y** = 0 for stackY, and **x** = 0 for stackX). If the *wiggle* offset is used, the default **order** changes to *inside-out*.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    order: None | ParamRef | StackOrder
    '''The order in which stacks are layered; one of:

- null (default) for input order
- a named stack order method such as *inside-out* or *sum*
- a field name, for natural order of the corresponding values
- a function of data, for natural order of the corresponding values
- an array of explicit **z** values in the desired order

If the *wiggle* **offset** is used, as for a streamgraph, the default changes to *inside-out*.'''
    rx: ParamRef | float | str
    '''The rounded corner [*x*-radius][1], either in pixels or as a percentage of the rect width. If **rx** is not specified, it defaults to **ry** if present, and otherwise draws square corners.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/rx'''
    ry: ParamRef | float | str
    '''The rounded corner [*y*-radius][1], either in pixels or as a percentage of the rect height. If **ry** is not specified, it defaults to **rx** if present, and otherwise draws square corners.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/ry'''
    x: ChannelValueIntervalSpec
    '''The horizontal position (or length/width) channel, typically bound to the
*x* scale.

If neither **x1** nor **x2** nor **interval** is specified, an implicit stackX transform is applied and **x** defaults to the identity function, assuming that *data* = [*x₀*, *x₁*, *x₂*, …]. Otherwise if an **interval** is specified, then **x1** and **x2** are derived from **x**, representing the lower and upper bound of the containing interval, respectively. Otherwise, if only one of **x1** or **x2** is specified, the other defaults to **x**, which defaults to zero.'''
    x1: ChannelValueSpec
    '''The required primary (starting, often left) horizontal position channel, typically bound to the *x* scale. Setting this option disables the implicit stackX transform.

If *x* represents ordinal values, use a cell mark instead.'''
    x2: ChannelValueSpec
    '''The required secondary (ending, often right) horizontal position channel, typically bound to the *x* scale. Setting this option disables the implicit stackX transform.

If *x* represents ordinal values, use a cell mark instead.'''
    y: ChannelValueSpec
    '''The optional vertical position of the bar; a ordinal channel typically bound to the *y* scale. If not specified, the bar spans the vertical extent of the frame; otherwise the *y* scale must be a *band* scale.

If *y* represents quantitative or temporal values, use a rectX mark instead.'''
    z: ChannelValue
    '''The **z** channel defines the series of each value in the stack. Used when the **order** is *sum*, *appearance*, *inside-out*, or an explicit array of
**z** values.'''
class _BarYOpen(MarkOptions,total=False):
    """The barY mark."""
    inset: ParamRef | float
    '''Shorthand to set the same default for all four insets: **insetTop**,
**insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it.'''
    inset_bottom: ParamRef | float
    '''Insets the bottom edge by the specified number of pixels. A positive value insets towards the top edge (reducing effective area), while a negative value insets away from the top edge (increasing it).'''
    inset_left: ParamRef | float
    '''Insets the left edge by the specified number of pixels. A positive value insets towards the right edge (reducing effective area), while a negative value insets away from the right edge (increasing it).'''
    inset_right: ParamRef | float
    '''Insets the right edge by the specified number of pixels. A positive value insets towards the left edge (reducing effective area), while a negative value insets away from the left edge (increasing it).'''
    inset_top: ParamRef | float
    '''Insets the top edge by the specified number of pixels. A positive value insets towards the bottom edge (reducing effective area), while a negative value insets away from the bottom edge (increasing it).'''
    interval: Interval | ParamRef
    '''How to convert a continuous value (**x** for barX, or **y** for barY) into an interval (**x1** and **x2** for barX, or **y1** and **y2** for barY); one of:

- a named time interval such as *day* (for date intervals)
- a number (for number intervals), defining intervals at integer multiples of *n*

Setting this option disables the implicit stack transform (stackX for barX, or stackY for barY).'''
    mark: Required[L['barY']]
    '''A vertical bar mark. The required *y* values should be quantitative or temporal, and the optional *x* values should be ordinal.

If neither **y1** nor **y2** nor **interval** is specified, an implicit stackY transform is applied and **y** defaults to the identity function, assuming that *data* = [*y₀*, *y₁*, *y₂*, …]. Otherwise if an **interval** is specified, then **y1** and **y2** are derived from **y**, representing the lower and upper bound of the containing interval, respectively. Otherwise, if only one of **y1** or **y2** is specified, the other defaults to **y**, which defaults to zero.

The optional **x** ordinal channel specifies the horizontal position; it is typically bound to the *x* scale, which must be a *band* scale. If the
**x** channel is not specified, the bar will span the horizontal extent of the plot's frame.

If *x* is quantitative, use the rectY mark instead. If *y* is ordinal, use the cell mark instead.'''
    offset: None | ParamRef | StackOffset
    '''After stacking, an optional **offset** can be applied to translate and scale stacks, say to produce a streamgraph; defaults to null for a zero baseline (**y** = 0 for stackY, and **x** = 0 for stackX). If the *wiggle* offset is used, the default **order** changes to *inside-out*.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    order: None | ParamRef | StackOrder
    '''The order in which stacks are layered; one of:

- null (default) for input order
- a named stack order method such as *inside-out* or *sum*
- a field name, for natural order of the corresponding values
- a function of data, for natural order of the corresponding values
- an array of explicit **z** values in the desired order

If the *wiggle* **offset** is used, as for a streamgraph, the default changes to *inside-out*.'''
    rx: ParamRef | float | str
    '''The rounded corner [*x*-radius][1], either in pixels or as a percentage of the rect width. If **rx** is not specified, it defaults to **ry** if present, and otherwise draws square corners.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/rx'''
    ry: ParamRef | float | str
    '''The rounded corner [*y*-radius][1], either in pixels or as a percentage of the rect height. If **ry** is not specified, it defaults to **rx** if present, and otherwise draws square corners.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/ry'''
    x: ChannelValueSpec
    '''The optional horizontal position of the bar; a ordinal channel typically bound to the *x* scale. If not specified, the bar spans the horizontal extent of the frame; otherwise the *x* scale must be a *band* scale.

If *x* represents quantitative or temporal values, use a rectY mark instead.'''
    y: ChannelValueIntervalSpec
    '''The vertical position (or length/height) channel, typically bound to the
*y* scale.

If neither **y1** nor **y2** nor **interval** is specified, an implicit stackY transform is applied and **y** defaults to the identity function, assuming that *data* = [*y₀*, *y₁*, *y₂*, …]. Otherwise if an **interval** is specified, then **y1** and **y2** are derived from **y**, representing the lower and upper bound of the containing interval, respectively. Otherwise, if only one of **y1** or **y2** is specified, the other defaults to **y**, which defaults to zero.'''
    y1: ChannelValueSpec
    '''The required primary (starting, often bottom) vertical position channel, typically bound to the *y* scale. Setting this option disables the implicit stackY transform.

If *y* represents ordinal values, use a cell mark instead.'''
    y2: ChannelValueSpec
    '''The required secondary (ending, often top) horizontal position channel, typically bound to the *y* scale. Setting this option disables the implicit stackY transform.

If *y* represents ordinal values, use a cell mark instead.'''
    z: ChannelValue
    '''The **z** channel defines the series of each value in the stack. Used when the **order** is *sum*, *appearance*, *inside-out*, or an explicit array of
**z** values.'''
class _CellOpen(MarkOptions,total=False):
    """The cell mark."""
    inset: ParamRef | float
    '''Shorthand to set the same default for all four insets: **insetTop**,
**insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it.'''
    inset_bottom: ParamRef | float
    '''Insets the bottom edge by the specified number of pixels. A positive value insets towards the top edge (reducing effective area), while a negative value insets away from the top edge (increasing it).'''
    inset_left: ParamRef | float
    '''Insets the left edge by the specified number of pixels. A positive value insets towards the right edge (reducing effective area), while a negative value insets away from the right edge (increasing it).'''
    inset_right: ParamRef | float
    '''Insets the right edge by the specified number of pixels. A positive value insets towards the left edge (reducing effective area), while a negative value insets away from the left edge (increasing it).'''
    inset_top: ParamRef | float
    '''Insets the top edge by the specified number of pixels. A positive value insets towards the bottom edge (reducing effective area), while a negative value insets away from the bottom edge (increasing it).'''
    mark: Required[L['cell']]
    '''A rectangular cell mark. Along with **x** and/or **y**, a **fill** channel is typically specified to encode value as color.

If neither **x** nor **y** are specified, *data* is assumed to be an array of pairs [[*x₀*, *y₀*], [*x₁*, *y₁*], [*x₂*, *y₂*], …] such that **x** = [*x₀*,
*x₁*, *x₂*, …] and **y** = [*y₀*, *y₁*, *y₂*, …].

Both **x** and **y** should be ordinal; if only **x** is quantitative (or temporal), use a barX mark; if only **y** is quantitative, use a barY mark; if both are quantitative, use a rect mark.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    rx: ParamRef | float | str
    '''The rounded corner [*x*-radius][1], either in pixels or as a percentage of the rect width. If **rx** is not specified, it defaults to **ry** if present, and otherwise draws square corners.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/rx'''
    ry: ParamRef | float | str
    '''The rounded corner [*y*-radius][1], either in pixels or as a percentage of the rect height. If **ry** is not specified, it defaults to **rx** if present, and otherwise draws square corners.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/ry'''
    x: ChannelValueSpec
    '''The horizontal position of the cell; an optional ordinal channel typically bound to the *x* scale. If not specified, the cell spans the horizontal extent of the frame; otherwise the *x* scale must be a *band* scale.

If *x* represents quantitative or temporal values, use a barX mark instead; if *y* is also quantitative or temporal, use a rect mark.'''
    y: ChannelValueSpec
    '''The vertical position of the cell; an optional ordinal channel typically bound to the *y* scale. If not specified, the cell spans the vertical extent of the frame; otherwise the *y* scale must be a *band* scale.

If *y* represents quantitative or temporal values, use a barY mark instead; if *x* is also quantitative or temporal, use a rect mark.'''
class _CellXOpen(MarkOptions,total=False):
    """The cellX mark."""
    inset: ParamRef | float
    '''Shorthand to set the same default for all four insets: **insetTop**,
**insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it.'''
    inset_bottom: ParamRef | float
    '''Insets the bottom edge by the specified number of pixels. A positive value insets towards the top edge (reducing effective area), while a negative value insets away from the top edge (increasing it).'''
    inset_left: ParamRef | float
    '''Insets the left edge by the specified number of pixels. A positive value insets towards the right edge (reducing effective area), while a negative value insets away from the right edge (increasing it).'''
    inset_right: ParamRef | float
    '''Insets the right edge by the specified number of pixels. A positive value insets towards the left edge (reducing effective area), while a negative value insets away from the left edge (increasing it).'''
    inset_top: ParamRef | float
    '''Insets the top edge by the specified number of pixels. A positive value insets towards the bottom edge (reducing effective area), while a negative value insets away from the bottom edge (increasing it).'''
    mark: Required[L['cellX']]
    '''Like cell, but **x** defaults to the zero-based index [0, 1, 2, …], and if
**stroke** is not a channel, **fill** defaults to the identity function, assuming that *data* = [*x₀*, *x₁*, *x₂*, …].'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    rx: ParamRef | float | str
    '''The rounded corner [*x*-radius][1], either in pixels or as a percentage of the rect width. If **rx** is not specified, it defaults to **ry** if present, and otherwise draws square corners.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/rx'''
    ry: ParamRef | float | str
    '''The rounded corner [*y*-radius][1], either in pixels or as a percentage of the rect height. If **ry** is not specified, it defaults to **rx** if present, and otherwise draws square corners.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/ry'''
    x: ChannelValueSpec
    '''The horizontal position of the cell; an optional ordinal channel typically bound to the *x* scale. If not specified, the cell spans the horizontal extent of the frame; otherwise the *x* scale must be a *band* scale.

If *x* represents quantitative or temporal values, use a barX mark instead; if *y* is also quantitative or temporal, use a rect mark.'''
    y: ChannelValueSpec
    '''The vertical position of the cell; an optional ordinal channel typically bound to the *y* scale. If not specified, the cell spans the vertical extent of the frame; otherwise the *y* scale must be a *band* scale.

If *y* represents quantitative or temporal values, use a barY mark instead; if *x* is also quantitative or temporal, use a rect mark.'''
class _CellYOpen(MarkOptions,total=False):
    """The cellY mark."""
    inset: ParamRef | float
    '''Shorthand to set the same default for all four insets: **insetTop**,
**insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it.'''
    inset_bottom: ParamRef | float
    '''Insets the bottom edge by the specified number of pixels. A positive value insets towards the top edge (reducing effective area), while a negative value insets away from the top edge (increasing it).'''
    inset_left: ParamRef | float
    '''Insets the left edge by the specified number of pixels. A positive value insets towards the right edge (reducing effective area), while a negative value insets away from the right edge (increasing it).'''
    inset_right: ParamRef | float
    '''Insets the right edge by the specified number of pixels. A positive value insets towards the left edge (reducing effective area), while a negative value insets away from the left edge (increasing it).'''
    inset_top: ParamRef | float
    '''Insets the top edge by the specified number of pixels. A positive value insets towards the bottom edge (reducing effective area), while a negative value insets away from the bottom edge (increasing it).'''
    mark: Required[L['cellY']]
    '''Like cell, but **y** defaults to the zero-based index [0, 1, 2, …], and if
**stroke** is not a channel, **fill** defaults to the identity function, assuming that *data* = [*y₀*, *y₁*, *y₂*, …].'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    rx: ParamRef | float | str
    '''The rounded corner [*x*-radius][1], either in pixels or as a percentage of the rect width. If **rx** is not specified, it defaults to **ry** if present, and otherwise draws square corners.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/rx'''
    ry: ParamRef | float | str
    '''The rounded corner [*y*-radius][1], either in pixels or as a percentage of the rect height. If **ry** is not specified, it defaults to **rx** if present, and otherwise draws square corners.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/ry'''
    x: ChannelValueSpec
    '''The horizontal position of the cell; an optional ordinal channel typically bound to the *x* scale. If not specified, the cell spans the horizontal extent of the frame; otherwise the *x* scale must be a *band* scale.

If *x* represents quantitative or temporal values, use a barX mark instead; if *y* is also quantitative or temporal, use a rect mark.'''
    y: ChannelValueSpec
    '''The vertical position of the cell; an optional ordinal channel typically bound to the *y* scale. If not specified, the cell spans the vertical extent of the frame; otherwise the *y* scale must be a *band* scale.

If *y* represents quantitative or temporal values, use a barY mark instead; if *x* is also quantitative or temporal, use a rect mark.'''
class _CircleOpen(MarkOptions,total=False):
    """The circle mark."""
    frame_anchor: FrameAnchor | ParamRef
    '''The frame anchor specifies defaults for **x** and **y** based on the plot's frame; it may be one of the four sides (*top*, *right*, *bottom*, *left*), one of the four corners (*top-left*, *top-right*, *bottom-right*,
*bottom-left*), or the *middle* of the frame. For example, for dots distributed horizontally at the top of the frame:

```js Plot.dot(data, {x: "date", frameAnchor: "top"}) ```'''
    mark: Required[L['circle']]
    '''Like dot, except that the **symbol** option is set to *circle*.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    r: ChannelValueSpec | ParamRef | float
    '''The radius of dots; either a channel or constant. When a number, it is interpreted as a constant radius in pixels. Otherwise it is interpreted as a channel, typically bound to the *r* channel, which defaults to the *sqrt* type for proportional symbols. The radius defaults to 4.5 pixels when using the **symbol** channel, and otherwise 3 pixels. Dots with a nonpositive radius are not drawn.'''
    rotate: ChannelValue | ParamRef | float
    '''The rotation angle of dots in degrees clockwise; either a channel or a constant. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel. Defaults to 0°, pointing up.'''
    symbol: ChannelValueSpec | ParamRef | SymbolType
    '''The categorical symbol; either a channel or a constant. A constant symbol can be specified by a valid symbol name such as *star*, or a symbol object (implementing the draw method); otherwise it is interpreted as a channel. Defaults to *circle* for the **dot** mark, and *hexagon* for the
**hexagon** mark.

If the **symbol** channel's values are all symbols, symbol names, or nullish, the channel is unscaled (values are interpreted literally); otherwise, the channel is bound to the *symbol* scale.'''
    x: ChannelValueSpec
    '''The horizontal position channel specifying the dot's center, typically bound to the *x* scale.'''
    y: ChannelValueSpec
    '''The vertical position channel specifying the dot's center, typically bound to the *y* scale.'''
    z: ChannelValue
    '''An optional ordinal channel for grouping data into series.'''
class _ContourOpen(MarkOptions,total=False):
    """The contour mark."""
    bandwidth: ParamRef | float
    '''The kernel density bandwidth for smoothing, in pixels.'''
    height: ParamRef | float
    '''The height (number of rows) of the grid, in actual pixels.'''
    interpolate: GridInterpolate | None | ParamRef
    '''The spatial interpolation method; one of:

- *none* - do not perform interpolation (the default), maps samples to single bins
- *linear* - apply proportional linear interpolation across adjacent bins
- *nearest* - assign each pixel to the closest sample's value (Voronoi diagram)
- *barycentric* - apply barycentric interpolation over the Delaunay triangulation
- *random-walk* - apply a random walk from each pixel, stopping when near a sample'''
    mark: Required[L['contour']]
    '''A contour mark that draws isolines to delineate regions above and below a particular continuous value. It is often used to convey densities as a height field. The special column name "density" can be used to map density values to the fill or stroke options.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    pad: ParamRef | float
    '''The bin padding, one of 1 (default) to include extra padding for the final bin, or 0 to make the bins flush with the maximum domain value.'''
    pixel_size: ParamRef | float
    '''The effective screen size of a raster pixel, used to determine the height and width of the raster from the frame's dimensions; defaults to 1.'''
    thresholds: ParamRef | Sequence[float] | float
    '''The number of contour thresholds to subdivide the domain into discrete level sets; defaults to 10. One of:

- a count representing the desired number of bins
- an array of *n* threshold values for *n* - 1 bins'''
    width: ParamRef | float
    '''The width (number of columns) of the grid, in actual pixels.'''
    x: ChannelValueSpec
    '''The horizontal position channel, typically bound to the *x* scale. Domain values are binned into a grid with *width* horizontal bins.'''
    y: ChannelValueSpec
    '''The vertical position channel, typically bound to the *y* scale. Domain values are binned into a grid with *height* vertical bins.'''
class _DelaunayLinkOpen(MarkOptions,total=False):
    """The delaunayLink mark."""
    curve: Curve | ParamRef
    '''The curve (interpolation) method for connecting adjacent points. One of:

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
- *step-before* - a piecewise constant function where *x* changes after *y*'''
    mark: Required[L['delaunayLink']]
    '''A mark that draws links for each edge of the Delaunay triangulation of points given by the **x** and **y** channels. Like the link mark, except that **x1**, **y1**, **x2**, and **y2** are derived automatically from **x** and **y**. When an aesthetic channel is specified (such as
**stroke** or **strokeWidth**), the link inherits the corresponding channel value from one of its two endpoints arbitrarily.

If **z** is specified, the input points are grouped by *z*, producing a separate Delaunay triangulation for each group.'''
    marker: L['none'] | MarkerName | None | ParamRef | bool
    '''Shorthand to set the same default for markerStart, markerMid, and markerEnd; one of:

- a marker name such as *arrow* or *circle*
- *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_end: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the ending point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_mid: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for any middle (interior) points of a line segment. If the line segment only has a start and end point, this option has no effect. One of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*
* a function - a custom marker function; see below'''
    marker_start: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the starting point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    tension: ParamRef | float
    '''The tension option only has an effect on bundle, cardinal and Catmull-Rom splines (*bundle*, *cardinal*, *cardinal-open*, *cardinal-closed*,
*catmull-rom*, *catmull-rom-open*, and *catmull-rom-closed*). For bundle splines, it corresponds to [beta][1]; for cardinal splines, [tension][2]; for Catmull-Rom splines, [alpha][3].

[1]: https://d3js.org/d3-shape/curve#curveBundle_beta [2]: https://d3js.org/d3-shape/curve#curveCardinal_tension [3]: https://d3js.org/d3-shape/curve#curveCatmullRom_alpha'''
    x: ChannelValueSpec
    '''The horizontal position channel, typically bound to the *x* scale.'''
    y: ChannelValueSpec
    '''The vertical position channel, typically bound to the *y* scale.'''
    z: ChannelValue
    '''An optional ordinal channel for grouping to produce multiple (possibly overlapping) triangulations.'''
class _DelaunayMeshOpen(MarkOptions,total=False):
    """The delaunayMesh mark."""
    curve: Curve | ParamRef
    '''The curve (interpolation) method for connecting adjacent points. One of:

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
- *step-before* - a piecewise constant function where *x* changes after *y*'''
    mark: Required[L['delaunayMesh']]
    '''A mark that draws a mesh of the Delaunay triangulation of the points given by the **x** and **y** channels. The **stroke** option defaults to _currentColor_, and the **strokeOpacity** defaults to 0.2; the **fill** option is not supported. When an aesthetic channel is specified (such as
**stroke** or **strokeWidth**), the mesh inherits the corresponding channel value from one of its constituent points arbitrarily.

If **z** is specified, the input points are grouped by *z*, producing a separate Delaunay triangulation for each group.'''
    marker: L['none'] | MarkerName | None | ParamRef | bool
    '''Shorthand to set the same default for markerStart, markerMid, and markerEnd; one of:

- a marker name such as *arrow* or *circle*
- *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_end: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the ending point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_mid: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for any middle (interior) points of a line segment. If the line segment only has a start and end point, this option has no effect. One of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*
* a function - a custom marker function; see below'''
    marker_start: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the starting point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    tension: ParamRef | float
    '''The tension option only has an effect on bundle, cardinal and Catmull-Rom splines (*bundle*, *cardinal*, *cardinal-open*, *cardinal-closed*,
*catmull-rom*, *catmull-rom-open*, and *catmull-rom-closed*). For bundle splines, it corresponds to [beta][1]; for cardinal splines, [tension][2]; for Catmull-Rom splines, [alpha][3].

[1]: https://d3js.org/d3-shape/curve#curveBundle_beta [2]: https://d3js.org/d3-shape/curve#curveCardinal_tension [3]: https://d3js.org/d3-shape/curve#curveCatmullRom_alpha'''
    x: ChannelValueSpec
    '''The horizontal position channel, typically bound to the *x* scale.'''
    y: ChannelValueSpec
    '''The vertical position channel, typically bound to the *y* scale.'''
    z: ChannelValue
    '''An optional ordinal channel for grouping to produce multiple (possibly overlapping) triangulations.'''
class _DenseLineOpen(MarkOptions,total=False):
    """The denseLine mark."""
    bandwidth: ParamRef | float
    '''The kernel density bandwidth for smoothing, in pixels.'''
    height: ParamRef | float
    '''The height (number of rows) of the grid, in actual pixels.'''
    image_rendering: ParamRef | str
    '''The [image-rendering attribute][1]; defaults to *auto* (bilinear). The option may be set to *pixelated* to disable bilinear interpolation for a sharper image; however, note that this is not supported in WebKit.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/image-rendering'''
    interpolate: GridInterpolate | None | ParamRef
    '''The spatial interpolation method; one of:

- *none* - do not perform interpolation (the default), maps samples to single bins
- *linear* - apply proportional linear interpolation across adjacent bins
- *nearest* - assign each pixel to the closest sample's value (Voronoi diagram)
- *barycentric* - apply barycentric interpolation over the Delaunay triangulation
- *random-walk* - apply a random walk from each pixel, stopping when near a sample'''
    mark: Required[L['denseLine']]
    '''A denseLine mark that plots line densities rather than point densities. The mark forms a binned raster grid and "draws" straight lines into it. To avoid over-weighting steep lines, by default each drawn series is normalized on a per-column basis to approximate arc length normalization. The values for each series are aggregated to form the line density, which is then drawn as an image similar to the raster mark.'''
    normalize: ParamRef | bool
    '''Flag to perform approximate arc length normalization of line segments to prevent artifacts due to overcounting steep lines. Defaults to `true`.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    pad: ParamRef | float
    '''The bin padding, one of 1 (default) to include extra padding for the final bin, or 0 to make the bins flush with the maximum domain value.'''
    pixel_size: ParamRef | float
    '''The effective screen size of a raster pixel, used to determine the height and width of the raster from the frame's dimensions; defaults to 1.'''
    width: ParamRef | float
    '''The width (number of columns) of the grid, in actual pixels.'''
    x: ChannelValueSpec
    '''The horizontal position channel, typically bound to the *x* scale. Domain values are binned into a grid with *width* horizontal bins.'''
    y: ChannelValueSpec
    '''The vertical position channel, typically bound to the *y* scale. Domain values are binned into a grid with *height* vertical bins.'''
    z: ChannelValue
    '''A ordinal channel for grouping data into series to be drawn as separate lines.'''
class _DensityOpen(MarkOptions,total=False):
    """The density mark for 2D densities."""
    bandwidth: ParamRef | float
    '''The kernel density bandwidth for smoothing, in pixels.'''
    font_family: ParamRef | str
    '''The [font-family][1]; a constant; defaults to the plot's font family, which is typically [*system-ui*][2].

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-family [2]: https://drafts.csswg.org/css-fonts-4/#valdef-font-family-system-ui'''
    font_size: ChannelValue | ParamRef
    '''The [font size][1] in pixels; either a constant or a channel; defaults to the plot's font size, which is typically 10. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-size'''
    font_style: ParamRef | str
    '''The [font style][1]; a constant; defaults to the plot's font style, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-style'''
    font_variant: ParamRef | str
    '''The [font variant][1]; a constant; if the **text** channel contains numbers or dates, defaults to *tabular-nums* to facilitate comparing numbers; otherwise defaults to the plot's font style, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant'''
    font_weight: ParamRef | float | str
    '''The [font weight][1]; a constant; defaults to the plot's font weight, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight'''
    frame_anchor: FrameAnchor | ParamRef
    '''The frame anchor specifies defaults for **x** and **y** based on the plot's frame; it may be one of the four sides (*top*, *right*, *bottom*, *left*), one of the four corners (*top-left*, *top-right*, *bottom-right*,
*bottom-left*), or the *middle* of the frame. For example, for dots distributed horizontally at the top of the frame:

```js Plot.dot(data, {x: "date", frameAnchor: "top"}) ```'''
    height: ParamRef | float
    '''The height (number of rows) of the grid, in actual pixels.'''
    interpolate: GridInterpolate | None | ParamRef
    '''The spatial interpolation method; one of:

- *none* - do not perform interpolation (the default), maps samples to single bins
- *linear* - apply proportional linear interpolation across adjacent bins
- *nearest* - assign each pixel to the closest sample's value (Voronoi diagram)
- *barycentric* - apply barycentric interpolation over the Delaunay triangulation
- *random-walk* - apply a random walk from each pixel, stopping when near a sample'''
    line_height: ParamRef | float
    '''The line height in ems; defaults to 1. The line height affects the (typically vertical) separation between adjacent baselines of text, as well as the separation between the text and its anchor point.'''
    line_width: ParamRef | float
    '''The line width in ems (e.g., 10 for about 20 characters); defaults to infinity, disabling wrapping and clipping.

If **textOverflow** is null, lines will be wrapped at the specified length. If a line is split at a soft hyphen (\xad), a hyphen (-) will be displayed at the end of the line. If **textOverflow** is not null, lines will be clipped according to the given strategy.'''
    mark: Required[L['density']]
    '''A 2D density mark that shows smoothed point cloud densities along two dimensions. The mark bins the data, counts the number of records that fall into each bin, and smooths the resulting counts, then plots the smoothed distribution, by default using a circular dot mark. The density mark calculates density values that can be mapped to encoding channels such as fill or r using the special field name "density".

Set the *type* property to use a different base mark type.'''
    monospace: ParamRef | bool
    '''If true, changes the default **fontFamily** to *monospace*, and uses simplified monospaced text metrics calculations.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    pad: ParamRef | float
    '''The bin padding, one of 1 (default) to include extra padding for the final bin, or 0 to make the bins flush with the maximum domain value.'''
    pixel_size: ParamRef | float
    '''The effective screen size of a raster pixel, used to determine the height and width of the raster from the frame's dimensions; defaults to 1.'''
    r: ChannelValueSpec | ParamRef | float
    '''The radius of dots; either a channel or constant. When a number, it is interpreted as a constant radius in pixels. Otherwise it is interpreted as a channel, typically bound to the *r* channel, which defaults to the *sqrt* type for proportional symbols. The radius defaults to 4.5 pixels when using the **symbol** channel, and otherwise 3 pixels. Dots with a nonpositive radius are not drawn.'''
    rotate: ChannelValue | ParamRef | float
    '''The rotation angle of dots in degrees clockwise; either a channel or a constant. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel. Defaults to 0°, pointing up.'''
    symbol: ChannelValueSpec | ParamRef | SymbolType
    '''The categorical symbol; either a channel or a constant. A constant symbol can be specified by a valid symbol name such as *star*, or a symbol object (implementing the draw method); otherwise it is interpreted as a channel. Defaults to *circle* for the **dot** mark, and *hexagon* for the
**hexagon** mark.

If the **symbol** channel's values are all symbols, symbol names, or nullish, the channel is unscaled (values are interpreted literally); otherwise, the channel is bound to the *symbol* scale.'''
    text_anchor: L['end','middle','start'] | ParamRef
    '''The [text anchor][1] controls how text is aligned (typically horizontally) relative to its anchor point; it is one of *start*, *end*, or *middle*. If the frame anchor is *left*, *top-left*, or *bottom-left*, the default text anchor is *start*; if the frame anchor is *right*, *top-right*, or
*bottom-right*, the default is *end*; otherwise it is *middle*.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/text-anchor'''
    text_overflow: L['clip','clip-end','clip-start','ellipsis','ellipsis-end','ellipsis-middle','ellipsis-start'] | None | ParamRef
    '''How truncate (or wrap) lines of text longer than the given **lineWidth**; one of:

- null (default) - preserve overflowing characters (and wrap if needed)
- *clip* or *clip-end* - remove characters from the end
- *clip-start* - remove characters from the start
- *ellipsis* or *ellipsis-end* - replace characters from the end with an ellipsis (…)
- *ellipsis-start* - replace characters from the start with an ellipsis (…)
- *ellipsis-middle* - replace characters from the middle with an ellipsis (…)

If no **title** was specified, if text requires truncation, a title containing the non-truncated text will be implicitly added.'''
    type: L['cell','circle','dot','hexagon','text'] | ParamRef
    '''The basic mark type to use to render 2D density values. Defaults to a dot mark; cell and text marks are also supported.'''
    width: ParamRef | float
    '''The width (number of columns) of the grid, in actual pixels.'''
    x: ChannelValueSpec
    '''The horizontal position channel, typically bound to the *x* scale. Domain values are binned into a grid with *width* horizontal bins.'''
    y: ChannelValueSpec
    '''The vertical position channel, typically bound to the *y* scale. Domain values are binned into a grid with *height* vertical bins.'''
    z: ChannelValue
    '''An optional ordinal channel for grouping data into series.'''
class _DensityXAreaXOpen(MarkOptions,total=False):
    """The densityX mark."""
    bandwidth: ParamRef | float
    '''The kernel density bandwidth for smoothing, in pixels. Defaults to 20.'''
    bins: ParamRef | float
    '''The number of bins over which to discretize the data prior to smoothing. Defaults to 1024.'''
    curve: Curve | ParamRef
    '''The curve (interpolation) method for connecting adjacent points. One of:

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
- *step-before* - a piecewise constant function where *x* changes after *y*'''
    mark: Required[L['densityX']]
    '''A densityX mark that visualizes smoothed point cloud densities along the
**x** dimension. The mark bins the data, counts the number of records that fall into each bin, smooths the resulting counts, and then plots the smoothed distribution, by default using an areaX mark.

Set the *type* property to use a different base mark type.'''
    normalize: L['max','none','sum'] | ParamRef | bool
    '''Normalization method for density estimates. If `false` or `'none'` (the default), the density estimates are smoothed weighted counts. If `true` or `'sum'`, density estimates are divided by the sum of the total point mass. If `'max'`, estimates are divided by the maximum smoothed value.'''
    offset: None | ParamRef | StackOffset
    '''After stacking, an optional **offset** can be applied to translate and scale stacks, say to produce a streamgraph; defaults to null for a zero baseline (**y** = 0 for stackY, and **x** = 0 for stackX). If the *wiggle* offset is used, the default **order** changes to *inside-out*.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    order: None | ParamRef | StackOrder
    '''The order in which stacks are layered; one of:

- null (default) for input order
- a named stack order method such as *inside-out* or *sum*
- a field name, for natural order of the corresponding values
- a function of data, for natural order of the corresponding values
- an array of explicit **z** values in the desired order

If the *wiggle* **offset** is used, as for a streamgraph, the default changes to *inside-out*.'''
    stack: ParamRef | bool
    '''Flag indicating if densities should be stacked. Defaults to false.'''
    tension: ParamRef | float
    '''The tension option only has an effect on bundle, cardinal and Catmull-Rom splines (*bundle*, *cardinal*, *cardinal-open*, *cardinal-closed*,
*catmull-rom*, *catmull-rom-open*, and *catmull-rom-closed*). For bundle splines, it corresponds to [beta][1]; for cardinal splines, [tension][2]; for Catmull-Rom splines, [alpha][3].

[1]: https://d3js.org/d3-shape/curve#curveBundle_beta [2]: https://d3js.org/d3-shape/curve#curveCardinal_tension [3]: https://d3js.org/d3-shape/curve#curveCatmullRom_alpha'''
    type: Required[L['areaX']]
    '''The basic mark type to use to render 1D density values. Defaults to an areaX mark; lineX, dotX, and textX marks are also supported.'''
    y: ChannelValueSpec
    '''The vertical position channel, typically bound to the *y* scale; defaults to the zero-based index of the data [0, 1, 2, …].'''
    z: ChannelValue
    '''An optional ordinal channel for grouping data into (possibly stacked) series to be drawn as separate areas; defaults to **fill** if a channel, or
**stroke** if a channel.'''
class _DensityXDotXOpen(MarkOptions,total=False):
    """The densityX mark."""
    bandwidth: ParamRef | float
    '''The kernel density bandwidth for smoothing, in pixels. Defaults to 20.'''
    bins: ParamRef | float
    '''The number of bins over which to discretize the data prior to smoothing. Defaults to 1024.'''
    frame_anchor: FrameAnchor | ParamRef
    '''The frame anchor specifies defaults for **x** and **y** based on the plot's frame; it may be one of the four sides (*top*, *right*, *bottom*, *left*), one of the four corners (*top-left*, *top-right*, *bottom-right*,
*bottom-left*), or the *middle* of the frame. For example, for dots distributed horizontally at the top of the frame:

```js Plot.dot(data, {x: "date", frameAnchor: "top"}) ```'''
    mark: Required[L['densityX']]
    '''A densityX mark that visualizes smoothed point cloud densities along the
**x** dimension. The mark bins the data, counts the number of records that fall into each bin, smooths the resulting counts, and then plots the smoothed distribution, by default using an areaX mark.

Set the *type* property to use a different base mark type.'''
    normalize: L['max','none','sum'] | ParamRef | bool
    '''Normalization method for density estimates. If `false` or `'none'` (the default), the density estimates are smoothed weighted counts. If `true` or `'sum'`, density estimates are divided by the sum of the total point mass. If `'max'`, estimates are divided by the maximum smoothed value.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    r: ChannelValueSpec | ParamRef | float
    '''The radius of dots; either a channel or constant. When a number, it is interpreted as a constant radius in pixels. Otherwise it is interpreted as a channel, typically bound to the *r* channel, which defaults to the *sqrt* type for proportional symbols. The radius defaults to 4.5 pixels when using the **symbol** channel, and otherwise 3 pixels. Dots with a nonpositive radius are not drawn.'''
    rotate: ChannelValue | ParamRef | float
    '''The rotation angle of dots in degrees clockwise; either a channel or a constant. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel. Defaults to 0°, pointing up.'''
    symbol: ChannelValueSpec | ParamRef | SymbolType
    '''The categorical symbol; either a channel or a constant. A constant symbol can be specified by a valid symbol name such as *star*, or a symbol object (implementing the draw method); otherwise it is interpreted as a channel. Defaults to *circle* for the **dot** mark, and *hexagon* for the
**hexagon** mark.

If the **symbol** channel's values are all symbols, symbol names, or nullish, the channel is unscaled (values are interpreted literally); otherwise, the channel is bound to the *symbol* scale.'''
    type: Required[L['dotX']]
    '''The basic mark type to use to render 1D density values. Defaults to an areaX mark; lineX, dotX, and textX marks are also supported.'''
    y: ChannelValueSpec
    '''The vertical position channel specifying the dot's center, typically bound to the *y* scale.'''
    z: ChannelValue
    '''An optional ordinal channel for grouping data into series.'''
class _DensityXLineXOpen(MarkOptions,total=False):
    """The densityX mark."""
    bandwidth: ParamRef | float
    '''The kernel density bandwidth for smoothing, in pixels. Defaults to 20.'''
    bins: ParamRef | float
    '''The number of bins over which to discretize the data prior to smoothing. Defaults to 1024.'''
    curve: Curve | L['auto'] | ParamRef
    '''The curve (interpolation) method for connecting adjacent points. One of:

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
- *auto* (default) - like *linear*, but use the (possibly spherical) projection, if any

The *auto* curve is typically used in conjunction with a spherical projection to interpolate along geodesics.'''
    mark: Required[L['densityX']]
    '''A densityX mark that visualizes smoothed point cloud densities along the
**x** dimension. The mark bins the data, counts the number of records that fall into each bin, smooths the resulting counts, and then plots the smoothed distribution, by default using an areaX mark.

Set the *type* property to use a different base mark type.'''
    marker: L['none'] | MarkerName | None | ParamRef | bool
    '''Shorthand to set the same default for markerStart, markerMid, and markerEnd; one of:

- a marker name such as *arrow* or *circle*
- *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_end: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the ending point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_mid: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for any middle (interior) points of a line segment. If the line segment only has a start and end point, this option has no effect. One of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*
* a function - a custom marker function; see below'''
    marker_start: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the starting point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    normalize: L['max','none','sum'] | ParamRef | bool
    '''Normalization method for density estimates. If `false` or `'none'` (the default), the density estimates are smoothed weighted counts. If `true` or `'sum'`, density estimates are divided by the sum of the total point mass. If `'max'`, estimates are divided by the maximum smoothed value.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    tension: ParamRef | float
    '''The tension option only has an effect on bundle, cardinal and Catmull-Rom splines (*bundle*, *cardinal*, *cardinal-open*, *cardinal-closed*,
*catmull-rom*, *catmull-rom-open*, and *catmull-rom-closed*). For bundle splines, it corresponds to [beta][1]; for cardinal splines, [tension][2]; for Catmull-Rom splines, [alpha][3].

[1]: https://d3js.org/d3-shape/curve#curveBundle_beta [2]: https://d3js.org/d3-shape/curve#curveCardinal_tension [3]: https://d3js.org/d3-shape/curve#curveCatmullRom_alpha'''
    type: Required[L['lineX']]
    '''The basic mark type to use to render 1D density values. Defaults to an areaX mark; lineX, dotX, and textX marks are also supported.'''
    y: ChannelValueSpec
    '''The vertical position channel, typically bound to the *y* scale; defaults to the zero-based index of the data [0, 1, 2, …].'''
    z: ChannelValue
    '''An optional ordinal channel for grouping data into (possibly stacked) series to be drawn as separate lines. If not specified, it defaults to
**fill** if a channel, or **stroke** if a channel.'''
class _DensityXTextXOpen(MarkOptions,total=False):
    """The densityX mark."""
    bandwidth: ParamRef | float
    '''The kernel density bandwidth for smoothing, in pixels. Defaults to 20.'''
    bins: ParamRef | float
    '''The number of bins over which to discretize the data prior to smoothing. Defaults to 1024.'''
    font_family: ParamRef | str
    '''The [font-family][1]; a constant; defaults to the plot's font family, which is typically [*system-ui*][2].

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-family [2]: https://drafts.csswg.org/css-fonts-4/#valdef-font-family-system-ui'''
    font_size: ChannelValue | ParamRef
    '''The [font size][1] in pixels; either a constant or a channel; defaults to the plot's font size, which is typically 10. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-size'''
    font_style: ParamRef | str
    '''The [font style][1]; a constant; defaults to the plot's font style, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-style'''
    font_variant: ParamRef | str
    '''The [font variant][1]; a constant; if the **text** channel contains numbers or dates, defaults to *tabular-nums* to facilitate comparing numbers; otherwise defaults to the plot's font style, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant'''
    font_weight: ParamRef | float | str
    '''The [font weight][1]; a constant; defaults to the plot's font weight, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight'''
    frame_anchor: FrameAnchor | ParamRef
    '''The frame anchor specifies defaults for **x** and **y**, along with
**textAnchor** and **lineAnchor**, based on the plot's frame; it may be one of the four sides (*top*, *right*, *bottom*, *left*), one of the four corners (*top-left*, *top-right*, *bottom-right*, *bottom-left*), or the
*middle* of the frame.'''
    line_anchor: L['bottom','middle','top'] | ParamRef
    '''The line anchor controls how text is aligned (typically vertically) relative to its anchor point; it is one of *top*, *bottom*, or *middle*. If the frame anchor is *top*, *top-left*, or *top-right*, the default line anchor is *top*; if the frame anchor is *bottom*, *bottom-right*, or
*bottom-left*, the default is *bottom*; otherwise it is *middle*.'''
    line_height: ParamRef | float
    '''The line height in ems; defaults to 1. The line height affects the (typically vertical) separation between adjacent baselines of text, as well as the separation between the text and its anchor point.'''
    line_width: ParamRef | float
    '''The line width in ems (e.g., 10 for about 20 characters); defaults to infinity, disabling wrapping and clipping.

If **textOverflow** is null, lines will be wrapped at the specified length. If a line is split at a soft hyphen (\xad), a hyphen (-) will be displayed at the end of the line. If **textOverflow** is not null, lines will be clipped according to the given strategy.'''
    mark: Required[L['densityX']]
    '''A densityX mark that visualizes smoothed point cloud densities along the
**x** dimension. The mark bins the data, counts the number of records that fall into each bin, smooths the resulting counts, and then plots the smoothed distribution, by default using an areaX mark.

Set the *type* property to use a different base mark type.'''
    monospace: ParamRef | bool
    '''If true, changes the default **fontFamily** to *monospace*, and uses simplified monospaced text metrics calculations.'''
    normalize: L['max','none','sum'] | ParamRef | bool
    '''Normalization method for density estimates. If `false` or `'none'` (the default), the density estimates are smoothed weighted counts. If `true` or `'sum'`, density estimates are divided by the sum of the total point mass. If `'max'`, estimates are divided by the maximum smoothed value.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    rotate: ChannelValue | ParamRef
    '''The rotation angle in degrees clockwise; a constant or a channel; defaults to 0°. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel.'''
    text: ChannelValue
    '''The text contents channel, possibly with line breaks (\n, \r\n, or \r). If not specified, defaults to the zero-based index [0, 1, 2, …].'''
    text_anchor: L['end','middle','start'] | ParamRef
    '''The [text anchor][1] controls how text is aligned (typically horizontally) relative to its anchor point; it is one of *start*, *end*, or *middle*. If the frame anchor is *left*, *top-left*, or *bottom-left*, the default text anchor is *start*; if the frame anchor is *right*, *top-right*, or
*bottom-right*, the default is *end*; otherwise it is *middle*.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/text-anchor'''
    text_overflow: L['clip','clip-end','clip-start','ellipsis','ellipsis-end','ellipsis-middle','ellipsis-start'] | None | ParamRef
    '''How truncate (or wrap) lines of text longer than the given **lineWidth**; one of:

- null (default) - preserve overflowing characters (and wrap if needed)
- *clip* or *clip-end* - remove characters from the end
- *clip-start* - remove characters from the start
- *ellipsis* or *ellipsis-end* - replace characters from the end with an ellipsis (…)
- *ellipsis-start* - replace characters from the start with an ellipsis (…)
- *ellipsis-middle* - replace characters from the middle with an ellipsis (…)

If no **title** was specified, if text requires truncation, a title containing the non-truncated text will be implicitly added.'''
    type: Required[L['textX']]
    '''The basic mark type to use to render 1D density values. Defaults to an areaX mark; lineX, dotX, and textX marks are also supported.'''
    y: ChannelValueSpec
    '''The vertical position channel specifying the text's anchor point, typically bound to the *y* scale.'''
    z: ChannelValue
    '''An optional ordinal channel for grouping data into series.'''
class _DensityYAreaYOpen(MarkOptions,total=False):
    """The densityY mark."""
    bandwidth: ParamRef | float
    '''The kernel density bandwidth for smoothing, in pixels. Defaults to 20.'''
    bins: ParamRef | float
    '''The number of bins over which to discretize the data prior to smoothing. Defaults to 1024.'''
    curve: Curve | ParamRef
    '''The curve (interpolation) method for connecting adjacent points. One of:

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
- *step-before* - a piecewise constant function where *x* changes after *y*'''
    mark: Required[L['densityY']]
    '''A densityY mark that visualizes smoothed point cloud densities along the
**y** dimension. The mark bins the data, counts the number of records that fall into each bin, smooths the resulting counts, and then plots the smoothed distribution, by default using an areaY mark.

Set the *type* property to use a different base mark type.'''
    normalize: L['max','none','sum'] | ParamRef | bool
    '''Normalization method for density estimates. If `false` or `'none'` (the default), the density estimates are smoothed weighted counts. If `true` or `'sum'`, density estimates are divided by the sum of the total point mass. If `'max'`, estimates are divided by the maximum smoothed value.'''
    offset: None | ParamRef | StackOffset
    '''After stacking, an optional **offset** can be applied to translate and scale stacks, say to produce a streamgraph; defaults to null for a zero baseline (**y** = 0 for stackY, and **x** = 0 for stackX). If the *wiggle* offset is used, the default **order** changes to *inside-out*.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    order: None | ParamRef | StackOrder
    '''The order in which stacks are layered; one of:

- null (default) for input order
- a named stack order method such as *inside-out* or *sum*
- a field name, for natural order of the corresponding values
- a function of data, for natural order of the corresponding values
- an array of explicit **z** values in the desired order

If the *wiggle* **offset** is used, as for a streamgraph, the default changes to *inside-out*.'''
    stack: ParamRef | bool
    '''Flag indicating if densities should be stacked. Defaults to false.'''
    tension: ParamRef | float
    '''The tension option only has an effect on bundle, cardinal and Catmull-Rom splines (*bundle*, *cardinal*, *cardinal-open*, *cardinal-closed*,
*catmull-rom*, *catmull-rom-open*, and *catmull-rom-closed*). For bundle splines, it corresponds to [beta][1]; for cardinal splines, [tension][2]; for Catmull-Rom splines, [alpha][3].

[1]: https://d3js.org/d3-shape/curve#curveBundle_beta [2]: https://d3js.org/d3-shape/curve#curveCardinal_tension [3]: https://d3js.org/d3-shape/curve#curveCatmullRom_alpha'''
    type: L['areaY']
    '''The basic mark type to use to render 1D density values. Defaults to an areaY mark; lineY, dot, and text marks are also supported.'''
    x: ChannelValueSpec
    '''The horizontal position channel, typically bound to the *x* scale; defaults to the zero-based index of the data [0, 1, 2, …].'''
    z: ChannelValue
    '''An optional ordinal channel for grouping data into (possibly stacked) series to be drawn as separate areas; defaults to **fill** if a channel, or
**stroke** if a channel.'''
class _DensityYDotOpen(MarkOptions,total=False):
    """The densityY mark."""
    bandwidth: ParamRef | float
    '''The kernel density bandwidth for smoothing, in pixels. Defaults to 20.'''
    bins: ParamRef | float
    '''The number of bins over which to discretize the data prior to smoothing. Defaults to 1024.'''
    frame_anchor: FrameAnchor | ParamRef
    '''The frame anchor specifies defaults for **x** and **y** based on the plot's frame; it may be one of the four sides (*top*, *right*, *bottom*, *left*), one of the four corners (*top-left*, *top-right*, *bottom-right*,
*bottom-left*), or the *middle* of the frame. For example, for dots distributed horizontally at the top of the frame:

```js Plot.dot(data, {x: "date", frameAnchor: "top"}) ```'''
    mark: Required[L['densityY']]
    '''A densityY mark that visualizes smoothed point cloud densities along the
**y** dimension. The mark bins the data, counts the number of records that fall into each bin, smooths the resulting counts, and then plots the smoothed distribution, by default using an areaY mark.

Set the *type* property to use a different base mark type.'''
    normalize: L['max','none','sum'] | ParamRef | bool
    '''Normalization method for density estimates. If `false` or `'none'` (the default), the density estimates are smoothed weighted counts. If `true` or `'sum'`, density estimates are divided by the sum of the total point mass. If `'max'`, estimates are divided by the maximum smoothed value.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    r: ChannelValueSpec | ParamRef | float
    '''The radius of dots; either a channel or constant. When a number, it is interpreted as a constant radius in pixels. Otherwise it is interpreted as a channel, typically bound to the *r* channel, which defaults to the *sqrt* type for proportional symbols. The radius defaults to 4.5 pixels when using the **symbol** channel, and otherwise 3 pixels. Dots with a nonpositive radius are not drawn.'''
    rotate: ChannelValue | ParamRef | float
    '''The rotation angle of dots in degrees clockwise; either a channel or a constant. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel. Defaults to 0°, pointing up.'''
    symbol: ChannelValueSpec | ParamRef | SymbolType
    '''The categorical symbol; either a channel or a constant. A constant symbol can be specified by a valid symbol name such as *star*, or a symbol object (implementing the draw method); otherwise it is interpreted as a channel. Defaults to *circle* for the **dot** mark, and *hexagon* for the
**hexagon** mark.

If the **symbol** channel's values are all symbols, symbol names, or nullish, the channel is unscaled (values are interpreted literally); otherwise, the channel is bound to the *symbol* scale.'''
    type: Required[L['circle','dot','dotY','hexagon']]
    '''The basic mark type to use to render 1D density values. Defaults to an areaY mark; lineY, dot, and text marks are also supported.'''
    x: ChannelValueSpec
    '''The horizontal position channel specifying the dot's center, typically bound to the *x* scale.'''
    z: ChannelValue
    '''An optional ordinal channel for grouping data into series.'''
class _DensityYLineYOpen(MarkOptions,total=False):
    """The densityY mark."""
    bandwidth: ParamRef | float
    '''The kernel density bandwidth for smoothing, in pixels. Defaults to 20.'''
    bins: ParamRef | float
    '''The number of bins over which to discretize the data prior to smoothing. Defaults to 1024.'''
    curve: Curve | L['auto'] | ParamRef
    '''The curve (interpolation) method for connecting adjacent points. One of:

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
- *auto* (default) - like *linear*, but use the (possibly spherical) projection, if any

The *auto* curve is typically used in conjunction with a spherical projection to interpolate along geodesics.'''
    mark: Required[L['densityY']]
    '''A densityY mark that visualizes smoothed point cloud densities along the
**y** dimension. The mark bins the data, counts the number of records that fall into each bin, smooths the resulting counts, and then plots the smoothed distribution, by default using an areaY mark.

Set the *type* property to use a different base mark type.'''
    marker: L['none'] | MarkerName | None | ParamRef | bool
    '''Shorthand to set the same default for markerStart, markerMid, and markerEnd; one of:

- a marker name such as *arrow* or *circle*
- *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_end: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the ending point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_mid: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for any middle (interior) points of a line segment. If the line segment only has a start and end point, this option has no effect. One of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*
* a function - a custom marker function; see below'''
    marker_start: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the starting point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    normalize: L['max','none','sum'] | ParamRef | bool
    '''Normalization method for density estimates. If `false` or `'none'` (the default), the density estimates are smoothed weighted counts. If `true` or `'sum'`, density estimates are divided by the sum of the total point mass. If `'max'`, estimates are divided by the maximum smoothed value.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    tension: ParamRef | float
    '''The tension option only has an effect on bundle, cardinal and Catmull-Rom splines (*bundle*, *cardinal*, *cardinal-open*, *cardinal-closed*,
*catmull-rom*, *catmull-rom-open*, and *catmull-rom-closed*). For bundle splines, it corresponds to [beta][1]; for cardinal splines, [tension][2]; for Catmull-Rom splines, [alpha][3].

[1]: https://d3js.org/d3-shape/curve#curveBundle_beta [2]: https://d3js.org/d3-shape/curve#curveCardinal_tension [3]: https://d3js.org/d3-shape/curve#curveCatmullRom_alpha'''
    type: Required[L['lineY']]
    '''The basic mark type to use to render 1D density values. Defaults to an areaY mark; lineY, dot, and text marks are also supported.'''
    x: ChannelValueSpec
    '''The horizontal position channel, typically bound to the *x* scale; defaults to the zero-based index of the data [0, 1, 2, …].'''
    z: ChannelValue
    '''An optional ordinal channel for grouping data into (possibly stacked) series to be drawn as separate lines. If not specified, it defaults to
**fill** if a channel, or **stroke** if a channel.'''
class _DensityYTextOpen(MarkOptions,total=False):
    """The densityY mark."""
    bandwidth: ParamRef | float
    '''The kernel density bandwidth for smoothing, in pixels. Defaults to 20.'''
    bins: ParamRef | float
    '''The number of bins over which to discretize the data prior to smoothing. Defaults to 1024.'''
    font_family: ParamRef | str
    '''The [font-family][1]; a constant; defaults to the plot's font family, which is typically [*system-ui*][2].

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-family [2]: https://drafts.csswg.org/css-fonts-4/#valdef-font-family-system-ui'''
    font_size: ChannelValue | ParamRef
    '''The [font size][1] in pixels; either a constant or a channel; defaults to the plot's font size, which is typically 10. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-size'''
    font_style: ParamRef | str
    '''The [font style][1]; a constant; defaults to the plot's font style, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-style'''
    font_variant: ParamRef | str
    '''The [font variant][1]; a constant; if the **text** channel contains numbers or dates, defaults to *tabular-nums* to facilitate comparing numbers; otherwise defaults to the plot's font style, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant'''
    font_weight: ParamRef | float | str
    '''The [font weight][1]; a constant; defaults to the plot's font weight, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight'''
    frame_anchor: FrameAnchor | ParamRef
    '''The frame anchor specifies defaults for **x** and **y**, along with
**textAnchor** and **lineAnchor**, based on the plot's frame; it may be one of the four sides (*top*, *right*, *bottom*, *left*), one of the four corners (*top-left*, *top-right*, *bottom-right*, *bottom-left*), or the
*middle* of the frame.'''
    line_anchor: L['bottom','middle','top'] | ParamRef
    '''The line anchor controls how text is aligned (typically vertically) relative to its anchor point; it is one of *top*, *bottom*, or *middle*. If the frame anchor is *top*, *top-left*, or *top-right*, the default line anchor is *top*; if the frame anchor is *bottom*, *bottom-right*, or
*bottom-left*, the default is *bottom*; otherwise it is *middle*.'''
    line_height: ParamRef | float
    '''The line height in ems; defaults to 1. The line height affects the (typically vertical) separation between adjacent baselines of text, as well as the separation between the text and its anchor point.'''
    line_width: ParamRef | float
    '''The line width in ems (e.g., 10 for about 20 characters); defaults to infinity, disabling wrapping and clipping.

If **textOverflow** is null, lines will be wrapped at the specified length. If a line is split at a soft hyphen (\xad), a hyphen (-) will be displayed at the end of the line. If **textOverflow** is not null, lines will be clipped according to the given strategy.'''
    mark: Required[L['densityY']]
    '''A densityY mark that visualizes smoothed point cloud densities along the
**y** dimension. The mark bins the data, counts the number of records that fall into each bin, smooths the resulting counts, and then plots the smoothed distribution, by default using an areaY mark.

Set the *type* property to use a different base mark type.'''
    monospace: ParamRef | bool
    '''If true, changes the default **fontFamily** to *monospace*, and uses simplified monospaced text metrics calculations.'''
    normalize: L['max','none','sum'] | ParamRef | bool
    '''Normalization method for density estimates. If `false` or `'none'` (the default), the density estimates are smoothed weighted counts. If `true` or `'sum'`, density estimates are divided by the sum of the total point mass. If `'max'`, estimates are divided by the maximum smoothed value.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    rotate: ChannelValue | ParamRef
    '''The rotation angle in degrees clockwise; a constant or a channel; defaults to 0°. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel.'''
    text: ChannelValue
    '''The text contents channel, possibly with line breaks (\n, \r\n, or \r). If not specified, defaults to the zero-based index [0, 1, 2, …].'''
    text_anchor: L['end','middle','start'] | ParamRef
    '''The [text anchor][1] controls how text is aligned (typically horizontally) relative to its anchor point; it is one of *start*, *end*, or *middle*. If the frame anchor is *left*, *top-left*, or *bottom-left*, the default text anchor is *start*; if the frame anchor is *right*, *top-right*, or
*bottom-right*, the default is *end*; otherwise it is *middle*.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/text-anchor'''
    text_overflow: L['clip','clip-end','clip-start','ellipsis','ellipsis-end','ellipsis-middle','ellipsis-start'] | None | ParamRef
    '''How truncate (or wrap) lines of text longer than the given **lineWidth**; one of:

- null (default) - preserve overflowing characters (and wrap if needed)
- *clip* or *clip-end* - remove characters from the end
- *clip-start* - remove characters from the start
- *ellipsis* or *ellipsis-end* - replace characters from the end with an ellipsis (…)
- *ellipsis-start* - replace characters from the start with an ellipsis (…)
- *ellipsis-middle* - replace characters from the middle with an ellipsis (…)

If no **title** was specified, if text requires truncation, a title containing the non-truncated text will be implicitly added.'''
    type: Required[L['text','textY']]
    '''The basic mark type to use to render 1D density values. Defaults to an areaY mark; lineY, dot, and text marks are also supported.'''
    x: ChannelValueSpec
    '''The horizontal position channel specifying the text's anchor point, typically bound to the *x* scale.'''
    z: ChannelValue
    '''An optional ordinal channel for grouping data into series.'''
class _DotOpen(MarkOptions,total=False):
    """The dot mark."""
    frame_anchor: FrameAnchor | ParamRef
    '''The frame anchor specifies defaults for **x** and **y** based on the plot's frame; it may be one of the four sides (*top*, *right*, *bottom*, *left*), one of the four corners (*top-left*, *top-right*, *bottom-right*,
*bottom-left*), or the *middle* of the frame. For example, for dots distributed horizontally at the top of the frame:

```js Plot.dot(data, {x: "date", frameAnchor: "top"}) ```'''
    mark: Required[L['dot']]
    '''A dot mark that draws circles, or other symbols, as in a scatterplot.

If either **x** or **y** is not specified, the default is determined by the
**frameAnchor** option. If none of **x**, **y**, and **frameAnchor** are specified, *data* is assumed to be an array of pairs [[*x₀*, *y₀*], [*x₁*,
*y₁*], [*x₂*, *y₂*], …] such that **x** = [*x₀*, *x₁*, *x₂*, …] and **y** = [*y₀*, *y₁*, *y₂*, …].

Dots are sorted by descending radius **r** by default to mitigate overplotting; set the **sort** option to null to draw them in input order.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    r: ChannelValueSpec | ParamRef | float
    '''The radius of dots; either a channel or constant. When a number, it is interpreted as a constant radius in pixels. Otherwise it is interpreted as a channel, typically bound to the *r* channel, which defaults to the *sqrt* type for proportional symbols. The radius defaults to 4.5 pixels when using the **symbol** channel, and otherwise 3 pixels. Dots with a nonpositive radius are not drawn.'''
    rotate: ChannelValue | ParamRef | float
    '''The rotation angle of dots in degrees clockwise; either a channel or a constant. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel. Defaults to 0°, pointing up.'''
    symbol: ChannelValueSpec | ParamRef | SymbolType
    '''The categorical symbol; either a channel or a constant. A constant symbol can be specified by a valid symbol name such as *star*, or a symbol object (implementing the draw method); otherwise it is interpreted as a channel. Defaults to *circle* for the **dot** mark, and *hexagon* for the
**hexagon** mark.

If the **symbol** channel's values are all symbols, symbol names, or nullish, the channel is unscaled (values are interpreted literally); otherwise, the channel is bound to the *symbol* scale.'''
    x: ChannelValueSpec
    '''The horizontal position channel specifying the dot's center, typically bound to the *x* scale.'''
    y: ChannelValueSpec
    '''The vertical position channel specifying the dot's center, typically bound to the *y* scale.'''
    z: ChannelValue
    '''An optional ordinal channel for grouping data into series.'''
class _DotXOpen(MarkOptions,total=False):
    """The dotX mark."""
    frame_anchor: FrameAnchor | ParamRef
    '''The frame anchor specifies defaults for **x** and **y** based on the plot's frame; it may be one of the four sides (*top*, *right*, *bottom*, *left*), one of the four corners (*top-left*, *top-right*, *bottom-right*,
*bottom-left*), or the *middle* of the frame. For example, for dots distributed horizontally at the top of the frame:

```js Plot.dot(data, {x: "date", frameAnchor: "top"}) ```'''
    interval: Interval | ParamRef
    '''An interval (such as *day* or a number), to transform **y** values to the middle of the interval.'''
    mark: Required[L['dotX']]
    '''Like dot, except that **x** defaults to the identity function, assuming that
*data* = [*x₀*, *x₁*, *x₂*, …].

If an **interval** is specified, such as *day*, **y** is transformed to the middle of the interval.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    r: ChannelValueSpec | ParamRef | float
    '''The radius of dots; either a channel or constant. When a number, it is interpreted as a constant radius in pixels. Otherwise it is interpreted as a channel, typically bound to the *r* channel, which defaults to the *sqrt* type for proportional symbols. The radius defaults to 4.5 pixels when using the **symbol** channel, and otherwise 3 pixels. Dots with a nonpositive radius are not drawn.'''
    rotate: ChannelValue | ParamRef | float
    '''The rotation angle of dots in degrees clockwise; either a channel or a constant. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel. Defaults to 0°, pointing up.'''
    symbol: ChannelValueSpec | ParamRef | SymbolType
    '''The categorical symbol; either a channel or a constant. A constant symbol can be specified by a valid symbol name such as *star*, or a symbol object (implementing the draw method); otherwise it is interpreted as a channel. Defaults to *circle* for the **dot** mark, and *hexagon* for the
**hexagon** mark.

If the **symbol** channel's values are all symbols, symbol names, or nullish, the channel is unscaled (values are interpreted literally); otherwise, the channel is bound to the *symbol* scale.'''
    x: ChannelValueSpec
    '''The horizontal position channel specifying the dot's center, typically bound to the *x* scale.'''
    y: ChannelValueIntervalSpec
    '''The vertical position of the dot's center, typically bound to the *y* scale.'''
    z: ChannelValue
    '''An optional ordinal channel for grouping data into series.'''
class _DotYOpen(MarkOptions,total=False):
    """The dotY mark."""
    frame_anchor: FrameAnchor | ParamRef
    '''The frame anchor specifies defaults for **x** and **y** based on the plot's frame; it may be one of the four sides (*top*, *right*, *bottom*, *left*), one of the four corners (*top-left*, *top-right*, *bottom-right*,
*bottom-left*), or the *middle* of the frame. For example, for dots distributed horizontally at the top of the frame:

```js Plot.dot(data, {x: "date", frameAnchor: "top"}) ```'''
    interval: Interval | ParamRef
    '''An interval (such as *day* or a number), to transform **x** values to the middle of the interval.'''
    mark: Required[L['dotY']]
    '''Like dot, except that **y** defaults to the identity function, assuming that
*data* = [*y₀*, *y₁*, *y₂*, …].

If an **interval** is specified, such as *day*, **x** is transformed to the middle of the interval.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    r: ChannelValueSpec | ParamRef | float
    '''The radius of dots; either a channel or constant. When a number, it is interpreted as a constant radius in pixels. Otherwise it is interpreted as a channel, typically bound to the *r* channel, which defaults to the *sqrt* type for proportional symbols. The radius defaults to 4.5 pixels when using the **symbol** channel, and otherwise 3 pixels. Dots with a nonpositive radius are not drawn.'''
    rotate: ChannelValue | ParamRef | float
    '''The rotation angle of dots in degrees clockwise; either a channel or a constant. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel. Defaults to 0°, pointing up.'''
    symbol: ChannelValueSpec | ParamRef | SymbolType
    '''The categorical symbol; either a channel or a constant. A constant symbol can be specified by a valid symbol name such as *star*, or a symbol object (implementing the draw method); otherwise it is interpreted as a channel. Defaults to *circle* for the **dot** mark, and *hexagon* for the
**hexagon** mark.

If the **symbol** channel's values are all symbols, symbol names, or nullish, the channel is unscaled (values are interpreted literally); otherwise, the channel is bound to the *symbol* scale.'''
    x: ChannelValueIntervalSpec
    '''The horizontal position of the dot's center, typically bound to the *x* scale.'''
    y: ChannelValueSpec
    '''The vertical position channel specifying the dot's center, typically bound to the *y* scale.'''
    z: ChannelValue
    '''An optional ordinal channel for grouping data into series.'''
class _ErrorBarXOpen(MarkOptions,total=False):
    """The errorbarX mark."""
    ci: ParamRef | float
    '''The confidence interval in (0, 1); defaults to 0.95.'''
    mark: Required[L['errorbarX']]
    '''A mark that draws error bars for a calculated parametric confidence interval for a dependent variable (*x*), potentially grouped by an independent variable (*y*).

This mark aggregates raw values to produce a [parametric confidence interval][1] of the mean, assuming a normal distribution. To instead visualize pre-computed interval values or custom aggregations, use a **ruleY** mark with specified **x1** and **x2** channels.

Multiple error bars can be produced by specifying a **z** or **stroke** channel. Set the **marker** option to `'tick'` to add small perpendicular lines at the start and end of the error interval.

[1]: https://en.wikipedia.org/wiki/Normal_distribution#Confidence_intervals'''
    marker: L['none'] | MarkerName | None | ParamRef | bool
    '''Shorthand to set the same default for markerStart, markerMid, and markerEnd; one of:

- a marker name such as *arrow* or *circle*
- *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_end: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the ending point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_mid: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for any middle (interior) points of a line segment. If the line segment only has a start and end point, this option has no effect. One of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*
* a function - a custom marker function; see below'''
    marker_start: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the starting point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    x: Required[ChannelValueSpec]
    '''The dependent variable horizontal position channel, typically bound to the
*x* scale.'''
    y: ChannelValueSpec
    '''The independent variable vertical position channel, typically bound to the *y* scale; defaults to the zero-based index of the data [0, 1, 2, …].'''
    z: ChannelValue
    '''An optional ordinal channel for grouping data, producing an independent error bar for each group. If not specified, it defaults to **stroke** if a channel.'''
class _ErrorBarYOpen(MarkOptions,total=False):
    """The errorbarY mark."""
    ci: ParamRef | float
    '''The confidence interval in (0, 1); defaults to 0.95.'''
    mark: Required[L['errorbarY']]
    '''A mark that draws error bars for a calculated parametric confidence interval for a dependent variable (*y*), potentially grouped by an independent variable (*x*).

This mark aggregates raw values to produce a [parametric confidence interval][1] of the mean, assuming a normal distribution. To instead visualize pre-computed interval values or custom aggregations, use a **ruleX** mark with specified **y1** and **y2** channels.

Multiple error bars can be produced by specifying a **z** or **stroke** channel. Set the **marker** option to `'tick'` to add small perpendicular lines at the start and end of the error interval.

[1]: https://en.wikipedia.org/wiki/Normal_distribution#Confidence_intervals'''
    marker: L['none'] | MarkerName | None | ParamRef | bool
    '''Shorthand to set the same default for markerStart, markerMid, and markerEnd; one of:

- a marker name such as *arrow* or *circle*
- *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_end: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the ending point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_mid: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for any middle (interior) points of a line segment. If the line segment only has a start and end point, this option has no effect. One of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*
* a function - a custom marker function; see below'''
    marker_start: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the starting point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    x: ChannelValueSpec
    '''The independent variable horizontal position channel, typically bound to the *x* scale; defaults to the zero-based index of the data [0, 1, 2, …].'''
    y: Required[ChannelValueSpec]
    '''The dependent variable vertical position channel, typically bound to the
*y* scale.'''
    z: ChannelValue
    '''An optional ordinal channel for grouping data, producing an independent error bar for each group. If not specified, it defaults to **stroke** if a channel.'''
class _FrameOpen(MarkOptions,total=False):
    """The frame mark."""
    anchor: L['bottom','left','right','top'] | None | ParamRef
    '''If null (default), the rectangular outline of the frame is drawn; otherwise the frame is drawn as a line only on the given side, and the
**rx**, **ry**, **fill**, and **fillOpacity** options are ignored.'''
    inset: ParamRef | float
    '''Shorthand to set the same default for all four insets: **insetTop**,
**insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it.'''
    inset_bottom: ParamRef | float
    '''Insets the bottom edge by the specified number of pixels. A positive value insets towards the top edge (reducing effective area), while a negative value insets away from the top edge (increasing it).'''
    inset_left: ParamRef | float
    '''Insets the left edge by the specified number of pixels. A positive value insets towards the right edge (reducing effective area), while a negative value insets away from the right edge (increasing it).'''
    inset_right: ParamRef | float
    '''Insets the right edge by the specified number of pixels. A positive value insets towards the left edge (reducing effective area), while a negative value insets away from the left edge (increasing it).'''
    inset_top: ParamRef | float
    '''Insets the top edge by the specified number of pixels. A positive value insets towards the bottom edge (reducing effective area), while a negative value insets away from the bottom edge (increasing it).'''
    mark: Required[L['frame']]
    '''Draws a rectangle around the plot's frame, or if an **anchor** is given, a line on the given side. Useful for visual separation of facets, or in conjunction with axes and grids to fill the frame's background.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    rx: ParamRef | float | str
    '''The rounded corner [*x*-radius][1], either in pixels or as a percentage of the rect width. If **rx** is not specified, it defaults to **ry** if present, and otherwise draws square corners.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/rx'''
    ry: ParamRef | float | str
    '''The rounded corner [*y*-radius][1], either in pixels or as a percentage of the rect height. If **ry** is not specified, it defaults to **rx** if present, and otherwise draws square corners.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/ry'''
class _GeoOpen(MarkOptions,total=False):
    """The geo mark."""
    geometry: ChannelValue
    '''A required channel for the geometry to render; defaults to identity, assuming *data* is a GeoJSON object or an iterable of GeoJSON objects.'''
    mark: Required[L['geo']]
    '''A geo mark. The **geometry** channel, which defaults to the identity function assuming that *data* is a GeoJSON object or an iterable of GeoJSON objects, is projected to the plane using the plot's top-level
**projection**.

If *data* is a GeoJSON feature collection, then the mark's data is
*data*.features; if *data* is a GeoJSON geometry collection, then the mark's data is *data*.geometries; if *data* is some other GeoJSON object, then the mark's data is the single-element array [*data*].'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    r: ChannelValueSpec | ParamRef
    '''The size of Point and MultiPoint geometries, defaulting to a constant 3 pixels. If **r** is a number, it is interpreted as a constant radius in pixels; otherwise it is interpreted as a channel and the effective radius is controlled by the *r* scale, which defaults to a *sqrt* scale such that the visual area of a point is proportional to its associated value.

If **r** is a channel, geometries will be sorted by descending radius by default, to limit occlusion; use the **sort** transform to control render order. Geometries with a nonpositive radius are not drawn.'''
class _GraticuleOpen(MarkOptions,total=False):
    """The graticule mark."""
    mark: Required[L['graticule']]
    '''A geo mark whose *data* is a 10° global graticule. (For use with a spherical **projection** only.)'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
class _GridFxOpen(MarkOptions,total=False):
    """The gridFx mark."""
    anchor: L['bottom','left','right','top'] | ParamRef
    '''The side of the frame on which to place the axis: *top* or *bottom* for horizontal axes (axisX and axisFx) and their associated vertical grids (gridX and gridFx), or *left* or *right* for vertical axes (axisY and axisFY) and their associated horizontal grids (gridY and gridFy).

The default **anchor** depends on the associated scale:

- *x* - *bottom*
- *y* - *left*
- *fx* - *top* if there is a *bottom* *x* axis, and otherwise *bottom*
- *fy* - *right* if there is a *left* *y* axis, and otherwise *right*

For grids, the **anchor** also affects the extent of grid lines when the opposite dimension is specified (**x** for gridY and **y** for gridX).'''
    color: ChannelValueSpec | ParamRef
    '''A shorthand for setting both **fill** and **stroke**; affects the stroke of tick vectors and grid rules, and the fill of tick texts and axis label texts; defaults to *currentColor*.'''
    inset: ParamRef | float
    '''Shorthand to set the same default for all four insets: **insetTop**,
**insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it.'''
    inset_bottom: ParamRef | float
    '''Insets the bottom edge by the specified number of pixels. A positive value insets towards the top edge (reducing effective area), while a negative value insets away from the top edge (increasing it).'''
    inset_top: ParamRef | float
    '''Insets the top edge by the specified number of pixels. A positive value insets towards the bottom edge (reducing effective area), while a negative value insets away from the bottom edge (increasing it).'''
    interval: Interval | ParamRef
    '''Enforces uniformity for data at regular intervals, such as integer values or daily samples. The interval may be one of:

- a named time interval such as *day* (for date intervals)
- a number (for number intervals), defining intervals at integer multiples of *n*

This option sets the internal transform to the given interval's
*interval*.floor function. In addition, the default **domain** will align with interval boundaries.'''
    mark: Required[L['gridFx']]
    '''A horizontally-positioned ruleX mark (a vertical line, |) that renders a grid for the *fx* scale. The data defaults to the *fx* scale's domain; if desired, use the **ticks** option.'''
    marker: L['none'] | MarkerName | None | ParamRef | bool
    '''Shorthand to set the same default for markerStart, markerMid, and markerEnd; one of:

- a marker name such as *arrow* or *circle*
- *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_end: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the ending point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_mid: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for any middle (interior) points of a line segment. If the line segment only has a start and end point, this option has no effect. One of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*
* a function - a custom marker function; see below'''
    marker_start: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the starting point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    opacity: ChannelValueSpec
    '''A shorthand for setting both **fillOpacity** and **strokeOpacity**; affects the stroke opacity of tick vectors and grid rules, and the fill opacity of tick texts and axis label texts; defaults to 1 for axes and 0.1 for grids.'''
    tick_spacing: ParamRef | float
    '''The desired approximate spacing between adjacent axis ticks, affecting the default **ticks**; defaults to 80 pixels for *x* and *fx*, and 35 pixels for *y* and *fy*.'''
    ticks: Interval | ParamRef | Sequence[Any] | float
    '''The desired approximate number of axis ticks, or an explicit array of tick values, or an interval such as *day* or *month*.'''
    x: ChannelValueSpec
    '''The horizontal position of the tick; an optional channel bound to the *x* scale. If not specified, the rule will be horizontally centered in the plot's frame.'''
    y: ChannelValueIntervalSpec
    '''Shorthand for specifying both the primary and secondary vertical position of the tick as the bounds of the containing interval; can only be used in conjunction with the **interval** option.'''
    y1: ChannelValueSpec
    '''The primary (starting, often bottom) vertical position of the tick; a channel bound to the *y* scale.

If *y* represents ordinal values, use a tickX mark instead.'''
    y2: ChannelValueSpec
    '''The secondary (ending, often top) vertical position of the tick; a channel bound to the *y* scale.

If *y* represents ordinal values, use a tickX mark instead.'''
class _GridFyOpen(MarkOptions,total=False):
    """The gridFy mark."""
    anchor: L['bottom','left','right','top'] | ParamRef
    '''The side of the frame on which to place the axis: *top* or *bottom* for horizontal axes (axisX and axisFx) and their associated vertical grids (gridX and gridFx), or *left* or *right* for vertical axes (axisY and axisFY) and their associated horizontal grids (gridY and gridFy).

The default **anchor** depends on the associated scale:

- *x* - *bottom*
- *y* - *left*
- *fx* - *top* if there is a *bottom* *x* axis, and otherwise *bottom*
- *fy* - *right* if there is a *left* *y* axis, and otherwise *right*

For grids, the **anchor** also affects the extent of grid lines when the opposite dimension is specified (**x** for gridY and **y** for gridX).'''
    color: ChannelValueSpec | ParamRef
    '''A shorthand for setting both **fill** and **stroke**; affects the stroke of tick vectors and grid rules, and the fill of tick texts and axis label texts; defaults to *currentColor*.'''
    inset: ParamRef | float
    '''Shorthand to set the same default for all four insets: **insetTop**,
**insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it.'''
    inset_left: ParamRef | float
    '''Insets the left edge by the specified number of pixels. A positive value insets towards the right edge (reducing effective area), while a negative value insets away from the right edge (increasing it).'''
    inset_right: ParamRef | float
    '''Insets the right edge by the specified number of pixels. A positive value insets towards the left edge (reducing effective area), while a negative value insets away from the left edge (increasing it).'''
    interval: Interval | ParamRef
    '''Enforces uniformity for data at regular intervals, such as integer values or daily samples. The interval may be one of:

- a named time interval such as *day* (for date intervals)
- a number (for number intervals), defining intervals at integer multiples of *n*

This option sets the internal transform to the given interval's
*interval*.floor function. In addition, the default **domain** will align with interval boundaries.'''
    mark: Required[L['gridFy']]
    '''A vertically-positioned ruleY mark (a horizontal line, —) that renders a grid for the *fy* scale. The data defaults to the *fy* scale's domain; if desired, use the **ticks** option.'''
    marker: L['none'] | MarkerName | None | ParamRef | bool
    '''Shorthand to set the same default for markerStart, markerMid, and markerEnd; one of:

- a marker name such as *arrow* or *circle*
- *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_end: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the ending point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_mid: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for any middle (interior) points of a line segment. If the line segment only has a start and end point, this option has no effect. One of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*
* a function - a custom marker function; see below'''
    marker_start: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the starting point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    opacity: ChannelValueSpec
    '''A shorthand for setting both **fillOpacity** and **strokeOpacity**; affects the stroke opacity of tick vectors and grid rules, and the fill opacity of tick texts and axis label texts; defaults to 1 for axes and 0.1 for grids.'''
    tick_spacing: ParamRef | float
    '''The desired approximate spacing between adjacent axis ticks, affecting the default **ticks**; defaults to 80 pixels for *x* and *fx*, and 35 pixels for *y* and *fy*.'''
    ticks: Interval | ParamRef | Sequence[Any] | float
    '''The desired approximate number of axis ticks, or an explicit array of tick values, or an interval such as *day* or *month*.'''
    x: ChannelValueIntervalSpec
    '''Shorthand for specifying both the primary and secondary horizontal position of the tick as the bounds of the containing interval; can only be used in conjunction with the **interval** option.'''
    x1: ChannelValueSpec
    '''The primary (starting, often left) horizontal position of the tick; a channel bound to the *x* scale.

If *x* represents ordinal values, use a tickY mark instead.'''
    x2: ChannelValueSpec
    '''The secondary (ending, often right) horizontal position of the tick; a channel bound to the *x* scale.

If *x* represents ordinal values, use a tickY mark instead.'''
    y: ChannelValueSpec
    '''The vertical position of the tick; an optional channel bound to the *y* scale. If not specified, the rule will be vertically centered in the plot's frame.'''
class _GridXOpen(MarkOptions,total=False):
    """The gridX mark."""
    anchor: L['bottom','left','right','top'] | ParamRef
    '''The side of the frame on which to place the axis: *top* or *bottom* for horizontal axes (axisX and axisFx) and their associated vertical grids (gridX and gridFx), or *left* or *right* for vertical axes (axisY and axisFY) and their associated horizontal grids (gridY and gridFy).

The default **anchor** depends on the associated scale:

- *x* - *bottom*
- *y* - *left*
- *fx* - *top* if there is a *bottom* *x* axis, and otherwise *bottom*
- *fy* - *right* if there is a *left* *y* axis, and otherwise *right*

For grids, the **anchor** also affects the extent of grid lines when the opposite dimension is specified (**x** for gridY and **y** for gridX).'''
    color: ChannelValueSpec | ParamRef
    '''A shorthand for setting both **fill** and **stroke**; affects the stroke of tick vectors and grid rules, and the fill of tick texts and axis label texts; defaults to *currentColor*.'''
    inset: ParamRef | float
    '''Shorthand to set the same default for all four insets: **insetTop**,
**insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it.'''
    inset_bottom: ParamRef | float
    '''Insets the bottom edge by the specified number of pixels. A positive value insets towards the top edge (reducing effective area), while a negative value insets away from the top edge (increasing it).'''
    inset_top: ParamRef | float
    '''Insets the top edge by the specified number of pixels. A positive value insets towards the bottom edge (reducing effective area), while a negative value insets away from the bottom edge (increasing it).'''
    interval: Interval | ParamRef
    '''Enforces uniformity for data at regular intervals, such as integer values or daily samples. The interval may be one of:

- a named time interval such as *day* (for date intervals)
- a number (for number intervals), defining intervals at integer multiples of *n*

This option sets the internal transform to the given interval's
*interval*.floor function. In addition, the default **domain** will align with interval boundaries.'''
    mark: Required[L['gridX']]
    '''A horizontally-positioned ruleX mark (a vertical line, |) that renders a grid for the *x* scale. The data defaults to tick values sampled from the
*x* scale's domain; if desired, use one of the **ticks**, **tickSpacing**, or **interval** options.'''
    marker: L['none'] | MarkerName | None | ParamRef | bool
    '''Shorthand to set the same default for markerStart, markerMid, and markerEnd; one of:

- a marker name such as *arrow* or *circle*
- *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_end: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the ending point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_mid: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for any middle (interior) points of a line segment. If the line segment only has a start and end point, this option has no effect. One of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*
* a function - a custom marker function; see below'''
    marker_start: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the starting point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    opacity: ChannelValueSpec
    '''A shorthand for setting both **fillOpacity** and **strokeOpacity**; affects the stroke opacity of tick vectors and grid rules, and the fill opacity of tick texts and axis label texts; defaults to 1 for axes and 0.1 for grids.'''
    tick_spacing: ParamRef | float
    '''The desired approximate spacing between adjacent axis ticks, affecting the default **ticks**; defaults to 80 pixels for *x* and *fx*, and 35 pixels for *y* and *fy*.'''
    ticks: Interval | ParamRef | Sequence[Any] | float
    '''The desired approximate number of axis ticks, or an explicit array of tick values, or an interval such as *day* or *month*.'''
    x: ChannelValueSpec
    '''The horizontal position of the tick; an optional channel bound to the *x* scale. If not specified, the rule will be horizontally centered in the plot's frame.'''
    y: ChannelValueIntervalSpec
    '''Shorthand for specifying both the primary and secondary vertical position of the tick as the bounds of the containing interval; can only be used in conjunction with the **interval** option.'''
    y1: ChannelValueSpec
    '''The primary (starting, often bottom) vertical position of the tick; a channel bound to the *y* scale.

If *y* represents ordinal values, use a tickX mark instead.'''
    y2: ChannelValueSpec
    '''The secondary (ending, often top) vertical position of the tick; a channel bound to the *y* scale.

If *y* represents ordinal values, use a tickX mark instead.'''
class _GridYOpen(MarkOptions,total=False):
    """The gridY mark."""
    anchor: L['bottom','left','right','top'] | ParamRef
    '''The side of the frame on which to place the axis: *top* or *bottom* for horizontal axes (axisX and axisFx) and their associated vertical grids (gridX and gridFx), or *left* or *right* for vertical axes (axisY and axisFY) and their associated horizontal grids (gridY and gridFy).

The default **anchor** depends on the associated scale:

- *x* - *bottom*
- *y* - *left*
- *fx* - *top* if there is a *bottom* *x* axis, and otherwise *bottom*
- *fy* - *right* if there is a *left* *y* axis, and otherwise *right*

For grids, the **anchor** also affects the extent of grid lines when the opposite dimension is specified (**x** for gridY and **y** for gridX).'''
    color: ChannelValueSpec | ParamRef
    '''A shorthand for setting both **fill** and **stroke**; affects the stroke of tick vectors and grid rules, and the fill of tick texts and axis label texts; defaults to *currentColor*.'''
    inset: ParamRef | float
    '''Shorthand to set the same default for all four insets: **insetTop**,
**insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it.'''
    inset_left: ParamRef | float
    '''Insets the left edge by the specified number of pixels. A positive value insets towards the right edge (reducing effective area), while a negative value insets away from the right edge (increasing it).'''
    inset_right: ParamRef | float
    '''Insets the right edge by the specified number of pixels. A positive value insets towards the left edge (reducing effective area), while a negative value insets away from the left edge (increasing it).'''
    interval: Interval | ParamRef
    '''Enforces uniformity for data at regular intervals, such as integer values or daily samples. The interval may be one of:

- a named time interval such as *day* (for date intervals)
- a number (for number intervals), defining intervals at integer multiples of *n*

This option sets the internal transform to the given interval's
*interval*.floor function. In addition, the default **domain** will align with interval boundaries.'''
    mark: Required[L['gridY']]
    '''A vertically-positioned ruleY mark (a horizontal line, —) that renders a grid for the *y* scale. The data defaults to tick values sampled from the
*y* scale's domain; if desired, use one of the **ticks**, **tickSpacing**, or **interval** options.'''
    marker: L['none'] | MarkerName | None | ParamRef | bool
    '''Shorthand to set the same default for markerStart, markerMid, and markerEnd; one of:

- a marker name such as *arrow* or *circle*
- *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_end: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the ending point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_mid: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for any middle (interior) points of a line segment. If the line segment only has a start and end point, this option has no effect. One of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*
* a function - a custom marker function; see below'''
    marker_start: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the starting point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    opacity: ChannelValueSpec
    '''A shorthand for setting both **fillOpacity** and **strokeOpacity**; affects the stroke opacity of tick vectors and grid rules, and the fill opacity of tick texts and axis label texts; defaults to 1 for axes and 0.1 for grids.'''
    tick_spacing: ParamRef | float
    '''The desired approximate spacing between adjacent axis ticks, affecting the default **ticks**; defaults to 80 pixels for *x* and *fx*, and 35 pixels for *y* and *fy*.'''
    ticks: Interval | ParamRef | Sequence[Any] | float
    '''The desired approximate number of axis ticks, or an explicit array of tick values, or an interval such as *day* or *month*.'''
    x: ChannelValueIntervalSpec
    '''Shorthand for specifying both the primary and secondary horizontal position of the tick as the bounds of the containing interval; can only be used in conjunction with the **interval** option.'''
    x1: ChannelValueSpec
    '''The primary (starting, often left) horizontal position of the tick; a channel bound to the *x* scale.

If *x* represents ordinal values, use a tickY mark instead.'''
    x2: ChannelValueSpec
    '''The secondary (ending, often right) horizontal position of the tick; a channel bound to the *x* scale.

If *x* represents ordinal values, use a tickY mark instead.'''
    y: ChannelValueSpec
    '''The vertical position of the tick; an optional channel bound to the *y* scale. If not specified, the rule will be vertically centered in the plot's frame.'''
class _HeatmapOpen(MarkOptions,total=False):
    """The heatmap mark."""
    bandwidth: ParamRef | float
    '''The kernel density bandwidth for smoothing, in pixels.'''
    height: ParamRef | float
    '''The height (number of rows) of the grid, in actual pixels.'''
    image_rendering: ParamRef | str
    '''The [image-rendering attribute][1]; defaults to *auto* (bilinear). The option may be set to *pixelated* to disable bilinear interpolation for a sharper image; however, note that this is not supported in WebKit.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/image-rendering'''
    interpolate: GridInterpolate | None | ParamRef
    '''The spatial interpolation method; one of:

- *none* - do not perform interpolation (the default), maps samples to single bins
- *linear* - apply proportional linear interpolation across adjacent bins
- *nearest* - assign each pixel to the closest sample's value (Voronoi diagram)
- *barycentric* - apply barycentric interpolation over the Delaunay triangulation
- *random-walk* - apply a random walk from each pixel, stopping when near a sample'''
    mark: Required[L['heatmap']]
    '''Like raster, but with default options for accurate density estimation via smoothing. The *bandwidth* (20), *interpolate* ("linear"), and
*pixelSize* (2) options are set to produce smoothed density heatmaps.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    pad: ParamRef | float
    '''The bin padding, one of 1 (default) to include extra padding for the final bin, or 0 to make the bins flush with the maximum domain value.'''
    pixel_size: ParamRef | float
    '''The effective screen size of a raster pixel, used to determine the height and width of the raster from the frame's dimensions; defaults to 1.'''
    width: ParamRef | float
    '''The width (number of columns) of the grid, in actual pixels.'''
    x: ChannelValueSpec
    '''The horizontal position channel, typically bound to the *x* scale. Domain values are binned into a grid with *width* horizontal bins.'''
    y: ChannelValueSpec
    '''The vertical position channel, typically bound to the *y* scale. Domain values are binned into a grid with *height* vertical bins.'''
class _HexagonOpen(MarkOptions,total=False):
    """The hexagon mark."""
    frame_anchor: FrameAnchor | ParamRef
    '''The frame anchor specifies defaults for **x** and **y** based on the plot's frame; it may be one of the four sides (*top*, *right*, *bottom*, *left*), one of the four corners (*top-left*, *top-right*, *bottom-right*,
*bottom-left*), or the *middle* of the frame. For example, for dots distributed horizontally at the top of the frame:

```js Plot.dot(data, {x: "date", frameAnchor: "top"}) ```'''
    mark: Required[L['hexagon']]
    '''Like dot, except that the **symbol** option is set to *hexagon*.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    r: ChannelValueSpec | ParamRef | float
    '''The radius of dots; either a channel or constant. When a number, it is interpreted as a constant radius in pixels. Otherwise it is interpreted as a channel, typically bound to the *r* channel, which defaults to the *sqrt* type for proportional symbols. The radius defaults to 4.5 pixels when using the **symbol** channel, and otherwise 3 pixels. Dots with a nonpositive radius are not drawn.'''
    rotate: ChannelValue | ParamRef | float
    '''The rotation angle of dots in degrees clockwise; either a channel or a constant. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel. Defaults to 0°, pointing up.'''
    symbol: ChannelValueSpec | ParamRef | SymbolType
    '''The categorical symbol; either a channel or a constant. A constant symbol can be specified by a valid symbol name such as *star*, or a symbol object (implementing the draw method); otherwise it is interpreted as a channel. Defaults to *circle* for the **dot** mark, and *hexagon* for the
**hexagon** mark.

If the **symbol** channel's values are all symbols, symbol names, or nullish, the channel is unscaled (values are interpreted literally); otherwise, the channel is bound to the *symbol* scale.'''
    x: ChannelValueSpec
    '''The horizontal position channel specifying the dot's center, typically bound to the *x* scale.'''
    y: ChannelValueSpec
    '''The vertical position channel specifying the dot's center, typically bound to the *y* scale.'''
    z: ChannelValue
    '''An optional ordinal channel for grouping data into series.'''
class _HexbinOpen(MarkOptions,total=False):
    """The hexbin mark."""
    bin_width: ParamRef | float
    '''The distance between centers of neighboring hexagons, in pixels; defaults to 20. If also using a hexgrid mark, use matching **binWidth** values.'''
    font_family: ParamRef | str
    '''The [font-family][1]; a constant; defaults to the plot's font family, which is typically [*system-ui*][2].

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-family [2]: https://drafts.csswg.org/css-fonts-4/#valdef-font-family-system-ui'''
    font_size: ChannelValue | ParamRef
    '''The [font size][1] in pixels; either a constant or a channel; defaults to the plot's font size, which is typically 10. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-size'''
    font_style: ParamRef | str
    '''The [font style][1]; a constant; defaults to the plot's font style, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-style'''
    font_variant: ParamRef | str
    '''The [font variant][1]; a constant; if the **text** channel contains numbers or dates, defaults to *tabular-nums* to facilitate comparing numbers; otherwise defaults to the plot's font style, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant'''
    font_weight: ParamRef | float | str
    '''The [font weight][1]; a constant; defaults to the plot's font weight, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight'''
    frame_anchor: FrameAnchor | ParamRef
    '''The frame anchor specifies defaults for **x** and **y** based on the plot's frame; it may be one of the four sides (*top*, *right*, *bottom*, *left*), one of the four corners (*top-left*, *top-right*, *bottom-right*,
*bottom-left*), or the *middle* of the frame. For example, for dots distributed horizontally at the top of the frame:

```js Plot.dot(data, {x: "date", frameAnchor: "top"}) ```'''
    line_height: ParamRef | float
    '''The line height in ems; defaults to 1. The line height affects the (typically vertical) separation between adjacent baselines of text, as well as the separation between the text and its anchor point.'''
    line_width: ParamRef | float
    '''The line width in ems (e.g., 10 for about 20 characters); defaults to infinity, disabling wrapping and clipping.

If **textOverflow** is null, lines will be wrapped at the specified length. If a line is split at a soft hyphen (\xad), a hyphen (-) will be displayed at the end of the line. If **textOverflow** is not null, lines will be clipped according to the given strategy.'''
    mark: Required[L['hexbin']]
    '''A hexbin mark that bins **x** and **y** data into a hexagonal grid and visualizes aggregate functions per bin (e.g., count for binned density). Aggregate functions can be used for fill, stroke, or r (radius) options.'''
    monospace: ParamRef | bool
    '''If true, changes the default **fontFamily** to *monospace*, and uses simplified monospaced text metrics calculations.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    r: ChannelValueSpec | ParamRef | float
    '''The radius of dots; either a channel or constant. When a number, it is interpreted as a constant radius in pixels. Otherwise it is interpreted as a channel, typically bound to the *r* channel, which defaults to the *sqrt* type for proportional symbols. The radius defaults to 4.5 pixels when using the **symbol** channel, and otherwise 3 pixels. Dots with a nonpositive radius are not drawn.'''
    rotate: ChannelValue | ParamRef | float
    '''The rotation angle of dots in degrees clockwise; either a channel or a constant. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel. Defaults to 0°, pointing up.'''
    symbol: ChannelValueSpec | ParamRef | SymbolType
    '''The categorical symbol; either a channel or a constant. A constant symbol can be specified by a valid symbol name such as *star*, or a symbol object (implementing the draw method); otherwise it is interpreted as a channel. Defaults to *circle* for the **dot** mark, and *hexagon* for the
**hexagon** mark.

If the **symbol** channel's values are all symbols, symbol names, or nullish, the channel is unscaled (values are interpreted literally); otherwise, the channel is bound to the *symbol* scale.'''
    text_anchor: L['end','middle','start'] | ParamRef
    '''The [text anchor][1] controls how text is aligned (typically horizontally) relative to its anchor point; it is one of *start*, *end*, or *middle*. If the frame anchor is *left*, *top-left*, or *bottom-left*, the default text anchor is *start*; if the frame anchor is *right*, *top-right*, or
*bottom-right*, the default is *end*; otherwise it is *middle*.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/text-anchor'''
    text_overflow: L['clip','clip-end','clip-start','ellipsis','ellipsis-end','ellipsis-middle','ellipsis-start'] | None | ParamRef
    '''How truncate (or wrap) lines of text longer than the given **lineWidth**; one of:

- null (default) - preserve overflowing characters (and wrap if needed)
- *clip* or *clip-end* - remove characters from the end
- *clip-start* - remove characters from the start
- *ellipsis* or *ellipsis-end* - replace characters from the end with an ellipsis (…)
- *ellipsis-start* - replace characters from the start with an ellipsis (…)
- *ellipsis-middle* - replace characters from the middle with an ellipsis (…)

If no **title** was specified, if text requires truncation, a title containing the non-truncated text will be implicitly added.'''
    type: L['circle','dot','hexagon','text'] | ParamRef
    '''The basic mark type to use for hex-binned values. Defaults to a hexagon mark; dot and text marks are also supported.'''
    x: ChannelValueSpec
    '''The horizontal position channel specifying the dot's center, typically bound to the *x* scale.'''
    y: ChannelValueSpec
    '''The vertical position channel specifying the dot's center, typically bound to the *y* scale.'''
    z: ChannelValue
    '''How to subdivide bins. If not specified, defaults to the *fill* channel, if any, or the *stroke* channel, if any. If null, bins will not be subdivided.'''
class _HexgridOpen(MarkOptions,total=False):
    """The hexgrid mark."""
    bin_width: ParamRef | float
    '''The distance between centers of neighboring hexagons, in pixels; defaults to 20. Should match the **binWidth** of the hexbin mark.'''
    mark: Required[L['hexgrid']]
    '''The hexgrid decoration mark complements the hexbin mark, showing the outlines of all hexagons spanning the frame with a default **stroke** of
*currentColor* and a default **strokeOpacity** of 0.1, similar to the default axis grids.

Note that the **binWidth** option of the hexgrid mark should match that of the hexbin transform. The grid is clipped by the frame. This is a stroke-only mark, and **fill** is not supported; to fill the frame, use the frame mark.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
class _HullOpen(MarkOptions,total=False):
    """The hull mark."""
    curve: Curve | ParamRef
    '''The curve (interpolation) method for connecting adjacent points. One of:

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
- *step-before* - a piecewise constant function where *x* changes after *y*'''
    mark: Required[L['hull']]
    '''A mark that draws a convex hull around the points given by the **x** and
**y** channels. The **stroke** option defaults to _currentColor_ and the
**fill** option defaults to _none_. When an aesthetic channel is specified (such as **stroke** or **strokeWidth**), the hull inherits the corresponding channel value from one of its constituent points arbitrarily.

If **z** is specified, the input points are grouped by *z*, producing a separate hull for each group. If **z** is not specified, it defaults to the **fill** channel, if any, or the **stroke** channel, if any.'''
    marker: L['none'] | MarkerName | None | ParamRef | bool
    '''Shorthand to set the same default for markerStart, markerMid, and markerEnd; one of:

- a marker name such as *arrow* or *circle*
- *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_end: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the ending point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_mid: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for any middle (interior) points of a line segment. If the line segment only has a start and end point, this option has no effect. One of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*
* a function - a custom marker function; see below'''
    marker_start: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the starting point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    tension: ParamRef | float
    '''The tension option only has an effect on bundle, cardinal and Catmull-Rom splines (*bundle*, *cardinal*, *cardinal-open*, *cardinal-closed*,
*catmull-rom*, *catmull-rom-open*, and *catmull-rom-closed*). For bundle splines, it corresponds to [beta][1]; for cardinal splines, [tension][2]; for Catmull-Rom splines, [alpha][3].

[1]: https://d3js.org/d3-shape/curve#curveBundle_beta [2]: https://d3js.org/d3-shape/curve#curveCardinal_tension [3]: https://d3js.org/d3-shape/curve#curveCatmullRom_alpha'''
    x: ChannelValueSpec
    '''The horizontal position channel, typically bound to the *x* scale.'''
    y: ChannelValueSpec
    '''The vertical position channel, typically bound to the *y* scale.'''
    z: ChannelValue
    '''An optional ordinal channel for grouping to produce multiple (possibly overlapping) triangulations.'''
class _ImageOpen(MarkOptions,total=False):
    cross_origin: ParamRef | str
    '''The [cross-origin][1] behavior. See the [Plot.image notebook][2] for details.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/crossorigin [2]: https://observablehq.com/@observablehq/plot-image'''
    frame_anchor: FrameAnchor | ParamRef
    '''The frame anchor specifies defaults for **x** and **y** based on the plot's frame; it may be one of the four sides (*top*, *right*, *bottom*, *left*), one of the four corners (*top-left*, *top-right*, *bottom-right*,
*bottom-left*), or the *middle* of the frame.'''
    height: ChannelValue | ParamRef
    '''The image height in pixels. When a number, it is interpreted as a constant radius in pixels; otherwise it is interpreted as a channel. Also sets the default **height**; if neither are set, defaults to 16. Images with a nonpositive height are not drawn.'''
    image_rendering: ParamRef | str
    '''The [image-rendering attribute][1]; defaults to *auto* (bilinear). The option may be set to *pixelated* to disable bilinear interpolation for a sharper image; however, note that this is not supported in WebKit.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/image-rendering'''
    mark: Required[L['image']]
    '''An image mark that draws images as in a scatterplot.

If either **x** or **y** is not specified, the default is determined by the **frameAnchor** option. If none of **x**, **y**, and **frameAnchor** are specified, *data* is assumed to be an array of pairs [[*x₀*, *y₀*], [*x₁*, *y₁*], [*x₂*, *y₂*], …] such that **x** = [*x₀*, *x₁*, *x₂*, …] and **y** = [*y₀*, *y₁*, *y₂*, …].'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    preserve_aspect_ratio: ParamRef | str
    '''The image [aspect ratio][1]; defaults to *xMidYMid meet*. To crop the image instead of scaling it to fit, use *xMidYMid slice*.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/preserveAspectRatio'''
    r: ChannelValue | ParamRef
    '''The image clip radius, for circular images. If null (default), images are not clipped; when a number, it is interpreted as a constant in pixels; otherwise it is interpreted as a channel, typically bound to the *r* scale. Also defaults **height** and **width** to twice its value.'''
    rotate: ChannelValue | ParamRef
    '''The rotation angle, in degrees clockwise. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel.'''
    src: ChannelValue | ParamRef
    '''The required image URL (or relative path). If a string that starts with a dot, slash, or URL protocol (*e.g.*, “https:”) it is assumed to be a constant; otherwise it is interpreted as a channel.'''
    width: ChannelValue | ParamRef
    '''The image width in pixels. When a number, it is interpreted as a constant radius in pixels; otherwise it is interpreted as a channel. Also sets the default **height**; if neither are set, defaults to 16. Images with a nonpositive width are not drawn.'''
    x: ChannelValueSpec
    '''The horizontal position channel specifying the image's center; typically bound to the *x* scale.'''
    y: ChannelValueSpec
    '''The vertical position channel specifying the image's center; typically bound to the *y* scale.'''
class _LineOpen(MarkOptions,total=False):
    """The line mark."""
    curve: Curve | L['auto'] | ParamRef
    '''The curve (interpolation) method for connecting adjacent points. One of:

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
- *auto* (default) - like *linear*, but use the (possibly spherical) projection, if any

The *auto* curve is typically used in conjunction with a spherical projection to interpolate along geodesics.'''
    mark: Required[L['line']]
    '''A line mark that connects control points.

Points along the line are connected in input order. If there are multiple series via the **z**, **fill**, or **stroke** channel, series are drawn in input order such that the last series is drawn on top. Typically *data* is already in sorted order, such as chronological for time series; if needed, consider a **sort** transform.

If any **x** or **y** values are invalid (undefined, null, or NaN), the line will be interrupted, resulting in a break that divides the line shape into multiple segments. If a line segment consists of only a single point, it may appear invisible unless rendered with rounded or square line caps. In addition, some curves such as *cardinal-open* only render a visible segment if it contains multiple points.

Variable aesthetic channels are supported: if the **stroke** is defined as a channel, the line will be broken into contiguous overlapping segments when the stroke color changes; the stroke color will apply to the interval spanning the current data point and the following data point. This behavior also applies to the **fill**, **fillOpacity**, **strokeOpacity**,
**strokeWidth**, **opacity**, **href**, **title**, and **ariaLabel** channels. When any of these channels are used, setting an explicit **z** channel (possibly to null) is strongly recommended.'''
    marker: L['none'] | MarkerName | None | ParamRef | bool
    '''Shorthand to set the same default for markerStart, markerMid, and markerEnd; one of:

- a marker name such as *arrow* or *circle*
- *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_end: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the ending point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_mid: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for any middle (interior) points of a line segment. If the line segment only has a start and end point, this option has no effect. One of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*
* a function - a custom marker function; see below'''
    marker_start: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the starting point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    tension: ParamRef | float
    '''The tension option only has an effect on bundle, cardinal and Catmull-Rom splines (*bundle*, *cardinal*, *cardinal-open*, *cardinal-closed*,
*catmull-rom*, *catmull-rom-open*, and *catmull-rom-closed*). For bundle splines, it corresponds to [beta][1]; for cardinal splines, [tension][2]; for Catmull-Rom splines, [alpha][3].

[1]: https://d3js.org/d3-shape/curve#curveBundle_beta [2]: https://d3js.org/d3-shape/curve#curveCardinal_tension [3]: https://d3js.org/d3-shape/curve#curveCatmullRom_alpha'''
    x: ChannelValueSpec
    '''The required horizontal position channel, typically bound to the *x* scale.'''
    y: ChannelValueSpec
    '''The required vertical position channel, typically bound to the *y* scale.'''
    z: ChannelValue
    '''An optional ordinal channel for grouping data into (possibly stacked) series to be drawn as separate lines. If not specified, it defaults to
**fill** if a channel, or **stroke** if a channel.'''
class _LineXOpen(MarkOptions,total=False):
    """The lineX mark."""
    curve: Curve | L['auto'] | ParamRef
    '''The curve (interpolation) method for connecting adjacent points. One of:

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
- *auto* (default) - like *linear*, but use the (possibly spherical) projection, if any

The *auto* curve is typically used in conjunction with a spherical projection to interpolate along geodesics.'''
    mark: Required[L['lineX']]
    '''Like line, except that **x** defaults to the identity function assuming that *data* = [*x₀*, *x₁*, *x₂*, …] and **y** defaults to the zero-based index [0, 1, 2, …].'''
    marker: L['none'] | MarkerName | None | ParamRef | bool
    '''Shorthand to set the same default for markerStart, markerMid, and markerEnd; one of:

- a marker name such as *arrow* or *circle*
- *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_end: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the ending point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_mid: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for any middle (interior) points of a line segment. If the line segment only has a start and end point, this option has no effect. One of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*
* a function - a custom marker function; see below'''
    marker_start: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the starting point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    tension: ParamRef | float
    '''The tension option only has an effect on bundle, cardinal and Catmull-Rom splines (*bundle*, *cardinal*, *cardinal-open*, *cardinal-closed*,
*catmull-rom*, *catmull-rom-open*, and *catmull-rom-closed*). For bundle splines, it corresponds to [beta][1]; for cardinal splines, [tension][2]; for Catmull-Rom splines, [alpha][3].

[1]: https://d3js.org/d3-shape/curve#curveBundle_beta [2]: https://d3js.org/d3-shape/curve#curveCardinal_tension [3]: https://d3js.org/d3-shape/curve#curveCatmullRom_alpha'''
    x: ChannelValueSpec
    '''The required horizontal position channel, typically bound to the *x* scale.'''
    y: ChannelValueSpec
    '''The vertical position channel, typically bound to the *y* scale; defaults to the zero-based index of the data [0, 1, 2, …].'''
    z: ChannelValue
    '''An optional ordinal channel for grouping data into (possibly stacked) series to be drawn as separate lines. If not specified, it defaults to
**fill** if a channel, or **stroke** if a channel.'''
class _LineYOpen(MarkOptions,total=False):
    """The lineY mark."""
    curve: Curve | L['auto'] | ParamRef
    '''The curve (interpolation) method for connecting adjacent points. One of:

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
- *auto* (default) - like *linear*, but use the (possibly spherical) projection, if any

The *auto* curve is typically used in conjunction with a spherical projection to interpolate along geodesics.'''
    mark: Required[L['lineY']]
    '''Like line, except **y** defaults to the identity function and assumes that *data* = [*y₀*, *y₁*, *y₂*, …] and **x** defaults to the zero-based index [0, 1, 2, …].'''
    marker: L['none'] | MarkerName | None | ParamRef | bool
    '''Shorthand to set the same default for markerStart, markerMid, and markerEnd; one of:

- a marker name such as *arrow* or *circle*
- *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_end: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the ending point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_mid: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for any middle (interior) points of a line segment. If the line segment only has a start and end point, this option has no effect. One of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*
* a function - a custom marker function; see below'''
    marker_start: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the starting point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    tension: ParamRef | float
    '''The tension option only has an effect on bundle, cardinal and Catmull-Rom splines (*bundle*, *cardinal*, *cardinal-open*, *cardinal-closed*,
*catmull-rom*, *catmull-rom-open*, and *catmull-rom-closed*). For bundle splines, it corresponds to [beta][1]; for cardinal splines, [tension][2]; for Catmull-Rom splines, [alpha][3].

[1]: https://d3js.org/d3-shape/curve#curveBundle_beta [2]: https://d3js.org/d3-shape/curve#curveCardinal_tension [3]: https://d3js.org/d3-shape/curve#curveCatmullRom_alpha'''
    x: ChannelValueSpec
    '''The horizontal position channel, typically bound to the *x* scale; defaults to the zero-based index of the data [0, 1, 2, …].'''
    y: ChannelValueSpec
    '''The required vertical position channel, typically bound to the *y* scale.'''
    z: ChannelValue
    '''An optional ordinal channel for grouping data into (possibly stacked) series to be drawn as separate lines. If not specified, it defaults to
**fill** if a channel, or **stroke** if a channel.'''
class _LinkOpen(MarkOptions,total=False):
    """The link mark."""
    curve: Curve | L['auto'] | ParamRef | ParamRef
    '''The curve (interpolation) method for connecting adjacent points.

Since a link has exactly two points, only the following curves (or a custom curve) are recommended: *linear*, *step*, *step-after*, *step-before*,
*bump-x*, or *bump-y*. Note that the *linear* curve is incapable of showing a fill since a straight line has zero area. For a curved link, use an arrow mark with the **bend** option.

If the plot uses a spherical **projection**, the default *auto* **curve** will render links as geodesics; to draw a straight line instead, use the
*linear* **curve**.'''
    mark: Required[L['link']]
    '''A link mark, drawing line segments (curves) connecting pairs of points.

If the plot uses a spherical **projection**, the default *auto* **curve** will render links as geodesics; to draw a straight line instead, use the
*linear* **curve**.'''
    marker: L['none'] | MarkerName | None | ParamRef | bool
    '''Shorthand to set the same default for markerStart, markerMid, and markerEnd; one of:

- a marker name such as *arrow* or *circle*
- *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_end: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the ending point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_mid: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for any middle (interior) points of a line segment. If the line segment only has a start and end point, this option has no effect. One of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*
* a function - a custom marker function; see below'''
    marker_start: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the starting point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    tension: ParamRef | float
    '''The tension option only has an effect on bundle, cardinal and Catmull-Rom splines (*bundle*, *cardinal*, *cardinal-open*, *cardinal-closed*,
*catmull-rom*, *catmull-rom-open*, and *catmull-rom-closed*). For bundle splines, it corresponds to [beta][1]; for cardinal splines, [tension][2]; for Catmull-Rom splines, [alpha][3].

[1]: https://d3js.org/d3-shape/curve#curveBundle_beta [2]: https://d3js.org/d3-shape/curve#curveCardinal_tension [3]: https://d3js.org/d3-shape/curve#curveCatmullRom_alpha'''
    x: ChannelValueSpec
    '''The horizontal position, for vertical links; typically bound to the *x* scale; shorthand for setting defaults for both **x1** and **x2**.'''
    x1: ChannelValueSpec
    '''The starting horizontal position; typically bound to the *x* scale; also sets a default for **x2**.'''
    x2: ChannelValueSpec
    '''The ending horizontal position; typically bound to the *x* scale; also sets a default for **x1**.'''
    y: ChannelValueSpec
    '''The vertical position, for horizontal links; typically bound to the *y* scale; shorthand for setting defaults for both **y1** and **y2**.'''
    y1: ChannelValueSpec
    '''The starting vertical position; typically bound to the *y* scale; also sets a default for **y2**.'''
    y2: ChannelValueSpec
    '''The ending vertical position; typically bound to the *y* scale; also sets a default for **y1**.'''
class _RasterOpen(MarkOptions,total=False):
    """The raster mark."""
    bandwidth: ParamRef | float
    '''The kernel density bandwidth for smoothing, in pixels.'''
    height: ParamRef | float
    '''The height (number of rows) of the grid, in actual pixels.'''
    image_rendering: ParamRef | str
    '''The [image-rendering attribute][1]; defaults to *auto* (bilinear). The option may be set to *pixelated* to disable bilinear interpolation for a sharper image; however, note that this is not supported in WebKit.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/image-rendering'''
    interpolate: GridInterpolate | None | ParamRef
    '''The spatial interpolation method; one of:

- *none* - do not perform interpolation (the default), maps samples to single bins
- *linear* - apply proportional linear interpolation across adjacent bins
- *nearest* - assign each pixel to the closest sample's value (Voronoi diagram)
- *barycentric* - apply barycentric interpolation over the Delaunay triangulation
- *random-walk* - apply a random walk from each pixel, stopping when near a sample'''
    mark: Required[L['raster']]
    '''A raster mark which renders a raster image from spatial samples. It represents discrete samples in abstract coordinates **x** and **y**; the **fill** and **fillOpacity** channels specify further abstract values (_e.g._, height in a topographic map) to be spatially interpolated to produce an image.

The **x** and **y** data domains are binned into the cells ("pixels") of a raster grid, typically with an aggregate function evaluated over the binned data. The result can be optionally smoothed (blurred).

To create a smoothed density heatmap, use the heatmap mark, which is a raster mark with different default options.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    pad: ParamRef | float
    '''The bin padding, one of 1 (default) to include extra padding for the final bin, or 0 to make the bins flush with the maximum domain value.'''
    pixel_size: ParamRef | float
    '''The effective screen size of a raster pixel, used to determine the height and width of the raster from the frame's dimensions; defaults to 1.'''
    width: ParamRef | float
    '''The width (number of columns) of the grid, in actual pixels.'''
    x: ChannelValueSpec
    '''The horizontal position channel, typically bound to the *x* scale. Domain values are binned into a grid with *width* horizontal bins.'''
    y: ChannelValueSpec
    '''The vertical position channel, typically bound to the *y* scale. Domain values are binned into a grid with *height* vertical bins.'''
class _RasterTileOpen(MarkOptions,total=False):
    """The rasterTile mark."""
    bandwidth: ParamRef | float
    '''The kernel density bandwidth for smoothing, in pixels.'''
    height: ParamRef | float
    '''The height (number of rows) of the grid, in actual pixels.'''
    image_rendering: ParamRef | str
    '''The [image-rendering attribute][1]; defaults to *auto* (bilinear). The option may be set to *pixelated* to disable bilinear interpolation for a sharper image; however, note that this is not supported in WebKit.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/image-rendering'''
    interpolate: GridInterpolate | None | ParamRef
    '''The spatial interpolation method; one of:

- *none* - do not perform interpolation (the default), maps samples to single bins
- *linear* - apply proportional linear interpolation across adjacent bins
- *nearest* - assign each pixel to the closest sample's value (Voronoi diagram)
- *barycentric* - apply barycentric interpolation over the Delaunay triangulation
- *random-walk* - apply a random walk from each pixel, stopping when near a sample'''
    mark: Required[L['rasterTile']]
    '''An experimental raster mark which performs tiling and prefetching to support more scalable rasters upon panning the domain. Uses a tile size that matches with current width and height, and prefetches data from neighboring tile segments.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    origin: ParamRef | tuple[float,float]
    '''The coordinates of the tile origin in the **x** and **y** data domains. Defaults to [0, 0].'''
    pad: ParamRef | float
    '''The bin padding, one of 1 (default) to include extra padding for the final bin, or 0 to make the bins flush with the maximum domain value.'''
    pixel_size: ParamRef | float
    '''The effective screen size of a raster pixel, used to determine the height and width of the raster from the frame's dimensions; defaults to 1.'''
    width: ParamRef | float
    '''The width (number of columns) of the grid, in actual pixels.'''
    x: ChannelValueSpec
    '''The horizontal position channel, typically bound to the *x* scale. Domain values are binned into a grid with *width* horizontal bins.'''
    y: ChannelValueSpec
    '''The vertical position channel, typically bound to the *y* scale. Domain values are binned into a grid with *height* vertical bins.'''
class _RectOpen(MarkOptions,total=False):
    """The rect mark."""
    inset: ParamRef | float
    '''Shorthand to set the same default for all four insets: **insetTop**,
**insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it.'''
    inset_bottom: ParamRef | float
    '''Insets the bottom edge by the specified number of pixels. A positive value insets towards the top edge (reducing effective area), while a negative value insets away from the top edge (increasing it).'''
    inset_left: ParamRef | float
    '''Insets the left edge by the specified number of pixels. A positive value insets towards the right edge (reducing effective area), while a negative value insets away from the right edge (increasing it).'''
    inset_right: ParamRef | float
    '''Insets the right edge by the specified number of pixels. A positive value insets towards the left edge (reducing effective area), while a negative value insets away from the left edge (increasing it).'''
    inset_top: ParamRef | float
    '''Insets the top edge by the specified number of pixels. A positive value insets towards the bottom edge (reducing effective area), while a negative value insets away from the bottom edge (increasing it).'''
    interval: Interval | ParamRef
    '''How to convert a continuous value (**x** for rectY, **y** for rectX, or both for rect) into an interval (**x1** and **x2** for rectY, or **y1** and
**y2** for rectX, or both for rect); one of:

- a named time interval such as *day* (for date intervals)
- a number (for number intervals), defining intervals at integer multiples of *n*

Setting this option disables the implicit stack transform (stackX for rectX, or stackY for rectY).'''
    mark: Required[L['rect']]
    '''A rect mark. The rectangle extends horizontally from **x1** to **x2**, and vertically from **y1** to **y2**. The position channels are often derived with a transform.

When **y** extends from zero, for example for a histogram where the height of each rect reflects a count of values, use the rectY mark for an implicit stackY transform; similarly, if **x** extends from zero, use the rectX mark for an implicit stackX transform.

If an **interval** is specified, then **x1** and **x2** are derived from
**x**, and **y1** and **y2** are derived from **y**, each representing the lower and upper bound of the containing interval, respectively.

Both *x* and *y* should be quantitative or temporal; otherwise, use a bar or cell mark.'''
    offset: None | ParamRef | StackOffset
    '''After stacking, an optional **offset** can be applied to translate and scale stacks, say to produce a streamgraph; defaults to null for a zero baseline (**y** = 0 for stackY, and **x** = 0 for stackX). If the *wiggle* offset is used, the default **order** changes to *inside-out*.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    order: None | ParamRef | StackOrder
    '''The order in which stacks are layered; one of:

- null (default) for input order
- a named stack order method such as *inside-out* or *sum*
- a field name, for natural order of the corresponding values
- a function of data, for natural order of the corresponding values
- an array of explicit **z** values in the desired order

If the *wiggle* **offset** is used, as for a streamgraph, the default changes to *inside-out*.'''
    rx: ParamRef | float | str
    '''The rounded corner [*x*-radius][1], either in pixels or as a percentage of the rect width. If **rx** is not specified, it defaults to **ry** if present, and otherwise draws square corners.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/rx'''
    ry: ParamRef | float | str
    '''The rounded corner [*y*-radius][1], either in pixels or as a percentage of the rect height. If **ry** is not specified, it defaults to **rx** if present, and otherwise draws square corners.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/ry'''
    x: ChannelValueIntervalSpec
    '''The horizontal position (or length/width) channel, typically bound to the
*x* scale.

If an **interval** is specified, then **x1** and **x2** are derived from
**x**, representing the lower and upper bound of the containing interval, respectively. For example, for a vertical bar chart of items sold by day:

```js Plot.rectY(sales, {x: "date", interval: "day", y2: "items"}) ```

If *x* represents ordinal values, use a bar or cell mark instead.'''
    x1: ChannelValueSpec
    '''The required primary (starting, often left) horizontal position channel, typically bound to the *x* scale. Setting this option disables the rectX mark's implicit stackX transform.

If *x* represents ordinal values, use a bar or cell mark instead.'''
    x2: ChannelValueSpec
    '''The required secondary (ending, often right) horizontal position channel, typically bound to the *x* scale. Setting this option disables the rectX mark's implicit stackX transform.

If *x* represents ordinal values, use a bar or cell mark instead.'''
    y: ChannelValueIntervalSpec
    '''The vertical position (or length/height) channel, typically bound to the
*y* scale.

If an **interval** is specified, then **y1** and **y2** are derived from
**y**, representing the lower and upper bound of the containing interval, respectively. For example, for a horizontal bar chart of items sold by day:

```js Plot.rectX(sales, {y: "date", interval: "day", x2: "items"}) ```

If *y* represents ordinal values, use a bar or cell mark instead.'''
    y1: ChannelValueSpec
    '''The required primary (starting, often bottom) vertical position channel, typically bound to the *y* scale. Setting this option disables the rectY mark's implicit stackY transform.

If *y* represents ordinal values, use a bar or cell mark instead.'''
    y2: ChannelValueSpec
    '''The required secondary (ending, often top) vertical position channel, typically bound to the *y* scale. Setting this option disables the rectY mark's implicit stackY transform.

If *y* represents ordinal values, use a bar or cell mark instead.'''
    z: ChannelValue
    '''The **z** channel defines the series of each value in the stack. Used when the **order** is *sum*, *appearance*, *inside-out*, or an explicit array of
**z** values.'''
class _RectXOpen(MarkOptions,total=False):
    """The rectX mark."""
    inset: ParamRef | float
    '''Shorthand to set the same default for all four insets: **insetTop**,
**insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it.'''
    inset_bottom: ParamRef | float
    '''Insets the bottom edge by the specified number of pixels. A positive value insets towards the top edge (reducing effective area), while a negative value insets away from the top edge (increasing it).'''
    inset_left: ParamRef | float
    '''Insets the left edge by the specified number of pixels. A positive value insets towards the right edge (reducing effective area), while a negative value insets away from the right edge (increasing it).'''
    inset_right: ParamRef | float
    '''Insets the right edge by the specified number of pixels. A positive value insets towards the left edge (reducing effective area), while a negative value insets away from the left edge (increasing it).'''
    inset_top: ParamRef | float
    '''Insets the top edge by the specified number of pixels. A positive value insets towards the bottom edge (reducing effective area), while a negative value insets away from the bottom edge (increasing it).'''
    interval: Interval | ParamRef
    '''How to convert a continuous value (**x** for rectY, **y** for rectX, or both for rect) into an interval (**x1** and **x2** for rectY, or **y1** and
**y2** for rectX, or both for rect); one of:

- a named time interval such as *day* (for date intervals)
- a number (for number intervals), defining intervals at integer multiples of *n*

Setting this option disables the implicit stack transform (stackX for rectX, or stackY for rectY).'''
    mark: Required[L['rectX']]
    '''Like rect, but if neither **x1** nor **x2** is specified, an implicit stackX transform is applied to **x**, and if **x** is not specified, it defaults to the identity function, assuming that *data* is an array of numbers [*x₀*, *x₁*, *x₂*, …].'''
    offset: None | ParamRef | StackOffset
    '''After stacking, an optional **offset** can be applied to translate and scale stacks, say to produce a streamgraph; defaults to null for a zero baseline (**y** = 0 for stackY, and **x** = 0 for stackX). If the *wiggle* offset is used, the default **order** changes to *inside-out*.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    order: None | ParamRef | StackOrder
    '''The order in which stacks are layered; one of:

- null (default) for input order
- a named stack order method such as *inside-out* or *sum*
- a field name, for natural order of the corresponding values
- a function of data, for natural order of the corresponding values
- an array of explicit **z** values in the desired order

If the *wiggle* **offset** is used, as for a streamgraph, the default changes to *inside-out*.'''
    rx: ParamRef | float | str
    '''The rounded corner [*x*-radius][1], either in pixels or as a percentage of the rect width. If **rx** is not specified, it defaults to **ry** if present, and otherwise draws square corners.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/rx'''
    ry: ParamRef | float | str
    '''The rounded corner [*y*-radius][1], either in pixels or as a percentage of the rect height. If **ry** is not specified, it defaults to **rx** if present, and otherwise draws square corners.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/ry'''
    x: ChannelValueSpec
    '''The horizontal position (or length/width) channel, typically bound to the
*x* scale.

If neither **x1** nor **x2** is specified, an implicit stackX transform is applied and **x** defaults to the identity function, assuming that *data* = [*x₀*, *x₁*, *x₂*, …]. Otherwise, if only one of **x1** or **x2** is specified, the other defaults to **x**, which defaults to zero.'''
    x1: ChannelValueSpec
    '''The required primary (starting, often left) horizontal position channel, typically bound to the *x* scale. Setting this option disables the rectX mark's implicit stackX transform.

If *x* represents ordinal values, use a bar or cell mark instead.'''
    x2: ChannelValueSpec
    '''The required secondary (ending, often right) horizontal position channel, typically bound to the *x* scale. Setting this option disables the rectX mark's implicit stackX transform.

If *x* represents ordinal values, use a bar or cell mark instead.'''
    y: ChannelValueIntervalSpec
    '''The vertical position (or length/height) channel, typically bound to the
*y* scale.

If an **interval** is specified, then **y1** and **y2** are derived from
**y**, representing the lower and upper bound of the containing interval, respectively. For example, for a horizontal bar chart of items sold by day:

```js Plot.rectX(sales, {y: "date", interval: "day", x2: "items"}) ```

If *y* represents ordinal values, use a bar or cell mark instead.'''
    y1: ChannelValueSpec
    '''The required primary (starting, often bottom) vertical position channel, typically bound to the *y* scale. Setting this option disables the rectY mark's implicit stackY transform.

If *y* represents ordinal values, use a bar or cell mark instead.'''
    y2: ChannelValueSpec
    '''The required secondary (ending, often top) vertical position channel, typically bound to the *y* scale. Setting this option disables the rectY mark's implicit stackY transform.

If *y* represents ordinal values, use a bar or cell mark instead.'''
    z: ChannelValue
    '''The **z** channel defines the series of each value in the stack. Used when the **order** is *sum*, *appearance*, *inside-out*, or an explicit array of
**z** values.'''
class _RectYOpen(MarkOptions,total=False):
    """The rectY mark."""
    inset: ParamRef | float
    '''Shorthand to set the same default for all four insets: **insetTop**,
**insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it.'''
    inset_bottom: ParamRef | float
    '''Insets the bottom edge by the specified number of pixels. A positive value insets towards the top edge (reducing effective area), while a negative value insets away from the top edge (increasing it).'''
    inset_left: ParamRef | float
    '''Insets the left edge by the specified number of pixels. A positive value insets towards the right edge (reducing effective area), while a negative value insets away from the right edge (increasing it).'''
    inset_right: ParamRef | float
    '''Insets the right edge by the specified number of pixels. A positive value insets towards the left edge (reducing effective area), while a negative value insets away from the left edge (increasing it).'''
    inset_top: ParamRef | float
    '''Insets the top edge by the specified number of pixels. A positive value insets towards the bottom edge (reducing effective area), while a negative value insets away from the bottom edge (increasing it).'''
    interval: Interval | ParamRef
    '''How to convert a continuous value (**x** for rectY, **y** for rectX, or both for rect) into an interval (**x1** and **x2** for rectY, or **y1** and
**y2** for rectX, or both for rect); one of:

- a named time interval such as *day* (for date intervals)
- a number (for number intervals), defining intervals at integer multiples of *n*

Setting this option disables the implicit stack transform (stackX for rectX, or stackY for rectY).'''
    mark: Required[L['rectY']]
    '''Like rect, but if neither **y1** nor **y2** is specified, apply an implicit stackY transform is applied to **y**, and if **y** is not specified, it defaults to the identity function, assuming that *data* is an array of numbers [*y₀*, *y₁*, *y₂*, …].'''
    offset: None | ParamRef | StackOffset
    '''After stacking, an optional **offset** can be applied to translate and scale stacks, say to produce a streamgraph; defaults to null for a zero baseline (**y** = 0 for stackY, and **x** = 0 for stackX). If the *wiggle* offset is used, the default **order** changes to *inside-out*.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    order: None | ParamRef | StackOrder
    '''The order in which stacks are layered; one of:

- null (default) for input order
- a named stack order method such as *inside-out* or *sum*
- a field name, for natural order of the corresponding values
- a function of data, for natural order of the corresponding values
- an array of explicit **z** values in the desired order

If the *wiggle* **offset** is used, as for a streamgraph, the default changes to *inside-out*.'''
    rx: ParamRef | float | str
    '''The rounded corner [*x*-radius][1], either in pixels or as a percentage of the rect width. If **rx** is not specified, it defaults to **ry** if present, and otherwise draws square corners.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/rx'''
    ry: ParamRef | float | str
    '''The rounded corner [*y*-radius][1], either in pixels or as a percentage of the rect height. If **ry** is not specified, it defaults to **rx** if present, and otherwise draws square corners.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/ry'''
    x: ChannelValueIntervalSpec
    '''The horizontal position (or length/width) channel, typically bound to the
*x* scale.

If an **interval** is specified, then **x1** and **x2** are derived from
**x**, representing the lower and upper bound of the containing interval, respectively. For example, for a vertical bar chart of items sold by day:

```js Plot.rectY(sales, {x: "date", interval: "day", y2: "items"}) ```

If *x* represents ordinal values, use a bar or cell mark instead.'''
    x1: ChannelValueSpec
    '''The required primary (starting, often left) horizontal position channel, typically bound to the *x* scale. Setting this option disables the rectX mark's implicit stackX transform.

If *x* represents ordinal values, use a bar or cell mark instead.'''
    x2: ChannelValueSpec
    '''The required secondary (ending, often right) horizontal position channel, typically bound to the *x* scale. Setting this option disables the rectX mark's implicit stackX transform.

If *x* represents ordinal values, use a bar or cell mark instead.'''
    y: ChannelValueSpec
    '''The vertical position (or length/height) channel, typically bound to the
*y* scale.

If neither **y1** nor **y2** is specified, an implicit stackY transform is applied and **y** defaults to the identity function, assuming that *data* = [*y₀*, *y₁*, *y₂*, …]. Otherwise, if only one of **y1** or **y2** is specified, the other defaults to **y**, which defaults to zero.'''
    y1: ChannelValueSpec
    '''The required primary (starting, often bottom) vertical position channel, typically bound to the *y* scale. Setting this option disables the rectY mark's implicit stackY transform.

If *y* represents ordinal values, use a bar or cell mark instead.'''
    y2: ChannelValueSpec
    '''The required secondary (ending, often top) vertical position channel, typically bound to the *y* scale. Setting this option disables the rectY mark's implicit stackY transform.

If *y* represents ordinal values, use a bar or cell mark instead.'''
    z: ChannelValue
    '''The **z** channel defines the series of each value in the stack. Used when the **order** is *sum*, *appearance*, *inside-out*, or an explicit array of
**z** values.'''
class _RegressionYOpen(MarkOptions,total=False):
    """The regressionY mark."""
    ci: ParamRef | float
    '''The confidence interval in (0, 1), or 0 to hide bands; defaults to 0.95.'''
    mark: Required[L['regressionY']]
    '''A mark that draws [linear regression][1] lines with confidence bands, representing the estimated relation of a dependent variable (*y*) on an independent variable (*x*).

The linear regression line is fit using the [least squares][2] approach. See Torben Jansen's [“Linear regression with confidence bands”][3] and [this StatExchange question][4] for details on the confidence interval calculation.

Multiple regressions can be produced by specifying a **z**, **fill**, or
**stroke** channel.

[1]: https://en.wikipedia.org/wiki/Linear_regression [2]: https://en.wikipedia.org/wiki/Least_squares [3]: https://observablehq.com/@toja/linear-regression-with-confidence-bands [4]: https://stats.stackexchange.com/questions/101318/understanding-shape-and-calculation-of-confidence-bands-in-linear-regression'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    precision: ParamRef | float
    '''The distance in pixels between samples of the confidence band; defaults to 4.'''
    x: ChannelValueSpec
    '''The independent variable horizontal position channel, typically bound to the *x* scale; defaults to the zero-based index of the data [0, 1, 2, …].'''
    y: ChannelValueSpec
    '''The dependent variable vertical position channel, typically bound to the
*y* scale; defaults to identity, assuming that *data* = [*y₀*, *y₁*, *y₂*, …].'''
    z: ChannelValue
    '''An optional ordinal channel for grouping data into (possibly stacked) series, producing an independent regression for each group. If not specified, it defaults to **fill** if a channel, or **stroke** if a channel.'''
class _RuleXOpen(MarkOptions,total=False):
    """The ruleX mark."""
    inset: ParamRef | float
    '''Shorthand to set the same default for all four insets: **insetTop**,
**insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it.'''
    inset_bottom: ParamRef | float
    '''Insets the bottom edge by the specified number of pixels. A positive value insets towards the top edge (reducing effective area), while a negative value insets away from the top edge (increasing it).'''
    inset_top: ParamRef | float
    '''Insets the top edge by the specified number of pixels. A positive value insets towards the bottom edge (reducing effective area), while a negative value insets away from the bottom edge (increasing it).'''
    interval: Interval | ParamRef
    '''How to convert a continuous value (**y** for ruleX, or **x** for ruleY) into an interval (**y1** and **y2** for ruleX, or **x1** and **x2** for ruleY); one of:

- a named time interval such as *day* (for date intervals)
- a number (for number intervals), defining intervals at integer multiples of *n*'''
    mark: Required[L['ruleX']]
    '''A horizontally-positioned ruleX mark (a vertical line, |). The **x** channel specifies the rule's horizontal position and defaults to identity, assuming that *data* = [*x₀*, *x₁*, *x₂*, …]; the optional **y1** and
**y2** channels specify its vertical extent.

The ruleX mark is often used to highlight specific *x* values. If *y* represents ordinal values, use a tickX mark instead.'''
    marker: L['none'] | MarkerName | None | ParamRef | bool
    '''Shorthand to set the same default for markerStart, markerMid, and markerEnd; one of:

- a marker name such as *arrow* or *circle*
- *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_end: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the ending point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_mid: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for any middle (interior) points of a line segment. If the line segment only has a start and end point, this option has no effect. One of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*
* a function - a custom marker function; see below'''
    marker_start: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the starting point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    x: ChannelValueSpec
    '''The horizontal position of the tick; an optional channel bound to the *x* scale. If not specified, the rule will be horizontally centered in the plot's frame.'''
    y: ChannelValueIntervalSpec
    '''Shorthand for specifying both the primary and secondary vertical position of the tick as the bounds of the containing interval; can only be used in conjunction with the **interval** option.'''
    y1: ChannelValueSpec
    '''The primary (starting, often bottom) vertical position of the tick; a channel bound to the *y* scale.

If *y* represents ordinal values, use a tickX mark instead.'''
    y2: ChannelValueSpec
    '''The secondary (ending, often top) vertical position of the tick; a channel bound to the *y* scale.

If *y* represents ordinal values, use a tickX mark instead.'''
class _RuleYOpen(MarkOptions,total=False):
    """The ruleY mark."""
    inset: ParamRef | float
    '''Shorthand to set the same default for all four insets: **insetTop**,
**insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it.'''
    inset_bottom: ParamRef | float
    '''Insets the bottom edge by the specified number of pixels. A positive value insets towards the top edge (reducing effective area), while a negative value insets away from the top edge (increasing it).'''
    inset_top: ParamRef | float
    '''Insets the top edge by the specified number of pixels. A positive value insets towards the bottom edge (reducing effective area), while a negative value insets away from the bottom edge (increasing it).'''
    interval: Interval | ParamRef
    '''How to convert a continuous value (**y** for ruleX, or **x** for ruleY) into an interval (**y1** and **y2** for ruleX, or **x1** and **x2** for ruleY); one of:

- a named time interval such as *day* (for date intervals)
- a number (for number intervals), defining intervals at integer multiples of *n*'''
    mark: Required[L['ruleY']]
    '''A vertically-positioned ruleY mark (a horizontal line, —). The **y** channel specifies the rule's vertical position and defaults to identity, assuming that *data* = [*y₀*, *y₁*, *y₂*, …]; the optional **x1** and
**x2** channels specify its horizontal extent.

The ruleY mark is often used to highlight specific *y* values. If *x* represents ordinal values, use a tickY mark instead.'''
    marker: L['none'] | MarkerName | None | ParamRef | bool
    '''Shorthand to set the same default for markerStart, markerMid, and markerEnd; one of:

- a marker name such as *arrow* or *circle*
- *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_end: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the ending point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_mid: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for any middle (interior) points of a line segment. If the line segment only has a start and end point, this option has no effect. One of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*
* a function - a custom marker function; see below'''
    marker_start: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the starting point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    x: ChannelValueSpec
    '''The horizontal position of the tick; an optional channel bound to the *x* scale. If not specified, the rule will be horizontally centered in the plot's frame.'''
    y: ChannelValueIntervalSpec
    '''Shorthand for specifying both the primary and secondary vertical position of the tick as the bounds of the containing interval; can only be used in conjunction with the **interval** option.'''
    y1: ChannelValueSpec
    '''The primary (starting, often bottom) vertical position of the tick; a channel bound to the *y* scale.

If *y* represents ordinal values, use a tickX mark instead.'''
    y2: ChannelValueSpec
    '''The secondary (ending, often top) vertical position of the tick; a channel bound to the *y* scale.

If *y* represents ordinal values, use a tickX mark instead.'''
class _SphereOpen(MarkOptions,total=False):
    """The sphere mark."""
    mark: Required[L['sphere']]
    '''A geo mark whose *data* is the outline of the sphere on the projection's plane. (For use with a spherical **projection** only.)'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
class _SpikeOpen(MarkOptions,total=False):
    """The spike mark."""
    anchor: L['end','middle','start'] | ParamRef
    '''The vector's position along its orientation relative to its anchor point; a constant. Assuming a default **rotate** angle of 0°, one of:

- *start* - from [*x*, *y*] to [*x*, *y* - *l*]
- *middle* (default) - from [*x*, *y* + *l* / 2] to [*x*, *y* - *l* / 2]
- *end* - from [*x*, *y* + *l*] to [*x*, *y*]

where [*x*, *y*] is the vector's anchor point and *l* is the vector's (possibly scaled) length in pixels.'''
    frame_anchor: FrameAnchor | ParamRef
    '''The vector's frame anchor, to default **x** and **y** relative to the frame; a constant representing one of the frame corners (*top-left*,
*top-right*, *bottom-right*, *bottom-left*), sides (*top*, *right*,
*bottom*, *left*), or *middle* (default). Has no effect if both **x** and **y** are specified.'''
    length: ChannelValueSpec
    '''The vector's length; either an optional channel bound to the *length* scale or a constant number in pixels. Defaults to 12 pixels.'''
    mark: Required[L['spike']]
    '''Like vector, but with default *options* suitable for drawing a spike map.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    r: ParamRef | float
    '''The vector shape's radius, such as half the width of the *arrow*'s head or the *spike*'s base; a constant number in pixels. Defaults to 3.5 pixels.'''
    rotate: ChannelValue
    '''The vector's orientation (rotation angle); either a constant number in degrees clockwise, or an optional channel (with no associated scale). Defaults to 0 degrees with the vector pointing up.'''
    shape: ParamRef | VectorShape
    '''The shape of the vector; a constant. Defaults to *arrow*.'''
    x: ChannelValueSpec
    '''The horizontal position of the vector's anchor point; an optional channel bound to the *x* scale. Default depends on the **frameAnchor**.'''
    y: ChannelValueSpec
    '''The vertical position of the vector's anchor point; an optional channel bound to the *y* scale. Default depends on the **frameAnchor**.'''
class _TextOpen(MarkOptions,total=False):
    """The text mark."""
    font_family: ParamRef | str
    '''The [font-family][1]; a constant; defaults to the plot's font family, which is typically [*system-ui*][2].

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-family [2]: https://drafts.csswg.org/css-fonts-4/#valdef-font-family-system-ui'''
    font_size: ChannelValue | ParamRef
    '''The [font size][1] in pixels; either a constant or a channel; defaults to the plot's font size, which is typically 10. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-size'''
    font_style: ParamRef | str
    '''The [font style][1]; a constant; defaults to the plot's font style, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-style'''
    font_variant: ParamRef | str
    '''The [font variant][1]; a constant; if the **text** channel contains numbers or dates, defaults to *tabular-nums* to facilitate comparing numbers; otherwise defaults to the plot's font style, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant'''
    font_weight: ParamRef | float | str
    '''The [font weight][1]; a constant; defaults to the plot's font weight, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight'''
    frame_anchor: FrameAnchor | ParamRef
    '''The frame anchor specifies defaults for **x** and **y**, along with
**textAnchor** and **lineAnchor**, based on the plot's frame; it may be one of the four sides (*top*, *right*, *bottom*, *left*), one of the four corners (*top-left*, *top-right*, *bottom-right*, *bottom-left*), or the
*middle* of the frame.'''
    line_anchor: L['bottom','middle','top'] | ParamRef
    '''The line anchor controls how text is aligned (typically vertically) relative to its anchor point; it is one of *top*, *bottom*, or *middle*. If the frame anchor is *top*, *top-left*, or *top-right*, the default line anchor is *top*; if the frame anchor is *bottom*, *bottom-right*, or
*bottom-left*, the default is *bottom*; otherwise it is *middle*.'''
    line_height: ParamRef | float
    '''The line height in ems; defaults to 1. The line height affects the (typically vertical) separation between adjacent baselines of text, as well as the separation between the text and its anchor point.'''
    line_width: ParamRef | float
    '''The line width in ems (e.g., 10 for about 20 characters); defaults to infinity, disabling wrapping and clipping.

If **textOverflow** is null, lines will be wrapped at the specified length. If a line is split at a soft hyphen (\xad), a hyphen (-) will be displayed at the end of the line. If **textOverflow** is not null, lines will be clipped according to the given strategy.'''
    mark: Required[L['text']]
    '''A text mark. The **text** channel specifies the textual contents of the mark, which may be preformatted with line breaks (\n, \r\n, or \r), or wrapped or clipped using the **lineWidth** and **textOverflow** options.

If **text** contains numbers or dates, a default formatter will be applied, and the **fontVariant** will default to *tabular-nums* instead of *normal*. If **text** is not specified, it defaults to the identity function for primitive data (such as numbers, dates, and strings), and to the zero-based index [0, 1, 2, …] for objects (so that something identifying is visible by default).

If either **x** or **y** is not specified, the default is determined by the **frameAnchor** option.'''
    monospace: ParamRef | bool
    '''If true, changes the default **fontFamily** to *monospace*, and uses simplified monospaced text metrics calculations.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    rotate: ChannelValue | ParamRef
    '''The rotation angle in degrees clockwise; a constant or a channel; defaults to 0°. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel.'''
    text: ChannelValue
    '''The text contents channel, possibly with line breaks (\n, \r\n, or \r). If not specified, defaults to the zero-based index [0, 1, 2, …].'''
    text_anchor: L['end','middle','start'] | ParamRef
    '''The [text anchor][1] controls how text is aligned (typically horizontally) relative to its anchor point; it is one of *start*, *end*, or *middle*. If the frame anchor is *left*, *top-left*, or *bottom-left*, the default text anchor is *start*; if the frame anchor is *right*, *top-right*, or
*bottom-right*, the default is *end*; otherwise it is *middle*.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/text-anchor'''
    text_overflow: L['clip','clip-end','clip-start','ellipsis','ellipsis-end','ellipsis-middle','ellipsis-start'] | None | ParamRef
    '''How truncate (or wrap) lines of text longer than the given **lineWidth**; one of:

- null (default) - preserve overflowing characters (and wrap if needed)
- *clip* or *clip-end* - remove characters from the end
- *clip-start* - remove characters from the start
- *ellipsis* or *ellipsis-end* - replace characters from the end with an ellipsis (…)
- *ellipsis-start* - replace characters from the start with an ellipsis (…)
- *ellipsis-middle* - replace characters from the middle with an ellipsis (…)

If no **title** was specified, if text requires truncation, a title containing the non-truncated text will be implicitly added.'''
    x: ChannelValueSpec
    '''The horizontal position channel specifying the text's anchor point, typically bound to the *x* scale.'''
    y: ChannelValueSpec
    '''The vertical position channel specifying the text's anchor point, typically bound to the *y* scale.'''
    z: ChannelValue
    '''An optional ordinal channel for grouping data into series.'''
class _TextXOpen(MarkOptions,total=False):
    """The textX mark."""
    font_family: ParamRef | str
    '''The [font-family][1]; a constant; defaults to the plot's font family, which is typically [*system-ui*][2].

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-family [2]: https://drafts.csswg.org/css-fonts-4/#valdef-font-family-system-ui'''
    font_size: ChannelValue | ParamRef
    '''The [font size][1] in pixels; either a constant or a channel; defaults to the plot's font size, which is typically 10. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-size'''
    font_style: ParamRef | str
    '''The [font style][1]; a constant; defaults to the plot's font style, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-style'''
    font_variant: ParamRef | str
    '''The [font variant][1]; a constant; if the **text** channel contains numbers or dates, defaults to *tabular-nums* to facilitate comparing numbers; otherwise defaults to the plot's font style, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant'''
    font_weight: ParamRef | float | str
    '''The [font weight][1]; a constant; defaults to the plot's font weight, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight'''
    frame_anchor: FrameAnchor | ParamRef
    '''The frame anchor specifies defaults for **x** and **y**, along with
**textAnchor** and **lineAnchor**, based on the plot's frame; it may be one of the four sides (*top*, *right*, *bottom*, *left*), one of the four corners (*top-left*, *top-right*, *bottom-right*, *bottom-left*), or the
*middle* of the frame.'''
    interval: Interval | ParamRef
    '''An interval (such as *day* or a number), to transform **y** values to the middle of the interval.'''
    line_anchor: L['bottom','middle','top'] | ParamRef
    '''The line anchor controls how text is aligned (typically vertically) relative to its anchor point; it is one of *top*, *bottom*, or *middle*. If the frame anchor is *top*, *top-left*, or *top-right*, the default line anchor is *top*; if the frame anchor is *bottom*, *bottom-right*, or
*bottom-left*, the default is *bottom*; otherwise it is *middle*.'''
    line_height: ParamRef | float
    '''The line height in ems; defaults to 1. The line height affects the (typically vertical) separation between adjacent baselines of text, as well as the separation between the text and its anchor point.'''
    line_width: ParamRef | float
    '''The line width in ems (e.g., 10 for about 20 characters); defaults to infinity, disabling wrapping and clipping.

If **textOverflow** is null, lines will be wrapped at the specified length. If a line is split at a soft hyphen (\xad), a hyphen (-) will be displayed at the end of the line. If **textOverflow** is not null, lines will be clipped according to the given strategy.'''
    mark: Required[L['textX']]
    '''Like text, but **x** defaults to the identity function, assuming that
*data* = [*x₀*, *x₁*, *x₂*, …]. If an **interval** is specified, such as
*day*, **y** is transformed to the middle of the interval.'''
    monospace: ParamRef | bool
    '''If true, changes the default **fontFamily** to *monospace*, and uses simplified monospaced text metrics calculations.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    rotate: ChannelValue | ParamRef
    '''The rotation angle in degrees clockwise; a constant or a channel; defaults to 0°. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel.'''
    text: ChannelValue
    '''The text contents channel, possibly with line breaks (\n, \r\n, or \r). If not specified, defaults to the zero-based index [0, 1, 2, …].'''
    text_anchor: L['end','middle','start'] | ParamRef
    '''The [text anchor][1] controls how text is aligned (typically horizontally) relative to its anchor point; it is one of *start*, *end*, or *middle*. If the frame anchor is *left*, *top-left*, or *bottom-left*, the default text anchor is *start*; if the frame anchor is *right*, *top-right*, or
*bottom-right*, the default is *end*; otherwise it is *middle*.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/text-anchor'''
    text_overflow: L['clip','clip-end','clip-start','ellipsis','ellipsis-end','ellipsis-middle','ellipsis-start'] | None | ParamRef
    '''How truncate (or wrap) lines of text longer than the given **lineWidth**; one of:

- null (default) - preserve overflowing characters (and wrap if needed)
- *clip* or *clip-end* - remove characters from the end
- *clip-start* - remove characters from the start
- *ellipsis* or *ellipsis-end* - replace characters from the end with an ellipsis (…)
- *ellipsis-start* - replace characters from the start with an ellipsis (…)
- *ellipsis-middle* - replace characters from the middle with an ellipsis (…)

If no **title** was specified, if text requires truncation, a title containing the non-truncated text will be implicitly added.'''
    x: ChannelValueSpec
    '''The horizontal position channel specifying the text's anchor point, typically bound to the *x* scale.'''
    y: ChannelValueIntervalSpec
    '''The vertical position of the text's anchor point, typically bound to the
*y* scale.'''
    z: ChannelValue
    '''An optional ordinal channel for grouping data into series.'''
class _TextYOpen(MarkOptions,total=False):
    """The textY mark."""
    font_family: ParamRef | str
    '''The [font-family][1]; a constant; defaults to the plot's font family, which is typically [*system-ui*][2].

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-family [2]: https://drafts.csswg.org/css-fonts-4/#valdef-font-family-system-ui'''
    font_size: ChannelValue | ParamRef
    '''The [font size][1] in pixels; either a constant or a channel; defaults to the plot's font size, which is typically 10. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-size'''
    font_style: ParamRef | str
    '''The [font style][1]; a constant; defaults to the plot's font style, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-style'''
    font_variant: ParamRef | str
    '''The [font variant][1]; a constant; if the **text** channel contains numbers or dates, defaults to *tabular-nums* to facilitate comparing numbers; otherwise defaults to the plot's font style, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant'''
    font_weight: ParamRef | float | str
    '''The [font weight][1]; a constant; defaults to the plot's font weight, which is typically *normal*.

[1]: https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight'''
    frame_anchor: FrameAnchor | ParamRef
    '''The frame anchor specifies defaults for **x** and **y**, along with
**textAnchor** and **lineAnchor**, based on the plot's frame; it may be one of the four sides (*top*, *right*, *bottom*, *left*), one of the four corners (*top-left*, *top-right*, *bottom-right*, *bottom-left*), or the
*middle* of the frame.'''
    interval: Interval
    '''An interval (such as *day* or a number), to transform **x** values to the middle of the interval.'''
    line_anchor: L['bottom','middle','top'] | ParamRef
    '''The line anchor controls how text is aligned (typically vertically) relative to its anchor point; it is one of *top*, *bottom*, or *middle*. If the frame anchor is *top*, *top-left*, or *top-right*, the default line anchor is *top*; if the frame anchor is *bottom*, *bottom-right*, or
*bottom-left*, the default is *bottom*; otherwise it is *middle*.'''
    line_height: ParamRef | float
    '''The line height in ems; defaults to 1. The line height affects the (typically vertical) separation between adjacent baselines of text, as well as the separation between the text and its anchor point.'''
    line_width: ParamRef | float
    '''The line width in ems (e.g., 10 for about 20 characters); defaults to infinity, disabling wrapping and clipping.

If **textOverflow** is null, lines will be wrapped at the specified length. If a line is split at a soft hyphen (\xad), a hyphen (-) will be displayed at the end of the line. If **textOverflow** is not null, lines will be clipped according to the given strategy.'''
    mark: Required[L['textY']]
    '''Like text, but **y** defaults to the identity function, assuming that
*data* = [*y₀*, *y₁*, *y₂*, …]. If an **interval** is specified, such as
*day*, **x** is transformed to the middle of the interval.'''
    monospace: ParamRef | bool
    '''If true, changes the default **fontFamily** to *monospace*, and uses simplified monospaced text metrics calculations.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    rotate: ChannelValue | ParamRef
    '''The rotation angle in degrees clockwise; a constant or a channel; defaults to 0°. When a number, it is interpreted as a constant; otherwise it is interpreted as a channel.'''
    text: ChannelValue
    '''The text contents channel, possibly with line breaks (\n, \r\n, or \r). If not specified, defaults to the zero-based index [0, 1, 2, …].'''
    text_anchor: L['end','middle','start'] | ParamRef
    '''The [text anchor][1] controls how text is aligned (typically horizontally) relative to its anchor point; it is one of *start*, *end*, or *middle*. If the frame anchor is *left*, *top-left*, or *bottom-left*, the default text anchor is *start*; if the frame anchor is *right*, *top-right*, or
*bottom-right*, the default is *end*; otherwise it is *middle*.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/text-anchor'''
    text_overflow: L['clip','clip-end','clip-start','ellipsis','ellipsis-end','ellipsis-middle','ellipsis-start'] | None | ParamRef
    '''How truncate (or wrap) lines of text longer than the given **lineWidth**; one of:

- null (default) - preserve overflowing characters (and wrap if needed)
- *clip* or *clip-end* - remove characters from the end
- *clip-start* - remove characters from the start
- *ellipsis* or *ellipsis-end* - replace characters from the end with an ellipsis (…)
- *ellipsis-start* - replace characters from the start with an ellipsis (…)
- *ellipsis-middle* - replace characters from the middle with an ellipsis (…)

If no **title** was specified, if text requires truncation, a title containing the non-truncated text will be implicitly added.'''
    x: ChannelValueIntervalSpec
    '''The horizontal position of the text's anchor point, typically bound to the
*x* scale.'''
    y: ChannelValueSpec
    '''The vertical position channel specifying the text's anchor point, typically bound to the *y* scale.'''
    z: ChannelValue
    '''An optional ordinal channel for grouping data into series.'''
class _TickXOpen(MarkOptions,total=False):
    """The tickX mark."""
    inset: ParamRef | float
    '''Shorthand to set the same default for all four insets: **insetTop**,
**insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it.'''
    inset_bottom: ParamRef | float
    '''Insets the bottom edge by the specified number of pixels. A positive value insets towards the top edge (reducing effective area), while a negative value insets away from the top edge (increasing it).'''
    inset_top: ParamRef | float
    '''Insets the top edge by the specified number of pixels. A positive value insets towards the bottom edge (reducing effective area), while a negative value insets away from the bottom edge (increasing it).'''
    mark: Required[L['tickX']]
    '''A horizontally-positioned tickX mark (a vertical line, |). The **x** channel specifies the tick's horizontal position and defaults to identity, assuming that *data* = [*x₀*, *x₁*, *x₂*, …]; the optional **y** ordinal channel specifies its vertical position.

If *y* represents quantitative or temporal values, use a ruleX mark instead.'''
    marker: L['none'] | MarkerName | None | ParamRef | bool
    '''Shorthand to set the same default for markerStart, markerMid, and markerEnd; one of:

- a marker name such as *arrow* or *circle*
- *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_end: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the ending point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_mid: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for any middle (interior) points of a line segment. If the line segment only has a start and end point, this option has no effect. One of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*
* a function - a custom marker function; see below'''
    marker_start: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the starting point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    x: ChannelValueSpec
    '''The required horizontal position of the tick; a channel typically bound to the *x* scale.'''
    y: ChannelValueSpec
    '''The optional vertical position of the tick; an ordinal channel typically bound to the *y* scale. If not specified, the tick spans the vertical extent of the frame; otherwise the *y* scale must be a *band* scale.

If *y* represents quantitative or temporal values, use a ruleX mark instead.'''
class _TickYOpen(MarkOptions,total=False):
    """The tickY mark."""
    inset: ParamRef | float
    '''Shorthand to set the same default for all four insets: **insetTop**,
**insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it.'''
    inset_left: ParamRef | float
    '''Insets the left edge by the specified number of pixels. A positive value insets towards the right edge (reducing effective area), while a negative value insets away from the right edge (increasing it).'''
    inset_right: ParamRef | float
    '''Insets the right edge by the specified number of pixels. A positive value insets towards the left edge (reducing effective area), while a negative value insets away from the left edge (increasing it).'''
    mark: Required[L['tickY']]
    '''A vertically-positioned tickY mark (a horizontal line, —). The **y** channel specifies the tick's vertical position and defaults to identity, assuming that *data* = [*y₀*, *y₁*, *y₂*, …]; the optional **x** ordinal channel specifies its horizontal position.

If *x* represents quantitative or temporal values, use a ruleY mark instead.'''
    marker: L['none'] | MarkerName | None | ParamRef | bool
    '''Shorthand to set the same default for markerStart, markerMid, and markerEnd; one of:

- a marker name such as *arrow* or *circle*
- *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_end: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the ending point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_mid: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for any middle (interior) points of a line segment. If the line segment only has a start and end point, this option has no effect. One of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*
* a function - a custom marker function; see below'''
    marker_start: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the starting point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    x: ChannelValueSpec
    '''The optional horizontal position of the tick; an ordinal channel typically bound to the *x* scale. If not specified, the tick spans the horizontal extent of the frame; otherwise the *x* scale must be a *band* scale.

If *x* represents quantitative or temporal values, use a ruleY mark instead.'''
    y: ChannelValueSpec
    '''The required vertical position of the tick; a channel typically bound to the *y* scale.'''
class _VectorOpen(MarkOptions,total=False):
    """The vector mark."""
    anchor: L['end','middle','start'] | ParamRef
    '''The vector's position along its orientation relative to its anchor point; a constant. Assuming a default **rotate** angle of 0°, one of:

- *start* - from [*x*, *y*] to [*x*, *y* - *l*]
- *middle* (default) - from [*x*, *y* + *l* / 2] to [*x*, *y* - *l* / 2]
- *end* - from [*x*, *y* + *l*] to [*x*, *y*]

where [*x*, *y*] is the vector's anchor point and *l* is the vector's (possibly scaled) length in pixels.'''
    frame_anchor: FrameAnchor | ParamRef
    '''The vector's frame anchor, to default **x** and **y** relative to the frame; a constant representing one of the frame corners (*top-left*,
*top-right*, *bottom-right*, *bottom-left*), sides (*top*, *right*,
*bottom*, *left*), or *middle* (default). Has no effect if both **x** and **y** are specified.'''
    length: ChannelValueSpec
    '''The vector's length; either an optional channel bound to the *length* scale or a constant number in pixels. Defaults to 12 pixels.'''
    mark: Required[L['vector']]
    '''A vector mark.

If none of **frameAnchor**, **x**, and **y** are specified, then **x** and
**y** default to accessors assuming that *data* contains tuples [[*x₀*,
*y₀*], [*x₁*, *y₁*], [*x₂*, *y₂*], …]'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    r: ParamRef | float
    '''The vector shape's radius, such as half the width of the *arrow*'s head or the *spike*'s base; a constant number in pixels. Defaults to 3.5 pixels.'''
    rotate: ChannelValue
    '''The vector's orientation (rotation angle); either a constant number in degrees clockwise, or an optional channel (with no associated scale). Defaults to 0 degrees with the vector pointing up.'''
    shape: ParamRef | VectorShape
    '''The shape of the vector; a constant. Defaults to *arrow*.'''
    x: ChannelValueSpec
    '''The horizontal position of the vector's anchor point; an optional channel bound to the *x* scale. Default depends on the **frameAnchor**.'''
    y: ChannelValueSpec
    '''The vertical position of the vector's anchor point; an optional channel bound to the *y* scale. Default depends on the **frameAnchor**.'''
class _VectorXOpen(MarkOptions,total=False):
    """The vectorX mark."""
    anchor: L['end','middle','start'] | ParamRef
    '''The vector's position along its orientation relative to its anchor point; a constant. Assuming a default **rotate** angle of 0°, one of:

- *start* - from [*x*, *y*] to [*x*, *y* - *l*]
- *middle* (default) - from [*x*, *y* + *l* / 2] to [*x*, *y* - *l* / 2]
- *end* - from [*x*, *y* + *l*] to [*x*, *y*]

where [*x*, *y*] is the vector's anchor point and *l* is the vector's (possibly scaled) length in pixels.'''
    frame_anchor: FrameAnchor | ParamRef
    '''The vector's frame anchor, to default **x** and **y** relative to the frame; a constant representing one of the frame corners (*top-left*,
*top-right*, *bottom-right*, *bottom-left*), sides (*top*, *right*,
*bottom*, *left*), or *middle* (default). Has no effect if both **x** and **y** are specified.'''
    length: ChannelValueSpec
    '''The vector's length; either an optional channel bound to the *length* scale or a constant number in pixels. Defaults to 12 pixels.'''
    mark: Required[L['vectorX']]
    '''Like vector, but **x** instead defaults to the identity function and **y** defaults to null, assuming that *data* is an array of numbers [*x₀*, *x₁*,
*x₂*, …].'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    r: ParamRef | float
    '''The vector shape's radius, such as half the width of the *arrow*'s head or the *spike*'s base; a constant number in pixels. Defaults to 3.5 pixels.'''
    rotate: ChannelValue
    '''The vector's orientation (rotation angle); either a constant number in degrees clockwise, or an optional channel (with no associated scale). Defaults to 0 degrees with the vector pointing up.'''
    shape: ParamRef | VectorShape
    '''The shape of the vector; a constant. Defaults to *arrow*.'''
    x: ChannelValueSpec
    '''The horizontal position of the vector's anchor point; an optional channel bound to the *x* scale. Default depends on the **frameAnchor**.'''
    y: ChannelValueSpec
    '''The vertical position of the vector's anchor point; an optional channel bound to the *y* scale. Default depends on the **frameAnchor**.'''
class _VectorYOpen(MarkOptions,total=False):
    """The vectorY mark."""
    anchor: L['end','middle','start'] | ParamRef
    '''The vector's position along its orientation relative to its anchor point; a constant. Assuming a default **rotate** angle of 0°, one of:

- *start* - from [*x*, *y*] to [*x*, *y* - *l*]
- *middle* (default) - from [*x*, *y* + *l* / 2] to [*x*, *y* - *l* / 2]
- *end* - from [*x*, *y* + *l*] to [*x*, *y*]

where [*x*, *y*] is the vector's anchor point and *l* is the vector's (possibly scaled) length in pixels.'''
    frame_anchor: FrameAnchor | ParamRef
    '''The vector's frame anchor, to default **x** and **y** relative to the frame; a constant representing one of the frame corners (*top-left*,
*top-right*, *bottom-right*, *bottom-left*), sides (*top*, *right*,
*bottom*, *left*), or *middle* (default). Has no effect if both **x** and **y** are specified.'''
    length: ChannelValueSpec
    '''The vector's length; either an optional channel bound to the *length* scale or a constant number in pixels. Defaults to 12 pixels.'''
    mark: Required[L['vectorY']]
    '''Like vector, but **y** instead defaults to the identity function and **x** defaults to null, assuming that *data* is an array of numbers [*y₀*, *y₁*,
*y₂*, …].'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    r: ParamRef | float
    '''The vector shape's radius, such as half the width of the *arrow*'s head or the *spike*'s base; a constant number in pixels. Defaults to 3.5 pixels.'''
    rotate: ChannelValue
    '''The vector's orientation (rotation angle); either a constant number in degrees clockwise, or an optional channel (with no associated scale). Defaults to 0 degrees with the vector pointing up.'''
    shape: ParamRef | VectorShape
    '''The shape of the vector; a constant. Defaults to *arrow*.'''
    x: ChannelValueSpec
    '''The horizontal position of the vector's anchor point; an optional channel bound to the *x* scale. Default depends on the **frameAnchor**.'''
    y: ChannelValueSpec
    '''The vertical position of the vector's anchor point; an optional channel bound to the *y* scale. Default depends on the **frameAnchor**.'''
class _VoronoiMeshOpen(MarkOptions,total=False):
    """The voronoiMesh mark."""
    curve: Curve | ParamRef
    '''The curve (interpolation) method for connecting adjacent points. One of:

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
- *step-before* - a piecewise constant function where *x* changes after *y*'''
    mark: Required[L['voronoiMesh']]
    '''A mark that draws a mesh for the cell boundaries of the Voronoi tesselation of the points given by the **x** and **y** channels. The
**stroke** option defaults to _currentColor_, and the **strokeOpacity** defaults to 0.2. The **fill** option is not supported. When an aesthetic channel is specified (such as **stroke** or **strokeWidth**), the mesh inherits the corresponding channel value from one of its constituent points arbitrarily.

If **z** is specified, the input points are grouped by *z*, producing a separate Voronoi tesselation for each group.'''
    marker: L['none'] | MarkerName | None | ParamRef | bool
    '''Shorthand to set the same default for markerStart, markerMid, and markerEnd; one of:

- a marker name such as *arrow* or *circle*
- *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_end: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the ending point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_mid: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for any middle (interior) points of a line segment. If the line segment only has a start and end point, this option has no effect. One of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*
* a function - a custom marker function; see below'''
    marker_start: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the starting point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    tension: ParamRef | float
    '''The tension option only has an effect on bundle, cardinal and Catmull-Rom splines (*bundle*, *cardinal*, *cardinal-open*, *cardinal-closed*,
*catmull-rom*, *catmull-rom-open*, and *catmull-rom-closed*). For bundle splines, it corresponds to [beta][1]; for cardinal splines, [tension][2]; for Catmull-Rom splines, [alpha][3].

[1]: https://d3js.org/d3-shape/curve#curveBundle_beta [2]: https://d3js.org/d3-shape/curve#curveCardinal_tension [3]: https://d3js.org/d3-shape/curve#curveCatmullRom_alpha'''
    x: ChannelValueSpec
    '''The horizontal position channel, typically bound to the *x* scale.'''
    y: ChannelValueSpec
    '''The vertical position channel, typically bound to the *y* scale.'''
    z: ChannelValue
    '''An optional ordinal channel for grouping to produce multiple (possibly overlapping) triangulations.'''
class _VoronoiOpen(MarkOptions,total=False):
    """The voronoi mark."""
    curve: Curve | ParamRef
    '''The curve (interpolation) method for connecting adjacent points. One of:

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
- *step-before* - a piecewise constant function where *x* changes after *y*'''
    mark: Required[L['voronoi']]
    '''A mark that draws polygons for each cell of the Voronoi tesselation of the points given by the **x** and **y** channels.

If **z** is specified, the input points are grouped by *z*, producing a separate Voronoi tesselation for each group.'''
    marker: L['none'] | MarkerName | None | ParamRef | bool
    '''Shorthand to set the same default for markerStart, markerMid, and markerEnd; one of:

- a marker name such as *arrow* or *circle*
- *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_end: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the ending point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    marker_mid: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for any middle (interior) points of a line segment. If the line segment only has a start and end point, this option has no effect. One of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*
* a function - a custom marker function; see below'''
    marker_start: L['none'] | MarkerName | None | ParamRef | bool
    '''The marker for the starting point of a line segment; one of:

- a marker name such as *arrow* or *circle*
* *none* (default) - no marker
* true - alias for *circle-fill*
* false or null - alias for *none*'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    tension: ParamRef | float
    '''The tension option only has an effect on bundle, cardinal and Catmull-Rom splines (*bundle*, *cardinal*, *cardinal-open*, *cardinal-closed*,
*catmull-rom*, *catmull-rom-open*, and *catmull-rom-closed*). For bundle splines, it corresponds to [beta][1]; for cardinal splines, [tension][2]; for Catmull-Rom splines, [alpha][3].

[1]: https://d3js.org/d3-shape/curve#curveBundle_beta [2]: https://d3js.org/d3-shape/curve#curveCardinal_tension [3]: https://d3js.org/d3-shape/curve#curveCatmullRom_alpha'''
    x: ChannelValueSpec
    '''The horizontal position channel, typically bound to the *x* scale.'''
    y: ChannelValueSpec
    '''The vertical position channel, typically bound to the *y* scale.'''
    z: ChannelValue
    '''An optional ordinal channel for grouping to produce multiple (possibly overlapping) triangulations.'''
class _WaffleXOpen(MarkOptions,total=False):
    """The waffleX mark."""
    gap: ParamRef | float
    '''The gap in pixels between cells; defaults to 1.'''
    inset: ParamRef | float
    '''Shorthand to set the same default for all four insets: **insetTop**,
**insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it.'''
    inset_bottom: ParamRef | float
    '''Insets the bottom edge by the specified number of pixels. A positive value insets towards the top edge (reducing effective area), while a negative value insets away from the top edge (increasing it).'''
    inset_left: ParamRef | float
    '''Insets the left edge by the specified number of pixels. A positive value insets towards the right edge (reducing effective area), while a negative value insets away from the right edge (increasing it).'''
    inset_right: ParamRef | float
    '''Insets the right edge by the specified number of pixels. A positive value insets towards the left edge (reducing effective area), while a negative value insets away from the left edge (increasing it).'''
    inset_top: ParamRef | float
    '''Insets the top edge by the specified number of pixels. A positive value insets towards the bottom edge (reducing effective area), while a negative value insets away from the bottom edge (increasing it).'''
    interval: Interval | ParamRef
    '''How to convert a continuous value (**x** for barX, or **y** for barY) into an interval (**x1** and **x2** for barX, or **y1** and **y2** for barY); one of:

- a named time interval such as *day* (for date intervals)
- a number (for number intervals), defining intervals at integer multiples of *n*

Setting this option disables the implicit stack transform (stackX for barX, or stackY for barY).'''
    mark: Required[L['waffleX']]
    '''A horizontal waffle mark. The required *x* values should be quantitative, and the optional *y* values should be ordinal.

If neither **x1** nor **x2** nor **interval** is specified, an implicit stackX transform is applied and **x** defaults to the identity function, assuming that *data* = [*x₀*, *x₁*, *x₂*, …]. Otherwise if an **interval** is specified, then **x1** and **x2** are derived from **x**, representing the lower and upper bound of the containing interval, respectively. Otherwise, if only one of **x1** or **x2** is specified, the other defaults to **x**, which defaults to zero.

The optional **y** ordinal channel specifies the vertical position; it is typically bound to the *y* scale, which must be a *band* scale. If the
**y** channel is not specified, the bar will span the vertical extent of the plot's frame. Because a waffle represents a discrete number of square cells, it may not use all of the available bandwidth.'''
    multiple: ParamRef | float
    '''The number of cells per row or column; defaults to undefined for automatic.'''
    offset: None | ParamRef | StackOffset
    '''After stacking, an optional **offset** can be applied to translate and scale stacks, say to produce a streamgraph; defaults to null for a zero baseline (**y** = 0 for stackY, and **x** = 0 for stackX). If the *wiggle* offset is used, the default **order** changes to *inside-out*.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    order: None | ParamRef | StackOrder
    '''The order in which stacks are layered; one of:

- null (default) for input order
- a named stack order method such as *inside-out* or *sum*
- a field name, for natural order of the corresponding values
- a function of data, for natural order of the corresponding values
- an array of explicit **z** values in the desired order

If the *wiggle* **offset** is used, as for a streamgraph, the default changes to *inside-out*.'''
    round: ParamRef | bool
    '''If true, round to integers to avoid partial cells.'''
    rx: ParamRef | float | str
    '''The rounded corner [*x*-radius][1], either in pixels or as a percentage of the rect width. If **rx** is not specified, it defaults to **ry** if present, and otherwise draws square corners.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/rx'''
    ry: ParamRef | float | str
    '''The rounded corner [*y*-radius][1], either in pixels or as a percentage of the rect height. If **ry** is not specified, it defaults to **rx** if present, and otherwise draws square corners.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/ry'''
    unit: ParamRef | float
    '''The quantity each cell represents; defaults to 1.'''
    x: ChannelValueIntervalSpec
    '''The horizontal position (or length/width) channel, typically bound to the
*x* scale.

If neither **x1** nor **x2** nor **interval** is specified, an implicit stackX transform is applied and **x** defaults to the identity function, assuming that *data* = [*x₀*, *x₁*, *x₂*, …]. Otherwise if an **interval** is specified, then **x1** and **x2** are derived from **x**, representing the lower and upper bound of the containing interval, respectively. Otherwise, if only one of **x1** or **x2** is specified, the other defaults to **x**, which defaults to zero.'''
    x1: ChannelValueSpec
    '''The required primary (starting, often left) horizontal position channel, typically bound to the *x* scale. Setting this option disables the implicit stackX transform.

If *x* represents ordinal values, use a cell mark instead.'''
    x2: ChannelValueSpec
    '''The required secondary (ending, often right) horizontal position channel, typically bound to the *x* scale. Setting this option disables the implicit stackX transform.

If *x* represents ordinal values, use a cell mark instead.'''
    y: ChannelValueSpec
    '''The optional vertical position of the bar; a ordinal channel typically bound to the *y* scale. If not specified, the bar spans the vertical extent of the frame; otherwise the *y* scale must be a *band* scale.

If *y* represents quantitative or temporal values, use a rectX mark instead.'''
    z: ChannelValue
    '''The **z** channel defines the series of each value in the stack. Used when the **order** is *sum*, *appearance*, *inside-out*, or an explicit array of
**z** values.'''
class _WaffleYOpen(MarkOptions,total=False):
    """The waffleY mark."""
    gap: ParamRef | float
    '''The gap in pixels between cells; defaults to 1.'''
    inset: ParamRef | float
    '''Shorthand to set the same default for all four insets: **insetTop**,
**insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it.'''
    inset_bottom: ParamRef | float
    '''Insets the bottom edge by the specified number of pixels. A positive value insets towards the top edge (reducing effective area), while a negative value insets away from the top edge (increasing it).'''
    inset_left: ParamRef | float
    '''Insets the left edge by the specified number of pixels. A positive value insets towards the right edge (reducing effective area), while a negative value insets away from the right edge (increasing it).'''
    inset_right: ParamRef | float
    '''Insets the right edge by the specified number of pixels. A positive value insets towards the left edge (reducing effective area), while a negative value insets away from the left edge (increasing it).'''
    inset_top: ParamRef | float
    '''Insets the top edge by the specified number of pixels. A positive value insets towards the bottom edge (reducing effective area), while a negative value insets away from the bottom edge (increasing it).'''
    interval: Interval | ParamRef
    '''How to convert a continuous value (**x** for barX, or **y** for barY) into an interval (**x1** and **x2** for barX, or **y1** and **y2** for barY); one of:

- a named time interval such as *day* (for date intervals)
- a number (for number intervals), defining intervals at integer multiples of *n*

Setting this option disables the implicit stack transform (stackX for barX, or stackY for barY).'''
    mark: Required[L['waffleY']]
    '''A vertical waffle mark. The required *y* values should be quantitative, and the optional *x* values should be ordinal.

If neither **y1** nor **y2** nor **interval** is specified, an implicit stackY transform is applied and **y** defaults to the identity function, assuming that *data* = [*y₀*, *y₁*, *y₂*, …]. Otherwise if an **interval** is specified, then **y1** and **y2** are derived from **y**, representing the lower and upper bound of the containing interval, respectively. Otherwise, if only one of **y1** or **y2** is specified, the other defaults to **y**, which defaults to zero.

The optional **x** ordinal channel specifies the horizontal position; it is typically bound to the *x* scale, which must be a *band* scale. If the
**x** channel is not specified, the bar will span the horizontal extent of the plot's frame. Because a waffle represents a discrete number of square cells, it may not use all of the available bandwidth.'''
    multiple: ParamRef | float
    '''The number of cells per row or column; defaults to undefined for automatic.'''
    offset: None | ParamRef | StackOffset
    '''After stacking, an optional **offset** can be applied to translate and scale stacks, say to produce a streamgraph; defaults to null for a zero baseline (**y** = 0 for stackY, and **x** = 0 for stackX). If the *wiggle* offset is used, the default **order** changes to *inside-out*.'''
    opacity: ChannelValueSpec
    '''The [opacity][1]; a constant between 0 and 1, or a channel typically bound to the *opacity* scale. If all channel values are numbers in [0, 1], by default the channel will not be bound to the *opacity* scale, interpreting the opacities literally. For faster rendering, prefer the **strokeOpacity** or **fillOpacity** option.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/opacity'''
    order: None | ParamRef | StackOrder
    '''The order in which stacks are layered; one of:

- null (default) for input order
- a named stack order method such as *inside-out* or *sum*
- a field name, for natural order of the corresponding values
- a function of data, for natural order of the corresponding values
- an array of explicit **z** values in the desired order

If the *wiggle* **offset** is used, as for a streamgraph, the default changes to *inside-out*.'''
    round: ParamRef | bool
    '''If true, round to integers to avoid partial cells.'''
    rx: ParamRef | float | str
    '''The rounded corner [*x*-radius][1], either in pixels or as a percentage of the rect width. If **rx** is not specified, it defaults to **ry** if present, and otherwise draws square corners.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/rx'''
    ry: ParamRef | float | str
    '''The rounded corner [*y*-radius][1], either in pixels or as a percentage of the rect height. If **ry** is not specified, it defaults to **rx** if present, and otherwise draws square corners.

[1]: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/ry'''
    unit: ParamRef | float
    '''The quantity each cell represents; defaults to 1.'''
    x: ChannelValueSpec
    '''The optional horizontal position of the bar; a ordinal channel typically bound to the *x* scale. If not specified, the bar spans the horizontal extent of the frame; otherwise the *x* scale must be a *band* scale.

If *x* represents quantitative or temporal values, use a rectY mark instead.'''
    y: ChannelValueIntervalSpec
    '''The vertical position (or length/height) channel, typically bound to the
*y* scale.

If neither **y1** nor **y2** nor **interval** is specified, an implicit stackY transform is applied and **y** defaults to the identity function, assuming that *data* = [*y₀*, *y₁*, *y₂*, …]. Otherwise if an **interval** is specified, then **y1** and **y2** are derived from **y**, representing the lower and upper bound of the containing interval, respectively. Otherwise, if only one of **y1** or **y2** is specified, the other defaults to **y**, which defaults to zero.'''
    y1: ChannelValueSpec
    '''The required primary (starting, often bottom) vertical position channel, typically bound to the *y* scale. Setting this option disables the implicit stackY transform.

If *y* represents ordinal values, use a cell mark instead.'''
    y2: ChannelValueSpec
    '''The required secondary (ending, often top) horizontal position channel, typically bound to the *y* scale. Setting this option disables the implicit stackY transform.

If *y* represents ordinal values, use a cell mark instead.'''
    z: ChannelValue
    '''The **z** channel defines the series of each value in the stack. Used when the **order** is *sum*, *appearance*, *inside-out*, or an explicit array of
**z** values.'''
class Area(_AreaOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class AreaX(_AreaXOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class AreaY(_AreaYOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class Arrow(_ArrowOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class AxisFx(_AxisFxOpen,total=False,closed=True):...
class AxisFy(_AxisFyOpen,total=False,closed=True):...
class AxisX(_AxisXOpen,total=False,closed=True):...
class AxisY(_AxisYOpen,total=False,closed=True):...
class BarX(_BarXOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class BarY(_BarYOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class Cell(_CellOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class CellX(_CellXOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class CellY(_CellYOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class Circle(_CircleOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class Contour(_ContourOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class DelaunayLink(_DelaunayLinkOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class DelaunayMesh(_DelaunayMeshOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class DenseLine(_DenseLineOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class Density(_DensityOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class DensityXAreaX(_DensityXAreaXOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class DensityXDotX(_DensityXDotXOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class DensityXLineX(_DensityXLineXOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class DensityXTextX(_DensityXTextXOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class DensityYAreaY(_DensityYAreaYOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class DensityYDot(_DensityYDotOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class DensityYLineY(_DensityYLineYOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class DensityYText(_DensityYTextOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class Dot(_DotOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class DotX(_DotXOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class DotY(_DotYOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class ErrorBarX(_ErrorBarXOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class ErrorBarY(_ErrorBarYOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class Frame(_FrameOpen,total=False,closed=True):...
class Geo(_GeoOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class Graticule(_GraticuleOpen,total=False,closed=True):...
class GridFx(_GridFxOpen,total=False,closed=True):...
class GridFy(_GridFyOpen,total=False,closed=True):...
class GridX(_GridXOpen,total=False,closed=True):...
class GridY(_GridYOpen,total=False,closed=True):...
class Heatmap(_HeatmapOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class Hexagon(_HexagonOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class Hexbin(_HexbinOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class Hexgrid(_HexgridOpen,total=False,closed=True):...
class Hull(_HullOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class Image(_ImageOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class Line(_LineOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class LineX(_LineXOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class LineY(_LineYOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class Link(_LinkOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class Raster(_RasterOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class RasterTile(_RasterTileOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class Rect(_RectOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class RectX(_RectXOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class RectY(_RectYOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class RegressionY(_RegressionYOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class RuleX(_RuleXOpen,total=False,closed=True):
    data: PlotMarkData
    '''The data source for the mark.'''
class RuleY(_RuleYOpen,total=False,closed=True):
    data: PlotMarkData
    '''The data source for the mark.'''
class Sphere(_SphereOpen,total=False,closed=True):...
class Spike(_SpikeOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class Text(_TextOpen,total=False,closed=True):
    data: PlotMarkData
    '''The data source for the mark.'''
class TextX(_TextXOpen,total=False,closed=True):
    data: PlotMarkData
    '''The data source for the mark.'''
class TextY(_TextYOpen,total=False,closed=True):
    data: PlotMarkData
    '''The data source for the mark.'''
class TickX(_TickXOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class TickY(_TickYOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class Vector(_VectorOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class VectorX(_VectorXOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class VectorY(_VectorYOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class VoronoiMesh(_VoronoiMeshOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class Voronoi(_VoronoiOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class WaffleX(_WaffleXOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
class WaffleY(_WaffleYOpen,total=False,closed=True):
    data: Required[PlotMarkData]
    '''The data source for the mark.'''
PlotMark = TypeAliasType('PlotMark', Area | AreaX | AreaY | Arrow | AxisFx | AxisFy | AxisX | AxisY | BarX | BarY | Cell | CellX | CellY | Circle | Contour | DelaunayLink | DelaunayMesh | DenseLine | Density | DensityXAreaX | DensityXDotX | DensityXLineX | DensityXTextX | DensityYAreaY | DensityYDot | DensityYLineY | DensityYText | Dot | DotX | DotY | ErrorBarX | ErrorBarY | Frame | Geo | Graticule | GridFx | GridFy | GridX | GridY | Heatmap | Hexagon | Hexbin | Hexgrid | Hull | Image | Line | LineX | LineY | Link | Raster | RasterTile | Rect | RectX | RectY | RegressionY | RuleX | RuleY | Sphere | Spike | Text | TextX | TextY | TickX | TickY | Vector | VectorX | VectorY | Voronoi | VoronoiMesh | WaffleX | WaffleY)
'''A plot mark entry.'''


__all__ = ("Area","AreaX","AreaY","Arrow","AxisFx","AxisFy","AxisX","AxisY","BarX","BarY","Cell","CellX","CellY","ChannelDomainSort","ChannelDomainValueSpec","ChannelDomainValueSpec1","ChannelValue","ChannelValueIntervalSpec","ChannelValueIntervalSpec1","ChannelValueSpec","ChannelValueSpec1","Circle","Contour","DelaunayLink","DelaunayMesh","DenseLine","Density","DensityXAreaX","DensityXDotX","DensityXLineX","DensityXTextX","DensityYAreaY","DensityYDot","DensityYLineY","DensityYText","Dot","DotX","DotY","ErrorBarX","ErrorBarY","Format","Frame","Geo","Graticule","GridFx","GridFy","GridX","GridY","Heatmap","Hexagon","Hexbin","Hexgrid","Hull","Image","Line","LineX","LineY","Link","MarkOptions","PlotMark","Raster","RasterTile","Rect","RectX","RectY","RegressionY","RuleX","RuleY","SortOrder","SortOrder1","SortOrder2","Sphere","Spike","Text","TextX","TextY","TickX","TickY","Tip","Vector","VectorX","VectorY","Voronoi","VoronoiMesh","WaffleX","WaffleY",)
