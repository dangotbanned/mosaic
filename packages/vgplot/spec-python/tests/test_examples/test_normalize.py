"""Normalized Stock Prices.

What is the return on investment for different days? Hover over the chart to normalize the stock
prices for the percentage return on a given day. A `nearestX` interactor selects the nearest date,
and parameterized expressions reactively update in response.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.Plot = {
        "data": {
            "stocks": {"file": "data/stocks.parquet"},
            "labels": "SELECT MAX(Date) as Date, ARGMAX(Close, Date) AS Close, Symbol FROM stocks GROUP BY Symbol",
        },
        "params": {"point": {"date": "2013-05-13"}},
        "plot": [
            {"mark": "ruleX", "x": "$point"},
            {
                "mark": "textX",
                "x": "$point",
                "text": "$point",
                "frame_anchor": "top",
                "line_anchor": "bottom",
                "dy": -7,
            },
            {
                "mark": "text",
                "data": {"source": "labels"},
                "x": "Date",
                "y": {
                    "sql": "Close / (SELECT max(Close) FROM stocks WHERE Symbol = source.Symbol AND Date = $point)"
                },
                "dx": 2,
                "text": "Symbol",
                "fill": "Symbol",
                "text_anchor": "start",
            },
            {
                "mark": "lineY",
                "data": {"source": "stocks"},
                "x": "Date",
                "y": {
                    "sql": "Close / (SELECT max(Close) FROM stocks WHERE Symbol = source.Symbol AND Date = $point)"
                },
                "stroke": "Symbol",
            },
            {"select": "nearestX", "bind": "$point"},
        ],
        "y_scale": "log",
        "y_domain": [0.2, 6],
        "y_grid": True,
        "x_label": None,
        "y_label": None,
        "y_tick_format": "%",
        "width": 680,
        "height": 400,
        "margin_right": 35,
    }
