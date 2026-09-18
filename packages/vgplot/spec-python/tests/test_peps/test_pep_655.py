"""[PEP 655] - Marking individual TypedDict items as required or potentially-missing.

[PEP 655]: https://peps.python.org/pep-0655/
"""

from __future__ import annotations

from typing import Literal as L

import pytest

import mosaic_spec as ms


def test_missing_required() -> None:
    ms.Menu()  # ty: ignore[missing-typed-dict-key] # pyrefly: ignore [no-matching-overload] # pyright: ignore[reportCallIssue]
    ms.Menu({})  # ty: ignore[missing-typed-dict-key] # pyrefly: ignore [bad-typed-dict-key] # pyright: ignore[reportArgumentType]
    ms.Menu(input="menu")
    ms.Menu({"input": "menu"})


@pytest.mark.xfail(reason="https://github.com/python/cpython/issues/97727")
@pytest.mark.parametrize(
    ("special_name", "expected"),
    [
        ("__required_keys__", ("input",)),
        (
            "__optional_keys__",
            ("bind", "column", "field", "filter_by", "source", "list_match", "options", "value"),
        ),
    ],
    ids=["__required_keys__", "__optional_keys__"],
)
def test_introspectable_keys(
    special_name: L["__required_keys__", "__optional_keys__"], expected: tuple[str, ...]
) -> None:
    # https://peps.python.org/pep-0655/#interaction-with-required-keys-and-optional-keys
    required_keys = getattr(ms.Menu, special_name, frozenset())
    expected_keys = frozenset(expected)
    assert required_keys == expected_keys
