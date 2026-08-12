"""Density Groups.

Density plots of penguin bill depths, grouped by species. The normalize parameter supports different forms of comparison, controlling if an individual density estimate is scaled by total point mass or normalized by the sum or max of the point mass. The stack and offset parameters control stacking of density areas.

"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.VConcat = {
        "data": {"penguins": {"file": "data/penguins.parquet"}},
        "params": {"bandwidth": 20, "normalize": "none", "stack": False, "offset": None},
        "vconcat": [
            {
                "hconcat": [
                    {
                        "input": "menu",
                        "label": "Normalize",
                        "bind": "$normalize",
                        "options": ["none", "sum", "max"],
                    },
                    {"input": "menu", "label": "Stack", "bind": "$stack", "options": [False, True]},
                    {
                        "input": "menu",
                        "label": "Offset",
                        "bind": "$offset",
                        "options": [
                            {"label": "none", "value": None},
                            {"label": "normalize", "value": "normalize"},
                            {"label": "center", "value": "center"},
                        ],
                    },
                ]
            },
            {
                "plot": [
                    {
                        "mark": "densityY",
                        "data": {"source": "penguins"},
                        "x": "bill_depth",
                        "fill": "species",
                        "fill_opacity": 0.4,
                        "bandwidth": "$bandwidth",
                        "normalize": "$normalize",
                        "stack": "$stack",
                        "offset": "$offset",
                    }
                ],
                "margin_left": 50,
                "height": 200,
            },
        ],
    }
