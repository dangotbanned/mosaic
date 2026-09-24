from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, Final, Literal as L, final

import mosaic_spec as ms
from mosaic_spec._typing_compat import TypeAliasType, TypedDict, TypeVar, Unpack

if TYPE_CHECKING:
    from collections.abc import Sequence

    from tests.apis.params import Selection

T = TypeVar("T", infer_variance=True)


OneOrMore = TypeAliasType("OneOrMore", tuple[T, Unpack[tuple[T, ...]]], type_params=(T,))

# NOTE: not sure why this isn't listed
ChannelName = TypeAliasType("ChannelName", ms.ChannelName | L["color"])
"""The set of known channel names."""


class HighlightOptions(TypedDict, total=False, closed=True):
    fill: str
    """The fill color of deemphasized marks.

    By default the fill is unchanged.
    """

    fill_opacity: float
    """The fill opacity of deemphasized marks.

    By default the fill opacity is unchanged.
    """

    opacity: float
    """The overall opacity of deemphasized marks.

    By default the opacity is set to 0.2.
    """

    stroke: str
    """The stroke color of deemphasized marks.

    By default the stroke is unchanged.
    """

    stroke_opacity: float
    """The stroke opacity of deemphasized marks.

    By default the stroke opacity is unchanged.
    """


# TODO @dangotbanned: Report `nearest` as missing from `Spec` exports
# https://github.com/uwdata/mosaic/blob/80c72fc4e360f354b57f5369e6799561d86272b6/packages/vgplot/spec/src/spec/PlotInteractor.ts#L4
# https://github.com/uwdata/mosaic/blob/80c72fc4e360f354b57f5369e6799561d86272b6/packages/vgplot/spec/src/spec/interactors/Nearest.ts#L32-L36
class NearestOptions(TypedDict, total=False, closed=True):
    channels: Sequence[ChannelName]
    """The encoding channels whose domain values should be selected.

    For example, a setting of `['color']` selects the data value backing the color channel,
    whereas `['x', 'z']` selects both x and z channel domain values.

    If unspecified, the selected channels default to match the current pointer settings:
    - a `nearestX` interactor selects the `['x']` channels,
    - a `nearest` interactor selects the `['x', 'y']` channels.
    """

    fields: Sequence[str]
    """The fields (database column names) to use in generated selection clause predicates.

    If unspecified, the fields backing the selected *channels* in the first valid prior mark definition are used by default.
    """

    max_radius: float
    """The maximum radius of a nearest selection (default 40).

    Marks with (x, y) coordinates outside this radius will not be selected as nearest points.
    """


class _Peers(TypedDict, total=False):
    peers: bool
    """A flag indicating if peer (sibling) marks are excluded when cross-filtering (default `true`).

    If set, peer marks will not be filtered by this interactor's selection in cross-filtering setups.
    """


class _BrushPeers(_Peers, total=False):
    brush: ms.BrushStyles
    """CSS styles for the brush (SVG `rect`) element."""


class ToggleOptions(_Peers, closed=True): ...


class RegionOptions(_BrushPeers, closed=True): ...


class _IntervalOptions(_BrushPeers, total=False):
    pixel_size: float
    """The size of an interactive pixel (default `1`).

    Larger pixel sizes reduce the brush resolution, which can reduce the size of pre-aggregated materialized views.
    """


class _1DOptions(TypedDict, total=False):
    field: str
    """The name of the field (database column) over which the selection should be defined.

    If unspecified, the channel field of the first valid prior mark definition is used.
    """


# NOTE: Renamed `{x,y}field` -> `field_{x,y}`
class _2DOptions(TypedDict, total=False):
    field_x: str
    """The name of the field (database column) over which the `x`-component of the selection should be defined.

    If unspecified, the `x` channel field of the first valid prior mark definition is used.
    """
    field_y: str
    """The name of the field (database column) over which the `y`-component of the selection should be defined.

    If unspecified, the `y` channel field of the first valid prior mark definition is used.
    """


class Interval1DOptions(_IntervalOptions, _1DOptions, closed=True): ...


class IntervalOptions(_IntervalOptions, _2DOptions, closed=True): ...


class PanZoom1DOptions(_1DOptions, closed=True): ...


class PanZoomOptions(_2DOptions, closed=True): ...


