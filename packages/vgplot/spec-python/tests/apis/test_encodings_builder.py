from __future__ import annotations

import mosaic_spec as ms
from mosaic_spec._typing_compat import assert_type
from tests.apis import encodings_builder as eb


def test_moving_average() -> None:
    frame_ref = ms.ParamRef("$frame")
    # NOTE: params are mostly outside of the type system :(
    # Would want this to be rejected as not `tuple[FrameValue, FrameValue]`
    frame_param = ms.Param(value=[-6, 0])

    # NOTE: purely as a reminder that "cases" means 2 different things in the example
    CASES_COLUMN = "cases"
    CASES_TABLE = "cases"

    data = ms.DataParquet(type="parquet", file="data/berlin-covid.parquet")
    data_ref = ms.PlotFrom(source=CASES_TABLE)

    rect_y = ms.RectY(
        mark="rectY",
        data=data_ref,
        x1="day",
        x2=ms.SQLExpression(sql="day + 1"),
        inset=1,
        y=CASES_COLUMN,
        fill="steelblue",
    )

    y = eb.col(CASES_COLUMN).mean().over(order_by="day").rows(frame_ref)

    line_y = ms.LineY(
        mark="lineY",
        data=data_ref,
        x=ms.SQLExpression(sql=("day + 0.5")),
        y=y.to_dict(),
        curve="monotone-x",
        stroke="currentColor",
    )
    plot = ms.Plot(plot=(rect_y, line_y), x_label="day", width=680, height=300)

    menu = ms.Menu(
        input="menu",
        label="Window Frame",
        bind=frame_ref,
        options=[
            # NOTE: these values are `Any`-typed, but also should be tuples, in this specific case
            {"label": "7-day moving average, with prior 6 days: [-6, 0]", "value": [-6, 0]},
            {"label": "7-day moving average, centered at current day: [-3, 3]", "value": [-3, 3]},
            {"label": "Moving average, with all prior days [-∞, 0]", "value": [None, 0]},
            {"label": "Global average [-∞, +∞]", "value": [None, None]},
        ],
    )

    spec = ms.spec.VConcat(
        vconcat=(plot, menu), data={CASES_TABLE: data}, params={"frame": frame_param}
    )
    assert_type(spec, ms.spec.VConcat)
    assert_type(y.to_dict(), ms.Avg)
