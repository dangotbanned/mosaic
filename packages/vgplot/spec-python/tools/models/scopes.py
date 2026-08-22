"""Representation of `config.Scopes`.

The configuration syntax is designed for maximum flexibility, while remaining compact to write.

Here we convert that into something more optimized for the search itself.
"""

from __future__ import annotations

import typing
from collections.abc import Callable
from typing import Literal as L, Self

from tools.models.config import Filter, IdName, Scopes

if typing.TYPE_CHECKING:
    from tools.models import mlir

type Unused = typing.Any
type Incomplete = typing.Any
type Predicate[T = object, R = bool] = Callable[[T], R]


class Matcher:
    __slots__ = ("match_id", "todo_child", "todo_parent")
    match_id: Predicate[IdName]
    todo_parent: Incomplete
    todo_child: Incomplete

    @classmethod
    def from_scopes(cls, scopes: Scopes) -> Self:
        self = cls.__new__(cls)
        # Makes sense to do this at the beginning
        # It is cheap and can have the biggest perf win
        if not scopes:
            self.match_id = _always
        elif (include := scopes.include) and (exclude := scopes.exclude):
            self.match_id = _convert_incl_excl_id(include, exclude)
        # TODO @dangotbanned: `definition` needs to filter the keys of `definitions`,
        #  then the type of the values ( requires converting `MLIRType` string into a type for an `isinstance` check)
        # TODO @dangotbanned: `child``
        # TODO @dangotbanned: `ref`
        return self

    def search_eager(self, root: mlir.Root) -> None:
        if self.match_id(root.id):
            msg = f"TODO: successful match on id: {root.id!r}"
            raise NotImplementedError(msg)


def _convert_incl_excl_id(include: Filter, exclude: Filter) -> Predicate[IdName]:
    if incl_id := include.id:
        if excl_id := exclude.id:
            return _included_not_excluded(incl_id, excl_id)
        return incl_id.__contains__
    if excl_id := exclude.id:
        return _not_excluded(excl_id)
    return _always


def _always(_: Unused, /) -> L[True]:
    return True


def _included_not_excluded[T](include: frozenset[T], exclude: frozenset[T], /) -> Predicate[T]:
    in_include = include.__contains__
    in_exclude = exclude.__contains__

    def matches(obj: T, /) -> bool:
        return in_include(obj) and not in_exclude(obj)

    return matches


def _not_excluded[T](exclude: frozenset[T], /) -> Predicate[T]:
    in_exclude = exclude.__contains__

    def matches(obj: T, /) -> bool:
        return not in_exclude(obj)

    return matches
