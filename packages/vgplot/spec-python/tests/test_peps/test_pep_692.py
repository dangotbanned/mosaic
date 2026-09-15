"""[PEP 692] - Using TypedDict for more precise **kwargs typing.

- test_vgplot_{aggregate,window,column}` implement [vgplot/_generated/encodings.py] in terms of `Unpack[TypedDict]`

[PEP 692]: https://peps.python.org/pep-0692/
[vgplot/_generated/encodings.py]: https://github.com/uwdata/mosaic/blob/a2d19c3126beceb322119a7d471698bb850bcb3b/packages/vgplot/vgplot-python/vgplot/_generated/encodings.py
"""

from __future__ import annotations

# pyright: reportUnusedFunction=false
from typing import Any, overload

import mosaic_spec as ms
from mosaic_spec._typing_compat import TypeAliasType, Unpack

Arg = TypeAliasType("Arg", ms.ParamRef | bool | float | str)


# TODO @dangotbanned: Add positive/negative usage
def test_vgplot_aggregate() -> None:  # ruff: ignore[complex-structure]
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


# TODO @dangotbanned: Add positive/negative usage
def test_vgplot_window() -> None:  # ruff: ignore[complex-structure]
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
    def lead(
        col: Arg, offset: Arg, default: Arg, /, **kwds: Unpack[ms.WindowOptions]
    ) -> ms.Lead: ...
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


# TODO @dangotbanned: Add positive/negative usage
def test_vgplot_column() -> None:
    def bin(col: Arg, **kwds: Unpack[ms.BinOptions]) -> ms.Bin:
        return ms.Bin(bin=col, **kwds)

    def centroid(col: Arg) -> ms.Centroid:
        return ms.Centroid(centroid=col)

    def centroid_x(col: Arg) -> ms.CentroidX:
        return ms.CentroidX(centroid_x=col)

    def centroid_y(col: Arg) -> ms.CentroidY:
        return ms.CentroidY(centroid_y=col)

    def column(col: Arg) -> ms.Column:
        return ms.Column(column=col)

    def date_day(col: Arg) -> ms.DateDay:
        return ms.DateDay(date_day=col)

    def date_month(col: Arg) -> ms.DateMonth:
        return ms.DateMonth(date_month=col)

    def date_month_day(col: Arg) -> ms.DateMonthDay:
        return ms.DateMonthDay(date_month_day=col)

    def geojson(col: Arg) -> ms.GeoJSON:
        return ms.GeoJSON(geojson=col)


# TODO @dangotbanned: Review PEP for any gaps the above doesn't cover
# https://peps.python.org/pep-0692/
