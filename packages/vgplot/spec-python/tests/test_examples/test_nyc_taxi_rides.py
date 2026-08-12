"""NYC Taxi Rides.

Pickup and dropoff points for 1M NYC taxi rides on Jan 1-3, 2010.
This example projects lon/lat coordinates in the database upon load.
Select a region in one plot to filter the other.
What spatial patterns can you find?
Requires the DuckDB `spatial` extension.

_You may need to wait a few seconds for the dataset to load._
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.VConcat = {
        "config": {"extensions": "spatial"},
        "data": {
            "rides": {
                "file": "https://pub-1da360b43ceb401c809f68ca37c7f8a4.r2.dev/data/nyc-rides-2010.parquet",
                "select": [
                    "pickup_datetime::TIMESTAMP AS datetime",
                    "ST_Transform(ST_Point(pickup_latitude, pickup_longitude), 'EPSG:4326', 'ESRI:102718') AS pick",
                    "ST_Transform(ST_Point(dropoff_latitude, dropoff_longitude), 'EPSG:4326', 'ESRI:102718') AS drop",
                ],
            },
            "trips": "SELECT\n  (HOUR(datetime) + MINUTE(datetime)/60) AS time,\n  ST_X(pick) AS px, ST_Y(pick) AS py,\n  ST_X(drop) AS dx, ST_Y(drop) AS dy\nFROM rides\n",
        },
        "params": {"filter": {"select": "crossfilter"}},
        "vconcat": [
            {
                "hconcat": [
                    {
                        "plot": [
                            {
                                "mark": "raster",
                                "data": {"source": "trips", "filter_by": "$filter"},
                                "x": "px",
                                "y": "py",
                                "bandwidth": 0,
                            },
                            {"select": "intervalXY", "bind": "$filter"},
                            {
                                "mark": "text",
                                "data": [{"label": "Taxi Pickups"}],
                                "dx": 10,
                                "dy": 10,
                                "text": "label",
                                "fill": "black",
                                "font_size": "1.2em",
                                "frame_anchor": "top-left",
                            },
                        ],
                        "width": 335,
                        "height": 550,
                        "margin": 0,
                        "x_axis": None,
                        "y_axis": None,
                        "x_domain": ["9.75e5", "1.005e6"],
                        "y_domain": ["1.9e5", "2.4e5"],
                        "color_scale": "symlog",
                        "color_scheme": "blues",
                    },
                    {"hspace": 10},
                    {
                        "plot": [
                            {
                                "mark": "raster",
                                "data": {"source": "trips", "filter_by": "$filter"},
                                "x": "dx",
                                "y": "dy",
                                "bandwidth": 0,
                            },
                            {"select": "intervalXY", "bind": "$filter"},
                            {
                                "mark": "text",
                                "data": [{"label": "Taxi Dropoffs"}],
                                "dx": 10,
                                "dy": 10,
                                "text": "label",
                                "fill": "black",
                                "font_size": "1.2em",
                                "frame_anchor": "top-left",
                            },
                        ],
                        "width": 335,
                        "height": 550,
                        "margin": 0,
                        "x_axis": None,
                        "y_axis": None,
                        "x_domain": ["9.75e5", "1.005e6"],
                        "y_domain": ["1.9e5", "2.4e5"],
                        "color_scale": "symlog",
                        "color_scheme": "oranges",
                    },
                ]
            },
            {"vspace": 10},
            {
                "plot": [
                    {
                        "mark": "rectY",
                        "data": {"source": "trips"},
                        "x": {"bin": "time"},
                        "y": {"count": None},
                        "fill": "steelblue",
                        "inset": 0.5,
                    },
                    {"select": "intervalX", "bind": "$filter"},
                ],
                "y_tick_format": "s",
                "x_label": "Pickup Hour →",
                "width": 680,
                "height": 100,
            },
        ],  # ty: ignore[invalid-argument-type]
    }
