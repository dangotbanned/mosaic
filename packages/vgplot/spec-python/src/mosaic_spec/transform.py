from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from mosaic_spec._gen import ParamRef
from mosaic_spec._typing_compat import Required, TypeAliasType, TypedDict

if TYPE_CHECKING:
    from collections.abc import Sequence

    from mosaic_spec._gen import FrameValue, TransformField

## Some `Transform` cases
## They *could* use composition (e.g. everything in `.options`),
## but even exposing the options parts would help

### Current
### They all add a single field in TS, but are duplicated in the schema


class Argmax(TypedDict, total=False, closed=True):
    argmax: Required[Sequence[str | float | bool | ParamRef]]
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
    argmin: Required[Sequence[str | float | bool | ParamRef]]
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
    avg: Required[str | float | bool | ParamRef | Sequence[str | float | bool | ParamRef]]
    distinct: bool
    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    groups: Sequence[FrameValue] | ParamRef
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    range: Sequence[FrameValue] | ParamRef
    rows: Sequence[FrameValue] | ParamRef


class Rank(TypedDict, total=False, closed=True):
    exclude: Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ]
    groups: Sequence[FrameValue] | ParamRef
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    range: Sequence[FrameValue] | ParamRef
    rank: Required[Sequence[Any] | None]
    rows: Sequence[FrameValue] | ParamRef


### Improved
FrameExclude = TypeAliasType(
    "FrameExclude",
    Literal[
        "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
    ],
)

Arg = TypeAliasType("Arg", str | float | bool | ParamRef)
"""A transform argument."""

Arg0 = TypeAliasType("Arg0", tuple[()] | None)
"""A zero argument transform signature."""

Arg1 = TypeAliasType("Arg1", Arg | tuple[Arg])
"""A single argument transform signature."""

Arg2 = TypeAliasType("Arg2", tuple[Arg, Arg])
"""A two argument transform signature; both arguments are required."""


class WindowOptions(TypedDict, total=False):
    exclude: FrameExclude
    groups: tuple[FrameValue, FrameValue] | ParamRef
    orderby: TransformField | Sequence[TransformField]
    partitionby: TransformField | Sequence[TransformField]
    range: tuple[FrameValue, FrameValue] | ParamRef
    rows: tuple[FrameValue, FrameValue] | ParamRef


class AggregateOptions(WindowOptions, total=False):
    distinct: bool


class ArgmaxV2(AggregateOptions, closed=True):
    argmax: Arg2


class ArgminV2(AggregateOptions, closed=True):
    argmin: Arg2


class AvgV2(AggregateOptions, closed=True):
    avg: Arg1


class RankV2(WindowOptions, closed=True):
    rank: Arg0
