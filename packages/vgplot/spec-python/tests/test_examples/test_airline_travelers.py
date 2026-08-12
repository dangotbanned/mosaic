"""Airline Travelers.

A labeled line chart comparing airport travelers in 2019 and 2020.

## Credit
Adapted from an [Observable Plot example](https://observablehq.com/@observablehq/plot-labeled-line-chart).
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.Plot = {
        "data": {
            "travelers": {"file": "data/travelers.parquet"},
            "endpoint": "SELECT * FROM travelers ORDER BY date DESC LIMIT 1\n",
        },
        "plot": [
            {"mark": "ruleY", "data": [0]},
            {
                "mark": "lineY",
                "data": {"source": "travelers"},
                "x": "date",
                "y": "previous",
                "stroke_opacity": 0.35,
            },
            {"mark": "lineY", "data": {"source": "travelers"}, "x": "date", "y": "current"},
            {
                "mark": "text",
                "data": {"source": "endpoint"},
                "x": "date",
                "y": "previous",
                "text": ["2019"],
                "fill_opacity": 0.5,
                "line_anchor": "bottom",
                "dy": -6,
            },
            {
                "mark": "text",
                "data": {"source": "endpoint"},
                "x": "date",
                "y": "current",
                "text": ["2020"],
                "line_anchor": "top",
                "dy": 6,
            },
        ],
        "y_grid": True,
        "y_label": "↑ Travelers per day",
        "y_tick_format": "s",
    }
