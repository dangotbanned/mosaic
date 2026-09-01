from __future__ import annotations

import functools
import typing as t

from tools.codegen.convert import py_identifier, py_identifier_snake
from tools.ir.mlir import MLIR, Definition as mlir_Definition, nodes as mlir
from tools.ir.pyir import definition as d, expr, qualifier as q, value
from tools.ir.pyir.base import UntypedExtRef, UntypedRef
from tools.ir.pyir.field import Field

if t.TYPE_CHECKING:
    from collections.abc import Iterator, Mapping

    from tools.common import PyIdentifier
    from tools.ir import pyir
    from tools.ir.pyir.base import Expr
    from tools.models.base import DefName


_MLIR_TO_EXPR_NO_ATTR: t.Final[Mapping[type[MLIR], expr.DynExpr | expr.PyNone]] = {
    mlir.PyBool: expr.BOOL,
    mlir.PyInt: expr.INT,
    mlir.PyFloat: expr.FLOAT,
    mlir.Unknown: expr.ANY,
    mlir.PyStr: expr.STR,  # TODO @dangotbanned: handle configuration later (default)
    mlir.Any: expr.ANY,
    mlir.EmptyTuple: expr.EMPTY_TUPLE,
    mlir.PyNone: expr.PyNone(),
}
_PY_LITERAL: t.Final[Mapping[mlir.LiteralMember, expr.LiteralMember]] = {
    mlir.PyNone(): expr.PyNone(),
    mlir.PyFalse(): value.PyFalse(),
    mlir.PyTrue(): value.PyTrue(),
}


def from_def(obj: mlir_Definition[MLIR], name: DefName) -> pyir.Definition:
    """Convert an `mlir.Definition` into a `pyir.Definition`."""
    return _from_def(obj.inner, py_identifier(name))


@functools.singledispatch
def into_expr(obj: MLIR) -> Expr:
    """Try to convert an `mlir.MLIR` into a `pyir.Expr`."""
    if e := _MLIR_TO_EXPR_NO_ATTR.get(obj.__class__):
        return e
    return expr.Unresolved(inner=obj)


@into_expr.register(mlir.Reference)
def _(obj: mlir.Reference) -> UntypedRef:
    return UntypedRef(inner=obj)


@into_expr.register(mlir.ExtReference)
def _(obj: mlir.ExtReference) -> UntypedExtRef:
    return UntypedExtRef(inner=obj)


@into_expr.register(mlir.Literal)
def _(obj: mlir.Literal) -> expr.Literal:
    members = tuple(
        member if isinstance(member, str) else _PY_LITERAL[member] for member in obj.members
    )
    return expr.Literal(members=members)


@into_expr.register(mlir.Mapping)
def _(obj: mlir.Mapping[MLIR]) -> expr.Mapping:
    return expr.Mapping(expr=into_expr(obj.type))


@into_expr.register(mlir.Sequence)
def _(obj: mlir.Sequence[MLIR]) -> expr.Sequence:
    return expr.Sequence(expr=into_expr(obj.type))


@into_expr.register(mlir.HomogeneousTuple)
def _(obj: mlir.HomogeneousTuple[MLIR, int]) -> expr.HomogeneousTuple:
    return expr.HomogeneousTuple(expr=into_expr(obj.type), length=obj.length)


@into_expr.register(mlir.VariantHomogeneousTuple)
def _(obj: mlir.VariantHomogeneousTuple[MLIR, tuple[int, ...]]) -> expr.Union:
    elements = into_expr(obj.type)
    return expr.Union(
        members=tuple(expr.HomogeneousTuple(expr=elements, length=length) for length in obj.lengths)
    )


@into_expr.register(mlir.Union)
def _(obj: mlir.Union) -> expr.Union:
    return expr.Union(members=tuple(into_expr(member) for member in obj.members))


# TODO @dangotbanned: handle configuration later (default)
@into_expr.register(mlir.NamedTuple)
def _named_tuple_expr(obj: mlir.NamedTuple) -> expr.NamedTuple:
    fields = tuple(
        Field(name=py_identifier_snake(name), expr=into_expr(f.type), doc="")
        for name, f in obj.iter_fields_items()
    )
    return expr.NamedTuple(fields=fields)


@functools.singledispatch
def _from_def(obj: MLIR, name: PyIdentifier) -> pyir.Definition:
    msg = f"{name!r}: {type(obj).__name__} could not be converted into a PyIR definition, got:\n{obj!r}"
    raise NotImplementedError(msg)


def _expr_alias(obj: mlir.MLIR, name: PyIdentifier) -> d.TypeAlias[Expr]:
    return d.TypeAlias(name=name, expr=into_expr(obj), doc=obj.doc)


for tp in into_expr.registry:
    _from_def.register(tp, _expr_alias)


# TODO @dangotbanned: handle configuration later (not default)
@_from_def.register(mlir.NamedTuple)
def _(obj: mlir.NamedTuple, name: PyIdentifier) -> d.NamedTuple:
    fields = tuple(
        Field(name=py_identifier_snake(name), expr=into_expr(f.type), doc=f.doc)
        for name, f in obj.iter_fields_items()
    )
    return d.NamedTuple(name=name, fields=fields, doc=obj.doc)


# TODO @dangotbanned: handle configuration later (not default)
@_from_def.register(mlir.PyStr)
def _(obj: mlir.PyStr, name: PyIdentifier) -> d.NewTypeStr:
    return d.NewTypeStr(name=name, doc=obj.doc)


@_from_def.register(mlir.PyFalse)
@_from_def.register(mlir.PyTrue)
@_from_def.register(mlir.EmptyTuple)
@_from_def.register(mlir.PyNone)
@_from_def.register(mlir.Reference)
@_from_def.register(mlir.ExtReference)
@_from_def.register(mlir.Field)
def _(obj: mlir.MLIR, name: PyIdentifier) -> t.Never:
    msg = f"{name!r}: {type(obj).__name__} is not supported as a PyIR definition, got:\n{obj!r}"
    raise NotImplementedError(msg)


def _td_fields(fields: Iterator[tuple[str, mlir.Field]]) -> tuple[Field, ...]:
    return tuple(
        Field(
            name=py_identifier_snake(name),
            expr=q.Required(expr=into_expr(f.type)) if f.required else into_expr(f.type),
            doc=f.doc,
        )
        for name, f in fields
    )


@_from_def.register(mlir.OpenDict)
@_from_def.register(mlir.ClosedDict)
def _(obj: mlir.OpenDict | mlir.ClosedDict, name: PyIdentifier) -> d.OpenDict | d.ClosedDict:
    tp_pyir = d.ClosedDict if obj.__class__ is mlir.ClosedDict else d.OpenDict
    return tp_pyir(name=name, fields=_td_fields(obj.iter_fields_items()), doc=obj.doc)


@_from_def.register(mlir.ExtraDict)
def _(obj: mlir.ExtraDict, name: PyIdentifier) -> d.ExtraDict:
    return d.ExtraDict(
        name=name,
        fields=_td_fields(obj.iter_fields_items()),
        extra_items=into_expr(obj.extra_items),
        doc=obj.doc,
    )
