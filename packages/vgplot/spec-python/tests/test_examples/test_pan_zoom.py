"""Pan & Zoom.

Linked panning and zooming across plots: drag to pan, scroll to zoom. `panZoom` interactors update a set of bound selections, one per unique axis.

"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.Spec = {
        "data": {"penguins": {"file": "data/penguins.parquet"}},
        "hconcat": [
            {
                "vconcat": [
                    {
                        "plot": [
                            {"mark": "frame"},
                            {
                                "mark": "dot",
                                "data": {"source": "penguins"},
                                "x": "bill_length",
                                "y": "bill_depth",
                                "fill": "species",
                                "r": 2,
                                "clip": True,
                            },
                            {"select": "panZoom", "x": "$xs", "y": "$ys"},
                        ],
                        "width": 320,
                        "height": 240,
                    },
                    {"vspace": 10},
                    {
                        "plot": [
                            {"mark": "frame"},
                            {
                                "mark": "dot",
                                "data": {"source": "penguins"},
                                "x": "bill_length",
                                "y": "flipper_length",
                                "fill": "species",
                                "r": 2,
                                "clip": True,
                            },
                            {"select": "panZoom", "x": "$xs", "y": "$zs"},
                        ],
                        "width": 320,
                        "height": 240,
                    },
                ]
            },
            {"hspace": 10},
            {
                "vconcat": [
                    {
                        "plot": [
                            {"mark": "frame"},
                            {
                                "mark": "dot",
                                "data": {"source": "penguins"},
                                "x": "body_mass",
                                "y": "bill_depth",
                                "fill": "species",
                                "r": 2,
                                "clip": True,
                            },
                            {"select": "panZoom", "x": "$ws", "y": "$ys"},
                        ],
                        "width": 320,
                        "height": 240,
                    },
                    {"vspace": 10},
                    {
                        "plot": [
                            {"mark": "frame"},
                            {
                                "mark": "dot",
                                "data": {"source": "penguins"},
                                "x": "body_mass",
                                "y": "flipper_length",
                                "fill": "species",
                                "r": 2,
                                "clip": True,
                            },
                            {"select": "panZoom", "x": "$ws", "y": "$zs"},
                        ],
                        "width": 320,
                        "height": 240,
                    },
                ]
            },
        ],
    }
