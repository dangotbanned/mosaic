from __future__ import annotations

from typing import TYPE_CHECKING

from mosaic_spec._gen import (
    Area,
    AreaX,
    AreaY,
    Arrow,
    AxisFx,
    AxisFy,
    AxisX,
    AxisY,
    BarX,
    BarY,
    Cell,
    CellX,
    CellY,
    Circle,
    Contour,
    DelaunayLink,
    DelaunayMesh,
    DenseLine,
    Density,
    DensityX,
    DensityY,
    Dot,
    DotX,
    DotY,
    ErrorBarX,
    ErrorBarY,
    Frame,
    Geo,
    Graticule,
    GridFx,
    GridFy,
    GridX,
    GridY,
    HConcat,
    Heatmap,
    Hexagon,
    Hexbin,
    Hexgrid,
    HSpace,
    Hull,
    Image,
    Legend,
    Line,
    LineX,
    LineY,
    Link,
    Menu,
    Plot,
    Raster,
    RasterTile,
    Rect,
    RectX,
    RectY,
    RegressionY,
    RuleX,
    RuleY,
    Search,
    Slider,
    Sphere,
    Spike,
    Table,
    Text,
    TextX,
    TextY,
    TickX,
    TickY,
    VConcat,
    Vector,
    VectorX,
    VectorY,
    Voronoi,
    VoronoiMesh,
    VSpace,
    WaffleX,
    WaffleY,
)
from mosaic_spec._typing_compat import TypeAliasType, TypedDict

if TYPE_CHECKING:
    from mosaic_spec._gen.mosaic import Config, Data, Meta, Params, PlotAttributes


class SpecHead(TypedDict, total=False):
    config: Config
    """Configuration options."""
    data: Data
    """Dataset definitions."""
    meta: Meta
    """Specification metadata."""
    params: Params
    """Param and Selection definitions."""
    plot_defaults: PlotAttributes
    """A default set of attributes to apply to all plot components."""


# pyright: reportIncompatibleVariableOverride=false
class SpecHConcat(SpecHead, HConcat, closed=True): ...  # ty: ignore[invalid-typed-dict-header]


class SpecVConcat(SpecHead, VConcat, closed=True): ...  # ty: ignore[invalid-typed-dict-header]


class SpecHSpace(SpecHead, HSpace, closed=True): ...  # ty: ignore[invalid-typed-dict-header]


class SpecVSpace(SpecHead, VSpace, closed=True): ...  # ty: ignore[invalid-typed-dict-header]


class SpecMenu(SpecHead, Menu, closed=True): ...  # ty: ignore[invalid-typed-dict-header]


class SpecSearch(SpecHead, Search, closed=True): ...  # ty: ignore[invalid-typed-dict-header]


class SpecSlider(SpecHead, Slider, closed=True): ...  # ty: ignore[invalid-typed-dict-header]


class SpecTable(SpecHead, Table, closed=True): ...  # ty: ignore[invalid-typed-dict-header]


class SpecPlot(SpecHead, Plot, closed=True): ...  # ty: ignore[invalid-typed-dict-header]


