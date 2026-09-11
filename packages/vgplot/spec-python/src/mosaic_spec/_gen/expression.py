# Generated: `mosaic_spec._gen.expression`
from __future__ import annotations

from mosaic_spec._typing_compat import Required, TypedDict


class AggregateExpression(TypedDict, total=False, closed=True):
    """A custom SQL aggregate expression."""

    agg: Required[str]
    """A SQL expression string to calculate an aggregate value. Embedded Param references, such as `SUM($param + 1)`, are supported. For expressions without aggregate functions, use *sql* instead."""
    label: str
    """A label for this expression, for example to label a plot axis."""


class SQLExpression(TypedDict, total=False, closed=True):
    """A custom SQL expression."""

    label: str
    """A label for this expression, for example to label a plot axis."""
    sql: Required[str]
    """A SQL expression string to derive a new column value. Embedded Param references, such as `$param + 1`, are supported. For expressions with aggregate functions, use *agg* instead."""


__all__ = ("AggregateExpression", "SQLExpression")
