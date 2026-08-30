"""Density 1D.

Density plots (`densityY` mark) for over 200,000 flights, created using kernel density estimation.
Binning is performned in-database, subsequent smoothing in-browser. The distance density uses a
log-scaled domain. To change the amount of smoothing, use the slider to set the kernel bandwidth.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.VConcat = {
        "data": {"flights": {"file": "data/flights-200k.parquet"}},
        "params": {"brush": {"select": "crossfilter"}, "bandwidth": 20},
        "vconcat": [
            {
                "input": "slider",
                "label": "Bandwidth (σ)",
                "bind": "$bandwidth",
                "min": 0.1,
                "max": 100,
                "step": 0.1,
            },
            {
                "plot": [
                    {
                        "mark": "densityY",
                        "data": {"source": "flights", "filter_by": "$brush"},
                        "x": "delay",
                        "fill": "#888",
                        "fill_opacity": 0.5,
                        "bandwidth": "$bandwidth",
                    },
                    {"select": "intervalX", "bind": "$brush"},
                ],
                "y_axis": None,
                "x_domain": "Fixed",
                "width": 600,
                "margin_left": 10,
                "height": 200,
            },
            {
                "plot": [
                    {
                        "mark": "densityY",
                        "data": {"source": "flights", "filter_by": "$brush"},
                        "x": "distance",
                        "fill": "#888",
                        "fill_opacity": 0.5,
                        "bandwidth": "$bandwidth",
                    },
                    {"select": "intervalX", "bind": "$brush"},
                ],
                "y_axis": None,
                "x_scale": "log",
                "x_domain": "Fixed",
                "width": 600,
                "margin_left": 10,
                "height": 200,
            },
        ],
    }
