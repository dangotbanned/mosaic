"""[PEP 692] - Using TypedDict for more precise **kwargs typing.

[PEP 692]: https://peps.python.org/pep-0692/
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Final, assert_type

import pytest

import mosaic_spec as ms
from tests.test_peps import encodings as e

if TYPE_CHECKING:
    from collections.abc import Iterable


def test_vgplot_aggregate() -> None:
    e.count()
    e.count("column")
    e.count(())
    e.count(("one", "two"))  # ty: ignore[invalid-argument-type] # pyrefly: ignore[bad-argument-type]  # pyright: ignore[reportArgumentType]

    e.count(distinct=True)
    e.count(distinct=False)
    e.count(distinct="not a bool")  # ty: ignore[invalid-argument-type]  # pyrefly: ignore[bad-argument-type]  # pyright: ignore[reportArgumentType]

    e.stddev_pop("1", groups=ms.ParamRef("$groups"))
    e.var_pop("1", groups="a regular string")  # ty: ignore[invalid-argument-type] # pyrefly: ignore[bad-argument-type]  # pyright: ignore[reportArgumentType]

    e.last("aaa", groups=(None, 5))
    e.first("aaa", groups=[None, 5])  # ty: ignore[invalid-argument-type] # pyrefly: ignore[bad-argument-type]  # pyright: ignore[reportArgumentType]
    e.median("bbb", groups=(1.2, 4))  # ty: ignore[invalid-argument-type]  # pyrefly: ignore[bad-argument-type]  # pyright: ignore[reportArgumentType]
    e.max("ccc", rows=(1.2, 4))  # ty: ignore[invalid-argument-type]  # pyrefly: ignore[bad-argument-type]  # pyright: ignore[reportArgumentType]
    e.argmin("a", "b", range=(1.2, 4))  # ty: ignore[invalid-argument-type]  # pyrefly: ignore[bad-argument-type]  # pyright: ignore[reportArgumentType]

    e.mode("hi", i_dont_exist=1)  # ty: ignore[unknown-argument] # pyrefly: ignore[unexpected-keyword]   # pyright: ignore[reportCallIssue]

    with pytest.raises(TypeError):
        e.quantile("a", order_by=("b", "c"))  # ty: ignore[missing-argument] # pyrefly: ignore[missing-argument] # pyright: ignore[reportCallIssue]

    e.variance("upper", exclude="CURRENT ROW")
    e.variance("lower", exclude="current row")
    e.variance("bad", exclude="something else")  # ty: ignore[invalid-argument-type] # pyrefly: ignore[bad-argument-type]  # pyright: ignore[reportArgumentType]

    assert e.sum("num1")["sum"] == "num1"
    assert e.count("num1", distinct=True) == {"count": "num1", "distinct": True}
    assert e.argmax("num1", "num2") == {"argmax": ("num1", "num2")}
    assert e.min("a", partition_by=("num1", "num2")) == {
        "min": "a",
        "partition_by": ("num1", "num2"),
    }


def test_vgplot_window() -> None:
    kwds_annotated: ms.WindowOptions = {"order_by": ["a", "b", "c"], "partition_by": "d"}
    kwds_bare = {"order_by": ["a", "b", "c"], "partition_by": "d"}
    kwds_final: Final = {"order_by": ["a", "b", "c"], "partition_by": "d"}

    agg_1 = e.row_number(**kwds_annotated)
    agg_2 = e.row_number(order_by=("a", "b", "c"), partition_by=["d"])
    assert_type(agg_1, ms.RowNumber)
    assert_type(agg_2, ms.RowNumber)

    # NOTE: Interesting that pyrefly doesn't mind this
    e.row_number(**kwds_bare)  # ty: ignore[invalid-argument-type] # pyright: ignore[reportArgumentType]
    e.row_number(**kwds_final)  # ty: ignore[invalid-argument-type] # pyright: ignore[reportArgumentType]

    def over(
        partition_by: ms.TransformField | Iterable[ms.TransformField],
        *more_partition_by: ms.TransformField,
        order_by: ms.TransformField | Iterable[ms.TransformField] | None = None,
    ) -> ms.WindowOptions:
        partition_by = (partition_by,) if isinstance(partition_by, str) else partition_by
        partition_by = *partition_by, *more_partition_by
        if order_by is None:
            return ms.WindowOptions(partition_by=partition_by)
        return ms.WindowOptions(
            partition_by=partition_by,
            order_by=(order_by,) if isinstance(order_by, str) else tuple(order_by),
        )

    # NOTE: Only `ty` understands this
    agg_3 = e.cume_dist() | over("num1", "num2")  # pyrefly: ignore[unsupported-operation] # pyright: ignore[reportOperatorIssue]
    assert_type(agg_3, ms.CumeDist)  # pyrefly: ignore[assert-type]  # pyright: ignore[reportAssertTypeFailure]

    agg_4 = e.cume_dist(**over("num1", "num2"))
    assert_type(agg_4, ms.CumeDist)

    assert agg_3 == agg_4
    assert agg_3 == {"cume_dist": None, "partition_by": ("num1", "num2")}

    e.dense_rank(rows=(0, None))
    e.first_value("num1", rows=(None, None))
    e.nth_value("num1", rows=(0, 2))
    e.nth_value("num1", 1, rows=(2, 0))
    e.nth_value()  # ty: ignore[no-matching-overload] # pyrefly: ignore[no-matching-overload] # pyright: ignore[reportCallIssue]
    e.nth_value("num1", 1, 2)  # ty: ignore[no-matching-overload] # pyrefly: ignore[no-matching-overload] # pyright: ignore[reportCallIssue]

    # TODO @dangotbanned: Find out if this is supposed to be expressible in mosaic-spec
    # https://github.com/uwdata/mosaic/blob/a2d19c3126beceb322119a7d471698bb850bcb3b/packages/mosaic/sql/test/window.test.ts#L43-L44
    e.ntile("num1", rows=(2, None), exclude="current row")

    e.rank(exclude="TIES", partition_by="num1")
    e.percent_rank(exclude="NO OTHERS")

    assert_type(e.lead("a"), ms.Lead)
    assert_type(e.lead("a", "b"), ms.Lead)
    assert_type(e.lead("a", "b", "c"), ms.Lead)
    e.lead("a", "b", "c", "d")  # ty: ignore[no-matching-overload] # pyrefly: ignore[no-matching-overload] # pyright: ignore[reportCallIssue]
    e.lead()  # ty: ignore[no-matching-overload] # pyrefly: ignore[no-matching-overload] # pyright: ignore[reportCallIssue]

    assert_type(e.lag("a"), ms.Lag)
    assert_type(e.lag("a", "b"), ms.Lag)
    assert_type(e.lag("a", "b", "c"), ms.Lag)
    e.lag("a", "b", "c", "d")  # ty: ignore[no-matching-overload] # pyrefly: ignore[no-matching-overload] # pyright: ignore[reportCallIssue]
    e.lag(**over(["a"], order_by="b"))  # ty: ignore[no-matching-overload] # pyrefly: ignore[no-matching-overload] # pyright: ignore[reportCallIssue]


def test_vgplot_column() -> None:
    e.col()  # ty: ignore[no-matching-overload] # pyrefly: ignore[no-matching-overload] # pyright: ignore[reportCallIssue]
    assert_type(e.col(bin="b"), ms.Bin)
    assert_type(e.col(bin="a", interval="day"), ms.Bin)
    assert_type(e.col(centroid=("a",)), ms.Centroid)
    assert_type(e.col(centroid_x="a"), ms.CentroidX)
    # TODO @dangotbanned: Raise an issue about `Arg` containing `boolean | number` for column refs?
    assert_type(e.col(centroid_y=1), ms.CentroidY)
    assert_type(e.col(column=ms.ParamRef("$param")), ms.Column)
    assert_type(e.col(date_day="c"), ms.DateDay)
    assert_type(e.col(date_month=(ms.ParamRef("$param"),)), ms.DateMonth)
    assert_type(e.col(date_month_day="d"), ms.DateMonthDay)
    assert_type(e.col(geojson="e"), ms.GeoJSON)

    e.col(bin="d", column="a")  # ty: ignore[no-matching-overload] # pyrefly: ignore[no-matching-overload] # pyright: ignore[reportCallIssue]
    e.col(bin=["a", "b"])  # ty: ignore[invalid-argument-type] # pyrefly: ignore[no-matching-overload] # pyright: ignore[reportArgumentType]
    e.col(bin="a", step="yes please")  # ty: ignore[invalid-argument-type] # pyrefly: ignore[no-matching-overload] # pyright: ignore[reportArgumentType]

    assert_type(e.col(**e.date_month_day("a")), ms.DateMonthDay)
    with pytest.raises(TypeError):
        # https://peps.python.org/pep-0692/#keyword-collisions
        e.col(column="a", **e.column("a"))  # ty: ignore[no-matching-overload] # pyrefly: ignore[no-matching-overload] # pyright: ignore[reportCallIssue]
