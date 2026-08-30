"""Sortable Table.

A sortable, "infinite scroll" `table` view over a backing database table. Click column headers to
sort, or command-click to reset the order. Data is queried as needed as the table is sorted or
scrolled.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.spec.Table = {
        "data": {"flights": {"file": "data/flights-200k.parquet"}},
        "input": "table",
        "source": "flights",
        "height": 300,
    }
