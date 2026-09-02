from __future__ import annotations

from itertools import chain

# pyright: reportReturnType=false
# NOTE: Seems like a sentinel bug?
from typing import TYPE_CHECKING, Final, NewType

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
