from __future__ import annotations

from collections.abc import Callable, Iterable

from tools.models.base import DefName, IdName

type RefMap = Callable[[DefName], IdName | None]
"""A function that returns the name of a new `Root`, if `DefName` has moved."""


def into_ref_map(ref_names: Iterable[DefName], moved_to: IdName, /) -> RefMap:
    return dict.fromkeys(ref_names, moved_to).get
