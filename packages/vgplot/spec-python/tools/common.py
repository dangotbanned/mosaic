from __future__ import annotations

import typing as t
from itertools import chain

# pyright: reportReturnType=false
# NOTE: Seems like a sentinel bug?
from typing import TYPE_CHECKING, Any, Final, NewType

if TYPE_CHECKING:
    from collections.abc import Collection, Iterator, Mapping

    from typing_extensions import (
        Sentinel as sentinel,  # ruff: ignore[camelcase-imported-as-lowercase]
    )

    MISSING = sentinel("MISSING")
else:
    MISSING = object()

PyIdentifier = NewType("PyIdentifier", str)
"""A name that is a [valid python identifier][1].

[1]: https://docs.python.org/3/reference/lexical_analysis.html#names-identifiers-and-keywords
"""

PyIdentifierSnake = NewType("PyIdentifierSnake", str)
"""A snake_case name that is a [valid python identifier][1].

[1]: https://docs.python.org/3/reference/lexical_analysis.html#names-identifiers-and-keywords
"""

POUND_DEFS: Final = "#/definitions/"


def select_items[K, V](
    mapping: Mapping[K, V],
    targets: Collection[K],
    *,
    allow_missing: bool = False,
    preserve_order: bool = False,
    invert_limit: float = 0.1,
) -> Iterator[tuple[K, V]]:
    """Select items from a mapping, by key.

    A micro-optimized version of this pattern, with configurable trade-offs:

    ```py
    ((k, v) for k, v in mapping.items() if k in targets)
    ```

    Args:
        mapping: The mapping to iterate over.
        targets: Keys to select from `mapping`.
        allow_missing: Do not raise if a requested key is missing.
            By default, a fastpath may raise a `KeyError`.
        preserve_order: Guarantee iteration order matches insertion order.
            By default, a fastpath may yield in the order of `targets`.
        invert_limit: Iterate over `targets` instead of `mapping` when:
            `(len(targets) / len(mapping)) < invert_limit`.
    """
    if (len_keys := len(targets)) == 1:
        first = next(iter(targets))
        if not allow_missing:
            yield first, mapping[first]
        elif (result := mapping.get(first, MISSING)) is not MISSING:
            yield first, result

    elif not preserve_order and (len_keys / len(mapping)) < invert_limit:
        if not allow_missing:
            get = mapping.__getitem__
            for key in targets:
                yield key, get(key)
        else:
            get = mapping.get
            yield from ((k, result) for k in targets if (result := get(k, MISSING)) is not MISSING)

    else:
        for key, value in mapping.items():
            if key in targets:
                yield key, value


def prepend[T, S](first: T, iterable: Iterator[S], /) -> Iterator[T | S]:
    return chain((first,), iterable)


@t.overload
def ensure_type[T1](
    obj: Any, *valid_types: *tuple[type[T1]], name: str = "object", explain: str = ""
) -> T1: ...
@t.overload
def ensure_type[T1, T2](
    obj: Any, *valid_types: *tuple[type[T1], type[T2]], name: str = "object", explain: str = ""
) -> T1 | T2: ...
@t.overload
def ensure_type[T1, T2, T3](
    obj: Any,
    *valid_types: *tuple[type[T1], type[T2], type[T3]],
    name: str = "object",
    explain: str = "",
) -> T1 | T2 | T3: ...
@t.overload
def ensure_type[T1, T2, T3, T4](
    obj: Any,
    *valid_types: *tuple[type[T1], type[T2], type[T3], type[T4]],
    name: str = "object",
    explain: str = "",
) -> T1 | T2 | T3 | T4: ...


# NOTE: If you hit this overload, consider using a base class to simplify or write a type guard.
@t.overload
def ensure_type[T1, T2, T3, T4, T5](
    obj: Any,
    *valid_types: *tuple[type[T1], type[T2], type[T3], type[T4], type[T5], *tuple[type[Any], ...]],
    name: str = "object",
    explain: str = "",
) -> T1 | T2 | T3 | T4 | T5 | Any: ...
def ensure_type(obj: Any, *valid_types: type[Any], name: str = "object", explain: str = "") -> Any:
    """Raise if an object is not the expected type.

    Args:
        obj: The object to validate.
        *valid_types: One or more valid types that `obj` is expected to match.
        name: A name to identify the object in the error.
        explain: An additional message to add following the object repr.

    ## Notes
    An adaptation of something [from Narwhals], with the following changes:

    1. Long reprs are preserved and always displayed on their own line.
    2. Added `explain` parameter.
    3. **It provides static type checking too!**

    [from Narwhals]: https://github.com/narwhals-dev/narwhals/pull/2632#discussion_r2123391766

    ## Examples
    >>> _ = ensure_type(42, int, float)
    >>> _ = ensure_type("hello", str)

    >>> ensure_type("not an int", int, name="test")
    Traceback (most recent call last):
    TypeError: Expected 'test' to be of type 'int', got: 'str'
      'not an int'
    """
    if not isinstance(obj, valid_types):
        tp_names = " | ".join(qualified_type_name(tp) for tp in valid_types)
        got = qualified_type_name(obj)
        msg = f"Expected {name!r} to be of type {tp_names!r}, got: {got!r}\n  {obj!r}"
        if explain:
            msg = f"{msg}\n{explain.lstrip()}"
        raise TypeError(msg)
    return obj


def qualified_type_name(obj: object | type[Any], /) -> str:
    tp = obj if isinstance(obj, type) else type(obj)
    module = tp.__module__ if tp.__module__ != "builtins" else ""
    return f"{module}.{tp.__name__}".lstrip(".")
