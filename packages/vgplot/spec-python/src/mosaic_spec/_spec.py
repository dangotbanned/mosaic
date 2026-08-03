from __future__ import annotations

from mosaic_spec._gen.mosaic import (
    Config,
    Data,
    Meta,
    Params,
    PlotAttributes,
    _AreaOpen,
    _AreaXOpen,
    _AreaYOpen,
    _ArrowOpen,
    _AxisFxOpen,
    _AxisFyOpen,
    _AxisXOpen,
    _AxisYOpen,
    _BarXOpen,
    _BarYOpen,
    _CellOpen,
    _CellXOpen,
    _CellYOpen,
    _CircleOpen,
    _ContourOpen,
    _DelaunayLinkOpen,
    _DelaunayMeshOpen,
    _DenseLineOpen,
    _DensityOpen,
    _DensityX1Open,
    _DensityX2Open,
    _DensityX3Open,
    _DensityX4Open,
    _DensityY1Open,
    _DensityY2Open,
    _DensityY3Open,
    _DensityY4Open,
    _DotOpen,
    _DotXOpen,
    _DotYOpen,
    _ErrorBarXOpen,
    _ErrorBarYOpen,
    _FrameOpen,
    _GeoOpen,
    _GraticuleOpen,
    _GridFxOpen,
    _GridFyOpen,
    _GridXOpen,
    _GridYOpen,
    _HConcatOpen,
    _HeatmapOpen,
    _HexagonOpen,
    _HexbinOpen,
    _HexgridOpen,
    _HSpaceOpen,
    _HullOpen,
    _ImageOpen,
    _LegendOpen,
    _LineOpen,
    _LineXOpen,
    _LineYOpen,
    _LinkOpen,
    _MenuOpen,
    _PlotOpen,
    _RasterOpen,
    _RasterTileOpen,
    _RectOpen,
    _RectXOpen,
    _RectYOpen,
    _RegressionYOpen,
    _RuleXOpen,
    _RuleYOpen,
    _SearchOpen,
    _SliderOpen,
    _SphereOpen,
    _SpikeOpen,
    _TableOpen,
    _TextOpen,
    _TextXOpen,
    _TextYOpen,
    _TickXOpen,
    _TickYOpen,
    _VConcatOpen,
    _VectorOpen,
    _VectorXOpen,
    _VectorYOpen,
    _VoronoiMeshOpen,
    _VoronoiOpen,
    _VSpaceOpen,
    _WaffleXOpen,
    _WaffleYOpen,
)
from mosaic_spec._typing_compat import TypeAliasType, TypedDict


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


class SpecArea(SpecHead, _AreaOpen, closed=True): ...


class SpecAreaX(SpecHead, _AreaXOpen, closed=True): ...


class SpecAreaY(SpecHead, _AreaYOpen, closed=True): ...


class SpecArrow(SpecHead, _ArrowOpen, closed=True): ...


class SpecAxisFx(SpecHead, _AxisFxOpen, closed=True): ...


class SpecAxisFy(SpecHead, _AxisFyOpen, closed=True): ...


class SpecAxisX(SpecHead, _AxisXOpen, closed=True): ...


class SpecAxisY(SpecHead, _AxisYOpen, closed=True): ...


class SpecBarX(SpecHead, _BarXOpen, closed=True): ...


class SpecBarY(SpecHead, _BarYOpen, closed=True): ...


class SpecCell(SpecHead, _CellOpen, closed=True): ...


class SpecCellX(SpecHead, _CellXOpen, closed=True): ...


class SpecCellY(SpecHead, _CellYOpen, closed=True): ...


class SpecCircle(SpecHead, _CircleOpen, closed=True): ...


class SpecContour(SpecHead, _ContourOpen, closed=True): ...


class SpecDelaunayLink(SpecHead, _DelaunayLinkOpen, closed=True): ...


class SpecDelaunayMesh(SpecHead, _DelaunayMeshOpen, closed=True): ...


class SpecDenseLine(SpecHead, _DenseLineOpen, closed=True): ...


class SpecDensity(SpecHead, _DensityOpen, closed=True): ...


class SpecDot(SpecHead, _DotOpen, closed=True): ...


class SpecDotX(SpecHead, _DotXOpen, closed=True): ...


class SpecDotY(SpecHead, _DotYOpen, closed=True): ...


class SpecErrorBarX(SpecHead, _ErrorBarXOpen, closed=True): ...


class SpecErrorBarY(SpecHead, _ErrorBarYOpen, closed=True): ...


class SpecFrame(SpecHead, _FrameOpen, closed=True): ...


class SpecGeo(SpecHead, _GeoOpen, closed=True): ...


class SpecGraticule(SpecHead, _GraticuleOpen, closed=True): ...


class SpecGridFx(SpecHead, _GridFxOpen, closed=True): ...


class SpecGridFy(SpecHead, _GridFyOpen, closed=True): ...


class SpecGridX(SpecHead, _GridXOpen, closed=True): ...


class SpecGridY(SpecHead, _GridYOpen, closed=True): ...


class SpecHConcat(SpecHead, _HConcatOpen, closed=True): ...


class SpecHSpace(SpecHead, _HSpaceOpen, closed=True): ...


class SpecHeatmap(SpecHead, _HeatmapOpen, closed=True): ...


class SpecHexagon(SpecHead, _HexagonOpen, closed=True): ...


class SpecHexbin(SpecHead, _HexbinOpen, closed=True): ...


class SpecHexgrid(SpecHead, _HexgridOpen, closed=True): ...


