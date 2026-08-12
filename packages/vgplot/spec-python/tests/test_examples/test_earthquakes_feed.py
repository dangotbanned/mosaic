"""Earthquakes Feed.

Earthquake data from the USGS live feed. To show land masses, this example loads and parses TopoJSON data in the database. Requires the DuckDB `spatial` extension.


## Credit
Adapted from an [Observable Plot example](https://observablehq.com/@observablehq/plot-live-earthquake-map).
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.Spec = {
        "data": {
            "feed": {"type": "spatial", "file": "data/usgs-feed.geojson"},
            "world": {"type": "spatial", "file": "data/countries-110m.json", "layer": "land"},
        },
        "plot": [
            {
                "mark": "geo",
                "data": {"source": "world"},
                "fill": "currentColor",
                "fill_opacity": 0.2,
            },
            {"mark": "sphere", "stroke_width": 0.5},
            {
                "mark": "geo",
                "data": {"source": "feed"},
                "r": {"sql": "POW(10, mag)"},
                "stroke": "red",
                "fill": "red",
                "fill_opacity": 0.2,
                "title": "title",
                "href": "url",
                "target": "_blank",
            },
        ],
        "margin": 2,
        "projection_type": "equirectangular",
    }  # ty: ignore[invalid-assignment]
