# NOTE: DO NOT EDIT.
# Regenerate with: pnpm generate

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from mosaic_spec._typing_compat import Required, TypeAliasType, TypedDict
from mosaic_spec.typing import ParamRef

if TYPE_CHECKING:
    from collections.abc import Sequence

BinInterval = TypeAliasType(
    "BinInterval",
    Literal["date", "number", "millisecond", "second", "minute", "hour", "day", "month", "year"],
)
"""Binning interval names."""


class Days(TypedDict, total=False, closed=True):
    """A date/time interval in units of days."""

    days: Required[float]
    """A date/time interval in units of days."""


class Hours(TypedDict, total=False, closed=True):
    """A date/time interval in units of hours."""

    hours: Required[float]
    """A date/time interval in units of hours."""


class Microseconds(TypedDict, total=False, closed=True):
    """A date/time interval in units of microseconds."""

    microseconds: Required[float]
    """A date/time interval in units of microseconds."""


class Milliseconds(TypedDict, total=False, closed=True):
    """A date/time interval in units of milliseconds."""

    milliseconds: Required[float]
    """A date/time interval in units of milliseconds."""


class Minutes(TypedDict, total=False, closed=True):
    """A date/time interval in units of minutes."""

    minutes: Required[float]
    """A date/time interval in units of minutes."""


class Months(TypedDict, total=False, closed=True):
    """A date/time interval in units of months."""

    months: Required[float]
    """A date/time interval in units of months."""


class Seconds(TypedDict, total=False, closed=True):
    """A date/time interval in units of seconds."""

    seconds: Required[float]
    """A date/time interval in units of seconds."""


TransformField = TypeAliasType("TransformField", str | ParamRef)
"""A field argument to a data transform."""


class Years(TypedDict, total=False, closed=True):
    """A date/time interval in units of years."""

    years: Required[float]
    """A date/time interval in units of years."""


class Bin(TypedDict, total=False, closed=True):
    """A bin transform."""

    bin: Required[str | float | bool | ParamRef | Sequence[str | float | bool | ParamRef]]
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


class Centroid(TypedDict, total=False, closed=True):
    """A centroid transform."""

    centroid: Required[str | float | bool | ParamRef | Sequence[str | float | bool | ParamRef]]
    """Compute the 2D centroid of geometry-typed data. This transform requires the DuckDB `spatial` extension."""


class CentroidX(TypedDict, total=False, closed=True):
    """A centroidX transform."""

    centroid_x: Required[str | float | bool | ParamRef | Sequence[str | float | bool | ParamRef]]
    """Compute the centroid x-coordinate of geometry-typed data. This transform requires the DuckDB `spatial` extension."""


class CentroidY(TypedDict, total=False, closed=True):
    """A centroidY transform."""

    centroid_y: Required[str | float | bool | ParamRef | Sequence[str | float | bool | ParamRef]]
    """Compute the centroid y-coordinate of geometry-typed data. This transform requires the DuckDB `spatial` extension."""


class Column(TypedDict, total=False, closed=True):
    """A column transform."""

    column: Required[str | float | bool | ParamRef | Sequence[str | float | bool | ParamRef]]
    """Interpret a string or param-value as a column reference."""


class DateDay(TypedDict, total=False, closed=True):
    """A dateDay transform."""

    date_day: Required[str | float | bool | ParamRef | Sequence[str | float | bool | ParamRef]]
    """Transform a Date value to a day of the month for cyclic comparison. Year and month values are collapsed to enable comparison over days only."""


class DateMonth(TypedDict, total=False, closed=True):
    """A dateMonth transform."""

    date_month: Required[str | float | bool | ParamRef | Sequence[str | float | bool | ParamRef]]
    """Transform a Date value to a month boundary for cyclic comparison. Year values are collapsed to enable comparison over months only."""


class DateMonthDay(TypedDict, total=False, closed=True):
    """A dateMonthDay transform."""

    date_month_day: Required[
        str | float | bool | ParamRef | Sequence[str | float | bool | ParamRef]
    ]
    """Transform a Date value to a month and day boundary for cyclic comparison. Year values are collapsed to enable comparison over months and days only."""


class GeoJSON(TypedDict, total=False, closed=True):
    """A geojson transform."""

    geojson: Required[str | float | bool | ParamRef | Sequence[str | float | bool | ParamRef]]
    """Compute a GeoJSON-formatted string from geometry-typed data. This transform requires the DuckDB `spatial` extension."""


