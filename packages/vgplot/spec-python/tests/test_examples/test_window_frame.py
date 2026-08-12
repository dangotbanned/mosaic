"""TODO: missing meta."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.Spec = {
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
                "y": {"avg": "Close", "orderby": "Date", "range": [{"days": 15}, {"days": 15}]},
            },
            {
                "mark": "lineY",
                "data": {"source": "aapl"},
                "stroke": "firebrick",
                "x": "Date",
                "y": {"avg": "Close", "orderby": "Date", "range": [{"months": 3}, {"months": 3}]},
            },
        ],
        "y_label": "Close",
        "width": 680,
        "height": 200,
    }  # ty: ignore[invalid-assignment]
