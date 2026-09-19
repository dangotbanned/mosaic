"""Builder API, similar to `encodings.py` next door.

Inspired by [Polars] and [Mosaic SQL]

[Polars]: https://docs.pola.rs/user-guide/expressions/window-functions/
[Mosaic SQL]: https://idl.uw.edu/mosaic/sql/
"""

from __future__ import annotations

from collections.abc import Sequence
from functools import partial
from typing import TYPE_CHECKING, Any, Final, Generic, Literal as L, final

import mosaic_spec as ms
from mosaic_spec._typing_compat import Self, TypeAliasType, TypeVar, Unpack

if TYPE_CHECKING:
    from collections.abc import Collection, Iterable


FrameExclude = TypeAliasType(
    "FrameExclude",
    L["CURRENT ROW", "GROUP", "NO OTHERS", "TIES", "current row", "group", "no others", "ties"],
)
_Frame = TypeAliasType("_Frame", ms.ParamRef | tuple[ms.FrameValue, ms.FrameValue])


_AGG_UNARY: Final = {
    "avg": (ms.Avg, "avg"),
    "count": (ms.Count, "count"),
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

        def avg(self) -> Agg[ms.Avg]: ...
        def count(self) -> Agg[ms.Count]: ...
        def first(self) -> Agg[ms.First]: ...
        def last(self) -> Agg[ms.Last]: ...
        def max(self) -> Agg[ms.Max]: ...
        def median(self) -> Agg[ms.Median]: ...
        def min(self) -> Agg[ms.Min]: ...
        def mode(self) -> Agg[ms.Mode]: ...
        def product(self) -> Agg[ms.Product]: ...
        def std(self) -> Agg[ms.Stddev]: ...
        def std_pop(self) -> Agg[ms.StddevPop]: ...
        def sum(self) -> Agg[ms.Sum]: ...
        def var(self) -> Agg[ms.Variance]: ...
        def var_pop(self) -> Agg[ms.VarPop]: ...
    else:

        def __getattr__(self, attr: str) -> Any:
            if got := _AGG_UNARY.get(attr):
                tp, param_name = got
                return partial(Agg, tp({param_name: self._name}))
            msg = f"{self.__class__.__name__!r} has no attribute {attr!r}"
            raise AttributeError(msg)

    def arg_max(self, by: str | ms.ParamRef) -> Agg[ms.Argmax]:
        return Agg(ms.Argmax(argmax=(self._name, by)))

    def arg_min(self, by: str | ms.ParamRef) -> Agg[ms.Argmin]:
        return Agg(ms.Argmin(argmin=(self._name, by)))

    def quantile(self, p: str | ms.ParamRef | float) -> Agg[ms.Quantile]:
        return Agg(ms.Quantile(quantile=(self._name, p)))

    # TODO @dangotbanned: Remaining `WindowTransform`
    def first_value(self) -> Window[ms.FirstValue]:
        return Window(ms.FirstValue(first_value=self._name))


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
        elif len(d) == 1:
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


# TODO @dangotbanned: window functions that don't require a column
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
