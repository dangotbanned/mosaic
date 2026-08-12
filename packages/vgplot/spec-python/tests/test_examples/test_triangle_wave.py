"""Triangle Wave.

A test specification to compare M4 optimized and unoptimized line charts.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.VConcat = {
        "data": {"wave": {"file": "data/triangle-wave-day.csv"}},
        "vconcat": [
            {
                "plot": [
                    {
                        "mark": "lineY",
                        "data": {"source": "wave"},
                        "x": "time_stamp",
                        "y": "power",
                        "z": None,
                        "stroke": "time_stamp",
                    },
                    {"select": "intervalX", "bind": "$brush"},
                ],
                "x_label": None,
                "width": 680,
                "height": 150,
            },
            {"vspace": 5},
            {
                "plot": [
                    {
                        "mark": "lineY",
                        "data": {"source": "wave", "filter_by": "$brush"},
                        "x": "time_stamp",
                        "y": "power",
                        "z": None,
                        "stroke": "time_stamp",
                    }
                ],
                "y_domain": "Fixed",
                "color_domain": "Fixed",
                "x_label": None,
                "width": 680,
                "height": 150,
            },
            {"vspace": 5},
            {
                "plot": [
                    {
                        "mark": "lineY",
                        "data": {"source": "wave", "filter_by": "$brush", "optimize": False},
                        "x": "time_stamp",
                        "y": "power",
                        "z": None,
                        "stroke": "time_stamp",
                    }
                ],
                "y_domain": "Fixed",
                "color_domain": "Fixed",
                "x_label": None,
                "width": 680,
                "height": 150,
            },
        ],
    }
