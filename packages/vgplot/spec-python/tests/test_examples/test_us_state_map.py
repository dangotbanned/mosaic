"""U.S. States.

A map of U.S. states overlaid with computed centroids. Requires the DuckDB `spatial` extension.


## Credit
Adapted from an [Observable Plot example](https://observablehq.com/@observablehq/plot-state-centroids).
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.Spec = {
        "data": {
            "states": {"type": "spatial", "file": "data/us-counties-10m.json", "layer": "states"}
        },
        "plot": [
            {
                "mark": "geo",
                "data": {"source": "states"},
                "stroke": "currentColor",
                "stroke_width": 1,
            },
            {
                "mark": "dot",
                "data": {"source": "states"},
                "x": {"centroid_x": "geom"},
                "y": {"centroid_y": "geom"},
                "r": 2,
                "fill": "steelblue",
                "tip": True,
                "title": "name",
            },
        ],
        "margin": 0,
        "projection_type": "albers",
    }  # ty: ignore[invalid-assignment]
