from __future__ import annotations

import typing as t
from collections.abc import Callable, Iterable, Mapping

from tools.models.base import DefName, IdName

if t.TYPE_CHECKING:
    from tools.ir.mlir.definition import Definition
    from tools.ir.mlir.nodes import MLIR

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


@t.overload
def inner_type_is[M1: MLIR](
    *inner_type: *tuple[type[M1]],
) -> Callable[[Definition[t.Any]], t.TypeIs[Definition[M1]]]: ...
@t.overload
def inner_type_is[M1: MLIR, M2: MLIR](
    *inner_type: *tuple[type[M1], type[M2]],
) -> Callable[[Definition[t.Any]], t.TypeIs[Definition[M1 | M2]]]: ...
@t.overload
def inner_type_is[M1: MLIR, M2: MLIR, M3: MLIR](
    *inner_type: *tuple[type[M1], type[M2], type[M3]],
) -> Callable[[Definition[t.Any]], t.TypeIs[Definition[M1 | M2 | M3]]]: ...
@t.overload
def inner_type_is[M1: MLIR, M2: MLIR, M3: MLIR, M4: MLIR](
    *inner_type: *tuple[type[M1], type[M2], type[M3], type[M4]],
) -> Callable[[Definition[t.Any]], t.TypeIs[Definition[M1 | M2 | M3 | M4]]]: ...
@t.overload
def inner_type_is(
    *inner_type: *tuple[*tuple[type[MLIR], type[MLIR], type[MLIR], type[MLIR], type[MLIR]]],
) -> Callable[[Definition[t.Any]], t.TypeIs[Definition[MLIR]]]: ...
def inner_type_is(
    *inner_type: type[MLIR],
) -> Callable[[Definition[t.Any]], t.TypeIs[Definition[t.Any]]]:
    """Generate a typeguard to pass to [`mlir.Root.iter_defs`][].

    Args:
        inner_type: One or more `MLIR` types to check against `Definition.inner`.

    ## Examples
    ```py
    from typing import assert_type

    from tools.ir import mlir
    from tools.ir.mlir.nodes import ClosedDict


    def func(root: mlir.Root) -> None:
        _, first_closed_dict = next(root.iter_defs(mlir.inner_type_is(ClosedDict)))
        assert_type(first_closed_dict, mlir.Definition[ClosedDict])  # OK
    ```
    """

    def guard(obj: Definition[t.Any], /) -> t.TypeIs[Definition[t.Any]]:
        return isinstance(obj.inner, inner_type)

    return guard