class SpecHull(SpecHead, _HullOpen, closed=True): ...


class SpecImage(SpecHead, _ImageOpen, closed=True): ...


class SpecLegend(SpecHead, _LegendOpen, closed=True): ...


class SpecLine(SpecHead, _LineOpen, closed=True): ...


class SpecLineX(SpecHead, _LineXOpen, closed=True): ...


class SpecLineY(SpecHead, _LineYOpen, closed=True): ...


class SpecLink(SpecHead, _LinkOpen, closed=True): ...


class SpecMenu(SpecHead, _MenuOpen, closed=True): ...


class SpecPlot(SpecHead, _PlotOpen, closed=True): ...


class SpecRaster(SpecHead, _RasterOpen, closed=True): ...


class SpecRasterTile(SpecHead, _RasterTileOpen, closed=True): ...


class SpecRect(SpecHead, _RectOpen, closed=True): ...


class SpecRectX(SpecHead, _RectXOpen, closed=True): ...


class SpecRectY(SpecHead, _RectYOpen, closed=True): ...


class SpecRegressionY(SpecHead, _RegressionYOpen, closed=True): ...


class SpecRuleX(SpecHead, _RuleXOpen, closed=True): ...


class SpecRuleY(SpecHead, _RuleYOpen, closed=True): ...


class SpecSearch(SpecHead, _SearchOpen, closed=True): ...


class SpecSlider(SpecHead, _SliderOpen, closed=True): ...


class SpecSphere(SpecHead, _SphereOpen, closed=True): ...


class SpecSpike(SpecHead, _SpikeOpen, closed=True): ...


class SpecTable(SpecHead, _TableOpen, closed=True): ...


class SpecText(SpecHead, _TextOpen, closed=True): ...


class SpecTextX(SpecHead, _TextXOpen, closed=True): ...


class SpecTextY(SpecHead, _TextYOpen, closed=True): ...


class SpecTickX(SpecHead, _TickXOpen, closed=True): ...


class SpecTickY(SpecHead, _TickYOpen, closed=True): ...


class SpecVConcat(SpecHead, _VConcatOpen, closed=True): ...


class SpecVSpace(SpecHead, _VSpaceOpen, closed=True): ...


class SpecVector(SpecHead, _VectorOpen, closed=True): ...


class SpecVectorX(SpecHead, _VectorXOpen, closed=True): ...


class SpecVectorY(SpecHead, _VectorYOpen, closed=True): ...


class SpecVoronoi(SpecHead, _VoronoiOpen, closed=True): ...


class SpecVoronoiMesh(SpecHead, _VoronoiMeshOpen, closed=True): ...


class SpecWaffleX(SpecHead, _WaffleXOpen, closed=True): ...


class SpecWaffleY(SpecHead, _WaffleYOpen, closed=True): ...


class SpecDensityX1(SpecHead, _DensityX1Open, closed=True): ...


class SpecDensityX2(SpecHead, _DensityX2Open, closed=True): ...


class SpecDensityX3(SpecHead, _DensityX3Open, closed=True): ...


class SpecDensityX4(SpecHead, _DensityX4Open, closed=True): ...


class SpecDensityY1(SpecHead, _DensityY1Open, closed=True): ...


class SpecDensityY2(SpecHead, _DensityY2Open, closed=True): ...


class SpecDensityY3(SpecHead, _DensityY3Open, closed=True): ...


class SpecDensityY4(SpecHead, _DensityY4Open, closed=True): ...


Spec = TypeAliasType(
    "Spec",
    SpecArea
    | SpecAreaX
    | SpecAreaY
    | SpecArrow
    | SpecAxisFx
    | SpecAxisFy
    | SpecAxisX
    | SpecAxisY
    | SpecBarX
    | SpecBarY
    | SpecCell
    | SpecCellX
    | SpecCellY
    | SpecCircle
    | SpecContour
    | SpecDelaunayLink
    | SpecDelaunayMesh
    | SpecDenseLine
    | SpecDensity
    | SpecDot
    | SpecDotX
    | SpecDotY
    | SpecErrorBarX
    | SpecErrorBarY
    | SpecFrame
    | SpecGeo
    | SpecGraticule
    | SpecGridFx
    | SpecGridFy
    | SpecGridX
    | SpecGridY
    | SpecHConcat
    | SpecHSpace
    | SpecHeatmap
    | SpecHexagon
    | SpecHexbin
    | SpecHexgrid
    | SpecHull
    | SpecImage
    | SpecLegend
    | SpecLine
    | SpecLineX
    | SpecLineY
    | SpecLink
    | SpecMenu
    | SpecPlot
    | SpecRaster
    | SpecRasterTile
    | SpecRect
    | SpecRectX
    | SpecRectY
    | SpecRegressionY
    | SpecRuleX
    | SpecRuleY
    | SpecSearch
    | SpecSlider
    | SpecSphere
    | SpecSpike
    | SpecTable
    | SpecText
    | SpecTextX
    | SpecTextY
    | SpecTickX
    | SpecTickY
    | SpecVConcat
    | SpecVSpace
    | SpecVector
    | SpecVectorX
    | SpecVectorY
    | SpecVoronoi
    | SpecVoronoiMesh
    | SpecWaffleX
    | SpecWaffleY
    | SpecDensityX1
    | SpecDensityX2
    | SpecDensityX3
    | SpecDensityX4
    | SpecDensityY1
    | SpecDensityY2
    | SpecDensityY3
    | SpecDensityY4,
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
