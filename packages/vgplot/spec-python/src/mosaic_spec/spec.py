# Generated: `mosaic_spec.spec`
from __future__ import annotations

from typing import TYPE_CHECKING

from mosaic_spec._gen.inputs import _MenuOpen, _SearchOpen, _SliderOpen, _TableOpen
from mosaic_spec._gen.layout import _HConcatOpen, _HSpaceOpen, _VConcatOpen, _VSpaceOpen
from mosaic_spec._gen.marks import (
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
    _DensityXAreaXOpen,
    _DensityXDotXOpen,
    _DensityXLineXOpen,
    _DensityXTextXOpen,
    _DensityYAreaYOpen,
    _DensityYDotOpen,
    _DensityYLineYOpen,
    _DensityYTextOpen,
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
    _HeatmapOpen,
    _HexagonOpen,
    _HexbinOpen,
    _HexgridOpen,
    _HullOpen,
    _ImageOpen,
    _LineOpen,
    _LineXOpen,
    _LineYOpen,
    _LinkOpen,
    _RasterOpen,
    _RasterTileOpen,
    _RectOpen,
    _RectXOpen,
    _RectYOpen,
    _RegressionYOpen,
    _RuleXOpen,
    _RuleYOpen,
    _SphereOpen,
    _SpikeOpen,
    _TextOpen,
    _TextXOpen,
    _TextYOpen,
    _TickXOpen,
    _TickYOpen,
    _VectorOpen,
    _VectorXOpen,
    _VectorYOpen,
    _VoronoiMeshOpen,
    _VoronoiOpen,
    _WaffleXOpen,
    _WaffleYOpen,
)
from mosaic_spec._gen.plot import PlotAttributes, _PlotOpen
from mosaic_spec._gen.plot_legend import _LegendOpen
from mosaic_spec._typing_compat import TypeAliasType, TypedDict

if TYPE_CHECKING:
    from mosaic_spec._gen.data import Data
    from mosaic_spec._gen.mosaic import Config, Meta
    from mosaic_spec._gen.params import Params


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


class Area(SpecHead, _AreaOpen, closed=True): ...


class AreaX(SpecHead, _AreaXOpen, closed=True): ...


class AreaY(SpecHead, _AreaYOpen, closed=True): ...


class Arrow(SpecHead, _ArrowOpen, closed=True): ...


class AxisFx(SpecHead, _AxisFxOpen, closed=True): ...


class AxisFy(SpecHead, _AxisFyOpen, closed=True): ...


class AxisX(SpecHead, _AxisXOpen, closed=True): ...


class AxisY(SpecHead, _AxisYOpen, closed=True): ...


class BarX(SpecHead, _BarXOpen, closed=True): ...


class BarY(SpecHead, _BarYOpen, closed=True): ...


class Cell(SpecHead, _CellOpen, closed=True): ...


class CellX(SpecHead, _CellXOpen, closed=True): ...


class CellY(SpecHead, _CellYOpen, closed=True): ...


class Circle(SpecHead, _CircleOpen, closed=True): ...


class Contour(SpecHead, _ContourOpen, closed=True): ...


class DelaunayLink(SpecHead, _DelaunayLinkOpen, closed=True): ...


class DelaunayMesh(SpecHead, _DelaunayMeshOpen, closed=True): ...


class DenseLine(SpecHead, _DenseLineOpen, closed=True): ...


class Density(SpecHead, _DensityOpen, closed=True): ...


class DensityXAreaX(SpecHead, _DensityXAreaXOpen, closed=True): ...


class DensityXDotX(SpecHead, _DensityXDotXOpen, closed=True): ...


class DensityXLineX(SpecHead, _DensityXLineXOpen, closed=True): ...


class DensityXTextX(SpecHead, _DensityXTextXOpen, closed=True): ...


class DensityYAreaY(SpecHead, _DensityYAreaYOpen, closed=True): ...


class DensityYDot(SpecHead, _DensityYDotOpen, closed=True): ...


class DensityYLineY(SpecHead, _DensityYLineYOpen, closed=True): ...


class DensityYText(SpecHead, _DensityYTextOpen, closed=True): ...


class Dot(SpecHead, _DotOpen, closed=True): ...


class DotX(SpecHead, _DotXOpen, closed=True): ...


class DotY(SpecHead, _DotYOpen, closed=True): ...


class ErrorBarX(SpecHead, _ErrorBarXOpen, closed=True): ...


class ErrorBarY(SpecHead, _ErrorBarYOpen, closed=True): ...


class Frame(SpecHead, _FrameOpen, closed=True): ...


class Geo(SpecHead, _GeoOpen, closed=True): ...


class Graticule(SpecHead, _GraticuleOpen, closed=True): ...


class GridFx(SpecHead, _GridFxOpen, closed=True): ...


class GridFy(SpecHead, _GridFyOpen, closed=True): ...


class GridX(SpecHead, _GridXOpen, closed=True): ...


class GridY(SpecHead, _GridYOpen, closed=True): ...


class HConcat(SpecHead, _HConcatOpen, closed=True): ...


class HSpace(SpecHead, _HSpaceOpen, closed=True): ...


class Heatmap(SpecHead, _HeatmapOpen, closed=True): ...


class Hexagon(SpecHead, _HexagonOpen, closed=True): ...


class Hexbin(SpecHead, _HexbinOpen, closed=True): ...


class Hexgrid(SpecHead, _HexgridOpen, closed=True): ...


class Hull(SpecHead, _HullOpen, closed=True): ...


class Image(SpecHead, _ImageOpen, closed=True): ...


