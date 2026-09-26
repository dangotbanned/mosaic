"""Combining many modules together."""

from __future__ import annotations

from tests.apis import components_spec as vg, encodings_builder as eb
from tests.apis.attributes import attrs_mut
from tests.apis.data import Data
from tests.apis.params import p


def test_crossfilter() -> None:
    data = Data.from_parquet("data/flights-200k.parquet", "flights")
    brush = p.brush.cross()
    attrs_1 = (
        attrs_mut()
        .x(domain="Fixed", label="Arrival Delay (min)", label_anchor="center")
        .y(tick_format="s")
        .height(200)
    )
    plot_delay = (
        data.filter(brush)
        .mark.rect.y(
            x=eb.col("delay").bin(),
            y=eb.len().to_dict(),
            fill="steelblue",
            inset_left=0.5,
            inset_right=0.5,
        )
        .plot(vg.interval_x(brush))
        .with_attrs(attrs_1)
    )
    plot_time = (
        data.filter(brush)
        .mark.rect.y(
            x=eb.col("time").bin(),
            y=eb.len().to_dict(),
            fill="steelblue",
            inset_left=0.5,
            inset_right=0.5,
        )
        .plot(vg.interval_x(brush))
        .with_attrs(
            attrs_1.clone().x(domain="Fixed", label="Departure Time (hour)", label_anchor="center")
        )
    )
    _spec = vg.vconcat(plot_delay, plot_time).to_spec()
