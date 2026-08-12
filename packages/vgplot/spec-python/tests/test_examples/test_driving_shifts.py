"""Driving Shifts into Reverse.

A connected scatter plot of miles driven vs. gas prices.

## Credit
Adapted from an [Observable Plot example](https://observablehq.com/@observablehq/plot-connected-scatterplot), which in turn adapts Hannah Fairfield's [New York Times article](http://www.nytimes.com/imagepages/2010/05/02/business/02metrics.html).

"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.Plot = {
        "data": {"driving": {"file": "data/driving.parquet"}},
        "plot": [
            {
                "mark": "line",
                "data": {"source": "driving"},
                "x": "miles",
                "y": "gas",
                "curve": "catmull-rom",
                "marker": True,
            },
            {
                "mark": "text",
                "data": {"source": "driving"},
                "x": "miles",
                "y": "gas",
                "text": {"sql": "year::VARCHAR"},
                "dy": -6,
                "line_anchor": "bottom",
                "filter": {"sql": "year % 5 = 0"},
            },
        ],
        "inset": 10,
        "grid": True,
        "x_label": "Miles driven (per person-year)",
        "y_label": "Cost of gasoline ($ per gallon)",
    }
