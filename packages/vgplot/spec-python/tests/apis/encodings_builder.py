"""Builder API, similar to `encodings.py` next door.

Inspired by [Polars] and [Mosaic SQL]

[Polars]: https://docs.pola.rs/user-guide/expressions/window-functions/
[Mosaic SQL]: https://idl.uw.edu/mosaic/sql/
"""

from __future__ import annotations

import builtins
from collections.abc import Mapping, Sequence
from functools import partial
from typing import TYPE_CHECKING, Any, Final, Generic, Literal as L, final, overload

import mosaic_spec as ms
from mosaic_spec._typing_compat import Self, TypeAliasType, TypeVar, Unpack

if TYPE_CHECKING:
    from collections.abc import Collection, Iterable


FrameExclude = TypeAliasType(
    "FrameExclude",
    L["CURRENT ROW", "GROUP", "NO OTHERS", "TIES", "current row", "group", "no others", "ties"],
)
_Frame = TypeAliasType("_Frame", ms.ParamRef | tuple[ms.FrameValue, ms.FrameValue])
Arg = TypeAliasType("Arg", ms.ParamRef | bool | float | str)
_PositiveInteger = TypeAliasType(
    "_PositiveInteger",
    L[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
)
_NegativeInteger = TypeAliasType(
    "_NegativeInteger",
    L[-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20],
)

_AGG_UNARY: Final[Mapping[str, tuple[type[ms.AggregateTransform], str]]] = {
    "mean": (ms.Avg, "avg"),
    "count": (ms.Count, "count"),
    "len": (ms.Count, "count"),
    "first": (ms.First, "first"),
    "last": (ms.Last, "last"),
    "max": (ms.Max, "max"),
    "median": (ms.Median, "median"),
    "min": (ms.Min, "min"),
    "mode": (ms.Mode, "mode"),
    "product": (ms.Product, "product"),
    "std": (ms.Stddev, "stddev"),
    "std_pop": (ms.StddevPop, "stddev_pop"),
    "sum": (ms.Sum, "sum"),
    "var": (ms.Variance, "variance"),
    "var_pop": (ms.VarPop, "var_pop"),
}

_WINDOW_UNARY: Final[Mapping[str, tuple[type[ms.FirstValue | ms.LastValue | ms.NTile], str]]] = {
    "first_value": (ms.FirstValue, "first_value"),
    "last_value": (ms.LastValue, "last_value"),
    "ntile": (ms.NTile, "ntile"),
}


@final
class Col:
    __slots__ = ("_name",)

    def __repr__(self) -> str:
        return f"col({self._name!r})"

    def __init__(self, name: str | ms.ParamRef) -> None:
        self._name: str | ms.ParamRef = name

    def to_dict(self) -> ms.Column:
        return ms.Column(column=self._name)

    @property
    def dt(self) -> _DateNS:
        """Date/time-typed transforms."""
        return _DateNS(self)

    @property
    def st(self) -> _SpatialNS:
        """Geometry-typed transforms."""
        return _SpatialNS(self)

    def bin(self, step_: int | None = None, /, **kwds: Unpack[ms.BinOptions]) -> ms.Bin:
        """Bin numerical data."""
        if step_:
            kwds["step"] = step_
        kwds["interval"] = "number"
        return ms.Bin(bin=self._name, **kwds)

    if TYPE_CHECKING:

        def first(self) -> Agg[ms.First]: ...
        def first_value(self) -> Window[ms.FirstValue]: ...
        def last(self) -> Agg[ms.Last]: ...
        def last_value(self) -> Window[ms.LastValue]: ...
        def len(self) -> Agg[ms.Count]: ...
        def max(self) -> Agg[ms.Max]: ...
        def mean(self) -> Agg[ms.Avg]: ...
        def median(self) -> Agg[ms.Median]: ...
        def min(self) -> Agg[ms.Min]: ...
        def mode(self) -> Agg[ms.Mode]: ...
        def ntile(self) -> Window[ms.NTile]: ...
        def product(self) -> Agg[ms.Product]: ...
        def std(self) -> Agg[ms.Stddev]: ...
        def std_pop(self) -> Agg[ms.StddevPop]: ...
        def sum(self) -> Agg[ms.Sum]: ...
        def var(self) -> Agg[ms.Variance]: ...
        def var_pop(self) -> Agg[ms.VarPop]: ...

        count = len  # ruff: ignore[builtin-attribute-shadowing]

    else:

        def __getattr__(self, attr: str) -> Any:
            return _col_getattr(self, attr)

    def arg_max(self, by: str | ms.ParamRef) -> Agg[ms.Argmax]:
        return Agg(ms.Argmax(argmax=(self._name, by)))

    def arg_min(self, by: str | ms.ParamRef) -> Agg[ms.Argmin]:
        return Agg(ms.Argmin(argmin=(self._name, by)))

    # TODO @dangotbanned: Report upstream bug, should not be optional
    # https://github.com/uwdata/mosaic/blob/a2d19c3126beceb322119a7d471698bb850bcb3b/packages/vgplot/spec/src/spec/Transform.ts#L443
    # https://duckdb.org/docs/current/sql/functions/window_functions#nth_valueexpr-nth-order-by-ordering-ignore-nulls
    def nth_value(self, nth: int | ms.ParamRef, /) -> Window[ms.NthValue]:
        return Window(ms.NthValue(nth_value=(self._name, nth)))

    def n_unique(self) -> Agg[ms.Count]:
        return self.len().distinct()

    count_distinct = n_unique

    def quantile(self, p: str | ms.ParamRef | float) -> Agg[ms.Quantile]:
        return Agg(ms.Quantile(quantile=(self._name, p)))

    @overload
    def shift(self, n: _PositiveInteger = 1, fill_value: Arg | None = None) -> Window[ms.Lag]: ...
    @overload
    def shift(self, n: _NegativeInteger, fill_value: Arg | None = None) -> Window[ms.Lead]: ...
    @overload
    def shift(self, n: int, fill_value: Arg | None = None) -> Window[ms.Lag | ms.Lead]: ...
    def shift(self, n: int = 1, fill_value: Arg | None = None) -> Window[ms.Lag | ms.Lead]:
        if n >= 1:
            args = (self._name, n) if fill_value is None else (self._name, n, fill_value)
            return Window(ms.Lag(lag=args))
        if n < 0:
            n = abs(n)
            args = (self._name, n) if fill_value is None else (self._name, n, fill_value)
            return Window(ms.Lead(lead=args))
        msg = "`n` must be a non-zero integer"
        raise TypeError(msg)


def _col_getattr(self: Col, attr: str, /) -> partial[Agg[Any]] | partial[Window[Any]]:
    # NOTE: Provides some limited type checking for `Col.__getattr__`,
    # which is not visible to a type checker
    if agg_unary := _AGG_UNARY.get(attr):
        tp, param_name = agg_unary
        return partial(Agg, tp({param_name: self._name}))
    if window_unary := _WINDOW_UNARY.get(attr):
        tp, param_name = window_unary
        return partial(Window, tp({param_name: self._name}))
    msg = f"{self.__class__.__name__!r} has no attribute {attr!r}"
    raise AttributeError(msg)


@final
class _DateNS:
    __slots__ = ("_column",)

    def __init__(self, column: Col) -> None:
        self._column: Col = column

    def day(self) -> ms.DateDay:
        return ms.DateDay(date_day=self._column._name)

    def month(self) -> ms.DateMonth:
        return ms.DateMonth(date_month=self._column._name)

    def month_day(self) -> ms.DateMonthDay:
        return ms.DateMonthDay(date_month_day=self._column._name)

    def bin(
        self,
        step: int | None = None,
        unit: ms.BinInterval = "date",
        /,
        *,
        steps: int | None = None,
        offset: int = 0,
    ) -> ms.Bin:
        """Bin temporal data."""
        out = ms.Bin(bin=self._column._name, interval=unit)
        if step:
            out["step"] = step
        if offset:
            out["offset"] = offset
        if steps:
            out["steps"] = steps
        return out


@final
class _SpatialNS:
    __slots__ = ("_column",)

    def __init__(self, column: Col) -> None:
        self._column: Col = column

    def centroid(self) -> ms.Centroid:
        return ms.Centroid(centroid=self._column._name)

    def centroid_x(self) -> ms.CentroidX:
        return ms.CentroidX(centroid_x=self._column._name)

    def centroid_y(self) -> ms.CentroidY:
        return ms.CentroidY(centroid_y=self._column._name)

    def geojson(self) -> ms.GeoJSON:
        return ms.GeoJSON(geojson=self._column._name)


_A = TypeVar("_A", bound=ms.AggregateTransform | ms.WindowTransform, covariant=True)
A = TypeVar("A", bound=ms.AggregateTransform, covariant=True)
W = TypeVar("W", bound=ms.WindowTransform, covariant=True)


class _Aggregation(Generic[_A]):
    __slots__ = ("_inner",)

    def __init__(self, inner: _A) -> None:
        self._inner: Final[_A] = inner

    def __repr__(self) -> str:
        s = ""
        d = self._inner
        if "partition_by" in d:
            s = ", ".join(map(repr, d["partition_by"]))
        if "order_by" in d:
            if s:
                _s = ", ".join(map(repr, d["order_by"]))
                s = f"over({s}, order_by=({_s}))"
            else:
                s = f"over(order_by={d['order_by']!r})"
        elif s:
            s = f"over({s})"
        elif builtins.len(d) == 1:
            func, column = next(iter(d.items()))
            return self._fmt_function(column, func)  # pyrefly: ignore[bad-argument-type]

        for name in ("groups", "range", "rows"):
            if found := d.get(name):
                # NOTE: This one is unreasonable to expect a type checker to be happy with
                s = f"{s}.{self._fmt_frame(name, found)}"  # ty: ignore[invalid-argument-type] # pyrefly: ignore[bad-argument-type]
        it = (
            (k, v)
            for k, v in d.items()
            if k
            not in {"exclude", "groups", "range", "rows", "partition_by", "order_by", "distinct"}
        )
        func, column = next(it)
        return f"{self._fmt_function(column, func)}.{s.removeprefix('.')}"  # pyrefly: ignore[bad-argument-type]

    def _fmt_function(self, column: str | Sequence[Any] | float | None, function: str) -> str:
        s = f"{function}()"
        if not column:
            return s
        if not isinstance(column, str):
            if not isinstance(column, Sequence):
                # NOTE: Inherited `float` typing
                msg = f"{column!r} is not a column name"
                raise TypeError(msg)
            (column,) = column
        return f"col({column!r}).{s}"

    def _fmt_frame(self, name: L["groups", "range", "rows"], value: _Frame) -> str:
        g = repr(value) if isinstance(value, str) else f"{value[0]!r}, {value[1]!r}"
        return f"{name}({g})"

    # NOTE: pyrefly bug https://github.com/facebook/pyrefly/issues/4990
    def to_dict(self, *, copy: bool = False) -> _A:
        # pyrefly: ignore [bad-return]
        return self._inner if not copy else self._inner.copy()

    def over(
        self,
        partition_by: str | ms.ParamRef | Iterable[str | ms.ParamRef] = (),
        *more_partition_by: str | ms.ParamRef,
        order_by: str | ms.ParamRef | Collection[str | ms.ParamRef] = (),
    ) -> Self:
        inner = self._inner.copy()
        partition_by = (partition_by,) if isinstance(partition_by, str) else partition_by
        if more := more_partition_by:
            partition_by = *partition_by, *more
        else:
            partition_by = tuple(partition_by)
        if partition_by:
            inner["partition_by"] = partition_by
        if order := order_by:
            inner["order_by"] = (order,) if isinstance(order, str) else tuple(order)
        # NOTE: pyrefly bug https://github.com/facebook/pyrefly/issues/4990
        # pyrefly: ignore [bad-specialization]
        return type(self)(inner)

    def exclude(self, frame: FrameExclude, /) -> Self:
        inner = self._inner.copy()
        inner["exclude"] = frame
        # NOTE: pyrefly bug https://github.com/facebook/pyrefly/issues/4990
        # pyrefly: ignore [bad-specialization]
        return type(self)(inner)

    def groups(self, arg: ms.ParamRef | tuple[ms.FrameValue, ms.FrameValue], /) -> Self:
        return type(self)(_extent(self._inner, "groups", arg))

    def rows(self, arg: ms.ParamRef | tuple[ms.FrameValue, ms.FrameValue], /) -> Self:
        return type(self)(_extent(self._inner, "rows", arg))

    def range(self, arg: ms.ParamRef | tuple[ms.FrameValue, ms.FrameValue], /) -> Self:
        return type(self)(_extent(self._inner, "range", arg))


def _extent(inner: _A, key: L["groups", "range", "rows"], value: _Frame) -> _A:
    # NOTE: pyrefly bug https://github.com/facebook/pyrefly/issues/4990
    inner = inner.copy()  # pyrefly: ignore [bad-assignment]
    inner[key] = value
    return inner


@final
class Window(_Aggregation[W]):
    __slots__ = ()


@final
class Agg(_Aggregation[A]):
    __slots__ = ()

    def __repr__(self) -> str:
        s = super().__repr__()
        return s if not self._inner.get("distinct") else f"{s.removesuffix('.')}.distinct()"

    def distinct(self) -> Agg[A]:
        inner = self._inner.copy()
        inner["distinct"] = True
        # NOTE: pyrefly bug https://github.com/facebook/pyrefly/issues/4990
        # pyrefly: ignore [bad-return, bad-specialization]
        return Agg(inner)


# TODO @dangotbanned: intervals
def col(name: str | ms.ParamRef) -> Col:
    """Create a column expression.

    ## Examples

    >>> col("a")
    col('a')

    >>> expr = col("a").first().over("b", order_by=("c", "d"))
    >>> expr
    col('a').first().over('b', order_by=('c', 'd'))

    >>> expr.distinct()
    col('a').first().over('b', order_by=('c', 'd')).distinct()

    >>> col("b").count().distinct()
    col('b').count().distinct()

    >>> col("c").max().over("d")
    col('c').max().over('d')
    """
    return Col(name)


def len() -> Agg[ms.Count]:
    return Agg(ms.Count(count=()))


def n_unique() -> Agg[ms.Count]:
    return len().distinct()


count = len
count_distinct = n_unique


def row_index() -> Window[ms.RowNumber]:
    return Window(ms.RowNumber(row_number=None))


row_number = row_index


def rank() -> Window[ms.Rank]:
    return Window(ms.Rank(rank=None))


def dense_rank() -> Window[ms.DenseRank]:
    return Window(ms.DenseRank(dense_rank=None))


def percent_rank() -> Window[ms.PercentRank]:
    return Window(ms.PercentRank(percent_rank=None))
