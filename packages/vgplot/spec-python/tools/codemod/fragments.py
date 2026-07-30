from __future__ import annotations

from collections import deque
from collections.abc import Iterator
from typing import Final, LiteralString

type OneOrMore[T] = T | Iterator[T] | tuple[T, ...] | deque[T]
"""Consider this to be `T | Iterable[T]`."""


FUTURE_ANNOTATIONS: Final = "from __future__ import annotations"


def _join(strings: OneOrMore[str], separator: LiteralString = ", ") -> str:
    return strings if isinstance(strings, str) else separator.join(strings)


def import_from(from_module: str, names: OneOrMore[str]) -> str:
    return f"from {from_module} import {_join(names)}"
