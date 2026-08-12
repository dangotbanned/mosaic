"""Voronoi Diagram.

The `voronoi` mark shows the regions closest to each point. It is [constructed from its dual](https://observablehq.com/@mbostock/the-delaunays-dual), a Delaunay triangle mesh. Reveal triangulations or convex hulls using the dropdowns.


## Credit
Adapted from an [Observable Plot example](https://observablehq.com/@observablehq/plot-voronoi-scatterplot).
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.VConcat = {
        "data": {"penguins": {"file": "data/penguins.parquet"}},
        "params": {"mesh": 0, "hull": 0},
        "vconcat": [
            {
                "plot": [
                    {
                        "mark": "voronoi",
                        "data": {"source": "penguins"},
                        "x": "bill_length",
                        "y": "bill_depth",
                        "stroke": "white",
                        "stroke_width": 1,
                        "stroke_opacity": 0.5,
                        "fill": "species",
                        "fill_opacity": 0.2,
                    },
                    {
                        "mark": "hull",
                        "data": {"source": "penguins"},
                        "x": "bill_length",
                        "y": "bill_depth",
                        "stroke": "species",
                        "stroke_opacity": "$hull",
                        "stroke_width": 1.5,
                    },
                    {
                        "mark": "delaunayMesh",
                        "data": {"source": "penguins"},
                        "x": "bill_length",
                        "y": "bill_depth",
                        "z": "species",
                        "stroke": "species",
                        "stroke_opacity": "$mesh",
                        "stroke_width": 1,
                    },
                    {
                        "mark": "dot",
                        "data": {"source": "penguins"},
                        "x": "bill_length",
                        "y": "bill_depth",
                        "fill": "species",
                        "r": 2,
                    },
                    {"mark": "frame"},
                ],
                "inset": 10,
                "width": 680,
            },
            {
                "hconcat": [
                    {
                        "input": "menu",
                        "label": "Delaunay Mesh",
                        "options": [{"value": 0, "label": "Hide"}, {"value": 0.5, "label": "Show"}],
                        "bind": "$mesh",
                    },
                    {"hspace": 5},
                    {
                        "input": "menu",
                        "label": "Convex Hull",
                        "options": [{"value": 0, "label": "Hide"}, {"value": 1, "label": "Show"}],
                        "bind": "$hull",
                    },
                ]
            },
        ],
    }
