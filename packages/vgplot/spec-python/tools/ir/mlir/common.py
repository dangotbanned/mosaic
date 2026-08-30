from __future__ import annotations

from collections.abc import Callable, Iterable, Mapping

from tools.models.base import DefName, IdName

type NameMap[T: str = str, R: str = str] = Callable[[T], R | None]
"""A function that returns a replacement name iff a match was found."""

type RefMap = NameMap[DefName, IdName]
"""A function that returns the name of a new `Root`, if `DefName` has moved."""


def into_ref_map(ref_names: Iterable[DefName], moved_to: IdName, /) -> RefMap:
    return dict.fromkeys(ref_names, moved_to).get


def into_name_map[T: str = str, R: str = str](mapping: Mapping[T, R], /) -> NameMap[T, R]:
    """Convert a replacement mapping into a function.

    Typing supports all of: `str`, `Literal`, `LiteralString` and `NewType`.
    """
    return mapping.get
