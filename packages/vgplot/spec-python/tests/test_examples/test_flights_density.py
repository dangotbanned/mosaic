"""Flights Density.

Density `heatmap` and `contour` lines for 200,000+ flights by departure hour and arrival delay. The
sliders adjust the smoothing (bandwidth) and number of contour thresholds.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.VConcat = {
        "data": {"flights": {"file": "data/flights-200k.parquet"}},
        "params": {"bandwidth": 7, "thresholds": 10},
        "vconcat": [
            {
                "hconcat": [
                    {
                        "input": "slider",
                        "label": "Bandwidth (σ)",
                        "bind": "$bandwidth",
                        "min": 1,
                        "max": 100,
                    },
                    {
                        "input": "slider",
                        "label": "Thresholds",
                        "bind": "$thresholds",
                        "min": 2,
                        "max": 20,
                    },
                ]
            },
            {
                "plot": [
                    {
                        "mark": "heatmap",
                        "data": {"source": "flights"},
                        "x": "time",
                        "y": "delay",
                        "fill": "density",
                        "bandwidth": "$bandwidth",
                    },
                    {
                        "mark": "contour",
                        "data": {"source": "flights"},
                        "x": "time",
                        "y": "delay",
                        "stroke": "white",
                        "stroke_opacity": 0.5,
                        "bandwidth": "$bandwidth",
                        "thresholds": "$thresholds",
                    },
                ],
                "color_scale": "symlog",
                "color_scheme": "ylgnbu",
                "x_axis": "top",
                "x_label_anchor": "center",
                "x_zero": True,
                "y_axis": "right",
                "y_label_anchor": "center",
                "margin_top": 30,
                "margin_left": 5,
                "margin_right": 40,
                "width": 700,
                "height": 500,
            },
        ],
    }
