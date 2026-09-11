# Generated: `mosaic_spec._gen.typing`
from __future__ import annotations

from collections.abc import Mapping
from collections.abc import Sequence
from mosaic_spec._typing_compat import TypeAliasType
from typing import Any
from typing import Literal as L

ChannelName = TypeAliasType('ChannelName', L['ariaLabel','fill','fillOpacity','fontSize','fx','fy','geometry','height','href','length','opacity','path','r','rotate','src','stroke','strokeOpacity','strokeWidth','symbol','text','title','weight','width','x','x1','x2','y','y1','y2','z'])
'''The set of known channel names.'''
ColorScaleType = TypeAliasType('ColorScaleType', L['band','categorical','cyclical','diverging','diverging-log','diverging-pow','diverging-sqrt','diverging-symlog','identity','linear','log','ordinal','point','pow','quantile','quantize','sequential','sqrt','symlog','threshold','time','utc'])
'''The supported scale types for *color* encodings.

For quantitative data, one of:

- *linear* (default) - linear transform (translate and scale)
- *pow* - power (exponential) transform
- *sqrt* - square-root transform; *pow* with *exponent* = 0.5
- *log* - logarithmic transform
- *symlog* - bi-symmetric logarithmic transform per Webber et al.

For temporal data, one of:

- *utc* (default, recommended) - UTC time
- *time* - local time

For ordinal data, one of:

- *ordinal* - from discrete inputs to discrete outputs

For color, one of:

- *categorical* - equivalent to *ordinal*; defaults to *observable10*
- *sequential* - equivalent to *linear*; defaults to *turbo*
- *cyclical* - equivalent to *linear*; defaults to *rainbow*
- *threshold* - encodes using discrete thresholds; defaults to *rdylbu*
- *quantile* - encodes using quantile thresholds; defaults to *rdylbu*
- *quantize* - uniformly quantizes a continuous domain; defaults to *rdylbu*
- *diverging* - *linear*, but with a pivot; defaults to *rdbu*
- *diverging-log* - *log*, but with a pivot; defaults to *rdbu*
- *diverging-pow* - *pow*, but with a pivot; defaults to *rdbu*
- *diverging-sqrt* - *sqrt*, but with a pivot; defaults to *rdbu*
- *diverging-symlog* - *symlog*, but with a pivot; defaults to *rdbu*

Other scale types:

- *identity* - do not transform values when encoding'''
ColorScheme = TypeAliasType('ColorScheme', L['Accent','Blues','BrBG','BuGn','BuPu','BuRd','BuYlRd','Category10','Cividis','Cool','Cubehelix','Dark2','GnBu','Greens','Greys','Inferno','Magma','Observable10','OrRd','Oranges','PRGn','Paired','Pastel1','Pastel2','PiYG','Plasma','PuBu','PuBuGn','PuOr','PuRd','Purples','Rainbow','RdBu','RdGy','RdPu','RdYlBu','RdYlGn','Reds','Set1','Set2','Set3','Sinebow','Spectral','Tableau10','Turbo','Viridis','Warm','YlGn','YlGnBu','YlOrBr','YlOrRd'] | Mapping[str, Any])
'''The built-in color schemes. For categorical data, one of:

- *Accent* - eight colors
- *Category10* - ten colors
- *Dark2* - eight colors
- *Observable10* (default) - ten colors
- *Paired* - twelve paired colors
- *Pastel1* - nine colors
- *Pastel2* - eight colors
- *Set1* - nine colors
- *Set2* - eight colors
- *Set3* - twelve colors
- *Tableau10* - ten colors

For diverging data, one of:

- *BrBG* - from brown to white to blue-green
- *PRGn* - from purple to white to green
- *PiYG* - from pink to white to yellow-green
- *PuOr* - from purple to white to orange
- *RdBu* (default) - from red to white to blue
- *RdGy* - from red to white to gray
- *RdYlBu* - from red to yellow to blue
- *RdYlGn* - from red to yellow to green
- *Spectral* - from red to blue, through the spectrum
- *BuRd* - from blue to white to red
- *BuYlRd* - from blue to yellow to red

For sequential data, one of:

- *Blues* - from white to blue
- *Greens* - from white to green
- *Greys* - from white to gray
- *Oranges* - from white to orange
- *Purples* - from white to purple
- *Reds* - from white to red
- *Turbo* (default) - from blue to red, through the spectrum
- *Viridis* - from blue to green to yellow
- *Magma* - from purple to orange to yellow
- *Inferno* - from purple to orange to yellow
- *Plasma* - from purple to orange to yellow
- *Cividis* - from blue to yellow
- *Cubehelix* - from black to white, rotating hue
- *Warm* - from purple to green, through warm hues
- *Cool* - from green to to purple, through cool hues
- *BuGn* - from light blue to dark green
- *BuPu* - from light blue to dark purple
- *GnBu* - from light green to dark blue
- *OrRd* - from light orange to dark red
- *PuBu* - from light purple to dark blue
- *PuBuGn* - from light purple to blue to dark green
- *PuRd* - from light purple to dark red
- *RdPu* - from light red to dark purple
- *YlGn* - from light yellow to dark green
- *YlGnBu* - from light yellow to green to dark blue
- *YlOrBr* - from light yellow to orange to dark brown
- *YlOrRd* - from light yellow to orange to dark red

For cyclical data, one of:

- *Rainbow* (default) - the less-angry rainbow color scheme
- *Sinebow* - Bumgardner and Loyd's “sinebow” scheme'''
ContinuousScaleType = TypeAliasType('ContinuousScaleType', L['identity','linear','log','pow','sqrt','symlog','time','utc'])
'''The supported scale types for continuous encoding channels.

For quantitative data, one of:

- *linear* (default) - linear transform (translate and scale)
- *pow* - power (exponential) transform
- *sqrt* - square-root transform; *pow* with *exponent* = 0.5
- *log* - logarithmic transform
- *symlog* - bi-symmetric logarithmic transform per Webber et al.

For temporal data, one of:

- *utc* (default, recommended) - UTC time
- *time* - local time

Other scale types:

- *identity* - do not transform values when encoding'''
Curve = TypeAliasType('Curve', L['basis','basis-closed','basis-open','bump-x','bump-y','bundle','cardinal','cardinal-closed','cardinal-open','catmull-rom','catmull-rom-closed','catmull-rom-open','linear','linear-closed','monotone-x','monotone-y','natural','step','step-after','step-before'])
'''How to interpolate between control points.'''
DiscreteScaleType = TypeAliasType('DiscreteScaleType', L['identity','ordinal'])
'''The supported scale types for discrete encoding channels. One of:

- *ordinal* - from discrete inputs to discrete outputs
- *identity* - do not transform values when encoding'''
Fixed = TypeAliasType('Fixed', L['Fixed'])
'''A symbol indicating a fixed scale domain. A fixed domain is initially determined from data as usual, but subsequently "fixed" so that it does not change over subsequent interactive filtering, ensring stable comparisons.'''
FrameAnchor = TypeAliasType('FrameAnchor', L['bottom','bottom-left','bottom-right','left','middle','right','top','top-left','top-right'])
'''How to anchor a mark relative to the plot's frame; one of:

- *middle* - centered in the middle
- in the middle of one of the edges: *top*, *right*, *bottom*, *left*
- in one of the corners: *top-left*, *top-right*, *bottom-right*, *bottom-left*'''
GridInterpolate = TypeAliasType('GridInterpolate', L['barycentric','linear','nearest','none','random-walk'])
'''A spatial interpolation method; one of:

- *none* - do not perform interpolation (the default), maps samples to single bins
- *linear* - apply proportional linear interpolation across adjacent bins
- *nearest* - assign each pixel to the closest sample's value (Voronoi diagram)
- *barycentric* - apply barycentric interpolation over the Delaunay triangulation
- *random-walk* - apply a random walk from each pixel, stopping when near a sample'''
Interpolate = TypeAliasType('Interpolate', L['hcl','hsl','lab','number','rgb'])
'''How to interpolate range (output) values for continuous scales; one of:

- *number* - linear numeric interpolation
- *rgb* - red, green, blue (sRGB)
- *hsl* - hue, saturation, lightness (HSL; cylindrical sRGB)
- *hcl* - hue, chroma, perceptual lightness (CIELCh_ab; cylindrical CIELAB)
- *lab* - perceptual lightness and opponent colors (L\*a\*b\*, CIELAB)'''
TimeIntervalName = TypeAliasType('TimeIntervalName', L['day','friday','half','hour','minute','monday','month','quarter','saturday','second','sunday','thursday','tuesday','wednesday','week','year'])
'''The built-in time intervals; UTC or local time, depending on context. The
*week* interval is an alias for *sunday*. The *quarter* interval is every three months, and the *half* interval is every six months, aligned at the start of the year.'''
LabelArrow = TypeAliasType('LabelArrow', L['auto','down','left','none','right','up',False,None,True])
MarkerName = TypeAliasType('MarkerName', L['arrow','arrow-reverse','circle','circle-fill','circle-stroke','dot','tick','tick-x','tick-y'])
'''The built-in marker implementations; one of:

- *arrow* - an arrowhead with *auto* orientation
- *arrow-reverse* - an arrowhead with *auto-start-reverse* orientation
- *dot* - a filled *circle* with no stroke and 2.5px radius
- *circle-fill* - a filled circle with a white stroke and 3px radius
- *circle-stroke* - a stroked circle with a white fill and 3px radius
- *circle* - alias for *circle-fill*
- *tick* - a small opposing line
- *tick-x* - a small horizontal line
- *tick-y* - a small vertical line'''
PositionScaleType = TypeAliasType('PositionScaleType', L['band','identity','linear','log','point','pow','quantile','quantize','sqrt','symlog','threshold','time','utc'])
'''The supported scale types for *x* and *y* position encodings.

For quantitative data, one of:

- *linear* (default) - linear transform (translate and scale)
- *pow* - power (exponential) transform
- *sqrt* - square-root transform; *pow* with *exponent* = 0.5
- *log* - logarithmic transform
- *symlog* - bi-symmetric logarithmic transform per Webber et al.

For temporal data, one of:

- *utc* (default, recommended) - UTC time
- *time* - local time

For ordinal data, one of:

- *point* (for position only) - divide a continuous range into discrete points
- *band* (for position only) - divide a continuous range into discrete points

Other scale types:

- *identity* - do not transform values when encoding'''
ProjectionName = TypeAliasType('ProjectionName', L['albers','albers-usa','azimuthal-equal-area','azimuthal-equidistant','conic-conformal','conic-equal-area','conic-equidistant','equal-earth','equirectangular','gnomonic','identity','mercator','orthographic','reflect-y','stereographic','transverse-mercator'])
'''The built-in projection implementations; one of:

- *albers-usa* - a U.S.-centric composite projection with insets for Alaska and Hawaii
- *albers* - a U.S.-centric *conic-equal-area* projection
- *azimuthal-equal-area* - the azimuthal equal-area projection
- *azimuthal-equidistant* - the azimuthal equidistant projection
- *conic-conformal* - the conic conformal projection
- *conic-equal-area* - the conic equal-area projection
- *conic-equidistant* - the conic equidistant projection
- *equal-earth* - the Equal Earth projection Šavrič et al., 2018
- *equirectangular* - the equirectangular (plate carrée) projection
- *gnomonic* - the gnomonic projection
- *identity* - the identity projection
- *reflect-y* - the identity projection, but flipping *y*
- *mercator* - the spherical Mercator projection
- *orthographic* - the orthographic projection
- *stereographic* - the stereographic projection
- *transverse-mercator* - the transverse spherical Mercator projection'''
ReducerPercentile = TypeAliasType('ReducerPercentile', L['p00','p01','p02','p03','p04','p05','p06','p07','p08','p09','p10','p11','p12','p13','p14','p15','p16','p17','p18','p19','p20','p21','p22','p23','p24','p25','p26','p27','p28','p29','p30','p31','p32','p33','p34','p35','p36','p37','p38','p39','p40','p41','p42','p43','p44','p45','p46','p47','p48','p49','p50','p51','p52','p53','p54','p55','p56','p57','p58','p59','p60','p61','p62','p63','p64','p65','p66','p67','p68','p69','p70','p71','p72','p73','p74','p75','p76','p77','p78','p79','p80','p81','p82','p83','p84','p85','p86','p87','p88','p89','p90','p91','p92','p93','p94','p95','p96','p97','p98','p99'])
ScaleName = TypeAliasType('ScaleName', L['color','fx','fy','length','opacity','r','symbol','x','y'])
'''The built-in scale names; one of:

- *x* - horizontal position
- *y* - vertical position
- *fx* - horizontal facet position
- *fy* - vertical facet position
- *r* - radius (for dots and point geos)
- *color* - color
- *opacity* - opacity
- *symbol* - categorical symbol (for dots)
- *length* - length (for vectors)

Position scales may have associated axes. Color, opacity, and symbol scales may have an associated legend.'''
SelectFilter = TypeAliasType('SelectFilter', L['first','last','maxX','maxY','minX','minY','nearest','nearestX','nearestY'])
'''Selection filters to apply internally to mark data.'''
StackOffset = TypeAliasType('StackOffset', L['center','normalize','wiggle'])
'''A stack offset method; one of:

- *normalize* - rescale each stack to fill [0, 1]
- *center* - align the centers of all stacks
- *wiggle* - translate stacks to minimize apparent movement

If a given stack has zero total value, the *normalize* offset will not adjust the stack's position. Both the *center* and *wiggle* offsets ensure that the lowest element across stacks starts at zero for better default axes. The
*wiggle* offset is recommended for streamgraphs in conjunction with the
*inside-out* order. For more, see [Byron & Wattenberg][1].

[1]: https://leebyron.com/streamgraph/'''
StackOrderName = TypeAliasType('StackOrderName', L['appearance','inside-out','sum','value','x','y','z'])
'''The built-in stack order methods; one of:

- *x* - alias of *value*; for stackX only
- *y* - alias of *value*; for stackY only
- *value* - ascending value (or descending with **reverse**)
- *sum* - total value per series
- *appearance* - position of maximum value per series
- *inside-out* (default with *wiggle*) - order the earliest-appearing series on the inside

The *inside-out* order is recommended for streamgraphs in conjunction with the *wiggle* offset. For more, see [Byron & Wattenberg][1].

[1]: https://leebyron.com/streamgraph/'''
SymbolType = TypeAliasType('SymbolType', L['asterisk','circle','cross','diamond','diamond2','hexagon','plus','square','square2','star','times','triangle','triangle2','wye'])
'''The built-in symbol implementations. For fill, one of:

- *circle* - a circle
- *cross* - a Greek cross with arms of equal length
- *diamond* - a rhombus
- *square* - a square
- *star* - a pentagonal star (pentagram)
- *triangle* - an up-pointing triangle
- *wye* - a Y with arms of equal length

For stroke (based on [Heman Robinson's research][1]), one of:

- *circle* - a circle
- *plus* - a plus sign
- *times* - an X with arms of equal length
- *triangle2* - an (alternate) up-pointing triangle
- *asterisk* - an asterisk
- *square2* - a (alternate) square
- *diamond2* - a rotated square

The *hexagon* symbol is also supported.

[1]: https://www.tandfonline.com/doi/abs/10.1080/10618600.2019.1637746'''
TipPointer = TypeAliasType('TipPointer', L['x','xy','y'])
'''The pointer mode for the tip; corresponds to pointerX, pointerY, and pointer.'''
VectorShape = TypeAliasType('VectorShape', L['arrow','spike'])
'''The built-in vector shape implementations; one of:

- *arrow* - a straight line with an open arrowhead at the end (↑)
- *spike* - an isosceles triangle with a flat base (▲)'''
ChannelDomainValue = TypeAliasType('ChannelDomainValue', ChannelName | L['data','height','width'] | L['-ariaLabel','-data','-fill','-fillOpacity','-fontSize','-fx','-fy','-geometry','-height','-href','-length','-opacity','-path','-r','-rotate','-src','-stroke','-strokeOpacity','-strokeWidth','-symbol','-text','-title','-weight','-width','-x','-x1','-x2','-y','-y1','-y2','-z'] | None)
'''The available inputs for imputing scale domains. In addition to a named channel, an input may be specified as:

- *data* - impute from mark data
- *width* - impute from |*x2* - *x1*|
- *height* - impute from |*y2* - *y1*|
- null - impute from input order

If the *x* channel is not defined, the *x2* channel will be used instead if available, and similarly for *y* and *y2*; this is useful for marks that implicitly stack. The *data* input is typically used in conjunction with a custom **reduce** function, as when the built-in single-channel reducers are insufficient.'''
Interval = TypeAliasType('Interval', L['10 years','3 months','days','fridays','halfs','hours','minutes','mondays','months','quarters','saturdays','seconds','sundays','thursdays','tuesdays','wednesdays','weeks','years'] | TimeIntervalName | str)
'''How to partition a continuous range into discrete intervals; one of:

- a named time interval such as *day* (for date intervals)
- a number (for number intervals), defining intervals at integer multiples of *n*'''
Reducer = TypeAliasType('Reducer', L['count','deviation','distinct','first','identity','last','max','max-index','mean','median','min','min-index','mode','proportion','proportion-facet','sum','variance'] | ReducerPercentile)
'''How to reduce aggregated (binned or grouped) values; one of:

- *first* - the first value, in input order
- *last* - the last value, in input order
- *count* - the number of elements (frequency)
- *distinct* - the number of distinct values
- *sum* - the sum of values
- *proportion* - the sum proportional to the overall total (weighted frequency)
- *proportion-facet* - the sum proportional to the facet total
- *deviation* - the standard deviation
- *min* - the minimum value
- *min-index* - the zero-based index of the minimum value
- *max* - the maximum value
- *max-index* - the zero-based index of the maximum value
- *mean* - the mean value (average)
- *median* - the median value
- *variance* - the variance per [Welford's algorithm][1]
- *mode* - the value with the most occurrences
- *pXX* - the percentile value, where XX is a number in [00,99]
- *identity* - the array of values

[1]: https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Welford's_online_algorithm'''
StackOrder = TypeAliasType('StackOrder', L['-appearance','-inside-out','-sum','-value','-x','-y','-z'] | Sequence[Any] | StackOrderName | str)
'''How to order layers prior to stacking; one of:

- a named stack order method such as *inside-out* or *sum*
- a field name, for natural order of the corresponding values
- an array of explicit **z** values in the desired order'''


__all__ = ("ChannelDomainValue","ChannelName","ColorScaleType","ColorScheme","ContinuousScaleType","Curve","DiscreteScaleType","Fixed","FrameAnchor","GridInterpolate","Interpolate","Interval","LabelArrow","MarkerName","PositionScaleType","ProjectionName","Reducer","ReducerPercentile","ScaleName","SelectFilter","StackOffset","StackOrder","StackOrderName","SymbolType","TimeIntervalName","TipPointer","VectorShape",)
