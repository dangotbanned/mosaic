from __future__ import annotations

# ruff: file-ignore[builtin-argument-shadowing]
import dataclasses
import functools
import typing
from collections import defaultdict, deque
from typing import Final, NewType

from tools.codegen.convert import pascal_to_snake_case
from tools.common import POUND_DEFS
from tools.ir.json_wrapper import nodes as jw
from tools.ir.mlir import nodes as mlir
from tools.ir.mlir.nodes import MLIR
from tools.models.base import DefName, IdName

if typing.TYPE_CHECKING:
    from collections.abc import Iterator, Mapping


Idx = NewType("Idx", int)

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


@dataclasses.dataclass
class ConversionCtx:
    """A history of what happened during `JsonWrapper` to `MLIR` conversion.

    ## Notes
    - Everything is traced, and serves as a descriptive tool to start with
    - Need to build things differently to take advantage of this
        - Making aliases for common types and replacing the duplication with references
        - Identifying when to synthesize base classes and or intersections
    """

    seen: defaultdict[type[MLIR], list[MLIR]] = dataclasses.field(
        default_factory=lambda: defaultdict(list)
    )
    """Per-MLIR-type to instances, ordered by creation time.

    Can answer questions like:
    - How frequently does each `type[MLIR]` appear?
    - What does each instance look like?
    - Do we have runs of similar/duplicated instances?
    """

    positions: defaultdict[DefName, deque[tuple[type[MLIR], Idx]]] = dataclasses.field(
        default_factory=lambda: defaultdict(deque)
    )
    """Per-top-level definition to keys into `seen`.

    Can answer questions like:
    - What does each definition produce?
    - Do we have more patterns in `seen` that are repeated across definitions?
    """

    def add(self, result: MLIR, owner: DefName, /) -> None:
        seen_key = type(result)
        seen_list = self.seen[seen_key]
        seen_list.append(result)
        idx = Idx(seen_list.__len__() - 1)
        self.positions[owner].append((seen_key, idx))

    def get_instances_of[M: MLIR](self, tp: type[M], /) -> list[M]:
        return typing.cast("list[M]", self.seen[tp])

    def get_instances_owned(self, owner: DefName, /) -> Iterator[MLIR]:
        seen_get = self.seen.__getitem__
        for tp, idx in self.positions[owner]:
            yield seen_get(tp)[idx]


def from_json(obj: jw.JsonWrapper, owner: DefName, ctx: ConversionCtx, /) -> MLIR:
    """Convert a `JsonWrapper` to a `MLIR`.

    Args:
        obj: The object to convert.
        owner: The definition that we originated from.
            Used for error messages.
        ctx: Mutable state that records the conversion process.
    """
    result = _from_json_dispatch(obj, owner, ctx)
    ctx.add(result, owner)
    return result


@functools.singledispatch
def _from_json_dispatch(obj: jw.JsonWrapper, owner: DefName, ctx: ConversionCtx, /) -> MLIR:
    """Impl for `from_json`.

    Use this for registration only.
    """
    msg = f"Converting {obj.__class__.__name__!r} is not yet implemented, in {owner!r}\n\n{obj!r}"
    raise NotImplementedError(msg)


_I_KNOW_WHAT_IM_DOING: Final = _from_json_dispatch
"""A marker for rewrites inside of `from_json`.

The caller is responsible for recording the result in `ctx`, which allows things like:

- Replacing parts of the result
- De-duplicating members of a union
- Skipping things entirely
"""


@_from_json_dispatch.register(jw.EmptySequence)
def _(obj: jw.EmptySequence, _owner: DefName, _ctx: ConversionCtx, /) -> mlir.EmptyTuple:
    return mlir.EmptyTuple(doc=obj.description)


@_from_json_dispatch.register(jw.Unknown)
def _(obj: jw.Unknown, _owner: DefName, _ctx: ConversionCtx, /) -> mlir.Unknown:
    return mlir.Unknown(doc=obj.description)


@_from_json_dispatch.register(jw.Reference)
def _(
    obj: jw.Reference, _owner: DefName, _ctx: ConversionCtx, /
) -> mlir.Reference | mlir.ExtReference:
    ref = obj.ref
    if ref.startswith(POUND_DEFS):
        return mlir.Reference(ref=ref.removeprefix(POUND_DEFS), doc=obj.description)
    ext, ref = ref.split(POUND_DEFS)
    return mlir.ExtReference(ref=ref, ext=IdName(ext), doc=obj.description)


