"""Olympic Athletes.

An interactive dashboard of athlete statistics. The menus and searchbox filter the display and are
automatically populated by backing data columns.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.HConcat = {
        "data": {"athletes": {"file": "data/athletes.parquet"}},
        "params": {
            "category": {"select": "intersect"},
            "query": {"select": "intersect", "include": "$category"},
            "hover": {"select": "intersect", "empty": True},
        },
        "hconcat": [
            {
                "vconcat": [
                    {
                        "hconcat": [
                            {
                                "input": "menu",
                                "label": "Sport",
                                "bind": "$category",
                                "source": "athletes",
                                "column": "sport",
                            },
                            {
                                "input": "menu",
                                "label": "Sex",
                                "bind": "$category",
                                "source": "athletes",
                                "column": "sex",
                            },
                            {
                                "input": "search",
                                "label": "Name",
                                "filter_by": "$category",
                                "bind": "$query",
                                "source": "athletes",
                                "column": "name",
                                "type": "contains",
                            },
                        ]
                    },
                    {"vspace": 10},
                    {
                        "plot": [
                            {
                                "mark": "dot",
                                "data": {"source": "athletes", "filter_by": "$query"},
                                "x": "weight",
                                "y": "height",
                                "fill": "sex",
                                "r": 2,
                                "opacity": 0.1,
                            },
                            {
                                "mark": "regressionY",
                                "data": {"source": "athletes", "filter_by": "$query"},
                                "x": "weight",
                                "y": "height",
                                "stroke": "sex",
                            },
                            {
                                "select": "intervalXY",
                                "bind": "$query",
                                "brush": {"fill_opacity": 0, "stroke": "black"},
                            },
                            {
                                "mark": "dot",
                                "data": {"source": "athletes", "filter_by": "$hover"},
                                "x": "weight",
                                "y": "height",
                                "fill": "sex",
                                "stroke": "currentColor",
                                "stroke_width": 1,
                                "r": 3,
                            },
                        ],
                        "xy_domain": "Fixed",
                        "color_domain": "Fixed",
                        "margins": {"left": 35, "top": 20, "right": 1},
                        "width": 570,
                        "height": 350,
                    },
                    {"vspace": 5},
                    {
                        "input": "table",
                        "source": "athletes",
                        "max_width": 570,
                        "height": 250,
                        "filter_by": "$query",
                        "bind": "$hover",
                        "columns": ["name", "nationality", "sex", "height", "weight", "sport"],
                        "width": {
                            "name": 180,
                            "nationality": 100,
                            "sex": 50,
                            "height": 50,
                            "weight": 50,
                            "sport": 100,
                        },
                    },
                ]
            }
        ],
    }
