"""Contour Plot.

Here `heatmap` and `contour` marks visualize the density of data points in a scatter plot of penguin
measurments. Setting the `fill` color to `"species"` subdivides the data into three sets of
densities.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.VConcat = {
        "data": {"penguins": {"file": "data/penguins.parquet"}},
        "params": {"bandwidth": 40, "thresholds": 10},
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
                        "data": {"source": "penguins"},
                        "x": "bill_length",
                        "y": "bill_depth",
                        "fill": "species",
                        "bandwidth": "$bandwidth",
                    },
                    {
                        "mark": "contour",
                        "data": {"source": "penguins"},
                        "x": "bill_length",
                        "y": "bill_depth",
                        "stroke": "species",
                        "bandwidth": "$bandwidth",
                        "thresholds": "$thresholds",
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