@_from_json_dispatch.register(jw.Const)
@_from_json_dispatch.register(jw.Enum)
def _(obj: jw.Const | jw.Enum, _owner: DefName, _ctx: ConversionCtx, /) -> mlir.Literal:
    return mlir.Literal(members=tuple(obj.iter_values()), doc=obj.description)


@_from_json_dispatch.register(jw.Primitive)
def _(obj: jw.Primitive, _owner: DefName, _ctx: ConversionCtx, /) -> mlir.PyBuiltin:
    if doc := obj.description:
        return _JSON_PY_TYPE[obj.type](doc=doc)
    return _JSON_PY_INST[obj.type]


@_from_json_dispatch.register(jw.PrimitiveUnion)
def _(obj: jw.PrimitiveUnion, _owner: DefName, _ctx: ConversionCtx, /) -> mlir.Union:
    return mlir.Union(members=tuple(_JSON_PY_INST[t] for t in obj.types), doc=obj.description)


@_from_json_dispatch.register(jw.Sequence)
def _(
    obj: jw.Sequence, owner: DefName, ctx: ConversionCtx, /
) -> (
    mlir.Sequence[MLIR]
    | mlir.HomogeneousTuple[MLIR, int]
    | mlir.VariantHomogeneousTuple[MLIR, tuple[int, ...]]
):
    doc = obj.description
    type = from_json(obj.items, owner, ctx)
    match (obj.min, obj.max):
        case (0, None):
            result = mlir.Sequence(type=type, doc=doc)
        case (minimum, maximum) if minimum == maximum:
            result = mlir.HomogeneousTuple(type=type, length=minimum, doc=doc)
        case (minimum, int() as maximum):
            # NOTE: `Lag.lag` should be min 1, max 3 and datamodel-code-generator gets that wrong
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
def _(obj: jw.NamedSequence, owner: DefName, ctx: ConversionCtx, /) -> mlir.NamedTuple:
    fields = tuple(
        field(owner, f_name, f_type, ctx, required=True) for f_name, f_type in obj.fields.items()
    )
    return mlir.NamedTuple(fields=fields, doc=obj.description)


def field(
    owner: DefName, name: jw.camelCase, type: jw.JsonWrapper, ctx: ConversionCtx, *, required: bool
) -> mlir.Field:
    out_name = pascal_to_snake_case(name)
    out_type = _I_KNOW_WHAT_IM_DOING(type, owner, ctx)
    doc = out_type.doc
    out_type = out_type.with_doc("")
    ctx.add(out_type, owner)
    result = mlir.Field(name=out_name, type=out_type, required=required, doc=doc)
    ctx.add(result, owner)
    return result


# TODO @dangotbanned: Report pyrefly bug for `None` case (failed to narrow after trying the cheap cases)
@_from_json_dispatch.register(jw.Object)
def _(
    obj: jw.Object, owner: DefName, ctx: ConversionCtx, /
) -> mlir.OpenDict | mlir.ClosedDict | mlir.ExtraDict:
    # Having `required` paired with each field removes a surface to sync
    is_required = frozenset(obj.required).__contains__
    fields = tuple(
        field(owner, f_name, f_type, ctx, required=is_required(f_name))
        for f_name, f_type in obj.fields.items()
    )
    doc = obj.description
    match obj.closed, obj.extra_items:
        case (None, None):
            result = mlir.OpenDict(fields=fields, doc=doc)
        case ("closed", None):
            result = mlir.ClosedDict(fields=fields, doc=doc)
        case (None, extra):
            result = mlir.ExtraDict(
                fields=fields,
                extra_items=from_json(extra, owner, ctx),  # pyrefly: ignore[bad-argument-type]
                doc=doc,
            )
        case _:
            msg = f"Cannot combine closed={obj.closed!r} and extra_items={obj.extra_items!r} in {owner!r}\n\n{obj!r}"
            raise TypeError(msg)
    return result


@_from_json_dispatch.register(jw.Union)
def _(obj: jw.Union, owner: DefName, ctx: ConversionCtx, /) -> mlir.Union:
    merge_literals = set()
    members = set[MLIR]()
    for member in obj.members:
        converted = _I_KNOW_WHAT_IM_DOING(member, owner, ctx)
        if (not converted.doc) and isinstance(converted, mlir.Literal):
            merge_literals.update(converted.members)
        else:
            members.add(converted)
    if merge_literals:
        members.add(mlir.Literal(members=tuple(merge_literals)))
    members_final = tuple(members)
    for member in members_final:
        ctx.add(member, owner)
    return mlir.Union(members=members_final, doc=obj.description)