IntervalTransform = TypeAliasType(
    "IntervalTransform",
    Years | Months | Days | Hours | Minutes | Seconds | Milliseconds | Microseconds,
)
"""Date/time interval."""


ColumnTransform = TypeAliasType(
    "ColumnTransform",
    Bin | Column | DateMonth | DateMonthDay | DateDay | Centroid | CentroidX | CentroidY | GeoJSON,
)
"""A data transform that maps one column value to another."""


FrameValue = TypeAliasType("FrameValue", float | IntervalTransform | None)


class Lag(TypedDict, total=False, closed=True):
    """A lag window transform."""

    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    groups: Sequence[FrameValue] | ParamRef
    lag: Required[str | float | bool | ParamRef | Sequence[str | float | bool | ParamRef]]
    """Compute lagging values in a column. Returns the value at the row that is `offset` (second argument, default `1`) rows before the current row within the window frame. If there is no such row, instead return `default` (third argument, default `null`). Both offset and default are evaluated with respect to the current row."""
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    range: Sequence[FrameValue] | ParamRef
    rows: Sequence[FrameValue] | ParamRef


class Last(TypedDict, total=False, closed=True):
    """A last aggregate transform."""

    distinct: bool
    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    groups: Sequence[FrameValue] | ParamRef
    last: Required[str | float | bool | ParamRef | Sequence[str | float | bool | ParamRef]]
    """Return the last column value found in an aggregation group."""
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    range: Sequence[FrameValue] | ParamRef
    rows: Sequence[FrameValue] | ParamRef


class LastValue(TypedDict, total=False, closed=True):
    """A last_value window transform."""

    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    groups: Sequence[FrameValue] | ParamRef
    last_value: Required[str | float | bool | ParamRef | Sequence[str | float | bool | ParamRef]]
    """Get the last value of the given column in the current window frame."""
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    range: Sequence[FrameValue] | ParamRef
    rows: Sequence[FrameValue] | ParamRef


class Lead(TypedDict, total=False, closed=True):
    """A lead window transform."""

    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    groups: Sequence[FrameValue] | ParamRef
    lead: Required[str | float | bool | ParamRef | Sequence[str | float | bool | ParamRef]]
    """Compute leading values in a column. Returns the value at the row that is `offset` (second argument, default `1`) rows after the current row within the window frame. If there is no such row, instead return `default` (third argument, default `null`). Both offset and default are evaluated with respect to the current row."""
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    range: Sequence[FrameValue] | ParamRef
    rows: Sequence[FrameValue] | ParamRef


class Max(TypedDict, total=False, closed=True):
    """A max aggregate transform."""

    distinct: bool
    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    groups: Sequence[FrameValue] | ParamRef
    max: Required[str | float | bool | ParamRef | Sequence[str | float | bool | ParamRef]]
    """Compute the maximum value of the given column."""
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    range: Sequence[FrameValue] | ParamRef
    rows: Sequence[FrameValue] | ParamRef


class Median(TypedDict, total=False, closed=True):
    """A median aggregate transform."""

    distinct: bool
    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    groups: Sequence[FrameValue] | ParamRef
    median: Required[str | float | bool | ParamRef | Sequence[str | float | bool | ParamRef]]
    """Compute the median value of the given column."""
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    range: Sequence[FrameValue] | ParamRef
    rows: Sequence[FrameValue] | ParamRef


class Min(TypedDict, total=False, closed=True):
    """A min aggregate transform."""

    distinct: bool
    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    groups: Sequence[FrameValue] | ParamRef
    min: Required[str | float | bool | ParamRef | Sequence[str | float | bool | ParamRef]]
    """Compute the minimum value of the given column."""
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    range: Sequence[FrameValue] | ParamRef
    rows: Sequence[FrameValue] | ParamRef


class Mode(TypedDict, total=False, closed=True):
    """A mode aggregate transform."""

    distinct: bool
    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    groups: Sequence[FrameValue] | ParamRef
    mode: Required[str | float | bool | ParamRef | Sequence[str | float | bool | ParamRef]]
    """Compute the mode value of the given column."""
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    range: Sequence[FrameValue] | ParamRef
    rows: Sequence[FrameValue] | ParamRef


