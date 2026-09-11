# Generated: `mosaic_spec._gen.layout`
from __future__ import annotations

from collections.abc import Sequence
from mosaic_spec._gen.mosaic import Component
from mosaic_spec._typing_compat import Required
from mosaic_spec._typing_compat import TypedDict

class _HConcatOpen(TypedDict,total=False):
    """An hconcat component."""
    hconcat: Required[Sequence[Component]]
    '''Horizontally concatenate components in a row layout.'''
class _HSpaceOpen(TypedDict,total=False):
    """An hspace component."""
    hspace: Required[float | str]
    '''Horizontal space to place between components. Number values indicate screen pixels. String values may use CSS units (em, pt, px, etc).'''
class _VConcatOpen(TypedDict,total=False):
    """A vconcat component."""
    vconcat: Required[Sequence[Component]]
    '''Vertically concatenate components in a column layout.'''
class _VSpaceOpen(TypedDict,total=False):
    """A vspace component."""
    vspace: Required[float | str]
    '''Vertical space to place between components. Number values indicate screen pixels. String values may use CSS units (em, pt, px, etc).'''
class HConcat(_HConcatOpen,total=False,closed=True):...
class HSpace(_HSpaceOpen,total=False,closed=True):...
class VConcat(_VConcatOpen,total=False,closed=True):...
class VSpace(_VSpaceOpen,total=False,closed=True):...


__all__ = ("HConcat","HSpace","VConcat","VSpace",)
