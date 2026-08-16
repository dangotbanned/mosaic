# NOTE: DO NOT EDIT.
# Regenerate with: pnpm generate

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from mosaic_spec._gen.params import ParamRef
from mosaic_spec._typing_compat import Required, TypeAliasType, TypedDict

if TYPE_CHECKING:
    from collections.abc import Sequence


class WindowOptions(TypedDict, total=False):
    """Window transform options."""

    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    groups: tuple[FrameValue, FrameValue] | ParamRef
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    range: tuple[FrameValue, FrameValue] | ParamRef
    rows: tuple[FrameValue, FrameValue] | ParamRef


class AggregateOptions(WindowOptions, total=False):
    """Aggregate transform options."""

    distinct: bool


Arg = TypeAliasType("Arg", str | float | bool | ParamRef)
"""A transform argument."""


class Argmax(AggregateOptions, closed=True):
    """An argmax aggregate transform."""

    argmax: Required[tuple[Arg, Arg]]
    """Find a value of the first column that maximizes the second column."""


class Argmin(AggregateOptions, closed=True):
    """An argmin aggregate transform."""

    argmin: Required[tuple[Arg, Arg]]
    """Find a value of the first column that minimizes the second column."""


class Avg(AggregateOptions, closed=True):
    """An avg (average, or mean) aggregate transform."""

    avg: Required[Arg | tuple[Arg]]
    """Compute the average (mean) value of the given column."""


BinInterval = TypeAliasType(
    "BinInterval",
    Literal["date", "number", "millisecond", "second", "minute", "hour", "day", "month", "year"],
)
"""Binning interval names."""


class Centroid(TypedDict, total=False, closed=True):
    """A centroid transform."""

    centroid: Required[Arg | tuple[Arg]]
    """Compute the 2D centroid of geometry-typed data. This transform requires the DuckDB `spatial` extension."""


class CentroidX(TypedDict, total=False, closed=True):
    """A centroidX transform."""

    centroid_x: Required[Arg | tuple[Arg]]
    """Compute the centroid x-coordinate of geometry-typed data. This transform requires the DuckDB `spatial` extension."""


class CentroidY(TypedDict, total=False, closed=True):
    """A centroidY transform."""

    centroid_y: Required[Arg | tuple[Arg]]
    """Compute the centroid y-coordinate of geometry-typed data. This transform requires the DuckDB `spatial` extension."""


class Column(TypedDict, total=False, closed=True):
    """A column transform."""

    column: Required[Arg | tuple[Arg]]
    """Interpret a string or param-value as a column reference."""


class Count(AggregateOptions, closed=True):
    """A count aggregate transform."""

    count: Required[Sequence[Any] | Arg | tuple[Arg] | None]
    """Compute the count of records in an aggregation group."""


class CumeDist(WindowOptions, closed=True):
    """A cume_dist window transform."""

    cume_dist: Required[Sequence[Any] | None]
    """Compute the cumulative distribution value over an ordered window partition. Equals the number of partition rows preceding or peer with the current row, divided by the total number of partition rows."""


class DateDay(TypedDict, total=False, closed=True):
    """A dateDay transform."""

    date_day: Required[Arg | tuple[Arg]]
    """Transform a Date value to a day of the month for cyclic comparison. Year and month values are collapsed to enable comparison over days only."""


class DateMonth(TypedDict, total=False, closed=True):
    """A dateMonth transform."""

    date_month: Required[Arg | tuple[Arg]]
    """Transform a Date value to a month boundary for cyclic comparison. Year values are collapsed to enable comparison over months only."""


class DateMonthDay(TypedDict, total=False, closed=True):
    """A dateMonthDay transform."""

    date_month_day: Required[Arg | tuple[Arg]]
    """Transform a Date value to a month and day boundary for cyclic comparison. Year values are collapsed to enable comparison over months and days only."""


class Days(TypedDict, total=False, closed=True):
    """A date/time interval in units of days."""

    days: Required[float]
    """A date/time interval in units of days."""


class DenseRank(WindowOptions, closed=True):
    """A dense_rank window transform."""

    dense_rank: Required[Sequence[Any] | None]
    """Compute the dense row rank (no gaps) over an ordered window partition. Sorting ties do not result in gaps in the rank numbers ([1, 1, 2, ...])."""


class First(AggregateOptions, closed=True):
    """A first aggregate transform."""

    first: Required[Arg | tuple[Arg]]
    """Return the first column value found in an aggregation group."""


