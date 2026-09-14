"""Sorted Bars.

Sort and limit an aggregate bar chart of gold medals by country.
"""

from __future__ import annotations

import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.VConcat = {
        "data": {"athletes": {"file": "data/athletes.parquet"}},
        "vconcat": [
            {
                "input": "menu",
                "label": "Sport",
                "bind": ms.ParamRef("$query"),
                "source": "athletes",
                "column": "sport",
                "value": "aquatics",
            },
            {"vspace": 10},
            {
                "plot": [
                    {
                        "mark": "barX",
                        "data": {"source": "athletes", "filter_by": ms.ParamRef("$query")},
                        "x": {"sum": "gold"},
                        "y": "nationality",
                        "fill": "steelblue",
                        "sort": {"y": "-x", "limit": 10},
                    }
                ],
                "x_label": "Gold Medals",
                "y_label": "Nationality",
                "y_label_anchor": "top",
                "margin_top": 15,
            },
        ],
    }
