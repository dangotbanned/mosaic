"""[PEP 692] - Using TypedDict for more precise **kwargs typing.

- test_vgplot_{aggregate,window,column}` implement [vgplot/_generated/encodings.py] in terms of `Unpack[TypedDict]`

[PEP 692]: https://peps.python.org/pep-0692/
[vgplot/_generated/encodings.py]: https://github.com/uwdata/mosaic/blob/a2d19c3126beceb322119a7d471698bb850bcb3b/packages/vgplot/vgplot-python/vgplot/_generated/encodings.py
"""

from __future__ import annotations

# pyright: reportUnusedFunction=false
from typing import TYPE_CHECKING, Any, Final, assert_type, overload

import pytest

import mosaic_spec as ms
from mosaic_spec._typing_compat import TypeAliasType, Unpack

if TYPE_CHECKING:
    from collections.abc import Iterable

Arg = TypeAliasType("Arg", ms.ParamRef | bool | float | str)


# NOTE: `AggregateTransform`


def argmax(col: Arg, by: Arg, **kwds: Unpack[ms.AggregateOptions]) -> ms.Argmax:
    return ms.Argmax(argmax=(col, by), **kwds)


def argmin(col: Arg, by: Arg, **kwds: Unpack[ms.AggregateOptions]) -> ms.Argmin:
    return ms.Argmin(argmin=(col, by), **kwds)


def avg(col: Arg, **kwds: Unpack[ms.AggregateOptions]) -> ms.Avg:
    return ms.Avg(avg=col, **kwds)


def count(col: Arg | tuple[()] = (), **kwds: Unpack[ms.AggregateOptions]) -> ms.Count:
    return ms.Count(count=col, **kwds)


def first(col: Arg, **kwds: Unpack[ms.AggregateOptions]) -> ms.First:
    return ms.First(first=col, **kwds)


def last(col: Arg, **kwds: Unpack[ms.AggregateOptions]) -> ms.Last:
    return ms.Last(last=col, **kwds)


def max(col: Arg, **kwds: Unpack[ms.AggregateOptions]) -> ms.Max:
    return ms.Max(max=col, **kwds)


def median(col: Arg, **kwds: Unpack[ms.AggregateOptions]) -> ms.Median:
    return ms.Median(median=col, **kwds)


def min(col: Arg, **kwds: Unpack[ms.AggregateOptions]) -> ms.Min:
    return ms.Min(min=col, **kwds)


def mode(col: Arg, **kwds: Unpack[ms.AggregateOptions]) -> ms.Mode:
    return ms.Mode(mode=col, **kwds)


def product(col: Arg, **kwds: Unpack[ms.AggregateOptions]) -> ms.Product:
    return ms.Product(product=col, **kwds)


def quantile(col: Arg, p: Arg, **kwds: Unpack[ms.AggregateOptions]) -> ms.Quantile:
    return ms.Quantile(quantile=(col, p), **kwds)


def stddev(col: Arg, **kwds: Unpack[ms.AggregateOptions]) -> ms.Stddev:
    return ms.Stddev(stddev=col, **kwds)


def stddev_pop(col: Arg, **kwds: Unpack[ms.AggregateOptions]) -> ms.StddevPop:
    return ms.StddevPop(stddev_pop=col, **kwds)


def sum(col: Arg, **kwds: Unpack[ms.AggregateOptions]) -> ms.Sum:
    return ms.Sum(sum=col, **kwds)


def variance(col: Arg, **kwds: Unpack[ms.AggregateOptions]) -> ms.Variance:
    return ms.Variance(variance=col, **kwds)


def var_pop(col: Arg, **kwds: Unpack[ms.AggregateOptions]) -> ms.VarPop:
    return ms.VarPop(var_pop=col, **kwds)


# NOTE: `WindowTransform`


def cume_dist(**kwds: Unpack[ms.WindowOptions]) -> ms.CumeDist:
    return {"cume_dist": None, **kwds}


def dense_rank(**kwds: Unpack[ms.WindowOptions]) -> ms.DenseRank:
    return {"dense_rank": None, **kwds}


def first_value(col: Arg, **kwds: Unpack[ms.WindowOptions]) -> ms.FirstValue:
    return ms.FirstValue(first_value=col, **kwds)


