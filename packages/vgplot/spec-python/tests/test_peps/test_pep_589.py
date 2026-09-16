"""[PEP 589] - TypedDict: Type Hints for Dictionaries with a Fixed Set of Keys.

[PEP 589]: https://peps.python.org/pep-0589/
"""

from __future__ import annotations

# pyright: reportUnusedFunction=false
from typing import TYPE_CHECKING, Any, Final, Literal as L

import pytest

import mosaic_spec as ms
from mosaic_spec._gen.transform import _AggregateOptions, _WindowOptions
from mosaic_spec._typing_compat import NotRequired, TypeAliasType, assert_type

if TYPE_CHECKING:
    from collections.abc import Mapping

Arg = TypeAliasType("Arg", ms.ParamRef | bool | float | str)


def test_abstract() -> None:
    bins: ms.Bin = {"bin": "column", "steps": 10}
    bins = {"interval": "day", "bin": ms.ParamRef("$something"), "step": 3}
    bins = {"nice": True, "minstep": 2, "bin": "another_column", "offset": 0.0}
    # `error: "assert_type" mismatch: expected "Bin" but received "Bin"` 🤨
    assert_type(bins, ms.Bin)  # pyright: ignore[reportAssertTypeFailure]


def test_using_typed_dict_types() -> None:
    def add_slider(widget: ms.Slider) -> None: ...

    add_slider({"min": 0, "max": 10.5, "label": "slippery", "input": "slider", "select": "point"})

    table: ms.Table
    table = {
        "columns": ["a", "b", "c"],
        "align": {"a": "left"},
        "source": ms.ParamRef("$table_name"),
        "input": "table",
    }
    # `error: "assert_type" mismatch: expected "Table" but received "Table"` 🤨
    assert_type(table, ms.Table)  # pyright: ignore[reportAssertTypeFailure]

    # NOTE: Expected fail
    table["list_match"] = "any"  # ty: ignore[invalid-key]  # pyrefly: ignore[bad-typed-dict-key]  # pyright: ignore[reportGeneralTypeIssues]
    table["align"] = "justify"  # ty: ignore[invalid-assignment]  # pyrefly: ignore[bad-assignment]  # pyright: ignore[reportGeneralTypeIssues]
    table["width"] = "container"  # ty: ignore[invalid-assignment]  # pyrefly: ignore[bad-assignment]  # pyright: ignore[reportGeneralTypeIssues]

    _region = ms.Region(
        bind=ms.ParamRef("$brush"),
        select="region",
        brush={"fill": "red", "fill_opacity": 0.8, "stroke": "green"},
        channels=("x",),
    )


def test_inheritance() -> None:
    class NullCount1(_AggregateOptions):
        null_count: Arg | tuple[Arg]

    class NullCount2(_WindowOptions):
        null_count: Arg | tuple[Arg]
        distinct: NotRequired[bool]

    def accepts_null_count(agg: NullCount1) -> None: ...

    accepts_null_count(NullCount1(null_count="a1"))
    accepts_null_count(NullCount2(null_count="a2"))
    accepts_null_count({"distinct": True, "null_count": ("b",)})


def test_inheritance_multi() -> None:
    """Covering multi-inheritance indirectly via intersection types.

    Almost every public `TypedDict` uses `closed=True`, which makes inheritance mostly useless.
    """
    parquet = ms.DataParquet(type="parquet", file="path/to/file.parquet")
    param = ms.ParamRef("$table")

    # Ok
    ms.Area(mark="area", data={"source": param})
    ms.spec.Area(mark="area", params={"a": 1})
    ms.spec.Area(mark="area", data={"named": parquet})

    # Fail
    ms.spec.Area(mark="area", data={"source": param})  # ty: ignore[invalid-argument-type] # pyrefly: ignore[bad-assignment]  # pyright: ignore[reportArgumentType]
    ms.Area(mark="area", params={"a": 1})  # ty: ignore[missing-typed-dict-key, invalid-key] # pyrefly: ignore[missing-argument, unexpected-keyword]  # pyright: ignore[reportCallIssue]
    ms.Area(mark="area", data={"named": parquet})  # ty: ignore[missing-typed-dict-key, invalid-key] # pyrefly: ignore[bad-argument-type]  # pyright: ignore[reportArgumentType, reportCallIssue]


