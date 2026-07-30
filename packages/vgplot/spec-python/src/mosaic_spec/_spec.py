from __future__ import annotations

from typing import TYPE_CHECKING

from mosaic_spec._typing_compat import TypedDict

if TYPE_CHECKING:
    from mosaic_spec._gen import Component, Config, Data, Meta, Params, PlotAttributes  # noqa: F401


class SpecHead(TypedDict, total=False):
    """A declarative Mosaic specification.

    ## Notes
    - `Component` is **81** symbols after expanding `"anyOf"` recursively
        - 81 (in `Spec`)
        - 11 (in `Component`)
    - Each needs to be used like `class SpecHead(SpecHead, HConcat) ...`
    - Then `Spec` is the union of those new defs
    """

    # NOTE: [`SpecHead`] - $schema
    # [`SpecHead`](https://github.com/uwdata/mosaic/blob/f27e065f40c84dfbdb39eb78061db857601539fd/packages/vgplot/spec/src/spec/Spec.ts#L34-L53)

    config: Config
    """Configuration options."""
    data: Data
    """Dataset definitions."""
    meta: Meta
    """Specification metadata."""
    params: Params
    """Param and Selection definitions."""
    plot_defaults: PlotAttributes
    """A default set of attributes to apply to all plot components."""
