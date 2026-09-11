# Generated: `mosaic_spec._gen.layout`
from __future__ import annotations

from typing import TYPE_CHECKING

from mosaic_spec._typing_compat import Required, TypedDict

if TYPE_CHECKING:
    from collections.abc import Sequence

    from mosaic_spec._gen.mosaic import Component


class _HConcatOpen(TypedDict):
    """An hconcat component."""

    hconcat: Required[Sequence[Component]]
    """Horizontally concatenate components in a row layout."""


class _HSpaceOpen(TypedDict):
    """An hspace component."""

    hspace: Required[float | str]
    """Horizontal space to place between components. Number values indicate screen pixels. String values may use CSS units (em, pt, px, etc)."""


class _VConcatOpen(TypedDict):
    """A vconcat component."""

    vconcat: Required[Sequence[Component]]
    """Vertically concatenate components in a column layout."""


class _VSpaceOpen(TypedDict):
    """A vspace component."""

    vspace: Required[float | str]
    """Vertical space to place between components. Number values indicate screen pixels. String values may use CSS units (em, pt, px, etc)."""


class HConcat(_HConcatOpen, closed=True): ...


class HSpace(_HSpaceOpen, closed=True): ...


class VConcat(_VConcatOpen, closed=True): ...


class VSpace(_VSpaceOpen, closed=True): ...


__all__ = ("HConcat", "HSpace", "VConcat", "VSpace")