def test_totality() -> None:
    style_0: ms.CSSStyles = {}
    style_1: ms.CSSStyles = {"padding": "10px 50px 20px"}

    assert_type(style_0, ms.CSSStyles)
    # error: "assert_type" mismatch: expected "CSSStyles" but received "CSSStyles"
    assert_type(style_1, ms.CSSStyles)  # pyright: ignore[reportAssertTypeFailure]


def test_type_consistency() -> None:
    def only_bar_y(mark: ms.BarY) -> None: ...
    def only_dict(mark: dict[str, Any]) -> None: ...
    def only_mapping(mark: Mapping[str, Any]) -> None: ...

    data = ms.PlotFrom(source="table_name")
    bar_x = ms.BarX(mark="barX", data=data)
    bar_y = ms.BarY(mark="barY", data=data)

    only_bar_y({"mark": "barY", "data": data})
    only_bar_y({"mark": "barX", "data": data})  # ty: ignore[invalid-argument-type] # pyrefly: ignore[bad-assignment]  # pyright: ignore[reportArgumentType]
    only_bar_y(bar_y)
    only_bar_y(bar_x)  # ty: ignore[invalid-argument-type] # pyrefly: ignore[bad-argument-type]  # pyright: ignore[reportArgumentType]

    only_dict({"mark": "barY", "data": data})
    only_dict({"mark": "barX", "data": data})
    only_dict(bar_y)  # ty: ignore[invalid-argument-type] # pyrefly: ignore[bad-argument-type]  # pyright: ignore[reportArgumentType]
    only_dict(bar_x)  # ty: ignore[invalid-argument-type] # pyrefly: ignore[bad-argument-type]  # pyright: ignore[reportArgumentType]

    only_mapping({"mark": "barY", "data": data})
    only_mapping({"mark": "barX", "data": data})
    only_mapping(bar_y)
    only_mapping(bar_x)


def test_supported_and_unsupported_operations() -> None:
    ms.SQLExpression(label="hello")  # ty: ignore[missing-typed-dict-key] # pyrefly: ignore[missing-argument]   # pyright: ignore[reportCallIssue]
    ms.Search(input="search", bind="not a NewType")  # ty: ignore[invalid-argument-type] # pyrefly: ignore[bad-argument-type]  # pyright: ignore[reportArgumentType]
    ms.PlotLegend(legend="color", i_dont_exist=1)  # ty: ignore[invalid-key] # pyrefly: ignore[unexpected-keyword]  # pyright: ignore[reportCallIssue]

    def f(variable_key: str) -> None:
        _table: ms.Table = {"input": "table", "source": "over there", variable_key: ""}  # ty: ignore[invalid-key] # pyrefly: ignore[bad-typed-dict-key] # pyright: ignore[reportAssignmentType]

    agg = ms.AggregateExpression(agg="SUM($param + 1)")
    agg.clear()  # ty: ignore[unresolved-attribute] # pyrefly: ignore[missing-attribute] # pyright: ignore[reportAttributeAccessIssue]

    agg = ms.AggregateExpression(agg="SUM($param + 1)")
    del agg["agg"]  # ty: ignore[invalid-argument-type] # pyrefly: ignore[unsupported-delete]  # pyright: ignore[reportGeneralTypeIssues]
    with pytest.raises(KeyError):
        # Only optional keys can be deleted, but will raise if they were not there
        del agg["label"]

    agg = ms.AggregateExpression(agg="SUM($param + 1)")
    assert_type(agg.get("label"), str | None)
    assert_type(agg.get("agg"), str)


def test_use_of_final_values_and_literal_types() -> None:
    circle: ms.Circle = {"mark": "circle", "data": []}

    MARK: Final = "mark"

    _CIRCLE = circle[MARK].upper()

    def get_value(c: ms.Circle, key: L["data", "mark"]) -> ms.PlotMarkData | L["circle"]:
        return c[key]

    data = get_value(circle, "data")
    assert data == []
