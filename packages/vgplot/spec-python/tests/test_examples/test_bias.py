"""Bias Parameter.

Dynamically adjust queried values by adding a Param value. The SQL expression is re-computed in the database upon updates.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.VConcat = {
        "data": {"walk": {"file": "data/random-walk.parquet"}},
        "params": {"point": 0},
        "vconcat": [
            {
                "input": "slider",
                "label": "Bias",
                "bind": "$point",
                "min": 0,
                "max": 1000,
                "step": 1,
            },
            {
                "plot": [
                    {
                        "mark": "areaY",
                        "data": {"source": "walk"},
                        "x": "t",
                        "y": {"sql": "v + $point"},
                        "fill": "steelblue",
                    }
                ],
                "width": 680,
                "height": 200,
            },
        ],
    }
