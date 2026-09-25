from __future__ import annotations

from typing import TYPE_CHECKING, Literal as L

import mosaic_spec as ms
from mosaic_spec._gen.layout import _HConcatOpen, _VConcatOpen
from mosaic_spec._gen.plot import _PlotOpen
from mosaic_spec._typing_compat import (
    Protocol,
    Self,
    TypeAliasType as Type,
    TypedDict,
    TypeVar,
    Unpack,
)

if TYPE_CHECKING:
    from tests.apis.attributes import PlotAttributes


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


class _SpecHead(TypedDict, total=False):
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


class SpecHead(_SpecHead, closed=True): ...


# NOTE: Required for the `PlotAttributes` override vs `ms.spec.*` version
class SpecPlot(_SpecHead, _PlotOpen, closed=True): ...


class SpecHConcat(_SpecHead, _HConcatOpen, closed=True): ...


class SpecVConcat(_SpecHead, _VConcatOpen, closed=True): ...


ViewT = TypeVar("ViewT", bound="View", infer_variance=True)


class Spec(Protocol[ViewT]):
    """A declarative Mosaic specification."""

    __slots__ = ("options", "view")
    view: ViewT
    """The top-level component."""

    options: SpecHead
    """Top-level specification properties."""


class View(Protocol):
    """A top-level component.

    - Covers 53/55 examples
        - Skips 2 which use `Table`
    - Everything else can be nested within these to fit
    - Reduces the `Spec` intersection from **80** alternatives
    """

    __slots__ = ()

    def to_spec(self, **options: Unpack[SpecHead]) -> Spec[Self]: ...


R = TypeVar("R", infer_variance=True)


class ToDict(Protocol[R]):
    __slots__ = ()

    def to_dict(
        self, data: dict[str, ms.DataDefinition], params: dict[str, ms.ParamDefinition]
    ) -> R: ...


_IntoDict = Type("_IntoDict", R | ToDict[R], type_params=(R,))
"""A converted `R`, or an object that can be converted into `R`."""

IntoPlot = Type("IntoPlot", _IntoDict[ms.PlotInteractor | ms.PlotLegend | ms.PlotMark])
IntoComponent = Type("IntoComponent", _IntoDict[ms.Component])
"""A specification component such as a plot, input widget, or layout."""