@overload
def lag(col: Arg, /, **kwds: Unpack[ms.WindowOptions]) -> ms.Lag: ...
@overload
def lag(col: Arg, offset: Arg, /, **kwds: Unpack[ms.WindowOptions]) -> ms.Lag: ...
@overload
def lag(col: Arg, offset: Arg, default: Arg, /, **kwds: Unpack[ms.WindowOptions]) -> ms.Lag: ...
def lag(
    *args: Unpack[tuple[Arg, Unpack[tuple[Any, ...]]]], **kwds: Unpack[ms.WindowOptions]
) -> ms.Lag:
    return ms.Lag(lag=args, **kwds)


def last_value(col: Arg, **kwds: Unpack[ms.WindowOptions]) -> ms.LastValue:
    return ms.LastValue(last_value=col, **kwds)


@overload
def lead(col: Arg, /, **kwds: Unpack[ms.WindowOptions]) -> ms.Lead: ...
@overload
def lead(col: Arg, offset: Arg, /, **kwds: Unpack[ms.WindowOptions]) -> ms.Lead: ...
@overload
def lead(col: Arg, offset: Arg, default: Arg, /, **kwds: Unpack[ms.WindowOptions]) -> ms.Lead: ...
def lead(
    *args: Unpack[tuple[Arg, Unpack[tuple[Any, ...]]]], **kwds: Unpack[ms.WindowOptions]
) -> ms.Lead:
    return ms.Lead(lead=args, **kwds)


@overload
def nth_value(col: Arg, /, **kwds: Unpack[ms.WindowOptions]) -> ms.NthValue: ...
@overload
def nth_value(col: Arg, offset: Arg, /, **kwds: Unpack[ms.WindowOptions]) -> ms.NthValue: ...
def nth_value(
    *args: Unpack[tuple[Arg, Unpack[tuple[Any, ...]]]], **kwds: Unpack[ms.WindowOptions]
) -> ms.NthValue:
    return ms.NthValue(nth_value=args, **kwds)


def ntile(buckets: Arg, **kwds: Unpack[ms.WindowOptions]) -> ms.NTile:
    return ms.NTile(ntile=buckets, **kwds)


def percent_rank(**kwds: Unpack[ms.WindowOptions]) -> ms.PercentRank:
    return {"percent_rank": None, **kwds}


def rank(**kwds: Unpack[ms.WindowOptions]) -> ms.Rank:
    return {"rank": None, **kwds}


def row_number(**kwds: Unpack[ms.WindowOptions]) -> ms.RowNumber:
    return {"row_number": None, **kwds}


# NOTE: `ColumnTransform`


def bin(col: Arg, **kwds: Unpack[ms.BinOptions]) -> ms.Bin:
    return ms.Bin(bin=col, **kwds)


def centroid(col: Arg) -> ms.Centroid:
    return ms.Centroid(centroid=col)


def centroid_x(col: Arg) -> ms.CentroidX:
    return ms.CentroidX(centroid_x=col)


def centroid_y(col: Arg) -> ms.CentroidY:
    return ms.CentroidY(centroid_y=col)


def geojson(col: Arg) -> ms.GeoJSON:
    return ms.GeoJSON(geojson=col)


def column(col: Arg) -> ms.Column:
    return ms.Column(column=col)


def date_day(col: Arg) -> ms.DateDay:
    return ms.DateDay(date_day=col)


def date_month(col: Arg) -> ms.DateMonth:
    return ms.DateMonth(date_month=col)


def date_month_day(col: Arg) -> ms.DateMonthDay:
    return ms.DateMonthDay(date_month_day=col)


@overload
def col(**kwds: Unpack[ms.Bin]) -> ms.Bin: ...
@overload
def col(**kwds: Unpack[ms.Centroid]) -> ms.Centroid: ...
@overload
def col(**kwds: Unpack[ms.CentroidX]) -> ms.CentroidX: ...
@overload
def col(**kwds: Unpack[ms.CentroidY]) -> ms.CentroidY: ...
@overload
def col(**kwds: Unpack[ms.Column]) -> ms.Column: ...
@overload
def col(**kwds: Unpack[ms.DateDay]) -> ms.DateDay: ...
@overload
def col(**kwds: Unpack[ms.DateMonth]) -> ms.DateMonth: ...
@overload
def col(**kwds: Unpack[ms.DateMonthDay]) -> ms.DateMonthDay: ...
@overload
def col(**kwds: Unpack[ms.GeoJSON]) -> ms.GeoJSON: ...
def col(**kwds: Any) -> Any:
    """Represents the suggestion in [typeddict-unions].

    [typeddict-unions]: https://peps.python.org/pep-0692/#typeddict-unions
    """
    return kwds


