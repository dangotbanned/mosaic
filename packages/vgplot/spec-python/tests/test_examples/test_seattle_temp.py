"""Seattle Temperatures.

Historical monthly temperatures in Seattle, WA. The gray range shows the minimum and maximum recorded temperatures. The blue range shows the average lows and highs.

"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.Spec = {
        "data": {"weather": {"file": "data/seattle-weather.parquet"}},
        "plot": [
            {
                "mark": "areaY",
                "data": {"source": "weather"},
                "x": {"date_month": "date"},
                "y1": {"max": "temp_max"},
                "y2": {"min": "temp_min"},
                "fill": "#ccc",
                "fill_opacity": 0.25,
                "curve": "monotone-x",
            },
            {
                "mark": "areaY",
                "data": {"source": "weather"},
                "x": {"date_month": "date"},
                "y1": {"avg": "temp_max"},
                "y2": {"avg": "temp_min"},
                "fill": "steelblue",
                "fill_opacity": 0.75,
                "curve": "monotone-x",
            },
            {"mark": "ruleY", "data": [15], "stroke_opacity": 0.5, "stroke_dasharray": "5 5"},
        ],
        "x_tick_format": "%b",
        "y_label": "Temperature Range (°C)",
        "width": 680,
        "height": 300,
    }
