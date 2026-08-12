"""Area Sine Wave.

A test specification to compare M4 optimized and unoptimized area charts over a dense dual-tone sine wave.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.VConcat = {
        "data": {"wave": {"file": "data/m4-area-sine.csv"}},
        "vconcat": [
            {
                "plot": [
                    {
                        "mark": "areaY",
                        "data": {"source": "wave", "filter_by": "$brush"},
                        "x": "time_stamp",
                        "y": "power",
                    }
                ],
                "y_domain": "Fixed",
                "color_domain": "Fixed",
                "x_label": None,
                "width": 680,
                "height": 180,
            },
            {"vspace": 5},
            {
                "plot": [
                    {
                        "mark": "areaY",
                        "data": {"source": "wave", "filter_by": "$brush", "optimize": False},
                        "x": "time_stamp",
                        "y": "power",
                    }
                ],
                "y_domain": "Fixed",
                "color_domain": "Fixed",
                "x_label": None,
                "width": 680,
                "height": 180,
            },
            {"vspace": 10},
            {
                "plot": [
                    {
                        "mark": "areaY",
                        "data": {"source": "wave", "optimize": False},
                        "x": "time_stamp",
                        "y": "power",
                    },
                    {"select": "intervalX", "bind": "$brush"},
                ],
                "y_domain": "Fixed",
                "width": 680,
                "height": 90,
            },
        ],
    }
