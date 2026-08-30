"""Density 2D.

A 2D `density` plot in which circle size indicates the point density. The data is divided by fill
color into three sets of densities. To change the amount of smoothing, use the slider to set the
kernel bandwidth.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.VConcat = {
        "data": {"penguins": {"file": "data/penguins.parquet"}},
        "params": {"bandwidth": 20, "bins": 20},
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
                    {"input": "slider", "label": "Bins", "bind": "$bins", "min": 10, "max": 60},
                ]
            },
            {
                "plot": [
                    {
                        "mark": "density",
                        "data": {"source": "penguins"},
                        "x": "bill_length",
                        "y": "bill_depth",
                        "r": "density",
                        "fill": "species",
                        "fill_opacity": 0.5,
                        "width": "$bins",
                        "height": "$bins",
                        "bandwidth": "$bandwidth",
                    },
                    {
                        "mark": "dot",
                        "data": {"source": "penguins"},
                        "x": "bill_length",
                        "y": "bill_depth",
                        "fill": "currentColor",
                        "r": 1,
                    },
                ],
                "r_range": [0, 16],
                "x_axis": "bottom",
                "x_label_anchor": "center",
                "y_axis": "right",
                "y_label_anchor": "center",
                "margins": {"top": 5, "bottom": 30, "left": 5, "right": 50},
                "width": 700,
                "height": 480,
            },
        ],
    }