class Legend(SpecHead, _LegendOpen, closed=True): ...


class Line(SpecHead, _LineOpen, closed=True): ...


class LineX(SpecHead, _LineXOpen, closed=True): ...


class LineY(SpecHead, _LineYOpen, closed=True): ...


class Link(SpecHead, _LinkOpen, closed=True): ...


class Menu(SpecHead, _MenuOpen, closed=True): ...


class Plot(SpecHead, _PlotOpen, closed=True): ...


class Raster(SpecHead, _RasterOpen, closed=True): ...


class RasterTile(SpecHead, _RasterTileOpen, closed=True): ...


class Rect(SpecHead, _RectOpen, closed=True): ...


class RectX(SpecHead, _RectXOpen, closed=True): ...


class RectY(SpecHead, _RectYOpen, closed=True): ...


class RegressionY(SpecHead, _RegressionYOpen, closed=True): ...


class RuleX(SpecHead, _RuleXOpen, closed=True): ...


class RuleY(SpecHead, _RuleYOpen, closed=True): ...


class Search(SpecHead, _SearchOpen, closed=True): ...


class Slider(SpecHead, _SliderOpen, closed=True): ...


class Sphere(SpecHead, _SphereOpen, closed=True): ...


class Spike(SpecHead, _SpikeOpen, closed=True): ...


class Table(SpecHead, _TableOpen, closed=True): ...


class Text(SpecHead, _TextOpen, closed=True): ...


class TextX(SpecHead, _TextXOpen, closed=True): ...


class TextY(SpecHead, _TextYOpen, closed=True): ...


class TickX(SpecHead, _TickXOpen, closed=True): ...


class TickY(SpecHead, _TickYOpen, closed=True): ...


class VConcat(SpecHead, _VConcatOpen, closed=True): ...


class VSpace(SpecHead, _VSpaceOpen, closed=True): ...


class Vector(SpecHead, _VectorOpen, closed=True): ...


class VectorX(SpecHead, _VectorXOpen, closed=True): ...


class VectorY(SpecHead, _VectorYOpen, closed=True): ...


class Voronoi(SpecHead, _VoronoiOpen, closed=True): ...


class VoronoiMesh(SpecHead, _VoronoiMeshOpen, closed=True): ...


class WaffleX(SpecHead, _WaffleXOpen, closed=True): ...


class WaffleY(SpecHead, _WaffleYOpen, closed=True): ...


Spec = TypeAliasType(
    "Spec",
    Area
    | AreaX
    | AreaY
    | Arrow
    | AxisFx
    | AxisFy
    | AxisX
    | AxisY
    | BarX
    | BarY
    | Cell
    | CellX
    | CellY
    | Circle
    | Contour
    | DelaunayLink
    | DelaunayMesh
    | DenseLine
    | Density
    | DensityXAreaX
    | DensityXDotX
    | DensityXLineX
    | DensityXTextX
    | DensityYAreaY
    | DensityYDot
    | DensityYLineY
    | DensityYText
    | Dot
    | DotX
    | DotY
    | ErrorBarX
    | ErrorBarY
    | Frame
    | Geo
    | Graticule
    | GridFx
    | GridFy
    | GridX
    | GridY
    | HConcat
    | HSpace
    | Heatmap
    | Hexagon
    | Hexbin
    | Hexgrid
    | Hull
    | Image
    | Legend
    | Line
    | LineX
    | LineY
    | Link
    | Menu
    | Plot
    | Raster
    | RasterTile
    | Rect
    | RectX
    | RectY
    | RegressionY
    | RuleX
    | RuleY
    | Search
    | Slider
    | Sphere
    | Spike
    | Table
    | Text
    | TextX
    | TextY
    | TickX
    | TickY
    | VConcat
    | VSpace
    | Vector
    | VectorX
    | VectorY
    | Voronoi
    | VoronoiMesh
    | WaffleX
    | WaffleY,
)
"""A declarative Mosaic specification."""


__all__ = (
    "Area",
    "AreaX",
    "AreaY",
    "Arrow",
    "AxisFx",
    "AxisFy",
    "AxisX",
    "AxisY",
    "BarX",
    "BarY",
    "Cell",
    "CellX",
    "CellY",
    "Circle",
    "Contour",
    "DelaunayLink",
    "DelaunayMesh",
    "DenseLine",
    "Density",
    "DensityXAreaX",
    "DensityXDotX",
    "DensityXLineX",
    "DensityXTextX",
    "DensityYAreaY",
    "DensityYDot",
    "DensityYLineY",
    "DensityYText",
    "Dot",
    "DotX",
    "DotY",
    "ErrorBarX",
    "ErrorBarY",
    "Frame",
    "Geo",
    "Graticule",
    "GridFx",
    "GridFy",
    "GridX",
    "GridY",
    "HConcat",
    "HSpace",
    "Heatmap",
    "Hexagon",
    "Hexbin",
    "Hexgrid",
    "Hull",
    "Image",
    "Legend",
    "Line",
    "LineX",
    "LineY",
    "Link",
    "Menu",
    "Plot",
    "Raster",
    "RasterTile",
    "Rect",
    "RectX",
    "RectY",
    "RegressionY",
    "RuleX",
    "RuleY",
    "Search",
    "Slider",
    "Spec",
    "SpecHead",
    "Sphere",
    "Spike",
    "Table",
    "Text",
    "TextX",
    "TextY",
    "TickX",
    "TickY",
    "VConcat",
    "VSpace",
    "Vector",
    "VectorX",
    "VectorY",
    "Voronoi",
    "VoronoiMesh",
    "WaffleX",
    "WaffleY",
)
