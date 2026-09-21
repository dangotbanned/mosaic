"""Will be a big one.

## Notes

### Data

Could add a `mark` namespace to `Data`, which can be used with most marks

- `data` is optional (okay)
    - RuleX
    - RuleY
    - Text
    - TextX
    - TextY
    - TickX
    - TickY
- `data` is not permitted (nope)
    - AxisFx
    - AxisFy
    - AxisX
    - AxisY
    - Frame
    - Graticule
    - GridFx
    - GridFy
    - GridX
    - GridY
    - Hexgrid
    - Sphere
- `data` is required
    - everything else

### There are still gaps

Not allowed and optional data will need alternative entry points

### Hierarchical namespacing

Generally this'll be descriptor magic

- There are marks with e.g. `X, `Y` variants
- Some have a non-suffixed version too
- `RegressionY` has no variants
- `Density` is very complicated
    - Also, my auto-naming didn't account for multiple types (only on the `Y` versions)
        - `DensityYDot.type: L["circle", "dot", "dotY", "hexagon"]`
        - `DensityYText.type: L["text", "textY"]`
"""

from __future__ import annotations

from collections.abc import Callable, Iterator
from functools import partial
from typing import Any, Protocol

import mosaic_spec as ms
from mosaic_spec._typing_compat import TypeAliasType, TypeVar, Unpack
from tests.apis import _marks, encodings_builder as eb
from tests.apis.components_spec import Plot, VConcatSpec
from tests.apis.data import Data, Source
from tests.apis.params import ParamDef, p

Incomplete = TypeAliasType("Incomplete", Any)

_Fn = TypeVar("_Fn", bound=Callable[..., Any])

Direct = TypeAliasType("Direct", Incomplete)
"""The name maps directly to a mark.

So they can be top-level methods/functions.
"""


class _NestedOnly:
    """A namespace where the name is a common prefix to multiple marks.

    These objects can simply use the builtin `@property` and provide methods.
    """


# TODO @dangotbanned: What to do when descriptor is looked up on the `MarksNs` class?
# - want it to behave like `@property` in that case (e.g. not useful)
# - maybe need another level of indirection?
#   - an instance of this shouldn't live in `MarksNs`
#   - would need to check all the time to see if it had data
class _Mixed:
    """The name **both** maps directly to a mark, and is a common prefix to multiple marks.

    - Needs to support `__call__` and define methods itself.
    - It turns out that only `Text*` is optional data here, but all permit it
    """

    def __init__(self, source: Source) -> None:
        self._source: Source = source


def data_never(f: _Fn, /) -> _Fn:
    """(Visually) signal that a mark **doesn't support** `data`."""
    return f


def data_optional(f: _Fn, /) -> _Fn:
    """(Visually) signal that a mark **doesn't require** `data`."""
    return f


class IntoMark(Protocol):
    def __call__(self, *, data: ms.PlotFrom) -> ms.PlotMark: ...


class MarkData:
    """A mark that requires data.

    Wrapper to allow deferring param & data refs
    """

    def __init__(self, source: Source, into_mark: IntoMark) -> None:
        self._source: Source = source
        self._into_mark: IntoMark = into_mark
        """Might need to make less opaque.

        `IntoMark` doesn't provide a means to iterate over params.
        """

    def _mark(self) -> ms.PlotMark:
        return self._into_mark(data=self._source._plot_source())

    def _iter_params(self) -> Iterator[ParamDef]:
        yield from self._source._iter_params()

    def _iter_data(self) -> Iterator[Data]:
        yield from self._source._iter_data()


@data_never
class AxisNs(_NestedOnly):
    def fy(self) -> Incomplete: ...
    def fx(self) -> Incomplete: ...
    def x(self) -> Incomplete: ...
    def y(self) -> Incomplete: ...


class BarNs(_NestedOnly):
    def x(self) -> Incomplete: ...
    def y(self) -> Incomplete: ...


class DelaunayNs(_NestedOnly):
    def link(self) -> Incomplete: ...
    def mesh(self) -> Incomplete: ...


class ErrorBarNs(_NestedOnly):
    def x(self) -> Incomplete: ...
    def y(self) -> Incomplete: ...


@data_never
class GridNs(_NestedOnly):
    def fy(self) -> Incomplete: ...
    def fx(self) -> Incomplete: ...
    def x(self) -> Incomplete: ...
    def y(self) -> Incomplete: ...


@data_optional
class RuleNs(_NestedOnly):
    def x(self) -> Incomplete: ...
    def y(self) -> Incomplete: ...


@data_optional
class TickNs(_NestedOnly):
    def x(self) -> Incomplete: ...
    def y(self) -> Incomplete: ...


class WaffleNs(_NestedOnly):
    def x(self) -> Incomplete: ...
    def y(self) -> Incomplete: ...


class AreaNs(_Mixed):
    def x(self) -> Incomplete: ...
    def y(self) -> Incomplete: ...


