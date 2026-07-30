from __future__ import annotations

from collections import deque
from collections.abc import Iterator
from pathlib import Path
from typing import Final, LiteralString

from tools.codemod import common

type OneOrMore[T] = T | Iterator[T] | tuple[T, ...] | deque[T]
"""Consider this to be `T | Iterable[T]`."""


FUTURE_ANNOTATIONS: Final = "from __future__ import annotations"


def _join(strings: OneOrMore[str], separator: LiteralString = ", ") -> str:
    return strings if isinstance(strings, str) else separator.join(strings)


def import_from(module: common.DottedName | Path, names: OneOrMore[str]) -> str:
    module = common.module_name(module) if isinstance(module, Path) else module
    return f"from {module} import {_join(names)}"