class SpecArea(SpecHead, Area, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecAreaX(SpecHead, AreaX, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecAreaY(SpecHead, AreaY, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecArrow(SpecHead, Arrow, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecAxisX(SpecHead, AxisX, closed=True): ...  # ty: ignore[invalid-typed-dict-header]


class SpecAxisY(SpecHead, AxisY, closed=True): ...  # ty: ignore[invalid-typed-dict-header]


class SpecAxisFx(SpecHead, AxisFx, closed=True): ...  # ty: ignore[invalid-typed-dict-header]


class SpecAxisFy(SpecHead, AxisFy, closed=True): ...  # ty: ignore[invalid-typed-dict-header]


class SpecGridX(SpecHead, GridX, closed=True): ...  # ty: ignore[invalid-typed-dict-header]


class SpecGridY(SpecHead, GridY, closed=True): ...  # ty: ignore[invalid-typed-dict-header]


class SpecGridFx(SpecHead, GridFx, closed=True): ...  # ty: ignore[invalid-typed-dict-header]


class SpecGridFy(SpecHead, GridFy, closed=True): ...  # ty: ignore[invalid-typed-dict-header]


class SpecBarX(SpecHead, BarX, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecBarY(SpecHead, BarY, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecCell(SpecHead, Cell, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecCellX(SpecHead, CellX, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecCellY(SpecHead, CellY, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecContour(SpecHead, Contour, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecDelaunayLink(SpecHead, DelaunayLink, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecDelaunayMesh(SpecHead, DelaunayMesh, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecHull(SpecHead, Hull, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecVoronoi(SpecHead, Voronoi, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecVoronoiMesh(SpecHead, VoronoiMesh, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecDenseLine(SpecHead, DenseLine, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecDensity(SpecHead, Density, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


# TODO @dangotbanned: `Density{X,Y}` are unexpanded unions
class SpecDensityX(SpecHead, DensityX, closed=True): ...  # ty: ignore[invalid-base] # pyright: ignore[reportCallIssue, reportGeneralTypeIssues]


# TODO @dangotbanned: `Density{X,Y}` are unexpanded unions
class SpecDensityY(SpecHead, DensityY, closed=True): ...  # ty: ignore[invalid-base] # pyright: ignore[reportCallIssue, reportGeneralTypeIssues]


class SpecDot(SpecHead, Dot, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecDotX(SpecHead, DotX, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecDotY(SpecHead, DotY, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecCircle(SpecHead, Circle, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecHexagon(SpecHead, Hexagon, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecErrorBarX(SpecHead, ErrorBarX, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecErrorBarY(SpecHead, ErrorBarY, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecFrame(SpecHead, Frame, closed=True): ...  # ty: ignore[invalid-typed-dict-header]


class SpecGeo(SpecHead, Geo, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecGraticule(SpecHead, Graticule, closed=True): ...  # ty: ignore[invalid-typed-dict-header]


class SpecSphere(SpecHead, Sphere, closed=True): ...  # ty: ignore[invalid-typed-dict-header]


class SpecHexbin(SpecHead, Hexbin, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecHexgrid(SpecHead, Hexgrid, closed=True): ...  # ty: ignore[invalid-typed-dict-header]


class SpecImage(SpecHead, Image, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecLine(SpecHead, Line, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecLineX(SpecHead, LineX, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecLineY(SpecHead, LineY, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecLink(SpecHead, Link, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecRaster(SpecHead, Raster, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecHeatmap(SpecHead, Heatmap, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecRasterTile(SpecHead, RasterTile, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecRect(SpecHead, Rect, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecRectX(SpecHead, RectX, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecRectY(SpecHead, RectY, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecRegressionY(SpecHead, RegressionY, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecRuleX(SpecHead, RuleX, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecRuleY(SpecHead, RuleY, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecText(SpecHead, Text, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecTextX(SpecHead, TextX, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecTextY(SpecHead, TextY, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecTickX(SpecHead, TickX, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecTickY(SpecHead, TickY, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecVector(SpecHead, Vector, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecVectorX(SpecHead, VectorX, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecVectorY(SpecHead, VectorY, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecSpike(SpecHead, Spike, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecWaffleX(SpecHead, WaffleX, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecWaffleY(SpecHead, WaffleY, closed=True): ...  # ty: ignore[invalid-typed-dict-field, invalid-typed-dict-header]


class SpecLegend(SpecHead, Legend, closed=True): ...  # ty: ignore[invalid-typed-dict-header]


Spec = TypeAliasType(
    "Spec",
    SpecHConcat
    | SpecVConcat
    | SpecHSpace
    | SpecVSpace
    | SpecMenu
    | SpecSearch
    | SpecSlider
    | SpecTable
    | SpecPlot
    | SpecArea
    | SpecAreaX
    | SpecAreaY
    | SpecArrow
    | SpecAxisX
    | SpecAxisY
    | SpecAxisFx
    | SpecAxisFy
    | SpecGridX
    | SpecGridY
    | SpecGridFx
    | SpecGridFy
    | SpecBarX
    | SpecBarY
    | SpecCell
    | SpecCellX
    | SpecCellY
    | SpecContour
    | SpecDelaunayLink
    | SpecDelaunayMesh
    | SpecHull
    | SpecVoronoi
    | SpecVoronoiMesh
    | SpecDenseLine
    | SpecDensity
    | SpecDensityX
    | SpecDensityY
    | SpecDot
    | SpecDotX
    | SpecDotY
    | SpecCircle
    | SpecHexagon
    | SpecErrorBarX
    | SpecErrorBarY
    | SpecFrame
    | SpecGeo
    | SpecGraticule
    | SpecSphere
    | SpecHexbin
    | SpecHexgrid
    | SpecImage
    | SpecLine
    | SpecLineX
    | SpecLineY
    | SpecLink
    | SpecRaster
    | SpecHeatmap
    | SpecRasterTile
    | SpecRect
    | SpecRectX
    | SpecRectY
    | SpecRegressionY
    | SpecRuleX
    | SpecRuleY
    | SpecText
    | SpecTextX
    | SpecTextY
    | SpecTickX
    | SpecTickY
    | SpecVector
    | SpecVectorX
    | SpecVectorY
    | SpecSpike
    | SpecWaffleX
    | SpecWaffleY
    | SpecLegend,
)
__all__ = (
    "Spec",
    "SpecArea",
    "SpecAreaX",
    "SpecAreaY",
    "SpecArrow",
    "SpecAxisFx",
    "SpecAxisFy",
    "SpecAxisX",
    "SpecAxisY",
    "SpecBarX",
    "SpecBarY",
    "SpecCell",
    "SpecCellX",
    "SpecCellY",
    "SpecCircle",
    "SpecContour",
    "SpecDelaunayLink",
    "SpecDelaunayMesh",
    "SpecDenseLine",
    "SpecDensity",
    "SpecDensityX",
    "SpecDensityY",
    "SpecDot",
    "SpecDotX",
    "SpecDotY",
    "SpecErrorBarX",
    "SpecErrorBarY",
    "SpecFrame",
    "SpecGeo",
    "SpecGraticule",
    "SpecGridFx",
    "SpecGridFy",
    "SpecGridX",
    "SpecGridY",
    "SpecHConcat",
    "SpecHSpace",
    "SpecHeatmap",
    "SpecHexagon",
    "SpecHexbin",
    "SpecHexgrid",
    "SpecHull",
    "SpecImage",
    "SpecLegend",
    "SpecLine",
    "SpecLineX",
    "SpecLineY",
    "SpecLink",
    "SpecMenu",
    "SpecPlot",
    "SpecRaster",
    "SpecRasterTile",
    "SpecRect",
    "SpecRectX",
    "SpecRectY",
    "SpecRegressionY",
    "SpecRuleX",
    "SpecRuleY",
    "SpecSearch",
    "SpecSlider",
    "SpecSphere",
    "SpecSpike",
    "SpecTable",
    "SpecText",
    "SpecTextX",
    "SpecTextY",
    "SpecTickX",
    "SpecTickY",
    "SpecVConcat",
    "SpecVSpace",
    "SpecVector",
    "SpecVectorX",
    "SpecVectorY",
    "SpecVoronoi",
    "SpecVoronoiMesh",
    "SpecWaffleX",
    "SpecWaffleY",
)
