"""[PEP 589] - TypedDict: Type Hints for Dictionaries with a Fixed Set of Keys.

[PEP 589]: https://peps.python.org/pep-0589/
"""

from __future__ import annotations

from typing_extensions import assert_type

import mosaic_spec as ms
from mosaic_spec._gen.transform import AggregateOptions, WindowOptions
from mosaic_spec._typing_compat import NotRequired, TypeAliasType

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
    class NullCount1(AggregateOptions):
        null_count: Arg | tuple[Arg]

    class NullCount2(WindowOptions):
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
