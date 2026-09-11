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


class Area(SpecHead, _AreaOpen, total=False, closed=True): ...


class AreaX(SpecHead, _AreaXOpen, total=False, closed=True): ...


class AreaY(SpecHead, _AreaYOpen, total=False, closed=True): ...


class Arrow(SpecHead, _ArrowOpen, total=False, closed=True): ...


class AxisFx(SpecHead, _AxisFxOpen, total=False, closed=True): ...


class AxisFy(SpecHead, _AxisFyOpen, total=False, closed=True): ...


class AxisX(SpecHead, _AxisXOpen, total=False, closed=True): ...


class AxisY(SpecHead, _AxisYOpen, total=False, closed=True): ...


class BarX(SpecHead, _BarXOpen, total=False, closed=True): ...


class BarY(SpecHead, _BarYOpen, total=False, closed=True): ...


class Cell(SpecHead, _CellOpen, total=False, closed=True): ...


class CellX(SpecHead, _CellXOpen, total=False, closed=True): ...


class CellY(SpecHead, _CellYOpen, total=False, closed=True): ...


class Circle(SpecHead, _CircleOpen, total=False, closed=True): ...


class Contour(SpecHead, _ContourOpen, total=False, closed=True): ...


class DelaunayLink(SpecHead, _DelaunayLinkOpen, total=False, closed=True): ...


class DelaunayMesh(SpecHead, _DelaunayMeshOpen, total=False, closed=True): ...


class DenseLine(SpecHead, _DenseLineOpen, total=False, closed=True): ...


class Density(SpecHead, _DensityOpen, total=False, closed=True): ...


class DensityXAreaX(SpecHead, _DensityXAreaXOpen, total=False, closed=True): ...


class DensityXDotX(SpecHead, _DensityXDotXOpen, total=False, closed=True): ...


class DensityXLineX(SpecHead, _DensityXLineXOpen, total=False, closed=True): ...


class DensityXTextX(SpecHead, _DensityXTextXOpen, total=False, closed=True): ...


class DensityYAreaY(SpecHead, _DensityYAreaYOpen, total=False, closed=True): ...


class DensityYDot(SpecHead, _DensityYDotOpen, total=False, closed=True): ...


class DensityYLineY(SpecHead, _DensityYLineYOpen, total=False, closed=True): ...


class DensityYText(SpecHead, _DensityYTextOpen, total=False, closed=True): ...


class Dot(SpecHead, _DotOpen, total=False, closed=True): ...


class DotX(SpecHead, _DotXOpen, total=False, closed=True): ...


class DotY(SpecHead, _DotYOpen, total=False, closed=True): ...


class ErrorBarX(SpecHead, _ErrorBarXOpen, total=False, closed=True): ...


class ErrorBarY(SpecHead, _ErrorBarYOpen, total=False, closed=True): ...


class Frame(SpecHead, _FrameOpen, total=False, closed=True): ...


class Geo(SpecHead, _GeoOpen, total=False, closed=True): ...


class Graticule(SpecHead, _GraticuleOpen, total=False, closed=True): ...


class GridFx(SpecHead, _GridFxOpen, total=False, closed=True): ...


class GridFy(SpecHead, _GridFyOpen, total=False, closed=True): ...


class GridX(SpecHead, _GridXOpen, total=False, closed=True): ...


class GridY(SpecHead, _GridYOpen, total=False, closed=True): ...


class HConcat(SpecHead, _HConcatOpen, total=False, closed=True): ...


class HSpace(SpecHead, _HSpaceOpen, total=False, closed=True): ...


class Heatmap(SpecHead, _HeatmapOpen, total=False, closed=True): ...


class Hexagon(SpecHead, _HexagonOpen, total=False, closed=True): ...


class Hexbin(SpecHead, _HexbinOpen, total=False, closed=True): ...


class Hexgrid(SpecHead, _HexgridOpen, total=False, closed=True): ...


class Hull(SpecHead, _HullOpen, total=False, closed=True): ...


class Image(SpecHead, _ImageOpen, total=False, closed=True): ...


class Legend(SpecHead, _LegendOpen, total=False, closed=True): ...


class Line(SpecHead, _LineOpen, total=False, closed=True): ...


class LineX(SpecHead, _LineXOpen, total=False, closed=True): ...


class LineY(SpecHead, _LineYOpen, total=False, closed=True): ...


class Link(SpecHead, _LinkOpen, total=False, closed=True): ...


class Menu(SpecHead, _MenuOpen, total=False, closed=True): ...


class Plot(SpecHead, _PlotOpen, total=False, closed=True): ...


class Raster(SpecHead, _RasterOpen, total=False, closed=True): ...


class RasterTile(SpecHead, _RasterTileOpen, total=False, closed=True): ...


class Rect(SpecHead, _RectOpen, total=False, closed=True): ...


class RectX(SpecHead, _RectXOpen, total=False, closed=True): ...


class RectY(SpecHead, _RectYOpen, total=False, closed=True): ...


class RegressionY(SpecHead, _RegressionYOpen, total=False, closed=True): ...


class RuleX(SpecHead, _RuleXOpen, total=False, closed=True): ...


class RuleY(SpecHead, _RuleYOpen, total=False, closed=True): ...


class Search(SpecHead, _SearchOpen, total=False, closed=True): ...


class Slider(SpecHead, _SliderOpen, total=False, closed=True): ...


class Sphere(SpecHead, _SphereOpen, total=False, closed=True): ...


class Spike(SpecHead, _SpikeOpen, total=False, closed=True): ...


class Table(SpecHead, _TableOpen, total=False, closed=True): ...


class Text(SpecHead, _TextOpen, total=False, closed=True): ...


class TextX(SpecHead, _TextXOpen, total=False, closed=True): ...


class TextY(SpecHead, _TextYOpen, total=False, closed=True): ...


class TickX(SpecHead, _TickXOpen, total=False, closed=True): ...


class TickY(SpecHead, _TickYOpen, total=False, closed=True): ...


class VConcat(SpecHead, _VConcatOpen, total=False, closed=True): ...


class VSpace(SpecHead, _VSpaceOpen, total=False, closed=True): ...


class Vector(SpecHead, _VectorOpen, total=False, closed=True): ...


class VectorX(SpecHead, _VectorXOpen, total=False, closed=True): ...


class VectorY(SpecHead, _VectorYOpen, total=False, closed=True): ...


class Voronoi(SpecHead, _VoronoiOpen, total=False, closed=True): ...


class VoronoiMesh(SpecHead, _VoronoiMeshOpen, total=False, closed=True): ...


class WaffleX(SpecHead, _WaffleXOpen, total=False, closed=True): ...


class WaffleY(SpecHead, _WaffleYOpen, total=False, closed=True): ...


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
