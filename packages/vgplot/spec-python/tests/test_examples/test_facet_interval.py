"""Faceted Interval Selections.

A faceted plot with 2D interval selections.

## Credit
Adapted from https://observablehq.com/@observablehq/plot-non-faceted-marks
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.Spec = {
        "data": {"penguins": {"file": "data/penguins.parquet"}},
        "hconcat": [
            {
                "name": "plot",
                "plot": [
                    {"mark": "frame"},
                    {
                        "mark": "dot",
                        "data": {"source": "penguins"},
                        "x": "bill_length",
                        "y": "bill_depth",
                        "fill": "#aaa",
                        "r": 1,
                    },
                    {
                        "mark": "dot",
                        "data": {"source": "penguins"},
                        "x": "bill_length",
                        "y": "bill_depth",
                        "fill": "species",
                        "fx": "sex",
                        "fy": "species",
                    },
                    {"select": "intervalXY", "bind": "$sel", "brush": {"stroke": "transparent"}},
                    {"select": "highlight", "by": "$sel"},
                ],
                "grid": True,
                "margin_right": 60,
                "x_domain": "Fixed",
                "y_domain": "Fixed",
                "fx_domain": "Fixed",
                "fy_domain": "Fixed",
                "fx_label": None,
                "fy_label": None,
            }
        ],
    }