class FirstValue(WindowOptions, closed=True):
    """A first_value window transform."""

    first_value: Required[Arg | tuple[Arg]]
    """Get the first value of the given column in the current window frame."""


class GeoJSON(TypedDict, total=False, closed=True):
    """A geojson transform."""

    geojson: Required[Arg | tuple[Arg]]
    """Compute a GeoJSON-formatted string from geometry-typed data. This transform requires the DuckDB `spatial` extension."""


class Hours(TypedDict, total=False, closed=True):
    """A date/time interval in units of hours."""

    hours: Required[float]
    """A date/time interval in units of hours."""


class Lag(WindowOptions, closed=True):
    """A lag window transform."""

    lag: Required[Arg | Sequence[Arg]]
    """Compute lagging values in a column. Returns the value at the row that is `offset` (second argument, default `1`) rows before the current row within the window frame. If there is no such row, instead return `default` (third argument, default `null`). Both offset and default are evaluated with respect to the current row."""


class Last(AggregateOptions, closed=True):
    """A last aggregate transform."""

    last: Required[Arg | tuple[Arg]]
    """Return the last column value found in an aggregation group."""


class LastValue(WindowOptions, closed=True):
    """A last_value window transform."""

    last_value: Required[Arg | tuple[Arg]]
    """Get the last value of the given column in the current window frame."""


class Lead(WindowOptions, closed=True):
    """A lead window transform."""

    lead: Required[Arg | Sequence[Arg]]
    """Compute leading values in a column. Returns the value at the row that is `offset` (second argument, default `1`) rows after the current row within the window frame. If there is no such row, instead return `default` (third argument, default `null`). Both offset and default are evaluated with respect to the current row."""


class Max(AggregateOptions, closed=True):
    """A max aggregate transform."""

    max: Required[Arg | tuple[Arg]]
    """Compute the maximum value of the given column."""


class Median(AggregateOptions, closed=True):
    """A median aggregate transform."""

    median: Required[Arg | tuple[Arg]]
    """Compute the median value of the given column."""


class Microseconds(TypedDict, total=False, closed=True):
    """A date/time interval in units of microseconds."""

    microseconds: Required[float]
    """A date/time interval in units of microseconds."""


class Milliseconds(TypedDict, total=False, closed=True):
    """A date/time interval in units of milliseconds."""

    milliseconds: Required[float]
    """A date/time interval in units of milliseconds."""


class Min(AggregateOptions, closed=True):
    """A min aggregate transform."""

    min: Required[Arg | tuple[Arg]]
    """Compute the minimum value of the given column."""


class Minutes(TypedDict, total=False, closed=True):
    """A date/time interval in units of minutes."""

    minutes: Required[float]
    """A date/time interval in units of minutes."""


class Mode(AggregateOptions, closed=True):
    """A mode aggregate transform."""

    mode: Required[Arg | tuple[Arg]]
    """Compute the mode value of the given column."""


class Months(TypedDict, total=False, closed=True):
    """A date/time interval in units of months."""

    months: Required[float]
    """A date/time interval in units of months."""


class NTile(WindowOptions, closed=True):
    """An ntile window transform."""

    ntile: Required[Arg | tuple[Arg]]
    """Compute an n-tile integer ranging from 1 to the provided argument (num_buckets), dividing the partition as equally as possible."""


class NthValue(WindowOptions, closed=True):
    """An nth_value window transform."""

    nth_value: Required[Arg | Sequence[Arg]]
    """Get the nth value of the given column in the current window frame, counting from one. The second argument is the offset for the nth row."""


class PercentRank(WindowOptions, closed=True):
    """A percent_rank window transform."""

    percent_rank: Required[Sequence[Any] | None]
    """Compute the percentage rank over an ordered window partition."""


class Product(AggregateOptions, closed=True):
    """A product aggregate transform."""

    product: Required[Arg | tuple[Arg]]
    """Compute the product of the given column."""


class Quantile(AggregateOptions, closed=True):
    """A quantile aggregate transform."""

    quantile: Required[tuple[Arg, Arg]]
    """Compute the quantile value of the given column at the provided probability threshold. For example, 0.5 is the median."""


class Rank(WindowOptions, closed=True):
    """A rank window transform."""

    rank: Required[Sequence[Any] | None]
    """Compute the row rank over an ordered window partition. Sorting ties result in gaps in the rank numbers ([1, 1, 3, ...])."""


