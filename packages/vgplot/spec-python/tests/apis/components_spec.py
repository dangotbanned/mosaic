"""Builds on `test.apis.plot`.

- Replaces `ms.Plot(Attributes)` with the versions defined here
- Required redefining everywhere that `ms.Component` is used
    - Including the `Spec` variants
"""

from __future__ import annotations

# ruff: file-ignore[useless-import-alias]
from typing import TYPE_CHECKING, Any, final

from mosaic_spec._typing_compat import Self, TypeVar, Unpack
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
from tests.apis.protocols import IntoComponent, IntoPlot, Spec, SpecHead, View

if TYPE_CHECKING:
    import mosaic_spec as ms
    from tests.apis.attributes import AttrsMut, PlotAttributes


class _ViewImpl(View):
    __slots__ = ()

    def to_spec(self, **options: Unpack[SpecHead]) -> SpecImpl[Self]:
        return SpecImpl(self, options)

    # NOTE: Every example that uses either `*space` is covered by these two methods
    def hspace(self, space: float | str, *then: IntoComponent) -> HConcat:
        """Add horizontal space between components.

        Numeric values indicate screen pixels.
        String values may use CSS units (em, pt, px, etc).
        """
        return hconcat(self, {"hspace": space}, *then)

    def vspace(self, space: float | str, *then: IntoComponent) -> VConcat:
        """Add vertical space between components.

        Numeric values indicate screen pixels.
        String values may use CSS units (em, pt, px, etc).
        """
        return vconcat(self, {"vspace": space}, *then)

    def to_dict(
        self, data: dict[str, ms.DataDefinition], params: dict[str, ms.ParamDefinition]
    ) -> ms.Plot | ms.VConcat | ms.HConcat:
        msg = f"{self.__class__.__name__}.to_dict() is not yet implemented"
        raise NotImplementedError(msg)


ViewT = TypeVar("ViewT", bound=_ViewImpl, infer_variance=True)


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

    def to_dict(
        self, data: dict[str, ms.DataDefinition], params: dict[str, ms.ParamDefinition]
    ) -> ms.Plot:
        msg = f"{self.__class__.__name__}.to_dict() is not yet implemented"
        raise NotImplementedError(msg)


def plot(*elements: IntoPlot, **options: Unpack[PlotAttributes]) -> Plot:
    return Plot(elements, options)


def vconcat(*columns: IntoComponent) -> VConcat:
    return VConcat(columns)


def hconcat(*rows: IntoComponent) -> HConcat:
    return HConcat(rows)


@final
class HConcat(_ViewImpl):
    """A hconcat component."""

    __slots__ = ("rows",)

    rows: tuple[IntoComponent, ...]

    def __init__(self, rows: tuple[IntoComponent, ...]) -> None:
        self.rows = rows

    def to_dict(
        self, data: dict[str, ms.DataDefinition], params: dict[str, ms.ParamDefinition]
    ) -> ms.HConcat:
        msg = f"{self.__class__.__name__}.to_dict() is not yet implemented"
        raise NotImplementedError(msg)


@final
class VConcat(_ViewImpl):
    """A vconcat component."""

    __slots__ = ("columns",)
    columns: tuple[IntoComponent, ...]

    def __init__(self, columns: tuple[IntoComponent, ...]) -> None:
        self.columns = columns

    def to_dict(
        self, data: dict[str, ms.DataDefinition], params: dict[str, ms.ParamDefinition]
    ) -> ms.VConcat:
        msg = f"{self.__class__.__name__}.to_dict() is not yet implemented"
        raise NotImplementedError(msg)


class SpecImpl(Spec[ViewT]):
    """A declarative Mosaic specification."""

    __slots__ = ()

    def __init__(self, view: ViewT, options: SpecHead | None = None) -> None:
        self.view: ViewT = view
        self.options: SpecHead = options or {}

    def to_dict(self) -> dict[str, Any]:
        _data = self.options.get("data", {})
        _params = self.options.get("params", {})
        raise NotImplementedError
