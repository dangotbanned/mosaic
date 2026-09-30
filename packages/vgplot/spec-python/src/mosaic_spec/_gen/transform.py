# NOTE: DO NOT EDIT MANUALLY.
# Regenerate with: pnpm generate
from __future__ import annotations

from typing import TYPE_CHECKING, Annotated as A, Literal as L

from mosaic_spec._typing_compat import Required, TypeAliasType, TypedDict

if TYPE_CHECKING:
    from collections.abc import Sequence

    from mosaic_spec._gen._typing import TransformField
    from mosaic_spec._gen.params import ParamRef


BinInterval = TypeAliasType(
    "BinInterval",
    L["date", "day", "hour", "millisecond", "minute", "month", "number", "second", "year"],
)
"""Binning interval names."""


class Centroid(TypedDict, closed=True):
    """A centroid transform."""

    centroid: Required[TransformField | tuple[TransformField]]
    """Compute the 2D centroid of geometry-typed data. This transform requires the DuckDB `spatial` extension."""


class CentroidX(TypedDict, closed=True):
    """A centroidX transform."""

    centroid_x: Required[TransformField | tuple[TransformField]]
    """Compute the centroid x-coordinate of geometry-typed data. This transform requires the DuckDB `spatial` extension."""


class CentroidY(TypedDict, closed=True):
    """A centroidY transform."""

    centroid_y: Required[TransformField | tuple[TransformField]]
    """Compute the centroid y-coordinate of geometry-typed data. This transform requires the DuckDB `spatial` extension."""


class Column(TypedDict, closed=True):
    """A column transform."""

    column: Required[ParamRef | str | tuple[ParamRef | str]]
    """Interpret a string or param-value as a column reference."""


class DateDay(TypedDict, closed=True):
    """A dateDay transform."""

    date_day: Required[TransformField | str | tuple[TransformField | str]]
    """Transform a Date value to a day of the month for cyclic comparison. Year and month values are collapsed to enable comparison over days only."""


class DateMonth(TypedDict, closed=True):
    """A dateMonth transform."""

    date_month: Required[TransformField | str | tuple[TransformField | str]]
    """Transform a Date value to a month boundary for cyclic comparison. Year values are collapsed to enable comparison over months only."""


class DateMonthDay(TypedDict, closed=True):
    """A dateMonthDay transform."""

    date_month_day: Required[TransformField | str | tuple[TransformField | str]]
    """Transform a Date value to a month and day boundary for cyclic comparison. Year values are collapsed to enable comparison over months and days only."""


class GeoJSON(TypedDict, closed=True):
    """A geojson transform."""

    geojson: Required[TransformField | tuple[TransformField]]
    """Compute a GeoJSON-formatted string from geometry-typed data. This transform requires the DuckDB `spatial` extension."""


class Days(TypedDict, closed=True):
    """A date/time interval in units of days."""

    days: Required[float]
    """A date/time interval in units of days."""


class Hours(TypedDict, closed=True):
    """A date/time interval in units of hours."""

    hours: Required[float]
    """A date/time interval in units of hours."""


class Microseconds(TypedDict, closed=True):
    """A date/time interval in units of microseconds."""

    microseconds: Required[float]
    """A date/time interval in units of microseconds."""


class Milliseconds(TypedDict, closed=True):
    """A date/time interval in units of milliseconds."""

    milliseconds: Required[float]
    """A date/time interval in units of milliseconds."""


class Minutes(TypedDict, closed=True):
    """A date/time interval in units of minutes."""

    minutes: Required[float]
    """A date/time interval in units of minutes."""


class Months(TypedDict, closed=True):
    """A date/time interval in units of months."""

    months: Required[float]
    """A date/time interval in units of months."""


class Seconds(TypedDict, closed=True):
    """A date/time interval in units of seconds."""

    seconds: Required[float]
    """A date/time interval in units of seconds."""


class Years(TypedDict, closed=True):
    """A date/time interval in units of years."""

    years: Required[float]
    """A date/time interval in units of years."""


class _BinOptions(TypedDict, total=False):
    interval: BinInterval
    """The interval bin unit to use, typically used to indicate a date/time unit for binning temporal values, such as `hour`, `day`, or `month`. If `date`, the extent of data values is used to automatically select an interval for temporal data. The value `number` enforces normal numerical binning, even over temporal data. If unspecified, defaults to `number` for numerical data and `date` for temporal data."""
    minstep: float
    """The minimum allowed bin step size (default `0`) when performing numerical binning. For example, a setting of `1` prevents step sizes less than 1. This option is ignored when **step** is specified."""
    nice: bool
    """A flag (default `true`) requesting "nice" human-friendly end points and step sizes when performing numerical binning. When **step** is specified, this option affects the binning end points (e.g., origin) only."""
    offset: float
    """Offset for computed bins (default `0`). For example, a value of `1` will result in using the next consecutive bin boundary."""
    step: float
    """The step size to use between bins. When binning numerical values (or interval type `number`), this setting specifies the numerical step size. For data/time intervals, this indicates the number of steps of that unit, such as hours, days, or years."""
    steps: float
    """The target number of binning steps to use. To accommodate human-friendly ("nice") bin boundaries, the actual number of bins may diverge from this exact value. This option is ignored when **step** is specified."""


