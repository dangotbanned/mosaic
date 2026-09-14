"""[PEP 589] - TypedDict: Type Hints for Dictionaries with a Fixed Set of Keys.

[PEP 589]: https://peps.python.org/pep-0589/
"""

from __future__ import annotations

from typing_extensions import assert_type

import mosaic_spec as ms


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
