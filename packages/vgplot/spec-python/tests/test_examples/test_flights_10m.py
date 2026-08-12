"""Cross-Filter Flights (10M).

Histograms showing arrival delay, departure time, and distance flown for 10 million flights.
Once loaded, automatic pre-aggregation optimizations enable efficient cross-filtered selections.

_You may need to wait a few seconds for the dataset to load._

"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.Spec = {
        "data": {
            "flights10m": "SELECT GREATEST(-60, LEAST(ARR_DELAY, 180))::DOUBLE AS delay, DISTANCE AS distance, DEP_TIME AS time FROM 'https://pub-1da360b43ceb401c809f68ca37c7f8a4.r2.dev/data/flights-10m.parquet'"
        },
        "params": {"brush": {"select": "crossfilter"}},
        "vconcat": [
            {
                "plot": [
                    {
                        "mark": "rectY",
                        "data": {"source": "flights10m", "filter_by": "$brush"},
                        "x": {"bin": "delay"},
                        "y": {"count": None},
                        "fill": "steelblue",
                        "inset_left": 0.5,
                        "inset_right": 0.5,
                    },
                    {"select": "intervalX", "bind": "$brush"},
                ],
                "x_domain": "Fixed",
                "x_label": "Arrival Delay (min)",
                "y_tick_format": "s",
                "width": 600,
                "height": 200,
            },
            {
                "plot": [
                    {
                        "mark": "rectY",
                        "data": {"source": "flights10m", "filter_by": "$brush"},
                        "x": {"bin": "time"},
                        "y": {"count": None},
                        "fill": "steelblue",
                        "inset_left": 0.5,
                        "inset_right": 0.5,
                    },
                    {"select": "intervalX", "bind": "$brush"},
                ],
                "x_domain": "Fixed",
                "x_label": "Departure Time (hour)",
                "y_tick_format": "s",
                "width": 600,
                "height": 200,
            },
            {
                "plot": [
                    {
                        "mark": "rectY",
                        "data": {"source": "flights10m", "filter_by": "$brush"},
                        "x": {"bin": "distance"},
                        "y": {"count": None},
                        "fill": "steelblue",
                        "inset_left": 0.5,
                        "inset_right": 0.5,
                    },
                    {"select": "intervalX", "bind": "$brush"},
                ],
                "x_domain": "Fixed",
                "x_label": "Flight Distance (miles)",
                "y_tick_format": "s",
                "width": 600,
                "height": 200,
            },
        ],
    }  # ty: ignore[invalid-assignment]
