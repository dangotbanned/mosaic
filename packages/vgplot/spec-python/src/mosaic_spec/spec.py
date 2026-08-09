from __future__ import annotations

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
from mosaic_spec._gen.mosaic import (
    Config,
    Data,
    Meta,
    Params,
    PlotAttributes,
    _HConcatOpen,
    _HSpaceOpen,
    _LegendOpen,
    _MenuOpen,
    _PlotOpen,
    _SearchOpen,
    _SliderOpen,
    _TableOpen,
    _VConcatOpen,
    _VSpaceOpen,
)
from mosaic_spec._typing_compat import TypeAliasType, TypedDict


class _SpecHead(TypedDict, total=False):
    config: Config
    """Configuration options."""
    meta: Meta
    """Specification metadata."""
    params: Params
    """Param and Selection definitions."""
    plot_defaults: PlotAttributes
    """A default set of attributes to apply to all plot components."""


class SpecHead(_SpecHead, total=False):
    data: Data
    """Dataset definitions."""


class HConcat(SpecHead, _HConcatOpen, closed=True): ...


class HSpace(SpecHead, _HSpaceOpen, closed=True): ...


class Legend(SpecHead, _LegendOpen, closed=True): ...


class Menu(SpecHead, _MenuOpen, closed=True): ...


class Plot(SpecHead, _PlotOpen, closed=True): ...


class Search(SpecHead, _SearchOpen, closed=True): ...


class Slider(SpecHead, _SliderOpen, closed=True): ...


class Table(SpecHead, _TableOpen, closed=True): ...


class VConcat(SpecHead, _VConcatOpen, closed=True): ...


class VSpace(SpecHead, _VSpaceOpen, closed=True): ...


class Area(_SpecHead, _AreaOpen, closed=True): ...


class AreaX(_SpecHead, _AreaXOpen, closed=True): ...


class AreaY(_SpecHead, _AreaYOpen, closed=True): ...


class Arrow(_SpecHead, _ArrowOpen, closed=True): ...


class AxisX(SpecHead, _AxisXOpen, closed=True): ...


class AxisY(SpecHead, _AxisYOpen, closed=True): ...


class AxisFx(SpecHead, _AxisFxOpen, closed=True): ...


class AxisFy(SpecHead, _AxisFyOpen, closed=True): ...


class GridX(SpecHead, _GridXOpen, closed=True): ...


class GridY(SpecHead, _GridYOpen, closed=True): ...


class GridFx(SpecHead, _GridFxOpen, closed=True): ...


class GridFy(SpecHead, _GridFyOpen, closed=True): ...


class BarX(_SpecHead, _BarXOpen, closed=True): ...


class BarY(_SpecHead, _BarYOpen, closed=True): ...


class Cell(_SpecHead, _CellOpen, closed=True): ...


class CellX(_SpecHead, _CellXOpen, closed=True): ...


class CellY(_SpecHead, _CellYOpen, closed=True): ...


class Contour(_SpecHead, _ContourOpen, closed=True): ...


class DelaunayLink(_SpecHead, _DelaunayLinkOpen, closed=True): ...


class DelaunayMesh(_SpecHead, _DelaunayMeshOpen, closed=True): ...


class Hull(_SpecHead, _HullOpen, closed=True): ...


class Voronoi(_SpecHead, _VoronoiOpen, closed=True): ...


class VoronoiMesh(_SpecHead, _VoronoiMeshOpen, closed=True): ...


class DenseLine(_SpecHead, _DenseLineOpen, closed=True): ...


class Density(_SpecHead, _DensityOpen, closed=True): ...


class DensityX1(_SpecHead, _DensityX1Open, closed=True): ...


class DensityX2(_SpecHead, _DensityX2Open, closed=True): ...


class DensityX3(_SpecHead, _DensityX3Open, closed=True): ...


class DensityX4(_SpecHead, _DensityX4Open, closed=True): ...


class DensityY1(_SpecHead, _DensityY1Open, closed=True): ...


class DensityY2(_SpecHead, _DensityY2Open, closed=True): ...


class DensityY3(_SpecHead, _DensityY3Open, closed=True): ...


class DensityY4(_SpecHead, _DensityY4Open, closed=True): ...


class Dot(_SpecHead, _DotOpen, closed=True): ...


class DotX(_SpecHead, _DotXOpen, closed=True): ...


class DotY(_SpecHead, _DotYOpen, closed=True): ...


class Circle(_SpecHead, _CircleOpen, closed=True): ...


class Hexagon(_SpecHead, _HexagonOpen, closed=True): ...


class ErrorBarX(_SpecHead, _ErrorBarXOpen, closed=True): ...


class ErrorBarY(_SpecHead, _ErrorBarYOpen, closed=True): ...


class Frame(SpecHead, _FrameOpen, closed=True): ...


class Geo(_SpecHead, _GeoOpen, closed=True): ...


class Graticule(SpecHead, _GraticuleOpen, closed=True): ...


class Sphere(SpecHead, _SphereOpen, closed=True): ...


class Hexbin(_SpecHead, _HexbinOpen, closed=True): ...


class Hexgrid(SpecHead, _HexgridOpen, closed=True): ...


class Image(_SpecHead, _ImageOpen, closed=True): ...


class Line(_SpecHead, _LineOpen, closed=True): ...


class LineX(_SpecHead, _LineXOpen, closed=True): ...


class LineY(_SpecHead, _LineYOpen, closed=True): ...


class Link(_SpecHead, _LinkOpen, closed=True): ...


class Raster(_SpecHead, _RasterOpen, closed=True): ...


class Heatmap(_SpecHead, _HeatmapOpen, closed=True): ...


class RasterTile(_SpecHead, _RasterTileOpen, closed=True): ...


class Rect(_SpecHead, _RectOpen, closed=True): ...


class RectX(_SpecHead, _RectXOpen, closed=True): ...


class RectY(_SpecHead, _RectYOpen, closed=True): ...


class RegressionY(_SpecHead, _RegressionYOpen, closed=True): ...


class RuleX(_SpecHead, _RuleXOpen, closed=True): ...


class RuleY(_SpecHead, _RuleYOpen, closed=True): ...


class Text(_SpecHead, _TextOpen, closed=True): ...


class TextX(_SpecHead, _TextXOpen, closed=True): ...


class TextY(_SpecHead, _TextYOpen, closed=True): ...


class TickX(_SpecHead, _TickXOpen, closed=True): ...


class TickY(_SpecHead, _TickYOpen, closed=True): ...


class Vector(_SpecHead, _VectorOpen, closed=True): ...


class VectorX(_SpecHead, _VectorXOpen, closed=True): ...


class VectorY(_SpecHead, _VectorYOpen, closed=True): ...


class Spike(_SpecHead, _SpikeOpen, closed=True): ...


class WaffleX(_SpecHead, _WaffleXOpen, closed=True): ...


class WaffleY(_SpecHead, _WaffleYOpen, closed=True): ...


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
    | DensityX1
    | DensityX2
    | DensityX3
    | DensityX4
    | DensityY1
    | DensityY2
    | DensityY3
    | DensityY4
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
    "DensityX1",
    "DensityX2",
    "DensityX3",
    "DensityX4",
    "DensityY1",
    "DensityY2",
    "DensityY3",
    "DensityY4",
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
