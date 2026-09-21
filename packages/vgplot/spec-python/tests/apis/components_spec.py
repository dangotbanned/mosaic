"""Builds on `test.apis.plot`.

- Replaces `ms.Plot(Attributes)` with the versions defined here
- Required redefining everywhere that `ms.Component` is used
    - Including the `Spec` variants
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Union

import mosaic_spec as ms
from mosaic_spec._gen.inputs import _TableOpen
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


# TODO @dangotbanned: Use `test_apis.data`
# TODO @dangotbanned: Use `test_apis.params`
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


class HConcatSpec(SpecHead, _HConcat, closed=True): ...


class VConcatSpec(SpecHead, _VConcat, closed=True): ...


class PlotSpec(SpecHead, _Plot, closed=True): ...


class TableSpec(SpecHead, _TableOpen, closed=True): ...


# NOTE: This covers all 55 examples and reduces the `Spec` union from 80 -> 4
Spec = TypeAliasType("Spec", PlotSpec | HConcatSpec | VConcatSpec | TableSpec)
"""A declarative Mosaic specification."""
