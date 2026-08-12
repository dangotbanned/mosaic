"""Wind Map.

`vector` marks on a grid show both direction and intensity—here, the speed of winds. Expressions for `rotate`, `length`, and `stroke` values are evaluated in the database. Both the legend and map support interactive selections to highlight values.

## Credit
Adapted from an [Observable Plot example](https://observablehq.com/@observablehq/plot-wind-map).
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.VConcat = {
        "data": {
            "wind": {"file": "data/wind.parquet", "select": ["*", "row_number() over () as id"]}
        },
        "params": {"selected": {"select": "union"}, "length": 2},
        "vconcat": [
            {"legend": "color", "plot": "wind-map", "label": "Speed (m/s)", "bind": "$selected"},
            {
                "name": "wind-map",
                "plot": [
                    {
                        "mark": "vector",
                        "data": {"source": "wind"},
                        "x": "longitude",
                        "y": "latitude",
                        "rotate": {"sql": "degrees(atan2(u, v))"},
                        "length": {"sql": "$length * sqrt(u * u + v * v)"},
                        "stroke": {"sql": "sqrt(u * u + v * v)"},
                        "channels": {"id": "id"},
                    },
                    {"select": "region", "bind": "$selected", "channels": ["id"]},
                    {"select": "highlight", "by": "$selected"},
                ],
                "length_scale": "identity",
                "color_zero": True,
                "inset": 10,
                "aspect_ratio": 1,
                "width": 680,
            },
            {
                "input": "slider",
                "min": 1,
                "max": 7,
                "step": 0.1,
                "bind": "$length",
                "label": "Vector Length",
            },
        ],  # ty: ignore[invalid-argument-type]
    }
