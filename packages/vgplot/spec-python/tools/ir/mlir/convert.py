from __future__ import annotations

# ruff: file-ignore[builtin-argument-shadowing]
import functools
import typing
from typing import Final

from tools.common import POUND_DEFS
from tools.ir.json_wrapper import nodes as jw
from tools.ir.mlir import nodes as mlir
from tools.ir.mlir.nodes import MLIR
from tools.models.base import DefName, IdName, Lit

if typing.TYPE_CHECKING:
    from collections.abc import Mapping


_JSON_PY_INST: Final[Mapping[jw.Scalar, mlir.PyBuiltin]] = {
    "boolean": mlir.PyBool(),
    "integer": mlir.PyInt(),
    "number": mlir.PyFloat(),
    "string": mlir.PyStr(),
    "null": mlir.PyNone(),
}
_JSON_PY_TYPE: Final[Mapping[jw.Scalar, type[mlir.PyBuiltin]]] = {
    "boolean": mlir.PyBool,
    "integer": mlir.PyInt,
    "number": mlir.PyFloat,
    "string": mlir.PyStr,
    "null": mlir.PyNone,
}

_PY_LITERAL: Final[Mapping[Lit | jw.LitBool | None, mlir.LiteralMember]] = {
    None: mlir.PyNone(),
    False: mlir.PyFalse(),
    True: mlir.PyTrue(),
}


def from_json(obj: jw.JsonWrapper, owner: DefName, /) -> MLIR:
    """Convert a `JsonWrapper` to a `MLIR`.

    Args:
        obj: The object to convert.
        owner: The definition that we originated from.
            Used for error messages.
    """
    return _from_json_dispatch(obj, owner)


@functools.singledispatch
def _from_json_dispatch(obj: jw.JsonWrapper, owner: DefName, /) -> MLIR:
    """Impl for `from_json`.

    Use this for registration only.
    """
    msg = f"Converting {obj.__class__.__name__!r} is not yet implemented, in {owner!r}\n\n{obj!r}"
    raise NotImplementedError(msg)


@_from_json_dispatch.register(jw.EmptySequence)
def _(obj: jw.EmptySequence, _owner: DefName, /) -> mlir.EmptyTuple:
    return mlir.EmptyTuple(doc=obj.description)


@_from_json_dispatch.register(jw.Unknown)
def _(obj: jw.Unknown, _owner: DefName, /) -> mlir.Unknown:
    return mlir.Unknown(doc=obj.description)


@_from_json_dispatch.register(jw.Reference)
def _(obj: jw.Reference, _owner: DefName, /) -> mlir.Reference | mlir.ExtReference:
    ref = obj.ref
    if ref.startswith(POUND_DEFS):
        return mlir.Reference(ref=ref.removeprefix(POUND_DEFS), doc=obj.description)
    ext, ref = ref.split(POUND_DEFS)
    return mlir.ExtReference(ref=ref, ext=IdName(ext), doc=obj.description)


@_from_json_dispatch.register(jw.Const)
@_from_json_dispatch.register(jw.Enum)
def _(obj: jw.Const | jw.Enum, _owner: DefName, /) -> mlir.Literal:
    it = obj.iter_values()
    members = tuple(member if isinstance(member, str) else _PY_LITERAL[member] for member in it)
    return mlir.Literal(members=members, doc=obj.description)


@_from_json_dispatch.register(jw.Primitive)
def _(obj: jw.Primitive, _owner: DefName, /) -> mlir.PyBuiltin:
    if doc := obj.description:
        return _JSON_PY_TYPE[obj.type](doc=doc)
    return _JSON_PY_INST[obj.type]


@_from_json_dispatch.register(jw.PrimitiveUnion)
def _(obj: jw.PrimitiveUnion, _owner: DefName, /) -> mlir.Union:
    return mlir.Union(members=tuple(_JSON_PY_INST[t] for t in obj.types), doc=obj.description)