class NTile(TypedDict, total=False, closed=True):
    """An ntile window transform."""

    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    groups: Sequence[FrameValue] | ParamRef
    ntile: Required[str | float | bool | ParamRef | Sequence[str | float | bool | ParamRef]]
    """Compute an n-tile integer ranging from 1 to the provided argument (num_buckets), dividing the partition as equally as possible."""
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    range: Sequence[FrameValue] | ParamRef
    rows: Sequence[FrameValue] | ParamRef


class NthValue(TypedDict, total=False, closed=True):
    """An nth_value window transform."""

    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    groups: Sequence[FrameValue] | ParamRef
    nth_value: Required[str | float | bool | ParamRef | Sequence[str | float | bool | ParamRef]]
    """Get the nth value of the given column in the current window frame, counting from one. The second argument is the offset for the nth row."""
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    range: Sequence[FrameValue] | ParamRef
    rows: Sequence[FrameValue] | ParamRef


class PercentRank(TypedDict, total=False, closed=True):
    """A percent_rank window transform."""

    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    groups: Sequence[FrameValue] | ParamRef
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    percent_rank: Required[Sequence[Any] | None]
    """Compute the percentage rank over an ordered window partition."""
    range: Sequence[FrameValue] | ParamRef
    rows: Sequence[FrameValue] | ParamRef


class Product(TypedDict, total=False, closed=True):
    """A product aggregate transform."""

    distinct: bool
    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    groups: Sequence[FrameValue] | ParamRef
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    product: Required[str | float | bool | ParamRef | Sequence[str | float | bool | ParamRef]]
    """Compute the product of the given column."""
    range: Sequence[FrameValue] | ParamRef
    rows: Sequence[FrameValue] | ParamRef


class Quantile(TypedDict, total=False, closed=True):
    """A quantile aggregate transform."""

    distinct: bool
    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    groups: Sequence[FrameValue] | ParamRef
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    quantile: Required[Sequence[str | float | bool | ParamRef]]
    """Compute the quantile value of the given column at the provided probability threshold. For example, 0.5 is the median."""
    range: Sequence[FrameValue] | ParamRef
    rows: Sequence[FrameValue] | ParamRef


class Rank(TypedDict, total=False, closed=True):
    """A rank window transform."""

    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    groups: Sequence[FrameValue] | ParamRef
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    range: Sequence[FrameValue] | ParamRef
    rank: Required[Sequence[Any] | None]
    """Compute the row rank over an ordered window partition. Sorting ties result in gaps in the rank numbers ([1, 1, 3, ...])."""
    rows: Sequence[FrameValue] | ParamRef


class RowNumber(TypedDict, total=False, closed=True):
    """A row_number window transform."""

    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    groups: Sequence[FrameValue] | ParamRef
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    range: Sequence[FrameValue] | ParamRef
    row_number: Required[Sequence[Any] | None]
    """Compute the 1-based row number over an ordered window partition."""
    rows: Sequence[FrameValue] | ParamRef


class Stddev(TypedDict, total=False, closed=True):
    """A sample standard deviation aggregate transform."""

    distinct: bool
    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    groups: Sequence[FrameValue] | ParamRef
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    range: Sequence[FrameValue] | ParamRef
    rows: Sequence[FrameValue] | ParamRef
    stddev: Required[str | float | bool | ParamRef | Sequence[str | float | bool | ParamRef]]
    """Compute the sum of the given column."""


class StddevPop(TypedDict, total=False, closed=True):
    """A population standard deviation aggregate transform."""

    distinct: bool
    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    groups: Sequence[FrameValue] | ParamRef
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    range: Sequence[FrameValue] | ParamRef
    rows: Sequence[FrameValue] | ParamRef
    stddev_pop: Required[str | float | bool | ParamRef | Sequence[str | float | bool | ParamRef]]
    """Compute the sum of the given column."""


class Sum(TypedDict, total=False, closed=True):
    """A sum aggregate transform."""

    distinct: bool
    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    groups: Sequence[FrameValue] | ParamRef
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    range: Sequence[FrameValue] | ParamRef
    rows: Sequence[FrameValue] | ParamRef
    sum: Required[str | float | bool | ParamRef | Sequence[str | float | bool | ParamRef]]
    """Compute the sum of the given column."""


