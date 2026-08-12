"""Athlete Birth Waffle.

Waffle chart counting Olympic athletes based on which half-decade they were born. The inputs enable adjustment of waffle mark design options.


## Credit
Adapted from an [Observable Plot example](https://observablehq.com/@observablehq/plot-waffle-unit).
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.Spec = {
        "data": {"athletes": {"file": "data/athletes.parquet"}},
        "params": {"unit": 10, "round": False, "gap": 1, "radius": 0},
        "vconcat": [
            {
                "hconcat": [
                    {
                        "input": "menu",
                        "bind": "$unit",
                        "options": [1, 2, 5, 10, 25, 50, 100],
                        "label": "Unit",
                    },
                    {"input": "menu", "bind": "$round", "options": [True, False], "label": "Round"},
                    {
                        "input": "menu",
                        "bind": "$gap",
                        "options": [0, 1, 2, 3, 4, 5],
                        "label": "Gap",
                    },
                    {
                        "input": "slider",
                        "bind": "$radius",
                        "min": 0,
                        "max": 10,
                        "step": 0.1,
                        "label": "Radius",
                    },
                ]
            },
            {"vspace": 10},
            {
                "plot": [
                    {
                        "mark": "waffleY",
                        "data": {"source": "athletes"},
                        "unit": "$unit",
                        "round": "$round",
                        "gap": "$gap",
                        "rx": "$radius",
                        "x": {"sql": '5 * floor(year("date_of_birth") / 5)'},
                        "y": {"count": None},
                    }
                ],
                "x_label": None,
                "x_tick_size": 0,
                "x_tick_format": "d",
            },
        ],
    }
