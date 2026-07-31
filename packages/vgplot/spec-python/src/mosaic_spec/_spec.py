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
    DensityX1,
    DensityX2,
    DensityX3,
    DensityX4,
    DensityY1,
    DensityY2,
    DensityY3,
    DensityY4,
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


class SpecHConcat(SpecHead, HConcat, closed=True): ...


class SpecVConcat(SpecHead, VConcat, closed=True): ...


class SpecHSpace(SpecHead, HSpace, closed=True): ...


class SpecVSpace(SpecHead, VSpace, closed=True): ...


class SpecMenu(SpecHead, Menu, closed=True): ...


class SpecSearch(SpecHead, Search, closed=True): ...


class SpecSlider(SpecHead, Slider, closed=True): ...


class SpecTable(SpecHead, Table, closed=True): ...


class SpecPlot(SpecHead, Plot, closed=True): ...


class SpecArea(SpecHead, Area, closed=True): ...


class SpecAreaX(SpecHead, AreaX, closed=True): ...


class SpecAreaY(SpecHead, AreaY, closed=True): ...


class SpecArrow(SpecHead, Arrow, closed=True): ...


class SpecAxisX(SpecHead, AxisX, closed=True): ...


class SpecAxisY(SpecHead, AxisY, closed=True): ...


class SpecAxisFx(SpecHead, AxisFx, closed=True): ...


class SpecAxisFy(SpecHead, AxisFy, closed=True): ...


class SpecGridX(SpecHead, GridX, closed=True): ...


class SpecGridY(SpecHead, GridY, closed=True): ...


class SpecGridFx(SpecHead, GridFx, closed=True): ...


class SpecGridFy(SpecHead, GridFy, closed=True): ...


class SpecBarX(SpecHead, BarX, closed=True): ...


class SpecBarY(SpecHead, BarY, closed=True): ...


class SpecCell(SpecHead, Cell, closed=True): ...


class SpecCellX(SpecHead, CellX, closed=True): ...


class SpecCellY(SpecHead, CellY, closed=True): ...


class SpecContour(SpecHead, Contour, closed=True): ...


class SpecDelaunayLink(SpecHead, DelaunayLink, closed=True): ...


class SpecDelaunayMesh(SpecHead, DelaunayMesh, closed=True): ...


class SpecHull(SpecHead, Hull, closed=True): ...


class SpecVoronoi(SpecHead, Voronoi, closed=True): ...


class SpecVoronoiMesh(SpecHead, VoronoiMesh, closed=True): ...


class SpecDenseLine(SpecHead, DenseLine, closed=True): ...


class SpecDensity(SpecHead, Density, closed=True): ...


class SpecDensityX1(SpecHead, DensityX1, closed=True): ...


class SpecDensityX2(SpecHead, DensityX2, closed=True): ...


class SpecDensityX3(SpecHead, DensityX3, closed=True): ...


class SpecDensityX4(SpecHead, DensityX4, closed=True): ...


class SpecDensityY1(SpecHead, DensityY1, closed=True): ...


class SpecDensityY2(SpecHead, DensityY2, closed=True): ...


class SpecDensityY3(SpecHead, DensityY3, closed=True): ...


class SpecDensityY4(SpecHead, DensityY4, closed=True): ...


class SpecDot(SpecHead, Dot, closed=True): ...


class SpecDotX(SpecHead, DotX, closed=True): ...


class SpecDotY(SpecHead, DotY, closed=True): ...


class SpecCircle(SpecHead, Circle, closed=True): ...


class SpecHexagon(SpecHead, Hexagon, closed=True): ...


class SpecErrorBarX(SpecHead, ErrorBarX, closed=True): ...


class SpecErrorBarY(SpecHead, ErrorBarY, closed=True): ...


class SpecFrame(SpecHead, Frame, closed=True): ...


class SpecGeo(SpecHead, Geo, closed=True): ...


class SpecGraticule(SpecHead, Graticule, closed=True): ...


class SpecSphere(SpecHead, Sphere, closed=True): ...


class SpecHexbin(SpecHead, Hexbin, closed=True): ...


class SpecHexgrid(SpecHead, Hexgrid, closed=True): ...


class SpecImage(SpecHead, Image, closed=True): ...


class SpecLine(SpecHead, Line, closed=True): ...


class SpecLineX(SpecHead, LineX, closed=True): ...


class SpecLineY(SpecHead, LineY, closed=True): ...


class SpecLink(SpecHead, Link, closed=True): ...


class SpecRaster(SpecHead, Raster, closed=True): ...


class SpecHeatmap(SpecHead, Heatmap, closed=True): ...


class SpecRasterTile(SpecHead, RasterTile, closed=True): ...


class SpecRect(SpecHead, Rect, closed=True): ...


class SpecRectX(SpecHead, RectX, closed=True): ...


class SpecRectY(SpecHead, RectY, closed=True): ...


class SpecRegressionY(SpecHead, RegressionY, closed=True): ...


class SpecRuleX(SpecHead, RuleX, closed=True): ...


class SpecRuleY(SpecHead, RuleY, closed=True): ...


class SpecText(SpecHead, Text, closed=True): ...


class SpecTextX(SpecHead, TextX, closed=True): ...


class SpecTextY(SpecHead, TextY, closed=True): ...


class SpecTickX(SpecHead, TickX, closed=True): ...


class SpecTickY(SpecHead, TickY, closed=True): ...


class SpecVector(SpecHead, Vector, closed=True): ...


class SpecVectorX(SpecHead, VectorX, closed=True): ...


class SpecVectorY(SpecHead, VectorY, closed=True): ...


class SpecSpike(SpecHead, Spike, closed=True): ...


class SpecWaffleX(SpecHead, WaffleX, closed=True): ...


class SpecWaffleY(SpecHead, WaffleY, closed=True): ...


class SpecLegend(SpecHead, Legend, closed=True): ...


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
    | SpecDensityX1
    | SpecDensityX2
    | SpecDensityX3
    | SpecDensityX4
    | SpecDensityY1
    | SpecDensityY2
    | SpecDensityY3
    | SpecDensityY4
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
    "SpecDensityX1",
    "SpecDensityX2",
    "SpecDensityX3",
    "SpecDensityX4",
    "SpecDensityY1",
    "SpecDensityY2",
    "SpecDensityY3",
    "SpecDensityY4",
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
