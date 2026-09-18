"""[PEP 655] - Marking individual TypedDict items as required or potentially-missing.

[PEP 655]: https://peps.python.org/pep-0655/
"""

from __future__ import annotations

from functools import partial
from typing import TYPE_CHECKING, Literal as L

import pytest

import mosaic_spec as ms
from mosaic_spec._typing_compat import (
    NotRequired,
    ParamSpec,
    ReadOnly,
    TypedDict,
    TypeVar,
    assert_type,
)

if TYPE_CHECKING:
    from collections.abc import Callable


def test_required_missing() -> None:
    ms.Menu()  # ty: ignore[missing-typed-dict-key] # pyrefly: ignore [no-matching-overload] # pyright: ignore[reportCallIssue]
    ms.Menu({})  # ty: ignore[missing-typed-dict-key] # pyrefly: ignore [bad-typed-dict-key] # pyright: ignore[reportArgumentType]
    ms.Menu(input="menu")
    ms.Menu({"input": "menu"})


P = ParamSpec("P")
R = TypeVar("R")


def into_callable(cb: Callable[P, R], /) -> Callable[P, R]:
    """https://typing.python.org/en/latest/spec/constructors.html#converting-a-constructor-to-callable"""
    return cb


def test_required_partial_direct() -> None:
    # NOTE: No type checker warns about this, yet?
    table = partial(ms.Table, input="table")
    bad = table()
    with pytest.raises(KeyError):
        bad["source"]


def test_required_partial_indirect() -> None:
    """This came from experimenting with a convenient syntax for discrimnator fields.

    ## Notes
    - `ty` fully understands
    - `pyright` isn't happy with `into_callable` mixing with overloads
        - But understands the use of `partial` afterwards
    - `pyrefly` treats everything as `Any`, and therefore fails
    """
    cb = into_callable(ms.Table)  # pyright: ignore[reportArgumentType]
    table = partial(cb, input="table")

    bad_1 = table()  # ty: ignore[no-matching-overload]  # pyright: ignore[reportCallIssue]
    _bad_2 = table(height=10)  # ty: ignore[no-matching-overload]  # pyright: ignore[reportCallIssue]

    good_1 = table(source="somewhere")
    good_2 = table(height=10, source="somewhere")

    # NOTE: `pyrefly` is wrong
    # if this becomes `unused-ignore` then using `functools.partial` to build an API is viable
    assert_type(good_1, ms.Table)  # pyrefly: ignore [assert-type]
    assert_type(good_2, ms.Table)  # pyrefly: ignore [assert-type]

    assert good_1["source"] == "somewhere"
    with pytest.raises(KeyError):
        bad_1["source"]


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


def test_not_required_invalid() -> None:
    def f(space: ms.HSpace) -> None: ...

    class BadH(TypedDict):
        hspace: NotRequired[float | str]

    class BadHBadSub(BadH):
        hspace: float | str  # ty: ignore[invalid-typed-dict-field] # pyrefly: ignore [bad-typed-dict-key] # pyright: ignore[reportGeneralTypeIssues]

    class BadHRO(TypedDict):
        hspace: ReadOnly[NotRequired[float | str]]

    class SubH(BadHRO):
        hspace: ReadOnly[float | str]

    h = ms.HSpace(hspace=1)
    bad_h = BadH(hspace=1)
    bad_h_ro = BadHRO(hspace=1)
    sub_h = SubH(hspace=1)

    f(h)
    f(bad_h)  # ty: ignore[invalid-argument-type] # pyrefly: ignore [bad-argument-type] # pyright: ignore[reportArgumentType]
    f(bad_h_ro)  # ty: ignore[invalid-argument-type]  # pyrefly: ignore [bad-argument-type] # pyright: ignore[reportArgumentType]
    f(sub_h)  # ty: ignore[invalid-argument-type] # pyrefly: ignore [bad-argument-type] # pyright: ignore[reportArgumentType]
