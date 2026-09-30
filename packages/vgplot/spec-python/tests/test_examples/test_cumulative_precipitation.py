"""Cumulative Precipitation.

Monthly and cumulative precipitation in Seattle during 2015. The bars sum daily observations within
each month. The line uses a nested aggregate to accumulate those monthly totals through the year.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


# NOTE: Depends on (manually removed) circular typing which broke `ty` and `pyright`
def test_infer() -> None:
    _spec: ms.spec.VConcat = {
        "data": {
            "seattle_2015": {
                "file": "data/seattle-weather.parquet",
                "where": "date >= DATE '2015-01-01' AND date < DATE '2016-01-01'",
            }
        },
        # pyrefly: ignore [bad-assignment]
        "vconcat": [
            {
                "plot": [
                    {
                        "mark": "barY",
                        "data": {"source": "seattle_2015"},
                        "x": {"date_month": "date"},
                        "y": {"sum": "precipitation"},
                        "fill": "steelblue",
                    }
                ],
                "x_scale": "band",
                "x_tick_format": "%b",
                "x_label": None,
                "y_label": "Monthly precipitation (mm)",
                "y_grid": True,
                "width": 680,
                "height": 200,
            },
            {  # pyright: ignore[reportAssignmentType]
                "plot": [
                    {
                        "mark": "lineY",
                        "data": {"source": "seattle_2015"},
                        "x": {"date_month": "date"},
                        "y": {"sum": {"sum": "precipitation"}, "order_by": {"date_month": "date"}},
                        "stroke": "steelblue",
                        "marker": "circle",
                    }
                ],
                "x_tick_format": "%b",
                "x_label": None,
                "y_label": "Cumulative precipitation (mm)",
                "y_grid": True,
                "y_zero": True,
                "width": 680,
                "height": 240,
            },
        ],  # ty: ignore[invalid-argument-type]
    }
