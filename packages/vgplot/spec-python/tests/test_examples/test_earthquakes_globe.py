"""Earthquakes Globe.

A rotatable globe of earthquake activity. To show land masses, this example loads and parses TopoJSON data in the database. Requires the DuckDB `spatial` extension.


## Credit
Adapted from an [Observable Plot example](https://observablehq.com/@observablehq/plot-earthquake-globe).
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.Spec = {
        "data": {
            "earthquakes": {"file": "data/earthquakes.parquet"},
            "land": {"type": "spatial", "file": "data/countries-110m.json", "layer": "land"},
        },
        "params": {"longitude": -180, "latitude": -30, "rotate": ["$longitude", "$latitude"]},
        "vconcat": [
            {
                "hconcat": [
                    {
                        "input": "slider",
                        "label": "Longitude",
                        "bind": "$longitude",
                        "min": -180,
                        "max": 180,
                        "step": 1,
                    },
                    {
                        "input": "slider",
                        "label": "Latitude",
                        "bind": "$latitude",
                        "min": -90,
                        "max": 90,
                        "step": 1,
                    },
                ]
            },
            {
                "plot": [
                    {
                        "mark": "geo",
                        "data": {"source": "land"},
                        "geometry": {"geojson": "geom"},
                        "fill": "currentColor",
                        "fill_opacity": 0.2,
                    },
                    {"mark": "sphere"},
                    {
                        "mark": "dot",
                        "data": {"source": "earthquakes"},
                        "x": "longitude",
                        "y": "latitude",
                        "r": {"sql": "POW(10, magnitude)"},
                        "stroke": "red",
                        "fill": "red",
                        "fill_opacity": 0.2,
                    },
                ],
                "margin": 10,
                "style": "overflow: visible;",
                "projection_type": "orthographic",
                "projection_rotate": "$rotate",
            },
        ],
    }  # ty: ignore[invalid-assignment]