_SelectKind = TypeAliasType(
    "_SelectKind",
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


class _Interactor:
    __slots__ = ()

    @property
    def select(self) -> _SelectKind:
        msg = f"{self.__class__.__name__}.select is not yet implemented"
        raise NotImplementedError(msg)

    def to_dict(
        self, data: dict[str, ms.DataDefinition], params: dict[str, ms.ParamDefinition]
    ) -> ms.PlotInteractor:
        msg = f"{self.__class__.__name__}.to_dict() is not yet implemented"
        raise NotImplementedError(msg)


class _SelectStatic(_Interactor):
    __slots__ = ()
    _SELECT: ClassVar[_SelectKind]

    @property
    def select(self) -> _SelectKind:
        return self._SELECT


@final
class Interval(_SelectStatic):
    """Select a continuous 2D interval selection over both the `x` and `y` scale domains."""

    __slots__ = ("bind", "options")
    bind: Selection
    """The output selection.

    A clause of the form `field BETWEEN lo AND hi` is added for the currently selected interval [lo, hi].
    """
    options: IntervalOptions
    _SELECT = "intervalXY"

    def __init__(self, bind: Selection, /, **options: Unpack[IntervalOptions]) -> None:
        self.bind = bind
        self.options = options


# TODO @dangotbanned: `Interval1D`, `Nearest`, `PanZoom1D` (+ some of `PanZoom` ) can share a base class
# - generic over options and select
# - add docs separately, but define slots in parent
@final
class Interval1D(_Interactor):
    """Select a continuous 1D interval selection over either the `x` or `y` scale domain."""

    __slots__ = ("_select", "bind", "options")
    bind: Selection
    """The output selection.

    A clause of the form `field BETWEEN lo AND hi` is added for the currently selected interval [lo, hi].
    """

    options: Interval1DOptions

    def __init__(
        self, bind: Selection, select: L["intervalX", "intervalY"], options: Interval1DOptions
    ) -> None:
        self.bind = bind
        self._select: L["intervalX", "intervalY"] = select
        self.options = options

    @property
    def select(self) -> L["intervalX", "intervalY"]:
        return self._select


def interval_x(bind: Selection, /, **options: Unpack[Interval1DOptions]) -> Interval1D:
    """Select a continuous 1D interval selection over the `x` scale domain."""
    return Interval1D(bind, "intervalX", options)


def interval_y(bind: Selection, /, **options: Unpack[Interval1DOptions]) -> Interval1D:
    """Select a continuous 1D interval selection over the `y` scale domain."""
    return Interval1D(bind, "intervalY", options)


@final
class PanZoom(_Interactor):
    """Pan/zoom along both the `x` and `y` scales."""

    __slots__ = ("_select", "bind_x", "bind_y", "options")
    bind_x: Selection
    bind_y: Selection
    options: PanZoomOptions

    def __init__(
        self,
        bind_x: Selection,
        bind_y: Selection,
        select: L["pan", "panZoom"],
        options: PanZoomOptions,
    ) -> None:
        self.bind_x = bind_x
        self.bind_y = bind_y
        self._select: L["pan", "panZoom"] = select
        self.options = options

    @property
    def select(self) -> L["pan", "panZoom"]:
        return self._select


def pan(bind_x: Selection, bind_y: Selection, /, **options: Unpack[PanZoomOptions]) -> PanZoom:
    """Pan a plot along both the `x` and `y` scales."""
    return PanZoom(bind_x, bind_y, "pan", options)


def pan_zoom(bind_x: Selection, bind_y: Selection, /, **options: Unpack[PanZoomOptions]) -> PanZoom:
    """Pan and zoom a plot along both the `x` and `y` scales."""
    return PanZoom(bind_x, bind_y, "panZoom", options)


@final
class PanZoom1D(_Interactor):
    """Pan/zoom along either the `x` or `y` scale."""

    __slots__ = ("_select", "bind", "options")
    bind: Selection
    """The output selection.

    A clause of the form `field BETWEEN value1 AND value2` is added for the current pan/zoom interval [value1, value2].
    """

    options: PanZoom1DOptions

    def __init__(
        self,
        bind: Selection,
        select: L["panX", "panY", "panZoomX", "panZoomY"],
        options: PanZoom1DOptions,
    ) -> None:
        self.bind = bind
        self._select: L["panX", "panY", "panZoomX", "panZoomY"] = select
        self.options = options

    @property
    def select(self) -> L["panX", "panY", "panZoomX", "panZoomY"]:
        return self._select


def pan_x(bind: Selection, /, **options: Unpack[PanZoom1DOptions]) -> PanZoom1D:
    """Pan a plot along the `x` scale only."""
    return PanZoom1D(bind, "panX", options)


def pan_y(bind: Selection, /, **options: Unpack[PanZoom1DOptions]) -> PanZoom1D:
    """Pan a plot along the `y` scale only."""
    return PanZoom1D(bind, "panY", options)


def pan_zoom_x(bind: Selection, /, **options: Unpack[PanZoom1DOptions]) -> PanZoom1D:
    """Pan and zoom a plot along the `x` scale only."""
    return PanZoom1D(bind, "panZoomX", options)


def pan_zoom_y(bind: Selection, /, **options: Unpack[PanZoom1DOptions]) -> PanZoom1D:
    """Pan and zoom a plot along the `y` scale only."""
    return PanZoom1D(bind, "panZoomY", options)


@final
class Nearest(_Interactor):
    __slots__ = ("_select", "bind", "options")
    bind: Selection
    """The output selection.

    A clause of the form `field = value` is added for the currently nearest value.
    """

    options: NearestOptions

    def __init__(
        self, bind: Selection, select: L["nearestX", "nearestY"], options: NearestOptions
    ) -> None:
        self.bind = bind
        self._select: L["nearestX", "nearestY"] = select
        self.options = options

    @property
    def select(self) -> L["nearestX", "nearestY"]:
        return self._select


def nearest_x(bind: Selection, /, **options: Unpack[NearestOptions]) -> Nearest:
    """Select values from the mark closest to the pointer *x* location."""
    return Nearest(bind, "nearestX", options)


def nearest_y(bind: Selection, /, **options: Unpack[NearestOptions]) -> Nearest:
    """Select values from the mark closest to the pointer *y* location."""
    return Nearest(bind, "nearestY", options)


class _RegionToggle(_SelectStatic):
    __slots__ = ("bind", "channels")
    bind: Selection
    """The output selection.

    A clause of the form `(field = value1) OR (field = value2) ...` is added for the currently selected values.
    """

    channels: OneOrMore[ChannelName]
    """The encoding channels over which to select values.

    For a selected mark, selection clauses will cover the backing data fields for each channel.
    """


@final
class Region(_RegionToggle):
    """Select aspects of individual marks within a 2D range."""

    __slots__ = ("options",)
    options: RegionOptions
    _SELECT = "region"

    def __init__(
        self,
        bind: Selection,
        *channels: Unpack[OneOrMore[ChannelName]],
        **options: Unpack[RegionOptions],
    ) -> None:
        self.bind = bind
        self.channels = channels
        self.options = options


# TODO @dangotbanned: Report `ToggleZ` as missing from `Spec` exports (less important than `Nearest`)
# https://github.com/uwdata/mosaic/blob/80c72fc4e360f354b57f5369e6799561d86272b6/packages/vgplot/spec/src/spec/PlotInteractor.ts#L7
# https://github.com/uwdata/mosaic/blob/80c72fc4e360f354b57f5369e6799561d86272b6/packages/vgplot/spec/src/spec/interactors/Toggle.ts#L49-L56
@final
class Toggle(_RegionToggle):
    """Select individual data values by clicking / shift-clicking points."""

    __slots__ = ("options",)
    options: ToggleOptions
    _SELECT = "toggle"

    def __init__(
        self,
        bind: Selection,
        *channels: Unpack[OneOrMore[ChannelName]],
        **options: Unpack[ToggleOptions],
    ) -> None:
        self.bind = bind
        self.channels = channels
        self.options = options


@final
class Highlight(_SelectStatic):
    """Highlight selected marks by deemphasizing the others."""

    __slots__ = ("by", "options")
    by: Selection
    """The input selection. Unselected marks are deemphasized."""

    options: HighlightOptions
    _SELECT = "highlight"

    def __init__(self, by: Selection, /, **options: Unpack[HighlightOptions]) -> None:
        self.by = by
        self.options = options


Interactor = TypeAliasType(
    "Interactor",
    Highlight | Interval | Interval1D | Nearest | PanZoom | PanZoom1D | Region | Toggle,
)
"""Interactors imbue plots with interactive behavior.

This includes selecting or highlighting values, and panning or zooming the display.

To determine which fields (database columns) an interactor should select,
an interactor defaults to looking at the corresponding encoding channels for the most recently added mark.
Alternatively, interactors accept options that explicitly indicate which data fields should be selected.
"""

# NOTE: constructor aliases for symmetry or whatever
interval: Final = Interval
highlight: Final = Highlight
region: Final = Region
toggle: Final = Toggle

__all__ = (
    "Interactor",
    "highlight",
    "interval",
    "interval_x",
    "interval_y",
    "nearest_x",
    "nearest_y",
    "pan",
    "pan_x",
    "pan_y",
    "pan_zoom",
    "pan_zoom_x",
    "pan_zoom_y",
    "region",
    "toggle",
)
