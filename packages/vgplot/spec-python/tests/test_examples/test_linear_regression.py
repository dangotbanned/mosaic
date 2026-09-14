"""Linear Regression.

A linear regression plot predicting athletes' heights based on their weights. Regression computation
is performed in the database. The area around a regression line shows a 95% confidence interval.
Select a region to view regression results for a data subset.
"""

from __future__ import annotations

import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.Plot = {
        "data": {"athletes": {"file": "data/athletes.parquet"}},
        "plot": [
            {
                "mark": "dot",
                "data": {"source": "athletes"},
                "x": "weight",
                "y": "height",
                "fill": "sex",
                "r": 2,
                "opacity": 0.05,
            },
            {
                "mark": "regressionY",
                "data": {"source": "athletes", "filter_by": ms.ParamRef("$query")},
                "x": "weight",
                "y": "height",
                "stroke": "sex",
            },
            {
                "select": "intervalXY",
                "bind": ms.ParamRef("$query"),
                "brush": {"fill_opacity": 0, "stroke": "currentColor"},
            },
        ],
        "xy_domain": "Fixed",
        "color_domain": "Fixed",
    }
