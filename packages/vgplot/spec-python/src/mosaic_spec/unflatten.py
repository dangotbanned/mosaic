from __future__ import annotations

from typing import TYPE_CHECKING, Any, Generic, Literal

from mosaic_spec._typing_compat import TypedDict, TypeVar

if TYPE_CHECKING:
    from collections.abc import Sequence

    from mosaic_spec._gen import Fixed, Interval, ParamRef


## Current
class PlotAttributes(TypedDict, total=False):
    """The current `{fx,fy}_*` fields-only."""

    fx_align: float | ParamRef
    fx_aria_description: str | ParamRef
    fx_aria_label: str | ParamRef
    fx_axis: Literal["top", "bottom", "both"] | bool | ParamRef | None
    fx_domain: Sequence[Any] | Fixed | ParamRef
    fx_font_variant: str | ParamRef
    fx_grid: bool | str | Interval | Sequence[Any] | ParamRef
    fx_inset: float | ParamRef
    fx_inset_left: float | ParamRef
    fx_inset_right: float | ParamRef
    fx_label: str | ParamRef | None
    fx_label_anchor: Literal["top", "right", "bottom", "left", "center"] | ParamRef
    fx_label_offset: float | ParamRef
    fx_line: bool | ParamRef
    fx_padding: float | ParamRef
    fx_padding_inner: float | ParamRef
    fx_padding_outer: float | ParamRef
    fx_range: Sequence[Any] | Fixed | ParamRef
    fx_reverse: bool | ParamRef
    fx_round: bool | ParamRef
    fx_tick_format: str | ParamRef | None
    fx_tick_padding: float | ParamRef
    fx_tick_rotate: float | ParamRef
    fx_tick_size: float | ParamRef
    fx_tick_spacing: float | ParamRef
    fx_ticks: float | Interval | Sequence[Any] | ParamRef
    fy_align: float | ParamRef
    fy_aria_description: str | ParamRef
    fy_aria_label: str | ParamRef
    fy_axis: Literal["left", "right", "both"] | bool | ParamRef | None
    fy_domain: Sequence[Any] | Fixed | ParamRef
    fy_font_variant: str | ParamRef
    fy_grid: bool | str | Interval | Sequence[Any] | ParamRef
    fy_inset: float | ParamRef
    fy_inset_bottom: float | ParamRef
    fy_inset_top: float | ParamRef
    fy_label: str | ParamRef | None
    fy_label_anchor: Literal["top", "right", "bottom", "left", "center"] | ParamRef
    fy_label_offset: float | ParamRef
    fy_line: bool | ParamRef
    fy_padding: float | ParamRef
    fy_padding_inner: float | ParamRef
    fy_padding_outer: float | ParamRef
    fy_range: Sequence[Any] | Fixed | ParamRef
    fy_reverse: bool | ParamRef
    fy_round: bool | ParamRef
    fy_tick_format: str | ParamRef | None
    fy_tick_padding: float | ParamRef
    fy_tick_rotate: float | ParamRef
    fy_tick_size: float | ParamRef
    fy_tick_spacing: float | ParamRef
    fy_ticks: float | Interval | Sequence[Any] | ParamRef


## Split up parts
class Padding(TypedDict, total=False):
    inner: float | ParamRef
    outer: float | ParamRef


class FxInset(TypedDict, total=False):
    left: float | ParamRef
    right: float | ParamRef


class FyInset(TypedDict, total=False):
    bottom: float | ParamRef
    top: float | ParamRef


class Inset(FxInset, FyInset, total=False): ...


class Label:
    label: str | ParamRef | None
    anchor: Literal["top", "right", "bottom", "left", "center"] | ParamRef
    offset: float | ParamRef


class Tick(TypedDict, total=False):
    format: str | ParamRef | None
    padding: float | ParamRef
    rotate: float | ParamRef
    size: float | ParamRef
    spacing: float | ParamRef


class Aria(TypedDict, total=False):
    description: str | ParamRef
    label: str | ParamRef


AxisT = TypeVar("AxisT")
InsetT = TypeVar("InsetT")


class _FBase(TypedDict, Generic[AxisT, InsetT], total=False):
    align: float | ParamRef
    aria: Aria
    axis: bool | ParamRef | AxisT | None
    domain: Sequence[Any] | Fixed | ParamRef
    font_variant: str | ParamRef
    grid: bool | str | Interval | Sequence[Any] | ParamRef
    inset: float | ParamRef | InsetT
    label: str | ParamRef | Label | None
    line: bool | ParamRef
    padding: float | ParamRef | Padding
    range: Sequence[Any] | Fixed | ParamRef
    reverse: bool | ParamRef
    round: bool | ParamRef
    tick: Tick
    ticks: float | Interval | Sequence[Any] | ParamRef


class Fx(_FBase[Literal["top", "bottom", "both"], FxInset], total=False): ...


class Fy(_FBase[Literal["left", "right", "both"], FyInset], total=False): ...


## 50 fields -> 2 fields
class PlotAttributesV2(TypedDict, total=False):
    fx: Fx
    fy: Fy


example: PlotAttributes = {
    "fx_padding_inner": 2,
    "fx_aria_label": "hello",
    "fx_inset": 100,
    "fy_padding": 2,
    "fy_tick_size": 10,
    "fy_inset_bottom": 20,
}

example_v2: PlotAttributesV2 = {
    "fx": {"padding": {"inner": 2}, "aria": {"label": "hello"}, "inset": 100},
    "fy": {"padding": 2, "tick": {"size": 10}, "inset": {"bottom": 20}},
}
