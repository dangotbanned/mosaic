"""Defining everything structurally."""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal as L

import mosaic_spec as ms
from mosaic_spec._typing_compat import Protocol, TypeAliasType as Type, TypedDict

if TYPE_CHECKING:
    from collections.abc import Iterator, Mapping

    from tests.apis.attributes import PlotAttributes


DataType = Type("DataType", L["csv", "json", "parquet", "spatial", "table"])
Input = Type("Input", L["menu", "search", "slider", "table"])
LegendKind = Type("LegendKind", L["color", "opacity", "symbol"])

# NOTE: Both of these use `select` as a discriminator (upstream)
SelectionStrategy = Type("SelectionStrategy", L["crossfilter", "intersect", "single", "union"])
InteractorSelect = Type(
    "InteractorSelect",
    L[
        "highlight",
        "intervalX",
        "intervalXY",
        "intervalY",
        "nearestX",
        "nearestY",
        "pan",
        "panX",
        "panY",
        "panZoom",
        "panZoomX",
        "panZoomY",
        "region",
        "toggle",
    ],
)

MarkName = Type(
    "MarkName",
    L[
        "area",
        "areaX",
        "areaY",
        "arrow",
        "axisFx",
        "axisFy",
        "axisX",
        "axisY",
        "barX",
        "barY",
        "cell",
        "cellX",
        "cellY",
        "circle",
        "contour",
        "delaunayLink",
        "delaunayMesh",
        "denseLine",
        "density",
        "densityX",
        "densityY",
        "dot",
        "dotX",
        "dotY",
        "errorbarX",
        "errorbarY",
        "frame",
        "geo",
        "graticule",
        "gridFx",
        "gridFy",
        "gridX",
        "gridY",
        "heatmap",
        "hexagon",
        "hexbin",
        "hexgrid",
        "hull",
        "image",
        "line",
        "lineX",
        "lineY",
        "link",
        "raster",
        "rasterTile",
        "rect",
        "rectX",
        "rectY",
        "regressionY",
        "ruleX",
        "ruleY",
        "sphere",
        "spike",
        "text",
        "textX",
        "textY",
        "tickX",
        "tickY",
        "vector",
        "vectorX",
        "vectorY",
        "voronoi",
        "voronoiMesh",
        "waffleX",
        "waffleY",
    ],
)
"""The type of `ms.PlotMark["mark"]`."""


class SpecHead(TypedDict, total=False, closed=True):
    config: ms.Config
    """Configuration options."""

    data: dict[str, ms.DataDefinition]
    """Dataset definitions."""

    meta: ms.Meta
    """Specification metadata."""

    params: dict[str, ms.ParamDefinition]
    """Param and Selection definitions."""

    plot_defaults: PlotAttributes
    """A default set of attributes to apply to all plot components."""


class HasParams(Protocol):
    __slots__ = ()

    def _iter_params(self) -> Iterator[Param]: ...


class HasData(Protocol):
    __slots__ = ()

    def _iter_data(self) -> Iterator[Data]: ...


class HasViews(Protocol):
    __slots__ = ()

    def _iter_views(self) -> Iterator[View]: ...


class CanPlot(Protocol):
    __slots__ = ()

    def plot(self) -> Plot: ...


class Spec(Protocol):
    """A declarative Mosaic specification."""

    __slots__ = ()
    view: View
    """The top-level component."""

    options: SpecHead


class View(Protocol):
    """A top-level component.

    - Covers 53/55 examples
        - Skips 2 which use `Table`
    - Everything else can be nested within these to fit
    - Reduces the `Spec` intersection from **80** alternatives
    """

    __slots__ = ()

    def to_spec(self) -> Spec: ...
    def _iter_views(self) -> Iterator[View]: ...


class Plot(View, Protocol):
    __slots__ = ()

    def _iter_elements(self) -> Iterator[Element]: ...
    def _iter_views(self) -> Iterator[View]:
        yield self


class Concat(View, Protocol):
    __slots__ = ()

    def _iter_components(self) -> Iterator[Component]: ...


class Widget(HasParams, Protocol):
    __slots__ = ()

    @property
    def input(self) -> Input: ...


class Interactor(HasParams, CanPlot, Protocol):
    __slots__ = ()

    @property
    def select(self) -> InteractorSelect: ...


class Legend(HasParams, CanPlot, Protocol):
    __slots__ = ()

    @property
    def legend(self) -> LegendKind: ...


class Mark(HasData, HasParams, CanPlot, Protocol):
    __slots__ = ()

    @property
    def mark(self) -> Mark: ...


Element = Type("Element", Interactor | Mark | Legend)
"""Marks, interactors, or legends."""

Component = Type("Component", View | Widget | Mark | ms.HSpace | ms.VSpace)
"""A specification component such as a plot, input widget, or layout."""


class Data(HasData, Protocol):
    __slots__ = ()

    # NOTE: Doesn't need `to_dict`
    @property
    def name(self) -> str: ...
    @property
    def type(self) -> DataType: ...
    def _iter_data(self) -> Iterator[Data]:
        yield self


# NOTE: Can always have params, but the actual source is either data or param
class Source(HasData, HasParams, Protocol):
    """An input data specification for a plot mark."""

    __slots__ = ()


class Param(HasParams, Protocol):
    __slots__ = ()

    @property
    def name(self) -> str: ...
    def __repr__(self) -> ms.ParamRef:
        """Interpolate the parameter in a query."""
        return self.ref()

    def ref(self) -> ms.ParamRef:
        return ms.ParamRef(f"${self.name}")

    def to_dict(self) -> Mapping[str, ms.ParamDefinition]:
        """Convert the current and all nested params into a dictionary."""


class Selection(Param, Protocol):
    __slots__ = ()

    @property
    def strategy(self) -> SelectionStrategy: ...
