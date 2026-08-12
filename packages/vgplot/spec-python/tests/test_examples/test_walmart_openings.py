"""Walmart Openings.

Maps showing Walmart store openings per decade. Requires the DuckDB `spatial` extension.


## Credit
Adapted from an [Observable Plot example](https://observablehq.com/@observablehq/plot-map-large-multiples).
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.VConcat = {
        "data": {
            "states": {"type": "spatial", "file": "data/us-counties-10m.json", "layer": "states"},
            "nation": {"type": "spatial", "file": "data/us-counties-10m.json", "layer": "nation"},
            "walmarts": {"file": "data/walmarts.parquet"},
        },
        "vconcat": [
            {
                "plot": [
                    {
                        "mark": "geo",
                        "data": {"source": "states"},
                        "stroke": "#aaa",
                        "stroke_width": 1,
                    },
                    {"mark": "geo", "data": {"source": "nation"}, "stroke": "currentColor"},
                    {
                        "mark": "dot",
                        "data": {"source": "walmarts"},
                        "x": "longitude",
                        "y": "latitude",
                        "fy": {"sql": "10 * decade(date)"},
                        "r": 1.5,
                        "fill": "blue",
                    },
                    {"mark": "axisFy", "frame_anchor": "top", "dy": 30, "tick_format": "d"},
                ],
                "margin": 0,
                "fy_label": None,
                "projection_type": "albers",
            }
        ],
    }
