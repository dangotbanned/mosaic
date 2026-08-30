"""Aeromagnetic Survey.

A raster visualization of the 1955 [Great Britain aeromagnetic survey], which measured the Earth's
magnetic field by plane. Each sample recorded the longitude and latitude alongside the strength of
the [IGRF] in [nanoteslas]. This example demonstrates both raster interpolation and smoothing (blur)
options.

## Credit

Adapted from an [Observable Plot example].

[Great Britain aeromagnetic survey]: https://www.bgs.ac.uk/datasets/gb-aeromagnetic-survey/
[IGRF]: https://www.ncei.noaa.gov/products/international-geomagnetic-reference-field
[nanoteslas]: https://en.wikipedia.org/wiki/Tesla_(unit)
[Observable Plot example]: https://observablehq.com/@observablehq/plot-igfr90-raster
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.VConcat = {
        "data": {"ca55": {"file": "data/ca55-south.parquet"}},
        "params": {"interp": "random-walk", "blur": 0},
        "vconcat": [
            {
                "hconcat": [
                    {
                        "input": "menu",
                        "label": "Interpolation Method",
                        "options": ["none", "nearest", "barycentric", "random-walk"],
                        "bind": "$interp",
                    },
                    {"hspace": "1em"},
                    {"input": "slider", "label": "Blur", "min": 0, "max": 100, "bind": "$blur"},
                ]
            },
            {"vspace": "1em"},
            {
                "plot": [
                    {
                        "mark": "raster",
                        "data": {"source": "ca55"},
                        "x": "LONGITUDE",
                        "y": "LATITUDE",
                        "fill": {"max": "MAG_IGRF90"},
                        "interpolate": "$interp",
                        "bandwidth": "$blur",
                    }
                ],
                "color_scale": "diverging",
                "color_domain": "Fixed",
            },
        ],
    }
