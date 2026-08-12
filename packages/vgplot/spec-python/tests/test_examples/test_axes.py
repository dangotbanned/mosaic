"""Axes & Gridlines.

Customized axis and gridline marks can be used in addition to standard scale attributes such as `xAxis`, `yGrid`, etc. Just add data!

"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.Plot = {
        "plot": [
            {"mark": "gridY", "stroke_dasharray": "0.75 2", "stroke_opacity": 1},
            {
                "mark": "axisY",
                "anchor": "left",
                "tick_size": 0,
                "dx": 38,
                "dy": -4,
                "line_anchor": "bottom",
            },
            {
                "mark": "axisY",
                "anchor": "right",
                "tick_size": 0,
                "tick_padding": 5,
                "label": "y-axis",
                "label_anchor": "center",
            },
            {"mark": "axisX", "label": "x-axis", "label_anchor": "center"},
            {"mark": "gridX"},
            {"mark": "ruleY", "data": [0]},
        ],
        "x_domain": [0, 100],
        "y_domain": [0, 100],
        "x_inset_left": 36,
        "margin_left": 0,
        "margin_right": 35,
        "width": 680,
    }