IntervalTransform = TypeAliasType(
    "IntervalTransform",
    Days | Hours | Microseconds | Milliseconds | Minutes | Months | Seconds | Years,
)
"""Date/time interval."""


class Bin(_BinOptions, closed=True):
    """A bin transform."""

    bin: Required[TransformField | tuple[TransformField]]
    """Bin a continuous variable into discrete intervals. The bin argument specifies a data column or expression to bin. Both numerical and temporal (date/time) values are supported."""


class BinOptions(_BinOptions, closed=True):
    """Bin transform options."""


FrameValue = TypeAliasType("FrameValue", IntervalTransform | int | None)
ColumnTransform = TypeAliasType(
    "ColumnTransform",
    Bin | Centroid | CentroidX | CentroidY | Column | DateDay | DateMonth | DateMonthDay | GeoJSON,
)
"""A data transform that maps one column value to another."""


class _WindowOptions(TypedDict, total=False):
    exclude: L[
        "CURRENT ROW", "GROUP", "NO OTHERS", "TIES", "current row", "group", "no others", "ties"
    ]
    groups: ParamRef | tuple[FrameValue, FrameValue]
    order_by: Sequence[TransformField] | TransformField
    partition_by: Sequence[TransformField] | TransformField
    range: ParamRef | tuple[FrameValue, FrameValue]
    rows: ParamRef | tuple[FrameValue, FrameValue]


class CumeDist(_WindowOptions, closed=True):
    """A cume_dist window transform."""

    cume_dist: Required[tuple[()] | None]
    """Compute the cumulative distribution value over an ordered window partition. Equals the number of partition rows preceding or peer with the current row, divided by the total number of partition rows."""


class DenseRank(_WindowOptions, closed=True):
    """A dense_rank window transform."""

    dense_rank: Required[tuple[()] | None]
    """Compute the dense row rank (no gaps) over an ordered window partition. Sorting ties do not result in gaps in the rank numbers ([1, 1, 2, ...])."""


class FirstValue(_WindowOptions, closed=True):
    """A first_value window transform."""

    first_value: Required[TransformField | tuple[TransformField]]
    """Get the first value of the given column in the current window frame."""


class Lag(_WindowOptions, closed=True):
    """A lag window transform."""

    lag: Required[
        TransformField
        | tuple[
            A[TransformField, L["expr"]],
            A[TransformField | float, L["offset"]],
            A[TransformField | bool | float | str | None, L["default_value"]],
        ]
    ]
    """Compute lagging values in a column. Returns the value at the row that is `offset` (second argument, default `1`) rows before the current row within the window frame. If there is no such row, instead return `default` (third argument, default `null`). Both offset and default are evaluated with respect to the current row."""


class LastValue(_WindowOptions, closed=True):
    """A last_value window transform."""

    last_value: Required[TransformField | tuple[TransformField]]
    """Get the last value of the given column in the current window frame."""


class Lead(_WindowOptions, closed=True):
    """A lead window transform."""

    lead: Required[
        TransformField
        | tuple[
            A[TransformField, L["expr"]],
            A[TransformField | float, L["offset"]],
            A[TransformField | bool | float | str | None, L["default_value"]],
        ]
    ]
    """Compute leading values in a column. Returns the value at the row that is `offset` (second argument, default `1`) rows after the current row within the window frame. If there is no such row, instead return `default` (third argument, default `null`). Both offset and default are evaluated with respect to the current row."""


class NTile(_WindowOptions, closed=True):
    """An ntile window transform."""

    ntile: Required[TransformField | tuple[TransformField]]
    """Compute an n-tile integer ranging from 1 to the provided argument (num_buckets), dividing the partition as equally as possible."""


class NthValue(_WindowOptions, closed=True):
    """An nth_value window transform."""

    nth_value: Required[tuple[A[TransformField, L["expr"]], A[TransformField | float, L["nth"]]]]
    """Get the nth value of the given column in the current window frame, counting from one. The second argument is the offset for the nth row."""


class PercentRank(_WindowOptions, closed=True):
    """A percent_rank window transform."""

    percent_rank: Required[tuple[()] | None]
    """Compute the percentage rank over an ordered window partition."""


class Rank(_WindowOptions, closed=True):
    """A rank window transform."""

    rank: Required[tuple[()] | None]
    """Compute the row rank over an ordered window partition. Sorting ties result in gaps in the rank numbers ([1, 1, 3, ...])."""


class RowNumber(_WindowOptions, closed=True):
    """A row_number window transform."""

    row_number: Required[tuple[()] | None]
    """Compute the 1-based row number over an ordered window partition."""


class WindowOptions(_WindowOptions, closed=True):
    """Window transform options."""


class _AggregateOptions(_WindowOptions, total=False):
    distinct: bool


WindowTransform = TypeAliasType(
    "WindowTransform",
    CumeDist
    | DenseRank
    | FirstValue
    | Lag
    | LastValue
    | Lead
    | NTile
    | NthValue
    | PercentRank
    | Rank
    | RowNumber,
)
"""A window transform that operates over a sorted domain."""


