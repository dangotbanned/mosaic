"""Presidential Opinion.

Opinion poll data on historical U.S. presidents. Image marks are used to show presidential pictures. The dropdown menu toggles the opinion metric shown.

## Credit
Adapted from an [Observable Plot example](https://observablehq.com/@observablehq/plot-image-medals).
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.VConcat = {
        "data": {"presidents": {"file": "data/us-president-favorability.parquet"}},
        "params": {"sign": 1},
        "vconcat": [
            {
                "plot": [
                    {"mark": "ruleY", "data": [0]},
                    {
                        "mark": "image",
                        "data": {"source": "presidents"},
                        "x": "First Inauguration Date",
                        "y": {
                            "sql": '"Very Favorable %" + "Somewhat Favorable %" + $sign * ("Very Unfavorable %" + "Somewhat Unfavorable %")'
                        },
                        "src": "Portrait URL",
                        "r": 20,
                        "preserve_aspect_ratio": "xMidYMin slice",
                        "title": "Name",
                    },
                ],
                "x_inset": 20,
                "x_label": "First inauguration date →",
                "y_inset_top": 4,
                "y_grid": True,
                "y_label": "↑ Opinion (%)",
                "y_tick_format": "+f",
            },
            {
                "input": "menu",
                "label": "Opinion Metric",
                "options": [
                    {"label": "Any Opinion", "value": 1},
                    {"label": "Net Favorability", "value": -1},
                ],
                "bind": "$sign",
            },
        ],
    }
