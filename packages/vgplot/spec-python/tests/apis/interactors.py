from __future__ import annotations

from typing import TYPE_CHECKING, Generic, Literal as L, final

import mosaic_spec as ms
from mosaic_spec._typing_compat import TypeAliasType as Type, TypeVar, Unpack

if TYPE_CHECKING:
    from _typeshed import Incomplete

    from tests.apis._interactors import (
        ChannelName,
        HighlightOptions,
        Interval1DOptions,
        IntervalOptions,
        NearestOptions,
        PanZoom1DOptions,
        PanZoomOptions,
        RegionOptions,
        ToggleOptions,
    )
    from tests.apis.params import Selection
    from tests.apis.protocols import DataDefs, ParamDefs

T = TypeVar("T", infer_variance=True)


OneOrMore = Type("OneOrMore", tuple[T, Unpack[tuple[T, ...]]], type_params=(T,))
_OutputT = TypeVar("_OutputT", bound=ms.PlotInteractor, infer_variance=True)


class _Interactor(Generic[_OutputT]):
    __slots__ = ()

    def to_dict(self, data: DataDefs, params: ParamDefs) -> _OutputT:
        msg = f"{self.__class__.__name__}.to_dict() is not yet implemented"
        raise NotImplementedError(msg)


@final
class Interval(_Interactor[ms.IntervalXY]):
    """Select a continuous 2D interval selection over both the `x` and `y` scale domains."""

    __slots__ = ("bind", "options")
    bind: Selection
    """The output selection.

    A clause of the form `field BETWEEN lo AND hi` is added for the currently selected interval [lo, hi].
    """
    options: IntervalOptions

    def __init__(self, bind: Selection, options: IntervalOptions) -> None:
        self.bind = bind
        self.options = options

    def to_dict(self, data: DataDefs, params: ParamDefs) -> ms.IntervalXY:
        # NOTE: Too painful to type 100%
        remap = {"field_x": "xfield", "field_y": "yfield"}
        opts: Incomplete = {remap.get(k, k): v for k, v in self.options.items()}
        return ms.IntervalXY(select="intervalXY", bind=self.bind.ref(params), **opts)


# TODO @dangotbanned: `Interval1D`, `Nearest`, `PanZoom1D` (+ some of `PanZoom` ) can share a base class
# - generic over options and select
# - add docs separately, but define slots in parent
@final
class Interval1D(_Interactor[ms.IntervalX | ms.IntervalY]):
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

    def to_dict(self, data: DataDefs, params: ParamDefs) -> ms.IntervalX | ms.IntervalY:
        bind = self.bind.ref(params)
        if self._select == "intervalX":
            return {"select": "intervalX", "bind": bind, **self.options}
        return {"select": "intervalY", "bind": bind, **self.options}


@final
class PanZoom(_Interactor[ms.Pan | ms.PanZoom]):
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

    def to_dict(self, data: DataDefs, params: ParamDefs) -> ms.Pan | ms.PanZoom:
        x = self.bind_x.ref(params)
        y = self.bind_y.ref(params)
        result: ms.Pan | ms.PanZoom
        if self._select == "pan":
            result = {"select": "pan", "x": x, "y": y}
        else:
            result = {"select": "panZoom", "x": x, "y": y}
        if opts := self.options:
            if xfield := opts.get("field_x"):
                result["xfield"] = xfield
            if yfield := opts.get("field_y"):
                result["yfield"] = yfield
        return result


@final
class PanZoom1D(_Interactor[ms.PanX | ms.PanZoomX | ms.PanY | ms.PanZoomY]):
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

    def to_dict(
        self, data: DataDefs, params: ParamDefs
    ) -> ms.PanX | ms.PanZoomX | ms.PanY | ms.PanZoomY:
        bind = self.bind.ref(params)
        select = self._select
        result: ms.PanX | ms.PanZoomX | ms.PanY | ms.PanZoomY
        # NOTE: 4 branches required for type checking :(
        match select:
            case "panX":
                result = {"select": select, "x": bind}
            case "panZoomX":
                result = {"select": select, "x": bind}
            case "panY":
                result = {"select": select, "y": bind}
            case _:
                result = {"select": select, "y": bind}
        if opts := self.options:
            if xfield := opts.get("field_x"):
                result["xfield"] = xfield
            if yfield := opts.get("field_y"):
                result["yfield"] = yfield
        return result


@final
class Nearest(_Interactor[ms.NearestX | ms.NearestY]):
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

    def to_dict(self, data: DataDefs, params: ParamDefs) -> ms.NearestX | ms.NearestY:
        bind = self.bind.ref(params)
        if self._select == "nearestX":
            return {"select": "nearestX", "bind": bind, **self.options}
        return {"select": "nearestY", "bind": bind, **self.options}