class RectNs(_Mixed):
    def __call__(self, **kwds: Unpack[_marks.RectOptions]) -> MarkData:
        """Create a rect mark.

        The rectangle extends horizontally from **x1** to **x2**, and vertically from **y1** to **y2**.
        The position channels are often derived with a transform.

        When **y** extends from zero, for example for a histogram where the height of each rect reflects a count of values,
        use the rectY mark for an implicit stackY transform; similarly, if **x** extends from zero,
        use the rectX mark for an implicit stackX transform.

        If an **interval** is specified, then **x1** and **x2** are derived from
        **x**, and **y1** and **y2** are derived from **y**,
        each representing the lower and upper bound of the containing interval, respectively.

        Both *x* and *y* should be quantitative or temporal; otherwise, use a bar or cell mark.
        """

        return MarkData(self._source, partial(ms.Rect, mark="rect", **kwds))

    def x(self, **kwds: Unpack[_marks.RectXOptions]) -> MarkData:
        """Create a rectX mark.

        Like rect, but if neither **x1** nor **x2** is specified, apply an implicit stackX transform is applied to **x**,
        and if **x** is not specified, it defaults to the identity function, assuming that *data* is an array of numbers [*x₀*, *x₁*, *x₂*, …].
        """
        return MarkData(self._source, partial(ms.RectX, mark="rectX", **kwds))

    def y(self, **kwds: Unpack[_marks.RectYOptions]) -> MarkData:
        """Create a rectY mark.

        Like rect, but if neither **y1** nor **y2** is specified, apply an implicit stackY transform is applied to **y**,
        and if **y** is not specified, it defaults to the identity function, assuming that *data* is an array of numbers [*y₀*, *y₁*, *y₂*, …].
        """
        return MarkData(self._source, partial(ms.RectY, mark="rectY", **kwds))


@data_optional
class TextNs(_Mixed):
    def x(self) -> Incomplete: ...
    def y(self) -> Incomplete: ...


class MarksNs:
    """A superset of what is possible.

    - Not dealing with optional/required/not allowed data yet
    - Working out propagating data first
    """

    def __init__(self, source: Source) -> None:
        self._source: Source = source

    @property
    def area(self) -> AreaNs:
        return AreaNs(self._source)

    def arrow(self) -> Direct: ...

    @property
    def axis(self) -> AxisNs:
        return AxisNs()

    @property
    def bar(self) -> BarNs:
        return BarNs()

    cell: _Mixed

    def circle(self) -> Direct: ...
    def contour(self) -> Direct: ...

    @property
    def delaunay(self) -> DelaunayNs:
        return DelaunayNs()

    def dense_line(self) -> Direct: ...

    density: _Mixed  # doubly nested
    dot: _Mixed

    @property
    def error_bar(self) -> ErrorBarNs:
        return ErrorBarNs()

    @data_never
    def frame(self) -> Direct: ...
    def geo(self) -> Direct: ...

    @data_never
    def graticule(self) -> Direct: ...

    @property
    def grid(self) -> GridNs:
        return GridNs()

    def heatmap(self) -> Direct: ...
    def hexagon(self) -> Direct: ...
    def hexbin(self) -> Direct: ...

    @data_never
    def hexgrid(self) -> Direct: ...

    def hull(self) -> Direct: ...
    def image(self) -> Direct: ...

    line: _Mixed

    def link(self) -> Direct: ...

    raster: _Mixed

    @property
    def rect(self) -> RectNs:
        """Create a rect mark."""
        return RectNs(self._source)

    def regression_y(self) -> Direct: ...

    @property
    def rule(self) -> RuleNs:
        return RuleNs()

    @data_never
    def sphere(self) -> Direct: ...
    def spike(self) -> Direct: ...

    @property
    def text(self) -> TextNs:
        return TextNs(self._source)

    @property
    def tick(self) -> TickNs:
        return TickNs()

    vector: _Mixed
    voronoi: _Mixed

    @property
    def waffle(self) -> WaffleNs:
        return WaffleNs()


def crossfilter_example() -> None:
    data = Data.from_parquet("data/flights-200k.parquet", "flights")
    # NOTE: aiming for this to be like `Data.from_*(...).mark.*`
    # - maybe have `mark` available on `Data`, and change `source` -> `Data.filter`?
    # - might also need to keep `Data` inside `Source` for later?

    # NOTE:
    brush = p.brush.cross()

    mark = MarksNs(data.filter(brush))

    # TODO @dangotbanned: Accept `MarkData` higher up (need `Plot` & `Spec` concepts)
    rect_y_1 = mark.rect.y(
        x=eb.col("delay").bin(),
        y=eb.len().to_dict(),
        fill="steelblue",
        inset_left=0.5,
        inset_right=0.5,
    )
    rect_y_2 = mark.rect.y(
        x=eb.col("time").bin(),
        y=eb.len().to_dict(),
        fill="steelblue",
        inset_left=0.5,
        inset_right=0.5,
    )
    interval = ms.IntervalX(select="intervalX", bind=brush.ref())
    _spec = VConcatSpec(
        vconcat=(
            Plot(
                plot=(rect_y_1._mark(), interval),
                x={"domain": "Fixed", "label": "Arrival Delay (min)", "label_anchor": "center"},
                y={"tick_format": "s"},
                height=200,
            ),
            Plot(
                plot=(rect_y_2._mark(), interval),
                x={"domain": "Fixed", "label": "Departure Time (hour)", "label_anchor": "center"},
                y={"tick_format": "s"},
                height=200,
            ),
        ),
        params=brush.to_dict(),
        data=data.to_dict(),
    )
