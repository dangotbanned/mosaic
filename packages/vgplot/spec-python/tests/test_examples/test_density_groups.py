"""Density Groups.

Density plots of penguin bill depths, grouped by species. The normalize parameter supports different
forms of comparison, controlling if an individual density estimate is scaled by total point mass or
normalized by the sum or max of the point mass. The stack and offset parameters control stacking of
density areas.
"""

from __future__ import annotations

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
                        "bind": ms.ParamRef("$normalize"),
                        "options": ["none", "sum", "max"],
                    },
                    {
                        "input": "menu",
                        "label": "Stack",
                        "bind": ms.ParamRef("$stack"),
                        "options": [False, True],
                    },
                    {
                        "input": "menu",
                        "label": "Offset",
                        "bind": ms.ParamRef("$offset"),
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
                        "bandwidth": ms.ParamRef("$bandwidth"),
                        "normalize": ms.ParamRef("$normalize"),
                        "stack": ms.ParamRef("$stack"),
                        "offset": ms.ParamRef("$offset"),
                    }
                ],
                "margin_left": 50,
                "height": 200,
            },
        ],
    }
