"""Seattle Weather.

An interactive view of Seattle's weather, including maximum temperature, amount of precipitation, and type of weather. By dragging on the scatter plot, you can see the proportion of days in that range that have sun, fog, drizzle, rain, or snow.


## Credit
Based on a [Vega-Lite/Altair example](https://vega.github.io/vega-lite/examples/interactive_seattle_weather.html) by Jake Vanderplas.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.Spec = {
        "data": {"weather": {"file": "data/seattle-weather.parquet"}},
        "params": {
            "click": {"select": "single"},
            "domain": ["sun", "fog", "drizzle", "rain", "snow"],
            "colors": ["#e7ba52", "#a7a7a7", "#aec7e8", "#1f77b4", "#9467bd"],
        },
        "vconcat": [
            {
                "hconcat": [
                    {
                        "plot": [
                            {
                                "mark": "dot",
                                "data": {"source": "weather", "filter_by": "$click"},
                                "x": {"date_month_day": "date"},
                                "y": "temp_max",
                                "fill": "weather",
                                "r": "precipitation",
                                "fill_opacity": 0.7,
                            },
                            {
                                "select": "intervalX",
                                "bind": "$range",
                                "brush": {"fill": "none", "stroke": "#888"},
                            },
                            {
                                "select": "highlight",
                                "by": "$range",
                                "fill": "#ccc",
                                "fill_opacity": 0.2,
                            },
                            {"legend": "color", "bind": "$click", "columns": 1},
                        ],
                        "xy_domain": "Fixed",
                        "x_tick_format": "%b",
                        "color_domain": "$domain",
                        "color_range": "$colors",
                        "r_domain": "Fixed",
                        "r_range": [2, 10],
                        "width": 680,
                        "height": 300,
                    }
                ]
            },
            {
                "plot": [
                    {
                        "mark": "barX",
                        "data": {"source": "weather"},
                        "x": {"count": None},
                        "y": "weather",
                        "fill": "#ccc",
                        "fill_opacity": 0.2,
                    },
                    {
                        "mark": "barX",
                        "data": {"source": "weather", "filter_by": "$range"},
                        "x": {"count": None},
                        "y": "weather",
                        "fill": "weather",
                    },
                    {"select": "toggleY", "bind": "$click"},
                    {"select": "highlight", "by": "$click"},
                ],
                "x_domain": "Fixed",
                "y_domain": "$domain",
                "y_label": None,
                "color_domain": "$domain",
                "color_range": "$colors",
                "width": 680,
            },
        ],
    }  # ty: ignore[invalid-assignment]
