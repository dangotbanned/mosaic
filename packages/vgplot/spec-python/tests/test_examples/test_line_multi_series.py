"""Line Multi-Series.

This line chart shows the unemployment rate of various U.S. metro divisions from 2000 through 2013.
On hover, the closest data point to the pointer and its associated series is highlighted.
Highlighting of series is performed using `nearestX` and `highlight` interactors. Point and text
annotations instead use the mark `select` filter option.

## Credit

Adapted from a [D3 example]. Data from the [Bureau of Labor Statistics].

[D3 example]: https://observablehq.com/@d3/multi-line-chart/2
[Bureau of Labor Statistics]: https://www.bls.gov/
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.Plot = {
        "data": {"bls_unemp": {"file": "data/bls-metro-unemployment.parquet"}},
        "plot": [
            {"mark": "ruleY", "data": [0]},
            {
                "mark": "lineY",
                "data": {"source": "bls_unemp", "optimize": False},
                "x": "date",
                "y": "unemployment",
                "z": "division",
                "stroke": "steelblue",
                "stroke_opacity": 0.9,
                "curve": "monotone-x",
            },
            {"select": "nearestX", "channels": ["z"], "bind": "$curr"},
            {"select": "highlight", "by": "$curr"},
            {
                "mark": "dot",
                "data": {"source": "bls_unemp"},
                "x": "date",
                "y": "unemployment",
                "z": "division",
                "r": 2,
                "fill": "currentColor",
                "select": "nearestX",
            },
            {
                "mark": "text",
                "data": {"source": "bls_unemp"},
                "x": "date",
                "y": "unemployment",
                "text": "division",
                "fill": "currentColor",
                "dy": -8,
                "select": "nearestX",
            },
        ],
        "margin_left": 24,
        "x_label": None,
        "x_ticks": 10,
        "y_label": "Unemployment (%)",
        "y_grid": True,
        "style": "overflow: visible;",
        "width": 680,
    }