class AggregateOptions(_AggregateOptions, closed=True):
    """Aggregate transform options."""


class Argmax(_AggregateOptions, closed=True):
    """An argmax aggregate transform."""

    argmax: Required[tuple[TransformField, TransformField]]
    """Find a value of the first column that maximizes the second column."""


class Argmin(_AggregateOptions, closed=True):
    """An argmin aggregate transform."""

    argmin: Required[tuple[TransformField, TransformField]]
    """Find a value of the first column that minimizes the second column."""


class Avg(_AggregateOptions, closed=True):
    """An avg (average, or mean) aggregate transform."""

    avg: Required[TransformField | tuple[TransformField]]
    """Compute the average (mean) value of the given column."""


class Count(_AggregateOptions, closed=True):
    """A count aggregate transform."""

    count: Required[tuple[()] | TransformField | tuple[TransformField] | None]
    """Compute the count of records in an aggregation group."""


class First(_AggregateOptions, closed=True):
    """A first aggregate transform."""

    first: Required[TransformField | tuple[TransformField]]
    """Return the first column value found in an aggregation group."""


class Last(_AggregateOptions, closed=True):
    """A last aggregate transform."""

    last: Required[TransformField | tuple[TransformField]]
    """Return the last column value found in an aggregation group."""


class Max(_AggregateOptions, closed=True):
    """A max aggregate transform."""

    max: Required[TransformField | tuple[TransformField]]
    """Compute the maximum value of the given column."""


class Median(_AggregateOptions, closed=True):
    """A median aggregate transform."""

    median: Required[TransformField | tuple[TransformField]]
    """Compute the median value of the given column."""


class Min(_AggregateOptions, closed=True):
    """A min aggregate transform."""

    min: Required[TransformField | tuple[TransformField]]
    """Compute the minimum value of the given column."""


class Mode(_AggregateOptions, closed=True):
    """A mode aggregate transform."""

    mode: Required[TransformField | tuple[TransformField]]
    """Compute the mode value of the given column."""


class Product(_AggregateOptions, closed=True):
    """A product aggregate transform."""

    product: Required[TransformField | tuple[TransformField]]
    """Compute the product of the given column."""


class Quantile(_AggregateOptions, closed=True):
    """A quantile aggregate transform."""

    quantile: Required[tuple[A[TransformField, L["expr"]], A[TransformField | float, L["p"]]]]
    """Compute the quantile value of the given column at the provided probability threshold. For example, 0.5 is the median."""


class Stddev(_AggregateOptions, closed=True):
    """A sample standard deviation aggregate transform."""

    stddev: Required[TransformField | tuple[TransformField]]
    """Compute the sum of the given column."""


class StddevPop(_AggregateOptions, closed=True):
    """A population standard deviation aggregate transform."""

    stddev_pop: Required[TransformField | tuple[TransformField]]
    """Compute the sum of the given column."""


class Sum(_AggregateOptions, closed=True):
    """A sum aggregate transform."""

    sum: Required[TransformField | tuple[TransformField]]
    """Compute the sum of the given column."""


class VarPop(_AggregateOptions, closed=True):
    """A population variance aggregate transform."""

    var_pop: Required[TransformField | tuple[TransformField]]
    """Compute the population variance of the given column."""


class Variance(_AggregateOptions, closed=True):
    """A sample variance aggregate transform."""

    variance: Required[TransformField | tuple[TransformField]]
    """Compute the sample variance of the given column."""


AggregateTransform = TypeAliasType(
    "AggregateTransform",
    Argmax
    | Argmin
    | Avg
    | Count
    | First
    | Last
    | Max
    | Median
    | Min
    | Mode
    | Product
    | Quantile
    | Stddev
    | StddevPop
    | Sum
    | VarPop
    | Variance,
)
"""An aggregate transform that combines multiple values."""
Transform = TypeAliasType("Transform", AggregateTransform | ColumnTransform | WindowTransform)
"""A data transform."""

__all__ = (
    "AggregateOptions",
    "AggregateTransform",
    "Argmax",
    "Argmin",
    "Avg",
    "Bin",
    "BinInterval",
    "BinOptions",
    "Centroid",
    "CentroidX",
    "CentroidY",
    "Column",
    "ColumnTransform",
    "Count",
    "CumeDist",
    "DateDay",
    "DateMonth",
    "DateMonthDay",
    "Days",
    "DenseRank",
    "First",
    "FirstValue",
    "FrameValue",
    "GeoJSON",
    "Hours",
    "IntervalTransform",
    "Lag",
    "Last",
    "LastValue",
    "Lead",
    "Max",
    "Median",
    "Microseconds",
    "Milliseconds",
    "Min",
    "Minutes",
    "Mode",
    "Months",
    "NTile",
    "NthValue",
    "PercentRank",
    "Product",
    "Quantile",
    "Rank",
    "RowNumber",
    "Seconds",
    "Stddev",
    "StddevPop",
    "Sum",
    "Transform",
    "VarPop",
    "Variance",
    "WindowOptions",
    "WindowTransform",
    "Years",
)
