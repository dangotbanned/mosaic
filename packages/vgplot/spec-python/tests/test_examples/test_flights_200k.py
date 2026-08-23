"""Cross-Filter Flights (200k).

Histograms showing arrival delay, departure time, and distance flown for over 200,000 flights. Select a histogram region to cross-filter the charts. Each plot uses an `intervalX` interactor to populate a shared Selection with `crossfilter` resolution.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.VConcat = {
        "data": {"flights": {"file": "data/flights-200k.parquet"}},
        "params": {"brush": {"select": "crossfilter"}},
        "vconcat": [
            {
                "plot": [
                    {
                        "mark": "rectY",
                        "data": {"source": "flights", "filter_by": "$brush"},
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
                        "data": {"source": "flights", "filter_by": "$brush"},
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
                        "data": {"source": "flights", "filter_by": "$brush"},
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
    }
