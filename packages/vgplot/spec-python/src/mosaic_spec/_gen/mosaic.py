# Generated: `mosaic_spec._gen.mosaic`
from __future__ import annotations

from collections.abc import Sequence
from mosaic_spec._gen.inputs import Menu
from mosaic_spec._gen.inputs import Search
from mosaic_spec._gen.inputs import Slider
from mosaic_spec._gen.inputs import Table
from mosaic_spec._gen.layout import HConcat
from mosaic_spec._gen.layout import HSpace
from mosaic_spec._gen.layout import VConcat
from mosaic_spec._gen.layout import VSpace
from mosaic_spec._gen.marks import PlotMark
from mosaic_spec._gen.plot import Plot
from mosaic_spec._gen.plot_legend import Legend
from mosaic_spec._typing_compat import TypeAliasType
from mosaic_spec._typing_compat import TypedDict
from typing import Any

Component = TypeAliasType('Component', HConcat | HSpace | Legend | Menu | Plot | PlotMark | Search | Slider | Table | VConcat | VSpace)
'''A specification component such as a plot, input widget, or layout.'''
class Config(TypedDict,total=False,extra_items=Any):
    """Configuration options."""
    extensions: Sequence[str] | str
class Meta(TypedDict,total=False,extra_items=Any):
    """Specification metadata."""
    credit: str
    '''Credits or other acknowledgements.'''
    description: str
    '''A description of the specification content.'''
    title: str
    '''The specification title.'''


__all__ = ("Component","Config","Meta",)
