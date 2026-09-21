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

from collections.abc import Callable
from typing import TYPE_CHECKING, Any

from mosaic_spec._typing_compat import TypeAliasType, TypeVar

if TYPE_CHECKING:
    from tests.apis.data import Data

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

    def __init__(self, data: Data) -> None:
        self._data: Data = data

    def __call__(self, *args: Incomplete, **kwds: Incomplete) -> Incomplete: ...


def data_never(f: _Fn, /) -> _Fn:
    """(Visually) signal that a mark **doesn't support** `data`."""
    return f


def data_optional(f: _Fn, /) -> _Fn:
    """(Visually) signal that a mark **doesn't require** `data`."""
    return f


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


@data_optional
class TextNs(_Mixed):
    def x(self) -> Incomplete: ...
    def y(self) -> Incomplete: ...


class MarksNs:
    """A superset of what is possible.

    - Not dealing with optional/required/not allowed data yet
    - Working out propagating data first
    """

    def __init__(self, data: Data) -> None:
        self._data: Data = data

    @property
    def area(self) -> AreaNs:
        return AreaNs(self._data)

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
    rect: _Mixed

    def regression_y(self) -> Direct: ...

    @property
    def rule(self) -> RuleNs:
        return RuleNs()

    @data_never
    def sphere(self) -> Direct: ...
    def spike(self) -> Direct: ...

    @property
    def text(self) -> TextNs:
        return TextNs(self._data)

    @property
    def tick(self) -> TickNs:
        return TickNs()

    vector: _Mixed
    voronoi: _Mixed

    @property
    def waffle(self) -> WaffleNs:
        return WaffleNs()
