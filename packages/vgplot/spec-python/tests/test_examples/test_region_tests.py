from __future__ import annotations

import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.Spec = {
        "meta": {
            "title": "Region Interactor Tests",
            "description": "Varied plots using region interactors to highlight selected values.\n",
        },
        "data": {
            "bls_unemp": {"file": "data/bls-metro-unemployment.parquet"},
            "feed": {"type": "spatial", "file": "data/usgs-feed.geojson"},
            "world": {"type": "spatial", "file": "data/countries-110m.json", "layer": "land"},
            "counties": {
                "type": "spatial",
                "file": "data/us-counties-10m.json",
                "layer": "counties",
            },
        },
        "params": {
            "series": {"select": "single"},
            "quakes": {"select": "single"},
            "counties_filter": {"select": "single"},
        },
        "vconcat": [
            {
                "plot": [
                    {"mark": "ruleY", "data": [0]},
                    {
                        "mark": "lineY",
                        "data": {"source": "bls_unemp", "optimize": False},
                        "x": "date",
                        "y": "unemployment",
                        "z": "division",
                        "stroke": "steelblue",
                        "stroke_opacity": 0.9,
                        "curve": "monotone-x",
                    },
                    {"select": "region", "channels": ["z"], "bind": "$series"},
                    {"select": "highlight", "by": "$series"},
                ],
                "margin_left": 24,
                "x_label": None,
                "x_ticks": 10,
                "x_line": True,
                "y_line": True,
                "y_label": "Unemployment (%)",
                "y_grid": True,
                "margin_right": 0,
            },
            {"vspace": 10},
            {
                "plot": [
                    {
                        "mark": "geo",
                        "data": {"source": "world"},
                        "fill": "currentColor",
                        "fill_opacity": 0.2,
                    },
                    {"mark": "sphere", "stroke_width": 0.5},
                    ms.Geo(
                        mark="geo",
                        data={"source": "feed"},
                        channels={"id": "id"},
                        # NOTE: Weird that `ty` gets tripped up by this?
                        # r={"sql": "POW(10, mag)"},  # ty: ignore[invalid-argument-type, unused-ignore-comment]  # ruff: ignore[commented-out-code]
                        r=ms.SQLExpression(sql="POW(10, mag)"),
                        stroke="red",
                        fill="red",
                        fill_opacity=0.2,
                        title="title",
                        href="url",
                        target="_blank",
                    ),
                    {"select": "region", "channels": ["id"], "bind": "$quakes"},
                    {"select": "highlight", "by": "$quakes"},
                ],
                "margin": 2,
                "projection_type": "equirectangular",
            },
            {"vspace": 10},
            {
                "plot": [
                    {
                        "mark": "geo",
                        "data": {"source": "counties"},
                        "channels": {"id": "id"},
                        "stroke": "currentColor",
                        "stroke_width": 0.25,
                    },
                    {"select": "region", "channels": ["id"], "bind": "$counties_filter"},
                    {"select": "highlight", "by": "$counties_filter"},
                ],
                "margin": 0,
                "projection_type": "albers",
            },
        ],
    }
