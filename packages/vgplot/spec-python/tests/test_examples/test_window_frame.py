"""Time-Based Moving Average.

Moving averages of Apple stock prices, using `range` window frames that span 15 days (black) and 3
months (red) around each date.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.Plot = {
        "data": {"aapl": {"file": "data/stocks.parquet", "where": "Symbol = 'AAPL'"}},
        "plot": [
            {
                "mark": "lineY",
                "data": {"source": "aapl"},
                "stroke": "#ccc",
                "x": "Date",
                "y": "Close",
            },
            {
                "mark": "lineY",
                "data": {"source": "aapl"},
                "stroke": "black",
                "x": "Date",
                "y": {"avg": "Close", "order_by": "Date", "range": ({"days": 15}, {"days": 15})},
            },
            {
                "mark": "lineY",
                "data": {"source": "aapl"},
                "stroke": "firebrick",
                "x": "Date",
                "y": {"avg": "Close", "order_by": "Date", "range": ({"months": 3}, {"months": 3})},
            },
        ],
        "y_label": "Close",
        "width": 680,
        "height": 200,
    }
