"""Athlete Height Intervals.

Confidence intervals of Olympic athlete heights, in meters. Data are batched into groups of 10 samples per sport. Use the samples slider to see how the intervals update as the sample size increases (as in [online aggregation](https://en.wikipedia.org/wiki/Online_aggregation)). For each sport, the numbers on the right show the maximum number of athletes in the full dataset.

"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.Spec = {
        "data": {
            "athletes_batched": {
                "file": "data/athletes.parquet",
                "select": ["*", "10 * CEIL(ROW_NUMBER() OVER (PARTITION BY sport) / 10) AS batch"],
                "where": "height IS NOT NULL",
            }
        },
        "params": {"ci": 0.95, "query": {"select": "single"}},
        "hconcat": [
            {
                "vconcat": [
                    {
                        "hconcat": [
                            {
                                "input": "slider",
                                "select": "interval",
                                "bind": "$query",
                                "column": "batch",
                                "source": "athletesBatched",
                                "step": 10,
                                "value": 20,
                                "label": "Max Samples",
                            },
                            {
                                "input": "slider",
                                "bind": "$ci",
                                "min": 0.5,
                                "max": 0.999,
                                "step": 0.001,
                                "label": "Conf. Level",
                            },
                        ]
                    },
                    {
                        "name": "heights",
                        "plot": [
                            {
                                "mark": "errorbarX",
                                "data": {"source": "athletesBatched", "filter_by": "$query"},
                                "ci": "$ci",
                                "x": "height",
                                "y": "sport",
                                "stroke": "sex",
                                "stroke_width": 1,
                                "marker": "tick",
                                "sort": {"y": "-x"},
                            },
                            {
                                "mark": "text",
                                "data": {"source": "athletesBatched"},
                                "frame_anchor": "right",
                                "font_size": 8,
                                "fill": "#999",
                                "dx": 25,
                                "text": {"count": None},
                                "y": "sport",
                            },
                        ],
                        "x_domain": [1.5, 2.1],
                        "y_domain": "Fixed",
                        "y_grid": True,
                        "y_label": None,
                        "margin_top": 5,
                        "margin_left": 105,
                        "margin_right": 30,
                        "height": 420,
                    },
                    {"legend": "color", "plot": "heights"},
                ]
            }
        ],
    }  # ty: ignore[invalid-assignment]
