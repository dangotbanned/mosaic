"""Mark Types.

A subset of supported mark types.

- Row 1: `barY`, `lineY`, `text`, `tickY`, `areaY`
- Row 2: `regressionY`, `hexbin`, `contour`, `heatmap`, `denseLine`

"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.Spec = {
        "data": {
            "md": [
                {"i": 0, "u": "A", "v": 2},
                {"i": 1, "u": "B", "v": 8},
                {"i": 2, "u": "C", "v": 3},
                {"i": 3, "u": "D", "v": 7},
                {"i": 4, "u": "E", "v": 5},
                {"i": 5, "u": "F", "v": 4},
                {"i": 6, "u": "G", "v": 6},
                {"i": 7, "u": "H", "v": 1},
            ]
        },
        "plot_defaults": {
            "x_axis": None,
            "y_axis": None,
            "margins": {"left": 5, "top": 5, "right": 5, "bottom": 5},
            "width": 160,
            "height": 100,
            "y_domain": [0, 9],
        },
        "vconcat": [
            {
                "hconcat": [
                    {
                        "mark": "barY",
                        "data": {"source": "md"},
                        "x": "u",
                        "y": "v",
                        "fill": "steelblue",
                    },
                    {
                        "mark": "lineY",
                        "data": {"source": "md"},
                        "x": "u",
                        "y": "v",
                        "stroke": "steelblue",
                        "curve": "monotone-x",
                        "marker": "circle",
                    },
                    {
                        "mark": "text",
                        "data": {"source": "md"},
                        "x": "u",
                        "y": "v",
                        "text": "u",
                        "fill": "steelblue",
                    },
                    {
                        "mark": "tickY",
                        "data": {"source": "md"},
                        "x": "u",
                        "y": "v",
                        "stroke": "steelblue",
                    },
                    {
                        "mark": "areaY",
                        "data": {"source": "md"},
                        "x": "u",
                        "y": "v",
                        "fill": "steelblue",
                    },
                ]
            },
            {
                "hconcat": [
                    {
                        "plot": [
                            {
                                "mark": "dot",
                                "data": {"source": "md"},
                                "x": "i",
                                "y": "v",
                                "fill": "currentColor",
                                "r": 1.5,
                            },
                            {
                                "mark": "regressionY",
                                "data": {"source": "md"},
                                "x": "i",
                                "y": "v",
                                "stroke": "steelblue",
                            },
                        ],
                        "x_domain": [-0.5, 7.5],
                    },
                    {
                        "plot": [
                            {"mark": "hexgrid", "stroke": "#aaa", "stroke_opacity": 0.5},
                            {
                                "mark": "hexbin",
                                "data": {"source": "md"},
                                "x": "i",
                                "y": "v",
                                "fill": {"count": None},
                            },
                        ],
                        "color_scheme": "blues",
                        "x_domain": [-1, 8],
                    },
                    {
                        "plot": [
                            {
                                "mark": "contour",
                                "data": {"source": "md"},
                                "x": "i",
                                "y": "v",
                                "stroke": "steelblue",
                                "bandwidth": 15,
                            }
                        ],
                        "x_domain": [-1, 8],
                    },
                    {
                        "plot": [
                            {
                                "mark": "heatmap",
                                "data": {"source": "md"},
                                "x": "i",
                                "y": "v",
                                "fill": "density",
                                "bandwidth": 15,
                            }
                        ],
                        "color_scheme": "blues",
                        "x_domain": [-1, 8],
                    },
                    {
                        "plot": [
                            {
                                "mark": "denseLine",
                                "data": {"source": "md"},
                                "x": "i",
                                "y": "v",
                                "fill": "density",
                                "bandwidth": 2,
                                "pixel_size": 1,
                            }
                        ],
                        "color_scheme": "blues",
                        "x_domain": [-1, 8],
                    },
                ]
            },
        ],
    }
