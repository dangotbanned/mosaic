"""Linear Regression 10M.

A linear regression plot predicting flight arrival delay based on the time of departure, over 10 million flight records. Regression computation is performed in the database, with optimized selection updates using pre-aggregated materialized views. The area around a regression line shows a 95% confidence interval. Select a region to view regression results for a data subset.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.VConcat = {
        "data": {
            "flights10m": "SELECT GREATEST(-60, LEAST(ARR_DELAY, 180))::DOUBLE AS delay, DISTANCE AS distance, DEP_TIME AS time FROM 'https://pub-1da360b43ceb401c809f68ca37c7f8a4.r2.dev/data/flights-10m.parquet'",
            "flights10p": "SELECT * FROM flights10m USING SAMPLE 10%",
            "flights5p": "SELECT * FROM flights10m USING SAMPLE 5%",
            "flights1p": "SELECT * FROM flights10m USING SAMPLE 1%",
        },
        "params": {"data": "flights10m"},
        "vconcat": [
            {
                "input": "menu",
                "label": "Sample",
                "bind": "$data",
                "options": [
                    {"value": "flights10m", "label": "Full Data"},
                    {"value": "flights10p", "label": "10% Sample"},
                    {"value": "flights5p", "label": "5% Sample"},
                    {"value": "flights1p", "label": "1% Sample"},
                ],
            },
            {"vspace": 10},
            {
                "plot": [
                    {
                        "mark": "raster",
                        "data": {"source": "$data"},
                        "x": "time",
                        "y": "delay",
                        "pixel_size": 4,
                        "pad": 0,
                        "image_rendering": "pixelated",
                    },
                    {
                        "mark": "regressionY",
                        "data": {"source": "$data"},
                        "x": "time",
                        "y": "delay",
                        "stroke": "gray",
                    },
                    {
                        "mark": "regressionY",
                        "data": {"source": "$data", "filter_by": "$query"},
                        "x": "time",
                        "y": "delay",
                        "stroke": "firebrick",
                    },
                    {
                        "select": "intervalXY",
                        "bind": "$query",
                        "brush": {"fill_opacity": 0, "stroke": "currentColor"},
                    },
                ],
                "x_domain": [0, 24],
                "y_domain": [-60, 180],
                "color_scale": "symlog",
                "color_scheme": "blues",
                "color_domain": "Fixed",
            },
        ],
    }
