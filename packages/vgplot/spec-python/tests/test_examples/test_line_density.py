"""Line Density.

The `denseLine` mark shows the densities of line series, here for a collection of stock prices. The
top plot normalizes by arc length to remove the vertical artifacts visible in the unnormalized plot
below. Select a region in the lower plot to zoom the upper plot. The bandwidth slider smooths the
data, while the pixel size menu adjusts the raster resolution.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.VConcat = {
        "data": {
            "stocks_after_2006": {
                "file": "data/stocks_after_2006.parquet",
                "select": ["Symbol", "Close", "Date"],
                "where": "Close < 100",
            }
        },
        "params": {
            "brush": {"select": "intersect"},
            "bandwidth": 0,
            "pixel_size": 2,
            "scheme_color": "pubugn",
            "scale_color": "sqrt",
        },
        "vconcat": [
            {
                "hconcat": [
                    {
                        "input": "slider",
                        "label": "Bandwidth (σ)",
                        "bind": "$bandwidth",
                        "min": 0,
                        "max": 10,
                        "step": 0.1,
                    },
                    {
                        "input": "menu",
                        "label": "Pixel Size",
                        "bind": "$pixelSize",
                        "options": [0.5, 1, 2],
                    },
                ]
            },
            {"vspace": 10},
            {
                "plot": [
                    {
                        "mark": "denseLine",
                        "data": {"source": "stocks_after_2006", "filter_by": "$brush"},
                        "x": "Date",
                        "y": "Close",
                        "z": "Symbol",
                        "fill": "density",
                        "bandwidth": "$bandwidth",
                        "pixel_size": "$pixelSize",
                    }
                ],
                "color_scheme": "$schemeColor",
                "color_scale": "$scaleColor",
                "y_label": "Close (Normalized) ↑",
                "y_nice": True,
                "margins": {"left": 30, "top": 20, "right": 0},
                "width": 680,
                "height": 240,
            },
            {
                "plot": [
                    {
                        "mark": "denseLine",
                        "data": {"source": "stocks_after_2006"},
                        "x": "Date",
                        "y": "Close",
                        "z": "Symbol",
                        "fill": "density",
                        "normalize": False,
                        "bandwidth": "$bandwidth",
                        "pixel_size": "$pixelSize",
                    },
                    {"select": "intervalXY", "bind": "$brush"},
                ],
                "color_scheme": "$schemeColor",
                "color_scale": "$scaleColor",
                "y_label": "Close (Unnormalized) ↑",
                "y_nice": True,
                "margins": {"left": 30, "top": 20, "right": 0},
                "width": 680,
                "height": 240,
            },
        ],
    }
