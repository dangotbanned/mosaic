"""Replaces `ms.Plot(Attributes)` with the versions defined here.

Requires redefining everywhere that `ms.Component` is used.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Union

import mosaic_spec as ms
from mosaic_spec._typing_compat import TypeAliasType, TypedDict
from tests.apis.attributes import PlotAttributes, _PlotOptions

if TYPE_CHECKING:
    from collections.abc import Sequence


class _Plot(_PlotOptions):
    """A plot component."""

    plot: Sequence[ms.PlotInteractor | ms.PlotLegend | ms.PlotMark]
    """An array of plot marks, interactors, or legends.

    Marks are graphical elements that make up plot layers.
    Unless otherwise configured, interactors will use the nearest previous mark as a basis for which data fields to select.
    """


class Plot(_Plot, closed=True):
    """A plot component."""


# NOTE: pyright gets tripped up if this is declared after `{H,V}Concat`
Component = TypeAliasType(
    "Component",
    Union[
        Plot,
        "HConcat",
        "VConcat",
        ms.HSpace,
        ms.Legend,
        ms.Menu,
        ms.PlotMark,
        ms.Search,
        ms.Slider,
        ms.Table,
        ms.VSpace,
    ],
)
"""A specification component such as a plot, input widget, or layout."""


class _HConcat(TypedDict):
    """A hconcat component."""

    hconcat: Sequence[Component]
    """Horizontally concatenate components in a row layout."""


class _VConcat(TypedDict):
    """A vconcat component."""

    vconcat: Sequence[Component]
    """Vertically concatenate components in a column layout."""


class HConcat(_HConcat, closed=True):
    """A hconcat component."""


class VConcat(_VConcat, closed=True):
    """A vconcat component."""


class SpecHead(TypedDict, total=False):
    config: ms.Config
    """Configuration options."""
    data: ms.Data
    """Dataset definitions."""
    meta: ms.Meta
    """Specification metadata."""
    params: ms.Params
    """Param and Selection definitions."""
    plot_defaults: PlotAttributes
    """A default set of attributes to apply to all plot components."""