# NOTE: `IntervalTransform`


def years(value: float, /) -> ms.Years:
    return ms.Years(years=value)


def months(value: float, /) -> ms.Months:
    return ms.Months(months=value)


def days(value: float, /) -> ms.Days:
    return ms.Days(days=value)


def hours(value: float, /) -> ms.Hours:
    return ms.Hours(hours=value)


def minutes(value: float, /) -> ms.Minutes:
    return ms.Minutes(minutes=value)


def seconds(value: float, /) -> ms.Seconds:
    return ms.Seconds(seconds=value)


def milliseconds(value: float, /) -> ms.Milliseconds:
    return ms.Milliseconds(milliseconds=value)


def microseconds(value: float, /) -> ms.Microseconds:
    return ms.Microseconds(microseconds=value)


def test_vgplot_aggregate() -> None:
    count()
    count("columm")
    count(())
    count(("one", "two"))  # ty: ignore[invalid-argument-type] # pyrefly: ignore[bad-argument-type]  # pyright: ignore[reportArgumentType]

    count(distinct=True)
    count(distinct=False)
    count(distinct="not a bool")  # ty: ignore[invalid-argument-type]  # pyrefly: ignore[bad-argument-type]  # pyright: ignore[reportArgumentType]

    stddev_pop("1", groups=ms.ParamRef("$groups"))
    var_pop("1", groups="a regular string")  # ty: ignore[invalid-argument-type] # pyrefly: ignore[bad-argument-type]  # pyright: ignore[reportArgumentType]

    last("aaa", groups=(None, 5))
    first("aaa", groups=[None, 5])  # ty: ignore[invalid-argument-type] # pyrefly: ignore[bad-argument-type]  # pyright: ignore[reportArgumentType]
    median("bbb", groups=(1.2, 4))  # ty: ignore[invalid-argument-type]  # pyrefly: ignore[bad-argument-type]  # pyright: ignore[reportArgumentType]
    max("ccc", rows=(1.2, 4))  # ty: ignore[invalid-argument-type]  # pyrefly: ignore[bad-argument-type]  # pyright: ignore[reportArgumentType]
    argmin("a", "b", range=(1.2, 4))  # ty: ignore[invalid-argument-type]  # pyrefly: ignore[bad-argument-type]  # pyright: ignore[reportArgumentType]

    mode("hi", i_dont_exist=1)  # ty: ignore[unknown-argument] # pyrefly: ignore[unexpected-keyword]   # pyright: ignore[reportCallIssue]

    with pytest.raises(TypeError):
        quantile("a", order_by=("b", "c"))  # ty: ignore[missing-argument] # pyrefly: ignore[missing-argument] # pyright: ignore[reportCallIssue]

    variance("upper", exclude="CURRENT ROW")
    variance("lower", exclude="current row")
    variance("bad", exclude="something else")  # ty: ignore[invalid-argument-type] # pyrefly: ignore[bad-argument-type]  # pyright: ignore[reportArgumentType]

    assert sum("num1")["sum"] == "num1"
    assert count("num1", distinct=True) == {"count": "num1", "distinct": True}
    assert argmax("num1", "num2") == {"argmax": ("num1", "num2")}
    assert min("a", partition_by=("num1", "num2")) == {"min": "a", "partition_by": ("num1", "num2")}