class VarPop(TypedDict, total=False, closed=True):
    """A population variance aggregate transform."""

    distinct: bool
    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    groups: Sequence[FrameValue] | ParamRef
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    range: Sequence[FrameValue] | ParamRef
    rows: Sequence[FrameValue] | ParamRef
    var_pop: Required[str | float | bool | ParamRef | Sequence[str | float | bool | ParamRef]]
    """Compute the population variance of the given column."""


class Variance(TypedDict, total=False, closed=True):
    """A sample variance aggregate transform."""

    distinct: bool
    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    groups: Sequence[FrameValue] | ParamRef
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    range: Sequence[FrameValue] | ParamRef
    rows: Sequence[FrameValue] | ParamRef
    variance: Required[str | float | bool | ParamRef | Sequence[str | float | bool | ParamRef]]
    """Compute the sample variance of the given column."""


class Argmax(TypedDict, total=False, closed=True):
    """An argmax aggregate transform."""

    argmax: Required[Sequence[str | float | bool | ParamRef]]
    """Find a value of the first column that maximizes the second column."""
    distinct: bool
    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    groups: Sequence[FrameValue] | ParamRef
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    range: Sequence[FrameValue] | ParamRef
    rows: Sequence[FrameValue] | ParamRef


class Argmin(TypedDict, total=False, closed=True):
    """An argmin aggregate transform."""

    argmin: Required[Sequence[str | float | bool | ParamRef]]
    """Find a value of the first column that minimizes the second column."""
    distinct: bool
    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    groups: Sequence[FrameValue] | ParamRef
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    range: Sequence[FrameValue] | ParamRef
    rows: Sequence[FrameValue] | ParamRef


class Avg(TypedDict, total=False, closed=True):
    """An avg (average, or mean) aggregate transform."""

    avg: Required[str | float | bool | ParamRef | Sequence[str | float | bool | ParamRef]]
    """Compute the average (mean) value of the given column."""
    distinct: bool
    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    groups: Sequence[FrameValue] | ParamRef
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    range: Sequence[FrameValue] | ParamRef
    rows: Sequence[FrameValue] | ParamRef


class Count(TypedDict, total=False, closed=True):
    """A count aggregate transform."""

    count: Required[
        Sequence[Any]
        | str
        | float
        | bool
        | ParamRef
        | Sequence[str | float | bool | ParamRef]
        | None
    ]
    """Compute the count of records in an aggregation group."""
    distinct: bool
    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    groups: Sequence[FrameValue] | ParamRef
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    range: Sequence[FrameValue] | ParamRef
    rows: Sequence[FrameValue] | ParamRef


class CumeDist(TypedDict, total=False, closed=True):
    """A cume_dist window transform."""

    cume_dist: Required[Sequence[Any] | None]
    """Compute the cumulative distribution value over an ordered window partition. Equals the number of partition rows preceding or peer with the current row, divided by the total number of partition rows."""
    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    groups: Sequence[FrameValue] | ParamRef
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    range: Sequence[FrameValue] | ParamRef
    rows: Sequence[FrameValue] | ParamRef


class DenseRank(TypedDict, total=False, closed=True):
    """A dense_rank window transform."""

    dense_rank: Required[Sequence[Any] | None]
    """Compute the dense row rank (no gaps) over an ordered window partition. Sorting ties do not result in gaps in the rank numbers ([1, 1, 2, ...])."""
    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    groups: Sequence[FrameValue] | ParamRef
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    range: Sequence[FrameValue] | ParamRef
    rows: Sequence[FrameValue] | ParamRef


class First(TypedDict, total=False, closed=True):
    """A first aggregate transform."""

    distinct: bool
    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    first: Required[str | float | bool | ParamRef | Sequence[str | float | bool | ParamRef]]
    """Return the first column value found in an aggregation group."""
    groups: Sequence[FrameValue] | ParamRef
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    range: Sequence[FrameValue] | ParamRef
    rows: Sequence[FrameValue] | ParamRef


class FirstValue(TypedDict, total=False, closed=True):
    """A first_value window transform."""

    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    first_value: Required[str | float | bool | ParamRef | Sequence[str | float | bool | ParamRef]]
    """Get the first value of the given column in the current window frame."""
    groups: Sequence[FrameValue] | ParamRef
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    range: Sequence[FrameValue] | ParamRef
    rows: Sequence[FrameValue] | ParamRef


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


Transform = TypeAliasType("Transform", ColumnTransform | AggregateTransform | WindowTransform)
"""A data transform."""
