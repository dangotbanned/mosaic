"""Combining many modules together."""

from __future__ import annotations

from tests.apis import components_spec as vg, encodings_builder as eb
from tests.apis.attributes import attrs_mut
from tests.apis.data import Data
from tests.apis.marks import MarksNs
from tests.apis.params import p


def test_crossfilter() -> None:
    data = Data.from_parquet("data/flights-200k.parquet", "flights")
    # NOTE: aiming for this to be like `Data.from_*(...).mark.*`
    # - maybe have `mark` available on `{Data,Source}`?

    brush = p.brush.cross()

    mark = MarksNs(data.filter(brush))

    rect_y_1 = mark.rect.y(
        x=eb.col("delay").bin(),
        y=eb.len().to_dict(),
        fill="steelblue",
        inset_left=0.5,
        inset_right=0.5,
    )
    rect_y_2 = mark.rect.y(
        x=eb.col("time").bin(),
        y=eb.len().to_dict(),
        fill="steelblue",
        inset_left=0.5,
        inset_right=0.5,
    )

    attrs_1 = (
        attrs_mut()
        .x(domain="Fixed", label="Arrival Delay (min)", label_anchor="center")
        .y(tick_format="s")
        .height(200)
    )

    view = vg.vconcat(
        vg.plot(rect_y_1, vg.interval_x(brush)).with_attrs(attrs_1),
        vg.plot(rect_y_2, vg.interval_x(brush)).with_attrs(
            attrs_1.clone().x(domain="Fixed", label="Departure Time (hour)", label_anchor="center")
        ),
    )
    _spec = view.to_spec()
