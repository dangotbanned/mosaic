"""U.S. Unemployment.

A choropleth map of unemployment rates for U.S. counties. Requires the DuckDB `spatial` extension.

## Credit
Adapted from an [Observable Plot example](https://observablehq.com/@observablehq/plot-us-choropleth).
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.VConcat = {
        "data": {
            "counties": {
                "type": "spatial",
                "file": "data/us-counties-10m.json",
                "layer": "counties",
            },
            "rates": {"file": "data/us-county-unemployment.parquet"},
            "combined": "SELECT a.geom AS geom, b.rate AS rate FROM counties AS a, rates AS b WHERE a.id = b.id\n",
        },
        "vconcat": [
            {"legend": "color", "plot": "county-map", "label": "Unemployment (%)"},
            {
                "name": "county-map",
                "plot": [
                    {
                        "mark": "geo",
                        "data": {"source": "combined"},
                        "fill": "rate",
                        "title": {"sql": "concat(rate, '%')"},
                    }
                ],
                "margin": 0,
                "color_scale": "quantile",
                "color_n": 9,
                "color_scheme": "blues",
                "projection_type": "albers-usa",
            },
        ],
    }
