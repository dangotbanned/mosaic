"""A limited representation of Python's type system & data model.

## Important
- No classes
- No objects
- No functions/methods/operators
- No AST
- Strictly, things that can be used in the generation of modules containing `TypedDict`s
"""

from __future__ import annotations

import contextlib as _contextlib
from typing import TYPE_CHECKING

from tools.ir.pyir import (
    base,
    convert,
    definition,
    expr,
    field,
    module,
    qualifier,
    special,
    type_param,
    value,
)
from tools.ir.pyir.base import Definition, Expr, ExtRef, PyIR, Ref, TypedExtRef, TypedRef
from tools.ir.pyir.field import Field
from tools.ir.pyir.module import Module, Package

if TYPE_CHECKING:
    from collections.abc import Iterator

    from tools.models import config as _cfg


def _noop[T](obj: T, /) -> T:
    return obj


@_contextlib.contextmanager
def configure(config: _cfg.PyIRConfig, /) -> Iterator[None]:
    name = config.name
    aliases = name.aliases
    typing = aliases.typing

    expr.Sequence._ALIAS = aliases.collections.abc.Sequence
    expr.Literal._ALIAS = typing.Literal
    expr.Annotated._ALIAS = typing.Annotated
    definition.TypeAlias._ALIAS = typing.TypeAliasType
    definition.OpenDict._FORMAT = name.format_base

    type_config = config.type
    from_def = convert._patch_type_alias_type if type_config.str == "TypeAliasType" else _noop
    into_expr = convert._patch_named_tuple if type_config.NamedTuple == "NamedTuple" else _noop

    try:
        with convert._from_def.context(from_def), convert.into_expr.context(into_expr):
            yield

    finally:
        ...


__all__ = (
    "Definition",
    "Expr",
    "ExtRef",
    "Field",
    "Module",
    "Package",
    "PyIR",
    "Ref",
    "TypedExtRef",
    "TypedRef",
    "base",
    "convert",
    "definition",
    "expr",
    "field",
    "module",
    "qualifier",
    "special",
    "type_param",
    "value",
)
