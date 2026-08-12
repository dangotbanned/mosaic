"""Legends.

Tests for different legend types and configurations. We test both legends defined within plots (with a zero-size frame) and external legends that reference a named plot.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.VConcat = {
        "params": {
            "toggle": {"select": "single"},
            "interval": {"select": "intersect"},
            "domain": ["foo", "bar", "baz", "bop", "doh"],
        },
        "plot_defaults": {"margin": 0, "width": 0, "height": 20},
        "vconcat": [
            {
                "hconcat": [
                    {
                        "plot": [{"legend": "color", "label": "Color Swatch", "bind": "$toggle"}],
                        "name": "color-categorical",
                        "color_scale": "categorical",
                        "color_domain": "$domain",
                    },
                    {"hspace": 35},
                    {
                        "legend": "color",
                        "plot": "color-categorical",
                        "label": "Color Swatch (External)",
                        "bind": "$toggle",
                    },
                ]
            },
            {
                "hconcat": [
                    {
                        "plot": [{"legend": "symbol", "label": "Symbol Swatch", "bind": "$toggle"}],
                        "name": "symbol-categorical",
                        "symbol_domain": "$domain",
                    },
                    {"hspace": 35},
                    {
                        "legend": "symbol",
                        "plot": "symbol-categorical",
                        "label": "Symbol Swatch (External)",
                        "bind": "$toggle",
                    },
                ]
            },
            {"vspace": "1em"},
            {
                "hconcat": [
                    {
                        "plot": [
                            {"legend": "opacity", "label": "Opacity Ramp", "bind": "$interval"}
                        ],
                        "name": "opacity-linear",
                        "opacity_domain": [0, 100],
                    },
                    {"hspace": 30},
                    {
                        "legend": "opacity",
                        "plot": "opacity-linear",
                        "label": "Opacity Ramp (External)",
                        "bind": "$interval",
                    },
                ]
            },
            {
                "hconcat": [
                    {
                        "plot": [{"legend": "opacity"}],
                        "name": "opacity-linear-no-label",
                        "opacity_domain": [0, 100],
                    },
                    {"hspace": 30},
                    {"legend": "opacity", "plot": "opacity-linear-no-label"},
                ]
            },
            {"vspace": "1em"},
            {
                "hconcat": [
                    {
                        "plot": [
                            {"legend": "color", "label": "Linear Color Ramp", "bind": "$interval"}
                        ],
                        "name": "color-linear",
                        "color_domain": [0, 100],
                    },
                    {"hspace": 30},
                    {
                        "legend": "color",
                        "plot": "color-linear",
                        "label": "Linear Color Ramp (External)",
                        "bind": "$interval",
                    },
                ]
            },
            {
                "hconcat": [
                    {
                        "plot": [{"legend": "color"}],
                        "name": "color-linear-no-label",
                        "color_domain": [0, 100],
                    },
                    {"hspace": 30},
                    {"legend": "color", "plot": "color-linear-no-label"},
                ]
            },
            {"vspace": "1em"},
            {
                "hconcat": [
                    {
                        "plot": [
                            {
                                "legend": "color",
                                "label": "Logarithmic Color Ramp",
                                "bind": "$interval",
                            }
                        ],
                        "name": "color-log",
                        "color_scale": "log",
                        "color_domain": [1, 100],
                    },
                    {"hspace": 30},
                    {
                        "legend": "color",
                        "plot": "color-log",
                        "label": "Logarithmic Color Ramp (External)",
                        "bind": "$interval",
                    },
                ]
            },
            {
                "hconcat": [
                    {
                        "plot": [
                            {
                                "legend": "color",
                                "label": "Diverging Color Ramp",
                                "bind": "$interval",
                            }
                        ],
                        "name": "color-diverging",
                        "color_scale": "diverging",
                        "color_domain": [-100, 100],
                        "color_constant": 20,
                    },
                    {"hspace": 30},
                    {
                        "legend": "color",
                        "plot": "color-diverging",
                        "label": "Diverging Color Ramp (External)",
                        "bind": "$interval",
                    },
                ]
            },
            {
                "hconcat": [
                    {
                        "plot": [
                            {
                                "legend": "color",
                                "label": "Diverging Symlog Color Ramp",
                                "bind": "$interval",
                            }
                        ],
                        "name": "color-diverging-symlog",
                        "color_scale": "diverging-symlog",
                        "color_domain": [-100, 100],
                        "color_constant": 20,
                    },
                    {"hspace": 30},
                    {
                        "legend": "color",
                        "plot": "color-diverging-symlog",
                        "label": "Diverging Symlog Color Ramp (External)",
                        "bind": "$interval",
                    },
                ]
            },
            {
                "hconcat": [
                    {
                        "plot": [{"legend": "color", "label": "Quantize Color Ramp"}],
                        "name": "color-quantize",
                        "color_scale": "quantize",
                        "color_domain": [0, 100],
                    },
                    {"hspace": 30},
                    {
                        "legend": "color",
                        "plot": "color-quantize",
                        "label": "Quantize Color Ramp (External)",
                    },
                ]
            },
            {
                "hconcat": [
                    {
                        "plot": [{"legend": "color", "label": "Threshold Color Ramp"}],
                        "name": "color-threshold",
                        "color_scale": "threshold",
                        "color_domain": [0, 10, 20, 40, 80],
                    },
                    {"hspace": 30},
                    {
                        "legend": "color",
                        "plot": "color-threshold",
                        "label": "Threshold Color Ramp (External)",
                    },
                ]
            },
        ],
    }
