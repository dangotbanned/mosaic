"""Overview + Detail.

Select the top "overview" series to zoom the "focus" view below. An `intervalX` interactor updates a
selection that filters the focus view. The `line` and `area` marks can apply [M4] optimization to
reduce the number of data points returned: rather than draw all points, a dramatically smaller
subset can still faithfully represent these area charts.

[M4]: https://observablehq.com/@uwdata/m4-scalable-time-series-visualization
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.VConcat = {
        "data": {"walk": {"file": "data/random-walk.parquet"}},
        "vconcat": [
            {
                "plot": [
                    {
                        "mark": "areaY",
                        "data": {"source": "walk"},
                        "x": "t",
                        "y": "v",
                        "fill": "steelblue",
                    },
                    {"select": "intervalX", "bind": "$brush"},
                ],
                "width": 680,
                "height": 200,
            },
            {
                "plot": [
                    {
                        "mark": "areaY",
                        "data": {"source": "walk", "filter_by": "$brush"},
                        "x": "t",
                        "y": "v",
                        "fill": "steelblue",
                    }
                ],
                "y_domain": "Fixed",
                "width": 680,
                "height": 200,
            },
        ],
    }
