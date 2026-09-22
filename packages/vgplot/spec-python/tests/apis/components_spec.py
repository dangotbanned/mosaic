"""Builds on `test.apis.plot`.

- Replaces `ms.Plot(Attributes)` with the versions defined here
- Required redefining everywhere that `ms.Component` is used
    - Including the `Spec` variants
"""

from __future__ import annotations

import dataclasses
from typing import TYPE_CHECKING, Union, final

import mosaic_spec as ms
from mosaic_spec._typing_compat import TypeAliasType, Unpack
from tests.apis.attributes import PlotAttributes

if TYPE_CHECKING:
    from collections.abc import Sequence


class _View:
    __slots__ = ()


@final
class Plot(_View):
    __slots__ = ("elements", "options")
    elements: tuple[ms.PlotInteractor | ms.PlotLegend | ms.PlotMark, ...]
    """An array of plot marks, interactors, or legends.

    Marks are graphical elements that make up plot layers.
    Unless otherwise configured, interactors will use the nearest previous mark as a basis for which data fields to select.
    """
    options: PlotAttributes

    def __init__(
        self,
        elements: tuple[ms.PlotInteractor | ms.PlotLegend | ms.PlotMark, ...],
        options: PlotAttributes,
    ) -> None:
        self.elements = elements
        self.options = options


def plot(
    *elements: ms.PlotInteractor | ms.PlotLegend | ms.PlotMark, **options: Unpack[PlotAttributes]
) -> Plot:
    return Plot(elements, options)


def vconcat(*columns: Component) -> VConcat:
    return VConcat(columns)


def hconcat(*rows: Component) -> HConcat:
    return HConcat(rows)


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


@final
class HConcat(_View):
    """A hconcat component."""

    __slots__ = ("rows",)

    rows: tuple[Component, ...]

    def __init__(self, rows: tuple[Component, ...]) -> None:
        self.rows = rows


@final
class VConcat(_View):
    """A vconcat component."""

    __slots__ = ("columns",)
    columns: Sequence[Component]

    def __init__(self, columns: tuple[Component, ...]) -> None:
        self.columns = columns


View = TypeAliasType("View", Plot | HConcat | VConcat)
"""A top-level component.

- Covers 53/55 examples
    - Skips 2 which use `Table`
- Everything else can be nested within these to fit
- Reduces the `Spec` intersection from **80** alternatives
"""


# TODO @dangotbanned: Use `test_apis.data`
# TODO @dangotbanned: Use `test_apis.params`
@dataclasses.dataclass
class Spec:
    """A declarative Mosaic specification."""

    view: View
    """The top-level component."""

    config: ms.Config = dataclasses.field(default_factory=ms.Config)
    """Configuration options."""

    data: dict[str, ms.DataDefinition] = dataclasses.field(default_factory=dict)
    """Dataset definitions."""

    meta: ms.Meta = dataclasses.field(default_factory=ms.Meta)
    """Specification metadata."""

    params: dict[str, ms.ParamDefinition] = dataclasses.field(default_factory=dict)
    """Param and Selection definitions."""

    plot_defaults: PlotAttributes = dataclasses.field(default_factory=PlotAttributes)
    """A default set of attributes to apply to all plot components."""
