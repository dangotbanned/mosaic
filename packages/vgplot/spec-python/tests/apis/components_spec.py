"""Builds on `test.apis.plot`.

- Replaces `ms.Plot(Attributes)` with the versions defined here
- Required redefining everywhere that `ms.Component` is used
    - Including the `Spec` variants
"""

from __future__ import annotations

# ruff: file-ignore[useless-import-alias]
import dataclasses
from typing import Any, Protocol, final

import mosaic_spec as ms
from mosaic_spec._typing_compat import TypeAliasType, Unpack
from tests.apis._marks import MarkData
from tests.apis.attributes import AttrsMut, PlotAttributes
from tests.apis.inputs import InputWidget
from tests.apis.interactors import (
    Interactor as Interactor,
    highlight as highlight,
    interval as interval,
    interval_x as interval_x,
    interval_y as interval_y,
    nearest_x as nearest_x,
    nearest_y as nearest_y,
    pan as pan,
    pan_x as pan_x,
    pan_y as pan_y,
    pan_zoom as pan_zoom,
    pan_zoom_x as pan_zoom_x,
    pan_zoom_y as pan_zoom_y,
    region as region,
    toggle as toggle,
)

PlotMark = TypeAliasType("PlotMark", MarkData[Any])
IntoPlot = TypeAliasType("IntoPlot", Interactor | ms.PlotLegend | PlotMark)
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
    __slots__ = ("_options", "elements")
    elements: tuple[IntoPlot, ...]
    """An array of plot marks, interactors, or legends.

    Marks are graphical elements that make up plot layers.
    Unless otherwise configured, interactors will use the nearest previous mark as a basis for which data fields to select.
    """
    _options: PlotAttributes

    def __init__(self, elements: tuple[IntoPlot, ...], options: PlotAttributes) -> None:
        self.elements = elements
        self._options = options

    def with_attrs(self, attributes: AttrsMut, /) -> Plot:
        return Plot(self.elements, attributes.to_dict())


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
