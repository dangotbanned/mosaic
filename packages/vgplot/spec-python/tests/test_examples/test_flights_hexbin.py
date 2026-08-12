"""Flights Hexbin.

Hexagonal bins show the density of over 200,000 flights by departure time and arrival delay. Select regions in the marginal histograms to filter the density display.

"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.Spec = {
        "data": {"flights": {"file": "data/flights-200k.parquet"}},
        "params": {"scale": {"value": "log"}, "query": {"select": "intersect"}},
        "vconcat": [
            {
                "hconcat": [
                    {
                        "input": "menu",
                        "label": "Color Scale",
                        "bind": "$scale",
                        "options": ["log", "linear", "sqrt"],
                    },
                    {"hspace": 10},
                    {"legend": "color", "plot": "hexbins"},
                ]
            },
            {
                "hconcat": [
                    {
                        "plot": [
                            {
                                "mark": "rectY",
                                "data": {"source": "flights"},
                                "x": {"bin": "time"},
                                "y": {"count": None},
                                "fill": "steelblue",
                                "inset": 0.5,
                            },
                            {"select": "intervalX", "bind": "$query"},
                        ],
                        "margins": {"left": 5, "right": 5, "top": 30, "bottom": 0},
                        "x_domain": "Fixed",
                        "x_axis": "top",
                        "y_axis": None,
                        "x_label_anchor": "center",
                        "width": 605,
                        "height": 70,
                    },
                    {"hspace": 80},
                ]
            },
            {
                "hconcat": [
                    {
                        "name": "hexbins",
                        "plot": [
                            {
                                "mark": "hexbin",
                                "data": {"source": "flights", "filter_by": "$query"},
                                "x": "time",
                                "y": "delay",
                                "fill": {"count": None},
                                "bin_width": 10,
                            },
                            {"mark": "hexgrid", "bin_width": 10},
                        ],
                        "color_scheme": "ylgnbu",
                        "color_scale": "$scale",
                        "margins": {"left": 5, "right": 0, "top": 0, "bottom": 5},
                        "x_axis": None,
                        "y_axis": None,
                        "xy_domain": "Fixed",
                        "width": 600,
                        "height": 455,
                    },
                    {
                        "plot": [
                            {
                                "mark": "rectX",
                                "data": {"source": "flights"},
                                "x": {"count": None},
                                "y": {"bin": "delay"},
                                "fill": "steelblue",
                                "inset": 0.5,
                            },
                            {"select": "intervalY", "bind": "$query"},
                        ],
                        "margins": {"left": 0, "right": 50, "top": 4, "bottom": 5},
                        "y_domain": [-60, 180],
                        "x_axis": None,
                        "y_axis": "right",
                        "y_label_anchor": "center",
                        "width": 80,
                        "height": 455,
                    },
                ]
            },
        ],
    }