def test_vgplot_window() -> None:
    kwds_annotated: ms.WindowOptions = {"order_by": ["a", "b", "c"], "partition_by": "d"}
    kwds_bare = {"order_by": ["a", "b", "c"], "partition_by": "d"}
    kwds_final: Final = {"order_by": ["a", "b", "c"], "partition_by": "d"}

    agg_1 = row_number(**kwds_annotated)
    agg_2 = row_number(order_by=("a", "b", "c"), partition_by=["d"])
    assert_type(agg_1, ms.RowNumber)
    assert_type(agg_2, ms.RowNumber)

    # NOTE: Interesting that pyrefly doesn't mind this
    row_number(**kwds_bare)  # ty: ignore[invalid-argument-type] # pyright: ignore[reportArgumentType]
    row_number(**kwds_final)  # ty: ignore[invalid-argument-type] # pyright: ignore[reportArgumentType]

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
    agg_3 = cume_dist() | over("num1", "num2")  # pyrefly: ignore[unsupported-operation] # pyright: ignore[reportOperatorIssue]
    assert_type(agg_3, ms.CumeDist)  # pyrefly: ignore[assert-type]  # pyright: ignore[reportAssertTypeFailure]

    agg_4 = cume_dist(**over("num1", "num2"))
    assert_type(agg_4, ms.CumeDist)

    assert agg_3 == agg_4
    assert agg_3 == {"cume_dist": None, "partition_by": ("num1", "num2")}

    dense_rank(rows=(0, None))
    first_value("num1", rows=(None, None))
    nth_value("num1", rows=(0, 2))
    nth_value("num1", 1, rows=(2, 0))
    nth_value()  # ty: ignore[no-matching-overload] # pyrefly: ignore[no-matching-overload] # pyright: ignore[reportCallIssue]
    nth_value("num1", 1, 2)  # ty: ignore[no-matching-overload] # pyrefly: ignore[no-matching-overload] # pyright: ignore[reportCallIssue]

    # TODO @dangotbanned: Find out if this is supposed to be expressible in mosaic-spec
    # https://github.com/uwdata/mosaic/blob/a2d19c3126beceb322119a7d471698bb850bcb3b/packages/mosaic/sql/test/window.test.ts#L43-L44
    ntile("num1", rows=(2, None), exclude="current row")

    rank(exclude="TIES", partition_by="num1")
    percent_rank(exclude="NO OTHERS")

    assert_type(lead("a"), ms.Lead)
    assert_type(lead("a", "b"), ms.Lead)
    assert_type(lead("a", "b", "c"), ms.Lead)
    lead("a", "b", "c", "d")  # ty: ignore[no-matching-overload] # pyrefly: ignore[no-matching-overload] # pyright: ignore[reportCallIssue]
    lead()  # ty: ignore[no-matching-overload] # pyrefly: ignore[no-matching-overload] # pyright: ignore[reportCallIssue]

    assert_type(lag("a"), ms.Lag)
    assert_type(lag("a", "b"), ms.Lag)
    assert_type(lag("a", "b", "c"), ms.Lag)
    lag("a", "b", "c", "d")  # ty: ignore[no-matching-overload] # pyrefly: ignore[no-matching-overload] # pyright: ignore[reportCallIssue]
    lag(**over(["a"], order_by="b"))  # ty: ignore[no-matching-overload] # pyrefly: ignore[no-matching-overload] # pyright: ignore[reportCallIssue]


def test_vgplot_column() -> None:
    col()  # ty: ignore[no-matching-overload] # pyrefly: ignore[no-matching-overload] # pyright: ignore[reportCallIssue]
    assert_type(col(bin="b"), ms.Bin)
    assert_type(col(bin="a", interval="day"), ms.Bin)
    assert_type(col(centroid=("a",)), ms.Centroid)
    assert_type(col(centroid_x="a"), ms.CentroidX)
    # TODO @dangotbanned: Raise an issue about `Arg` containing `boolean | number` for column refs?
    assert_type(col(centroid_y=1), ms.CentroidY)
    assert_type(col(column=ms.ParamRef("$param")), ms.Column)
    assert_type(col(date_day="c"), ms.DateDay)
    assert_type(col(date_month=(ms.ParamRef("$param"),)), ms.DateMonth)
    assert_type(col(date_month_day="d"), ms.DateMonthDay)
    assert_type(col(geojson="e"), ms.GeoJSON)

    col(bin="d", column="a")  # ty: ignore[no-matching-overload] # pyrefly: ignore[no-matching-overload] # pyright: ignore[reportCallIssue]
    col(bin=["a", "b"])  # ty: ignore[invalid-argument-type] # pyrefly: ignore[no-matching-overload] # pyright: ignore[reportArgumentType]
    col(bin="a", step="yes please")  # ty: ignore[invalid-argument-type] # pyrefly: ignore[no-matching-overload] # pyright: ignore[reportArgumentType]

    assert_type(col(**date_month_day("a")), ms.DateMonthDay)
    with pytest.raises(TypeError):
        # https://peps.python.org/pep-0692/#keyword-collisions
        col(column="a", **column("a"))  # ty: ignore[no-matching-overload] # pyrefly: ignore[no-matching-overload] # pyright: ignore[reportCallIssue]
