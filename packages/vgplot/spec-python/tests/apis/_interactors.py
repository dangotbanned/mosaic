from __future__ import annotations

from typing import TYPE_CHECKING, Literal as L

import mosaic_spec as ms
from mosaic_spec._typing_compat import TypeAliasType as Type, TypedDict

if TYPE_CHECKING:
    from collections.abc import Sequence


# NOTE: not sure why this isn't listed
ChannelName = Type("ChannelName", ms.ChannelName | L["color"])
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
