"""WNBA Shot Chart.

Every field goal attempt in the 2023 WNBA regular season. Shots are grouped into hexagonal bins, with color indicating shot potency (average score) and size indicating the total count of shots per location. The menu filters isolate shots by team or athlete.


## Credit
Data from [Wehoop](https://wehoop.sportsdataverse.org/). Design inspired by [Kirk Goldsberry](https://en.wikipedia.org/wiki/Kirk_Goldsberry) and a [UW CSE 512](https://courses.cs.washington.edu/courses/cse512/24sp/) project by Mackenzie Pitts and Madeline Brown.

"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.Spec = {
        "data": {
            "shots": {
                "file": "data/wnba-shots-2023.parquet",
                "where": "NOT starts_with(type, 'Free Throw') AND season_type = 2",
            },
            "court": {"file": "data/wnba-half-court.parquet"},
        },
        "params": {"filter": {"select": "crossfilter"}, "bin_width": 18},
        "vconcat": [
            {
                "hconcat": [
                    {
                        "input": "menu",
                        "source": "shots",
                        "column": "team_name",
                        "bind": "$filter",
                        "label": "Team",
                    },
                    {
                        "input": "menu",
                        "source": "shots",
                        "column": "athlete_name",
                        "filter_by": "$filter",
                        "bind": "$filter",
                        "label": "Athlete",
                    },
                ]
            },
            {"vspace": 5},
            {
                "plot": [
                    {"mark": "frame", "stroke_opacity": 0.5},
                    {"mark": "hexgrid", "bin_width": "$binWidth", "stroke_opacity": 0.05},
                    {
                        "mark": "hexbin",
                        "data": {"source": "shots", "filter_by": "$filter"},
                        "bin_width": "$binWidth",
                        "x": "x_position",
                        "y": "y_position",
                        "fill": {"avg": "score_value"},
                        "r": {"count": None},
                        "tip": {"format": {"x": False, "y": False}},
                    },
                    {
                        "mark": "line",
                        "data": {"source": "court"},
                        "stroke_linecap": "butt",
                        "stroke_opacity": 0.5,
                        "x": "x",
                        "y": "y",
                        "z": "z",
                    },
                ],
                "name": "shot-chart",
                "x_axis": None,
                "y_axis": None,
                "margin": 5,
                "x_domain": [0, 50],
                "y_domain": [0, 40],
                "color_domain": "Fixed",
                "color_scheme": "YlOrRd",
                "color_scale": "linear",
                "color_label": "Avg. Shot Value",
                "r_scale": "log",
                "r_range": [3, 9],
                "r_label": "Shot Count",
                "aspect_ratio": 1,
                "width": 510,
            },
            {"legend": "color", "plot": "shot-chart"},
        ],
    }
