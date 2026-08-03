from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_line() -> None:
    _spec: ms.Spec = {
        "data": {
            "aapl": {"type": "parquet", "file": "data/stocks.parquet", "where": "Symbol = 'AAPL'"}
        },
        "plot": [{"mark": "lineY", "data": {"source": "aapl"}, "x": "Date", "y": "Close"}],
        "width": 680,
        "height": 200,
    }