class _RegionToggle(_Interactor[_OutputT]):
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
class Region(_RegionToggle[ms.Region]):
    """Select aspects of individual marks within a 2D range."""

    __slots__ = ("options",)
    options: RegionOptions

    def __init__(
        self, bind: Selection, channels: OneOrMore[ChannelName], options: RegionOptions
    ) -> None:
        self.bind = bind
        self.channels = channels
        self.options = options

    def to_dict(self, data: DataDefs, params: ParamDefs) -> ms.Region:
        return {
            "select": "region",
            "bind": self.bind.ref(params),
            "channels": self.channels,
            **self.options,
        }


@final
class Toggle(_RegionToggle[ms.Toggle]):
    """Select individual data values by clicking / shift-clicking points."""

    __slots__ = ("options",)
    options: ToggleOptions

    def __init__(
        self, bind: Selection, channels: OneOrMore[ChannelName], options: ToggleOptions
    ) -> None:
        self.bind = bind
        self.channels = channels
        self.options = options

    def to_dict(self, data: DataDefs, params: ParamDefs) -> ms.Toggle:
        return {
            "select": "toggle",
            "bind": self.bind.ref(params),
            "channels": self.channels,
            **self.options,
        }


@final
class Highlight(_Interactor[ms.Highlight]):
    """Highlight selected marks by deemphasizing the others."""

    __slots__ = ("by", "options")
    by: Selection
    """The input selection. Unselected marks are deemphasized."""

    options: HighlightOptions

    def __init__(self, by: Selection, options: HighlightOptions) -> None:
        self.by = by
        self.options = options

    def to_dict(self, data: DataDefs, params: ParamDefs) -> ms.Highlight:
        return {"select": "highlight", "by": self.by.ref(params), **self.options}


Interactor = Type(
    "Interactor",
    Highlight | Interval | Interval1D | Nearest | PanZoom | PanZoom1D | Region | Toggle,
)
"""Interactors imbue plots with interactive behavior.

This includes selecting or highlighting values, and panning or zooming the display.

To determine which fields (database columns) an interactor should select,
an interactor defaults to looking at the corresponding encoding channels for the most recently added mark.
Alternatively, interactors accept options that explicitly indicate which data fields should be selected.
"""


def highlight(by: Selection, /, **options: Unpack[HighlightOptions]) -> Highlight:
    """Highlight selected marks by deemphasizing the others."""
    return Highlight(by, options)


def region(
    bind: Selection, *channels: Unpack[OneOrMore[ChannelName]], **options: Unpack[RegionOptions]
) -> Region:
    """Select aspects of individual marks within a 2D range."""
    return Region(bind, channels, options)


def toggle(
    bind: Selection, *channels: Unpack[OneOrMore[ChannelName]], **options: Unpack[ToggleOptions]
) -> Toggle:
    """Select individual data values by clicking / shift-clicking points."""
    return Toggle(bind, channels, options)


def interval(bind: Selection, /, **options: Unpack[IntervalOptions]) -> Interval:
    """Select a continuous 2D interval selection over both the `x` and `y` scale domains."""
    return Interval(bind, options)


def interval_x(bind: Selection, /, **options: Unpack[Interval1DOptions]) -> Interval1D:
    """Select a continuous 1D interval selection over the `x` scale domain."""
    return Interval1D(bind, "intervalX", options)


def interval_y(bind: Selection, /, **options: Unpack[Interval1DOptions]) -> Interval1D:
    """Select a continuous 1D interval selection over the `y` scale domain."""
    return Interval1D(bind, "intervalY", options)


def pan(bind_x: Selection, bind_y: Selection, /, **options: Unpack[PanZoomOptions]) -> PanZoom:
    """Pan a plot along both the `x` and `y` scales."""
    return PanZoom(bind_x, bind_y, "pan", options)


def pan_zoom(bind_x: Selection, bind_y: Selection, /, **options: Unpack[PanZoomOptions]) -> PanZoom:
    """Pan and zoom a plot along both the `x` and `y` scales."""
    return PanZoom(bind_x, bind_y, "panZoom", options)


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


def nearest_x(bind: Selection, /, **options: Unpack[NearestOptions]) -> Nearest:
    """Select values from the mark closest to the pointer *x* location."""
    return Nearest(bind, "nearestX", options)


def nearest_y(bind: Selection, /, **options: Unpack[NearestOptions]) -> Nearest:
    """Select values from the mark closest to the pointer *y* location."""
    return Nearest(bind, "nearestY", options)


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
