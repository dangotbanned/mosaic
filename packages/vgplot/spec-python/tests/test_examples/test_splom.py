"""Scatter Plot Matrix (SPLOM).

A scatter plot matrix enables inspection of pairwise bivariate distributions. Do points cluster or separate in some dimensions but not others? Select a region to highlight corresponding points across all plots.

"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.Spec = {
        "data": {"penguins": {"file": "data/penguins.parquet"}},
        "params": {"brush": {"select": "single"}},
        "plot_defaults": {
            "x_ticks": 3,
            "y_ticks": 4,
            "x_domain": "Fixed",
            "y_domain": "Fixed",
            "color_domain": "Fixed",
            "margin_top": 5,
            "margin_bottom": 10,
            "margin_left": 10,
            "margin_right": 5,
            "x_axis": None,
            "y_axis": None,
            "x_label_anchor": "center",
            "y_label_anchor": "center",
            "x_tick_format": "s",
            "y_tick_format": "s",
            "width": 150,
            "height": 150,
        },
        "vconcat": [
            {
                "hconcat": [
                    {
                        "plot": [
                            {"mark": "frame", "stroke": "#ccc"},
                            {
                                "mark": "dot",
                                "data": {"source": "penguins"},
                                "x": "bill_length",
                                "y": "body_mass",
                                "fill": "species",
                                "r": 2,
                            },
                            {"select": "intervalXY", "bind": "$brush"},
                            {"select": "highlight", "by": "$brush", "opacity": 0.1},
                        ],
                        "y_axis": "left",
                        "margin_left": 45,
                        "width": 185,
                    },
                    {
                        "plot": [
                            {"mark": "frame", "stroke": "#ccc"},
                            {
                                "mark": "dot",
                                "data": {"source": "penguins"},
                                "x": "bill_depth",
                                "y": "body_mass",
                                "fill": "species",
                                "r": 2,
                            },
                            {"select": "intervalXY", "bind": "$brush"},
                            {"select": "highlight", "by": "$brush", "opacity": 0.1},
                        ]
                    },
                    {
                        "plot": [
                            {"mark": "frame", "stroke": "#ccc"},
                            {
                                "mark": "dot",
                                "data": {"source": "penguins"},
                                "x": "flipper_length",
                                "y": "body_mass",
                                "fill": "species",
                                "r": 2,
                            },
                            {"select": "intervalXY", "bind": "$brush"},
                            {"select": "highlight", "by": "$brush", "opacity": 0.1},
                        ]
                    },
                    {
                        "plot": [
                            {"mark": "frame", "stroke": "#ccc"},
                            {
                                "mark": "dot",
                                "data": {"source": "penguins"},
                                "x": "body_mass",
                                "y": "body_mass",
                                "fill": "species",
                                "r": 2,
                            },
                            {"select": "intervalXY", "bind": "$brush"},
                            {"select": "highlight", "by": "$brush", "opacity": 0.1},
                        ]
                    },
                ]
            },
            {
                "hconcat": [
                    {
                        "plot": [
                            {"mark": "frame", "stroke": "#ccc"},
                            {
                                "mark": "dot",
                                "data": {"source": "penguins"},
                                "x": "bill_length",
                                "y": "flipper_length",
                                "fill": "species",
                                "r": 2,
                            },
                            {"select": "intervalXY", "bind": "$brush"},
                            {"select": "highlight", "by": "$brush", "opacity": 0.1},
                        ],
                        "y_axis": "left",
                        "margin_left": 45,
                        "width": 185,
                    },
                    {
                        "plot": [
                            {"mark": "frame", "stroke": "#ccc"},
                            {
                                "mark": "dot",
                                "data": {"source": "penguins"},
                                "x": "bill_depth",
                                "y": "flipper_length",
                                "fill": "species",
                                "r": 2,
                            },
                            {"select": "intervalXY", "bind": "$brush"},
                            {"select": "highlight", "by": "$brush", "opacity": 0.1},
                        ]
                    },
                    {
                        "plot": [
                            {"mark": "frame", "stroke": "#ccc"},
                            {
                                "mark": "dot",
                                "data": {"source": "penguins"},
                                "x": "flipper_length",
                                "y": "flipper_length",
                                "fill": "species",
                                "r": 2,
                            },
                            {"select": "intervalXY", "bind": "$brush"},
                            {"select": "highlight", "by": "$brush", "opacity": 0.1},
                        ]
                    },
                    {
                        "plot": [
                            {"mark": "frame", "stroke": "#ccc"},
                            {
                                "mark": "dot",
                                "data": {"source": "penguins"},
                                "x": "body_mass",
                                "y": "flipper_length",
                                "fill": "species",
                                "r": 2,
                            },
                            {"select": "intervalXY", "bind": "$brush"},
                            {"select": "highlight", "by": "$brush", "opacity": 0.1},
                        ]
                    },
                ]
            },
            {
                "hconcat": [
                    {
                        "plot": [
                            {"mark": "frame", "stroke": "#ccc"},
                            {
                                "mark": "dot",
                                "data": {"source": "penguins"},
                                "x": "bill_length",
                                "y": "bill_depth",
                                "fill": "species",
                                "r": 2,
                            },
                            {"select": "intervalXY", "bind": "$brush"},
                            {"select": "highlight", "by": "$brush", "opacity": 0.1},
                        ],
                        "y_axis": "left",
                        "margin_left": 45,
                        "width": 185,
                    },
                    {
                        "plot": [
                            {"mark": "frame", "stroke": "#ccc"},
                            {
                                "mark": "dot",
                                "data": {"source": "penguins"},
                                "x": "bill_depth",
                                "y": "bill_depth",
                                "fill": "species",
                                "r": 2,
                            },
                            {"select": "intervalXY", "bind": "$brush"},
                            {"select": "highlight", "by": "$brush", "opacity": 0.1},
                        ]
                    },
                    {
                        "plot": [
                            {"mark": "frame", "stroke": "#ccc"},
                            {
                                "mark": "dot",
                                "data": {"source": "penguins"},
                                "x": "flipper_length",
                                "y": "bill_depth",
                                "fill": "species",
                                "r": 2,
                            },
                            {"select": "intervalXY", "bind": "$brush"},
                            {"select": "highlight", "by": "$brush", "opacity": 0.1},
                        ]
                    },
                    {
                        "plot": [
                            {"mark": "frame", "stroke": "#ccc"},
                            {
                                "mark": "dot",
                                "data": {"source": "penguins"},
                                "x": "body_mass",
                                "y": "bill_depth",
                                "fill": "species",
                                "r": 2,
                            },
                            {"select": "intervalXY", "bind": "$brush"},
                            {"select": "highlight", "by": "$brush", "opacity": 0.1},
                        ]
                    },
                ]
            },
            {
                "hconcat": [
                    {
                        "plot": [
                            {"mark": "frame", "stroke": "#ccc"},
                            {
                                "mark": "dot",
                                "data": {"source": "penguins"},
                                "x": "bill_length",
                                "y": "bill_length",
                                "fill": "species",
                                "r": 2,
                            },
                            {"select": "intervalXY", "bind": "$brush"},
                            {"select": "highlight", "by": "$brush", "opacity": 0.1},
                        ],
                        "y_axis": "left",
                        "x_axis": "bottom",
                        "margin_left": 45,
                        "margin_bottom": 35,
                        "width": 185,
                        "height": 175,
                    },
                    {
                        "plot": [
                            {"mark": "frame", "stroke": "#ccc"},
                            {
                                "mark": "dot",
                                "data": {"source": "penguins"},
                                "x": "bill_depth",
                                "y": "bill_length",
                                "fill": "species",
                                "r": 2,
                            },
                            {"select": "intervalXY", "bind": "$brush"},
                            {"select": "highlight", "by": "$brush", "opacity": 0.1},
                        ],
                        "x_axis": "bottom",
                        "height": 175,
                        "margin_bottom": 35,
                    },
                    {
                        "plot": [
                            {"mark": "frame", "stroke": "#ccc"},
                            {
                                "mark": "dot",
                                "data": {"source": "penguins"},
                                "x": "flipper_length",
                                "y": "bill_length",
                                "fill": "species",
                                "r": 2,
                            },
                            {"select": "intervalXY", "bind": "$brush"},
                            {"select": "highlight", "by": "$brush", "opacity": 0.1},
                        ],
                        "x_axis": "bottom",
                        "height": 175,
                        "margin_bottom": 35,
                    },
                    {
                        "plot": [
                            {"mark": "frame", "stroke": "#ccc"},
                            {
                                "mark": "dot",
                                "data": {"source": "penguins"},
                                "x": "body_mass",
                                "y": "bill_length",
                                "fill": "species",
                                "r": 2,
                            },
                            {"select": "intervalXY", "bind": "$brush"},
                            {"select": "highlight", "by": "$brush", "opacity": 0.1},
                        ],
                        "x_axis": "bottom",
                        "height": 175,
                        "margin_bottom": 35,
                    },
                ]
            },
        ],
    }
