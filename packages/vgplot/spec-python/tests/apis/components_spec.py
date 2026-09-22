"""Builds on `test.apis.plot`.

- Replaces `ms.Plot(Attributes)` with the versions defined here
- Required redefining everywhere that `ms.Component` is used
    - Including the `Spec` variants
"""

from __future__ import annotations

import dataclasses
from typing import Any, Protocol, final

import mosaic_spec as ms
from mosaic_spec._typing_compat import TypeAliasType, Unpack
from tests.apis._marks import MarkData
from tests.apis.attributes import PlotAttributes
from tests.apis.inputs import InputWidget

PlotMark = TypeAliasType("PlotMark", MarkData[Any])
IntoPlot = TypeAliasType("IntoPlot", ms.PlotInteractor | ms.PlotLegend | PlotMark)
"""All of these need a `plot` method."""


class View(Protocol):
    """A top-level component.

    - Covers 53/55 examples
        - Skips 2 which use `Table`
    - Everything else can be nested within these to fit
    - Reduces the `Spec` intersection from **80** alternatives
    """

    __slots__ = ()

    def to_spec(self) -> Spec: ...


Component = TypeAliasType("Component", View | InputWidget | PlotMark | ms.VSpace | ms.HSpace)
"""A specification component such as a plot, input widget, or layout."""


class Spec(Protocol):
    """A declarative Mosaic specification."""

    __slots__ = ()
    view: View
    """The top-level component."""

    config: ms.Config
    """Configuration options."""

    data: dict[str, ms.DataDefinition]
    """Dataset definitions."""

    meta: ms.Meta
    """Specification metadata."""

    params: dict[str, ms.ParamDefinition]
    """Param and Selection definitions."""

    plot_defaults: PlotAttributes
    """A default set of attributes to apply to all plot components."""


class _ViewImpl(View):
    __slots__ = ()

    def to_spec(self) -> SpecImpl:
        return SpecImpl(self)

    # NOTE: Every example that uses either `*space` is covered by these two methods
    def hspace(self, space: float | str, *then: Component) -> HConcat:
        """Add horizontal space between components.

        Numeric values indicate screen pixels.
        String values may use CSS units (em, pt, px, etc).
        """
        return hconcat(self, {"hspace": space}, *then)

    def vspace(self, space: float | str, *then: Component) -> VConcat:
        """Add vertical space between components.

        Numeric values indicate screen pixels.
        String values may use CSS units (em, pt, px, etc).
        """
        return vconcat(self, {"vspace": space}, *then)


@final
class Plot(_ViewImpl):
    __slots__ = ("elements", "options")
    elements: tuple[IntoPlot, ...]
    """An array of plot marks, interactors, or legends.

    Marks are graphical elements that make up plot layers.
    Unless otherwise configured, interactors will use the nearest previous mark as a basis for which data fields to select.
    """
    options: PlotAttributes

    def __init__(self, elements: tuple[IntoPlot, ...], options: PlotAttributes) -> None:
        self.elements = elements
        self.options = options


def plot(*elements: IntoPlot, **options: Unpack[PlotAttributes]) -> Plot:
    return Plot(elements, options)


def vconcat(*columns: Component) -> VConcat:
    return VConcat(columns)


def hconcat(*rows: Component) -> HConcat:
    return HConcat(rows)


@final
class HConcat(_ViewImpl):
    """A hconcat component."""

    __slots__ = ("rows",)

    rows: tuple[Component, ...]

    def __init__(self, rows: tuple[Component, ...]) -> None:
        self.rows = rows


@final
class VConcat(_ViewImpl):
    """A vconcat component."""

    __slots__ = ("columns",)
    columns: tuple[Component, ...]

    def __init__(self, columns: tuple[Component, ...]) -> None:
        self.columns = columns


# TODO @dangotbanned: Use `test_apis.data`
# TODO @dangotbanned: Use `test_apis.params`
@dataclasses.dataclass
class SpecImpl:
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
