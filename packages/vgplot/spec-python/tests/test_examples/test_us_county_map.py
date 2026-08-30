"""U.S. Counties.

A map of U.S. counties. County name tooltips are anchored to invisible centroid dot marks. Requires
the DuckDB `spatial` extension.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.Plot = {
        "data": {
            "counties": {
                "type": "spatial",
                "file": "data/us-counties-10m.json",
                "layer": "counties",
            },
            "states": {"type": "spatial", "file": "data/us-counties-10m.json", "layer": "states"},
        },
        "plot": [
            {
                "mark": "geo",
                "data": {"source": "counties"},
                "stroke": "currentColor",
                "stroke_width": 0.25,
            },
            {
                "mark": "geo",
                "data": {"source": "states"},
                "stroke": "currentColor",
                "stroke_width": 1,
            },
            {
                "mark": "dot",
                "data": {"source": "counties"},
                "x": {"centroid_x": "geom"},
                "y": {"centroid_y": "geom"},
                "r": 2,
                "fill": "transparent",
                "tip": True,
                "title": "name",
            },
        ],
        "margin": 0,
        "projection_type": "albers",
    }