class RowNumber(WindowOptions, closed=True):
    """A row_number window transform."""

    row_number: Required[Sequence[Any] | None]
    """Compute the 1-based row number over an ordered window partition."""


class Seconds(TypedDict, total=False, closed=True):
    """A date/time interval in units of seconds."""

    seconds: Required[float]
    """A date/time interval in units of seconds."""


class Stddev(AggregateOptions, closed=True):
    """A sample standard deviation aggregate transform."""

    stddev: Required[Arg | tuple[Arg]]
    """Compute the sum of the given column."""


class StddevPop(AggregateOptions, closed=True):
    """A population standard deviation aggregate transform."""

    stddev_pop: Required[Arg | tuple[Arg]]
    """Compute the sum of the given column."""


class Sum(AggregateOptions, closed=True):
    """A sum aggregate transform."""

    sum: Required[Arg | tuple[Arg]]
    """Compute the sum of the given column."""


TransformField = TypeAliasType("TransformField", str | ParamRef)
"""A field argument to a data transform."""


class VarPop(AggregateOptions, closed=True):
    """A population variance aggregate transform."""

    var_pop: Required[Arg | tuple[Arg]]
    """Compute the population variance of the given column."""


class Variance(AggregateOptions, closed=True):
    """A sample variance aggregate transform."""

    variance: Required[Arg | tuple[Arg]]
    """Compute the sample variance of the given column."""


WindowTransform = TypeAliasType(
    "WindowTransform",
    RowNumber
    | Rank
    | DenseRank
    | PercentRank
    | CumeDist
    | NTile
    | Lag
    | Lead
    | FirstValue
    | LastValue
    | NthValue,
)
"""A window transform that operates over a sorted domain."""


class Years(TypedDict, total=False, closed=True):
    """A date/time interval in units of years."""

    years: Required[float]
    """A date/time interval in units of years."""


AggregateTransform = TypeAliasType(
    "AggregateTransform",
    Argmax
    | Argmin
    | Avg
    | Count
    | Max
    | Min
    | First
    | Last
    | Median
    | Mode
    | Product
    | Quantile
    | Stddev
    | StddevPop
    | Sum
    | Variance
    | VarPop,
)
"""An aggregate transform that combines multiple values."""


class Bin(TypedDict, total=False, closed=True):
    """A bin transform."""

    bin: Required[Arg | tuple[Arg]]
    """Bin a continuous variable into discrete intervals. The bin argument specifies a data column or expression to bin. Both numerical and temporal (date/time) values are supported."""
    interval: BinInterval
    """The interval bin unit to use, typically used to indicate a date/time unit for binning temporal values, such as `hour`, `day`, or `month`. If `date`, the extent of data values is used to automatically select an interval for temporal data. The value `number` enforces normal numerical binning, even over temporal data. If unspecified, defaults to `number` for numerical data and `date` for temporal data."""
    minstep: float
    """The minimum allowed bin step size (default `0`) when performing numerical binning. For example, a setting of `1` prevents step sizes less than 1. This option is ignored when **step** is specified."""
    nice: Literal[True]
    """A flag (default `true`) requesting "nice" human-friendly end points and step sizes when performing numerical binning. When **step** is specified, this option affects the binning end points (e.g., origin) only."""
    offset: float
    """Offset for computed bins (default `0`). For example, a value of `1` will result in using the next consecutive bin boundary."""
    step: float
    """The step size to use between bins. When binning numerical values (or interval type `number`), this setting specifies the numerical step size. For data/time intervals, this indicates the number of steps of that unit, such as hours, days, or years."""
    steps: float
    """The target number of binning steps to use. To accommodate human-friendly ("nice") bin boundaries, the actual number of bins may diverge from this exact value. This option is ignored when **step** is specified."""


ColumnTransform = TypeAliasType(
    "ColumnTransform",
    Bin | Column | DateMonth | DateMonthDay | DateDay | Centroid | CentroidX | CentroidY | GeoJSON,
)
"""A data transform that maps one column value to another."""


IntervalTransform = TypeAliasType(
    "IntervalTransform",
    Years | Months | Days | Hours | Minutes | Seconds | Milliseconds | Microseconds,
)
"""Date/time interval."""


Transform = TypeAliasType("Transform", ColumnTransform | AggregateTransform | WindowTransform)
"""A data transform."""


FrameValue = TypeAliasType("FrameValue", float | IntervalTransform | None)
