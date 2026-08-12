"""Gaia Star Catalog.

A 5M row sample of the 1.8B element Gaia star catalog.
A `raster` sky map reveals our Milky Way galaxy. Select high parallax stars in the histogram to reveal a
[Hertzsprung-Russel diagram](https://en.wikipedia.org/wiki/Hertzsprung%E2%80%93Russell_diagram)
in the plot of stellar color vs. magnitude on the right.

_You may need to wait a few seconds for the dataset to load._

"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.HConcat = {
        "data": {
            "gaia": "-- compute u and v with natural earth projection\nWITH prep AS (\n  SELECT\n    radians((-l + 540) % 360 - 180) AS lambda,\n    radians(b) AS phi,\n    asin(sqrt(3)/2 * sin(phi)) AS t,\n    t^2 AS t2,\n    t2^3 AS t6,\n    *\n  FROM 'https://pub-1da360b43ceb401c809f68ca37c7f8a4.r2.dev/data/gaia-5m.parquet'\n  WHERE parallax BETWEEN -5 AND 20 AND phot_g_mean_mag IS NOT NULL AND bp_rp IS NOT NULL\n)\nSELECT\n  (1.340264 * \"lambda\" * cos(t)) / (sqrt(3)/2 * (1.340264 + (-0.081106 * 3 * t2) + (t6 * (0.000893 * 7 + 0.003796 * 9 * t2)))) AS u,\n  t * (1.340264 + (-0.081106 * t2) + (t6 * (0.000893 + 0.003796 * t2))) AS v,\n  * EXCLUDE('t', 't2', 't6')\nFROM prep\n"
        },
        "params": {
            "brush": {"select": "crossfilter"},
            "bandwidth": 0,
            "pixel_size": 2,
            "scale_type": "sqrt",
        },
        "hconcat": [
            {
                "vconcat": [
                    {
                        "plot": [
                            {
                                "mark": "raster",
                                "data": {"source": "gaia", "filter_by": "$brush"},
                                "x": "u",
                                "y": "v",
                                "fill": "density",
                                "bandwidth": "$bandwidth",
                                "pixel_size": "$pixelSize",
                            },
                            {"select": "intervalXY", "pixel_size": 2, "bind": "$brush"},
                        ],
                        "xy_domain": "Fixed",
                        "color_scale": "$scaleType",
                        "color_scheme": "viridis",
                        "width": 440,
                        "height": 250,
                        "margin_left": 25,
                        "margin_top": 20,
                        "margin_right": 1,
                    },
                    {
                        "hconcat": [
                            {
                                "plot": [
                                    {
                                        "mark": "rectY",
                                        "data": {"source": "gaia", "filter_by": "$brush"},
                                        "x": {"bin": "phot_g_mean_mag"},
                                        "y": {"count": None},
                                        "fill": "steelblue",
                                        "inset": 0.5,
                                    },
                                    {"select": "intervalX", "bind": "$brush"},
                                ],
                                "x_domain": "Fixed",
                                "y_scale": "$scaleType",
                                "y_grid": True,
                                "width": 220,
                                "height": 120,
                                "margin_left": 65,
                            },
                            {
                                "plot": [
                                    {
                                        "mark": "rectY",
                                        "data": {"source": "gaia", "filter_by": "$brush"},
                                        "x": {"bin": "parallax"},
                                        "y": {"count": None},
                                        "fill": "steelblue",
                                        "inset": 0.5,
                                    },
                                    {"select": "intervalX", "bind": "$brush"},
                                ],
                                "x_domain": "Fixed",
                                "y_scale": "$scaleType",
                                "y_grid": True,
                                "width": 220,
                                "height": 120,
                                "margin_left": 65,
                            },
                        ]
                    },
                ]
            },
            {"hspace": 10},
            {
                "plot": [
                    {
                        "mark": "raster",
                        "data": {"source": "gaia", "filter_by": "$brush"},
                        "x": "bp_rp",
                        "y": "phot_g_mean_mag",
                        "fill": "density",
                        "bandwidth": "$bandwidth",
                        "pixel_size": "$pixelSize",
                    },
                    {"select": "intervalXY", "pixel_size": 2, "bind": "$brush"},
                ],
                "xy_domain": "Fixed",
                "color_scale": "$scaleType",
                "color_scheme": "viridis",
                "y_reverse": True,
                "width": 230,
                "height": 370,
                "margin_left": 25,
                "margin_top": 20,
                "margin_right": 1,
            },
        ],  # ty: ignore[invalid-argument-type]
    }