@_from_json_dispatch.register(jw.Sequence)
def _(
    obj: jw.Sequence, owner: DefName, /
) -> (
    mlir.Sequence[MLIR]
    | mlir.HomogeneousTuple[MLIR, int]
    | mlir.VariantHomogeneousTuple[MLIR, tuple[int, ...]]
):
    doc = obj.description
    type = from_json(obj.items, owner)
    match (obj.min, obj.max):
        case (0, None):
            result = mlir.Sequence(type=type, doc=doc)
        case (minimum, maximum) if minimum == maximum:
            result = mlir.HomogeneousTuple(type=type, length=minimum, doc=doc)
        case (minimum, int() as maximum):
            result = mlir.VariantHomogeneousTuple(
                type=type, lengths=tuple(range(minimum, maximum + 1)), doc=doc
            )
        case _:
            # NOTE: could be representable in python as `tuple[T, Min, *tuple[T, ...]]`
            # We don't have any cases like it yet though
            msg = f"Didn't expect to see ({(obj.min, obj.max)!r}) in {owner!r}\n\n{obj!r}"
            raise NotImplementedError(msg)
    return result


@_from_json_dispatch.register(jw.NamedSequence)
def _(obj: jw.NamedSequence, owner: DefName, /) -> mlir.NamedTuple:
    fields = tuple(
        field(owner, f_name, f_type, required=True) for f_name, f_type in obj.fields.items()
    )
    return mlir.NamedTuple(fields=fields, doc=obj.description)


def field(
    owner: DefName, name: jw.camelCase, type: jw.JsonWrapper, *, required: bool
) -> mlir.Field:
    out_type = from_json(type, owner)
    doc = out_type.doc
    return mlir.Field(name=name, type=out_type.with_doc(""), required=required, doc=doc)


# TODO @dangotbanned: Report pyrefly bug for `None` case (failed to narrow after trying the cheap cases)
@_from_json_dispatch.register(jw.Object)
def _(
    obj: jw.Object, owner: DefName, /
) -> mlir.OpenDict | mlir.ClosedDict | mlir.ExtraDict | mlir.Mapping:
    # Having `required` paired with each field removes a surface to sync
    is_required = frozenset(obj.required).__contains__
    fields = tuple(
        field(owner, f_name, f_type, required=is_required(f_name))
        for f_name, f_type in obj.fields.items()
    )
    doc = obj.description
    match obj.closed, obj.extra_items:
        case (None, None):
            result = mlir.OpenDict(fields=fields, doc=doc)
        case ("closed", None):
            result = mlir.ClosedDict(fields=fields, doc=doc)
        case (None, extra):
            if not fields:
                return mlir.Mapping(type=from_json(extra, owner), doc=doc)
            result = mlir.ExtraDict(
                fields=fields,
                extra_items=from_json(extra, owner),  # pyrefly: ignore[bad-argument-type]
                doc=doc,
            )
        case _:
            msg = f"Cannot combine closed={obj.closed!r} and extra_items={obj.extra_items!r} in {owner!r}\n\n{obj!r}"
            raise TypeError(msg)
    return result


@_from_json_dispatch.register(jw.Union)
def _(obj: jw.Union, owner: DefName, /) -> mlir.Union:
    merge_literals = set()
    members = set[MLIR]()
    for member in obj.members:
        converted = from_json(member, owner)
        if (not converted.doc) and isinstance(converted, mlir.Literal):
            merge_literals.update(converted.members)
        else:
            members.add(converted)
    if merge_literals:
        members.add(mlir.Literal(members=tuple(sorted(merge_literals, key=str))))

    return mlir.Union(members=tuple(sorted(members, key=sort_key)), doc=obj.description)


def sort_key(node: MLIR, /) -> str:
    # Doesn't make this fully deterministic, but improves common cases
    # of builtin unions
    return node.__class__.__name__
