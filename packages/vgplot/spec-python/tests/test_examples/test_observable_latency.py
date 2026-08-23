"""Observable Latency.

Web request latency on Observable.com.
Each pixel in the heatmap shows the most common route (URL pattern) at a given response latency within a time interval.
Use the bar chart of most-requested routes to filter the heatmap and isolate specific patterns.
Or, select a range in the heatmap to show the corresponding most-requested routes.

_You may need to wait a few seconds for the dataset to load._

## Credit
Adapted from an [Observable Framework example](https://observablehq.com/framework/examples/api/).
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.VConcat = {
        "data": {
            "latency": {
                "file": "https://pub-1da360b43ceb401c809f68ca37c7f8a4.r2.dev/data/observable-latency.parquet"
            }
        },
        "params": {"filter": {"select": "crossfilter"}},
        "vconcat": [
            {
                "plot": [
                    {"mark": "frame", "fill": "black"},
                    {
                        "mark": "raster",
                        "data": {"source": "latency", "filter_by": "$filter"},
                        "x": "time",
                        "y": "latency",
                        "fill": {"argmax": ("route", "count")},
                        "fill_opacity": {"sum": "count"},
                        "width": 2016,
                        "height": 500,
                        "image_rendering": "pixelated",
                    },
                    {"select": "intervalXY", "bind": "$filter"},
                ],
                "color_domain": "Fixed",
                "color_scheme": "observable10",
                "opacity_domain": [0, 25],
                "opacity_clamp": True,
                "y_scale": "log",
                "y_label": "↑ Duration (ms)",
                "y_domain": [0.5, 10000],
                "y_tick_format": "s",
                "x_scale": "utc",
                "x_label": None,
                "x_domain": [1706227200000, 1706832000000],
                "width": 680,
                "height": 300,
                "margins": {"left": 35, "top": 20, "bottom": 30, "right": 20},
            },
            {
                "plot": [
                    {
                        "mark": "barX",
                        "data": {"source": "latency", "filter_by": "$filter"},
                        "x": {"sum": "count"},
                        "y": "route",
                        "fill": "route",
                        "sort": {"y": "-x", "limit": 15},
                    },
                    {"select": "toggleY", "bind": "$filter"},
                    {"select": "toggleY", "bind": "$highlight"},
                    {"select": "highlight", "by": "$highlight"},
                ],
                "color_domain": "Fixed",
                "x_label": "Routes by Total Requests",
                "x_tick_format": "s",
                "y_label": None,
                "width": 680,
                "height": 300,
                "margin_top": 5,
                "margin_left": 220,
                "margin_bottom": 35,
            },
        ],
    }
