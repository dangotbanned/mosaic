"""Representation of `config.Scopes`.

The configuration syntax is designed for maximum flexibility, while remaining compact to write.

Here we convert that into something more optimized for the search itself.
"""

from __future__ import annotations

import typing
from collections.abc import Callable
from typing import Literal as L, Self

from tools.models import config

if typing.TYPE_CHECKING:
    from tools.models import mlir

type Unused = typing.Any
type Incomplete = typing.Any
type Predicate[T = object, R = bool] = Callable[[T], R]


class Matcher:
    __slots__ = ("match_id", "todo_child", "todo_parent")
    match_id: Predicate[config.IdName]
    todo_parent: Incomplete
    todo_child: Incomplete

    @classmethod
    def from_scopes(cls, scopes: config.Scopes) -> Self:
        self = cls.__new__(cls)
        self.match_id = _convert_incl_excl(scopes.id)
        # TODO @dangotbanned: `parent` needs to filter the keys of `definition`,
        #  then the type of the value ( requires converting `MLIRType` string into a type for an `isinstance` check)
        # - type of the value
        # TODO @dangotbanned: `child``
        return self

    def search_eager(self, root: mlir.Root) -> None:
        if self.match_id(root.id):
            msg = f"TODO: successful match on id: {root.id!r}"
            raise NotImplementedError(msg)


def _convert_incl_excl[T](filters: config.InclExcl[T], /) -> Predicate[T]:
    if filters:
        if include := filters.include:
            if exclude := filters.exclude:
                return _included_not_excluded(include, exclude)
            return include.__contains__
        return _not_excluded(filters.exclude)
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
