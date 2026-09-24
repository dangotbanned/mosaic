from __future__ import annotations

from typing import TYPE_CHECKING, Literal as L

from mosaic_spec._typing_compat import (
    Protocol,
    Self,
    TypeAliasType as Type,
    TypedDict,
    TypeVar,
    Unpack,
)

if TYPE_CHECKING:
    import mosaic_spec as ms
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
