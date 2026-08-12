"""Seattle Weather Pivot.

A DuckDB `PIVOT` query reshapes Seattle's daily weather observations into a cross-tab: one row per year, with a column counting the days of each weather type. The pivoted result is shown in a sortable `table` view. Click a column header to sort.

"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.Spec = {
        "data": {
            "seattle_weather": {"file": "data/seattle-weather.parquet"},
            "weather_by_year": "PIVOT (SELECT *, year(date) AS year FROM seattle_weather) ON weather IN ('drizzle', 'fog', 'rain', 'snow', 'sun') USING count(*) GROUP BY year ORDER BY year\n",
        },
        "input": "table",
        "source": "weatherByYear",
        "align": {"year": "left"},
        "width": {"year": 80},
        "height": 180,
    }
