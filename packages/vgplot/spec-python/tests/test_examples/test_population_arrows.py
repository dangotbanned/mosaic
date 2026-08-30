"""Population Change Arrows.

An `arrow` connects the positions in 1980 and 2015 of each city on this population × inequality
chart. Color encodes variation.

## Credit

Adapted from an [Observable Plot example].

[Observable Plot example]: https://observablehq.com/@observablehq/plot-arrow-variation-chart
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.VConcat = {
        "data": {"metros": {"file": "data/metros.parquet"}},
        "params": {"bend": True},
        "vconcat": [
            {
                "legend": "color",
                "plot": "arrows",
                "label": "Change in inequality from 1980 to 2015",
            },
            {
                "name": "arrows",
                "plot": [
                    {
                        "mark": "arrow",
                        "data": {"source": "metros"},
                        "x1": "POP_1980",
                        "y1": "R90_10_1980",
                        "x2": "POP_2015",
                        "y2": "R90_10_2015",
                        "bend": "$bend",
                        "stroke": {"sql": "R90_10_2015 - R90_10_1980"},
                    },
                    {
                        "mark": "text",
                        "data": {"source": "metros"},
                        "x": "POP_2015",
                        "y": "R90_10_2015",
                        "filter": "highlight",
                        "text": "nyt_display",
                        "fill": "currentColor",
                        "dy": -6,
                    },
                ],
                "grid": True,
                "inset": 10,
                "x_scale": "log",
                "x_label": "Population →",
                "y_label": "↑ Inequality",
                "y_ticks": 4,
                "color_scheme": "BuRd",
                "color_tick_format": "+f",
            },
            {"input": "menu", "label": "Bend Arrows?", "options": [True, False], "bind": "$bend"},
        ],
    }
