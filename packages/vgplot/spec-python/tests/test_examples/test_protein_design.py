"""Protein Design Explorer.

Explore synthesized proteins generated via
[RFDiffusion](https://www.bakerlab.org/2023/07/11/diffusion-model-for-protein-design/).
"Minibinders" are small proteins that bind to a specific protein target.
When designing a minibinder, a researcher inputs the structure of the
target protein and other parameters into the AI diffusion model. Often, a
single, promising (parent) _version_ can be run through the model again to
produce additional, similar designs to better sample the design space.

The pipeline generates tens of thousands of protein designs. The metric
_pAE_ (predicted alignment error) measures how accurate a model was at
predicting the minibinder shape, whereas _pLDDT_ (predicted local distance
difference test) measures a model's confidence in minibinder structure
prediction. For _pAE_ lower is better, for _pLDDT_ higher is better.

Additional parameters include _partial t_ to set the time steps used by
the model, _noise_ to create more diversity of designs, _gradient decay
function_ and _gradient scale_ to guide prioritizing different positions
at different time points, and _movement_ to denote whether the minibinder
was left in its original position ("og") or moved to a desirable position
("moved").

The dashboard below enables exploration of the results to identify
promising protein designs and assess the effects of process parameters.

## Credit
Adapted from a [UW CSE 512](https://courses.cs.washington.edu/courses/cse512/24sp/) project by Christina Savvides, Alexander Shida, Riti Biswas, and Nora McNamara-Bordewick. Data from the [UW Institute for Protein Design](https://www.ipd.uw.edu/).
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.VConcat = {
        "data": {"proteins": {"file": "data/protein-design.parquet"}},
        "params": {
            "query": {"select": "crossfilter"},
            "point": {"select": "intersect", "empty": True},
            "plddt_domain": [67, 94.5],
            "pae_domain": [5, 29],
            "scheme": "observable10",
        },
        "vconcat": [
            {
                "hconcat": [
                    {
                        "input": "menu",
                        "source": "proteins",
                        "column": "partial_t",
                        "label": "Partial t",
                        "bind": "$query",
                    },
                    {
                        "input": "menu",
                        "source": "proteins",
                        "column": "noise",
                        "label": "Noise",
                        "bind": "$query",
                    },
                    {
                        "input": "menu",
                        "source": "proteins",
                        "column": "gradient_decay_function",
                        "label": "Gradient Decay",
                        "bind": "$query",
                    },
                    {
                        "input": "menu",
                        "source": "proteins",
                        "column": "gradient_scale",
                        "label": "Gradient Scale",
                        "bind": "$query",
                    },
                ]
            },
            {"vspace": "1.5em"},
            {
                "hconcat": [
                    {
                        "plot": [
                            {
                                "mark": "rectY",
                                "data": {"source": "proteins", "filter_by": "$query"},
                                "x": {"bin": "plddt_total", "steps": 60},
                                "y": {"count": None},
                                "z": "version",
                                "fill": "version",
                                "order": "z",
                                "reverse": True,
                                "inset_left": 0.5,
                                "inset_right": 0.5,
                            }
                        ],
                        "width": 600,
                        "height": 55,
                        "x_axis": None,
                        "y_axis": None,
                        "x_domain": "$plddt_domain",
                        "color_domain": "Fixed",
                        "color_scheme": "$scheme",
                        "margin_left": 40,
                        "margin_right": 0,
                        "margin_top": 0,
                        "margin_bottom": 0,
                    },
                    {"hspace": 5},
                    {"legend": "color", "plot": "scatter", "columns": 1, "bind": "$query"},
                ]
            },
            {
                "hconcat": [
                    {
                        "name": "scatter",
                        "plot": [
                            {"mark": "frame", "stroke": "#ccc"},
                            {
                                "mark": "raster",
                                "data": {"source": "proteins", "filter_by": "$query"},
                                "x": "plddt_total",
                                "y": "pae_interaction",
                                "fill": "version",
                                "pad": 0,
                            },
                            {
                                "select": "intervalXY",
                                "bind": "$query",
                                "brush": {"stroke": "currentColor", "fill": "transparent"},
                            },
                            {
                                "mark": "dot",
                                "data": {"source": "proteins", "filter_by": "$point"},
                                "x": "plddt_total",
                                "y": "pae_interaction",
                                "fill": "version",
                                "stroke": "currentColor",
                                "stroke_width": 0.5,
                            },
                        ],
                        "opacity_domain": [0, 2],
                        "opacity_clamp": True,
                        "color_domain": "Fixed",
                        "color_scheme": "$scheme",
                        "x_domain": "$plddt_domain",
                        "y_domain": "$pae_domain",
                        "x_label_anchor": "center",
                        "y_label_anchor": "center",
                        "margin_top": 0,
                        "margin_left": 40,
                        "margin_right": 0,
                        "width": 600,
                        "height": 450,
                    },
                    {
                        "plot": [
                            {
                                "mark": "rectX",
                                "data": {"source": "proteins", "filter_by": "$query"},
                                "x": {"count": None},
                                "y": {"bin": "pae_interaction", "steps": 60},
                                "z": "version",
                                "fill": "version",
                                "order": "z",
                                "reverse": True,
                                "inset_top": 0.5,
                                "inset_bottom": 0.5,
                            }
                        ],
                        "width": 55,
                        "height": 450,
                        "x_axis": None,
                        "y_axis": None,
                        "margin_top": 0,
                        "margin_left": 0,
                        "margin_right": 0,
                        "y_domain": "$pae_domain",
                        "color_domain": "Fixed",
                        "color_scheme": "$scheme",
                    },
                ]
            },
            {"vspace": "1em"},
            {
                "input": "table",
                "bind": "$point",
                "filter_by": "$query",
                "source": "proteins",
                "columns": [
                    "version",
                    "pae_interaction",
                    "plddt_total",
                    "noise",
                    "gradient_decay_function",
                    "gradient_scale",
                    "movement",
                ],
                "width": 680,
                "height": 215,
            },
        ],  # ty: ignore[invalid-argument-type]
    }
