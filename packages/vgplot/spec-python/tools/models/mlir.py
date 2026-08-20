"""Mid-level IR, representing something that's not quite JSON or Python.

- Not a full transition to python yet
    - But nodes are not allowed to keep a `schema` field
    - Anything useful must have been peeled off
- Missing things like
    - TypeVar/parameters
    - Type qualifiers
    - Type alias
    - Special forms (well some of them at least)
    - Generics
- Not 100% sure what to call this yet.
"""

from __future__ import annotations

# ruff: file-ignore[builtin-argument-shadowing]
import functools
import typing
from collections import deque
from collections.abc import Mapping
from typing import Final, Literal as L, final

from tools.codegen.convert import pascal_to_snake_case
from tools.models import base, json_wrapper as jw
from tools.models.base import DefName

if typing.TYPE_CHECKING:
    from tools.common import snake_case

# NOTE: Use this instead of importing `Any`, since we have one defined here
type Incomplete = typing.Any


type Scalar = L["bool", "int", "float", "str", "None"]

_JSON_PY_SCALAR: Mapping[jw.Scalar, Scalar] = {
    "boolean": "bool",
    "integer": "int",
    "number": "float",
    "string": "str",
    "null": "None",
}


class MLIR(base.FrozenStruct, frozen=True, tag=True, tag_field="tag", kw_only=True):
    """Mid-level IR, representing something that's not quite JSON or Python."""

    doc: str


@final
class Reference(MLIR, frozen=True, kw_only=True):
    """A reference to a symbol defined in the same file."""

    ref: str
    doc: str = ""


@final
class ExtReference(MLIR, frozen=True, kw_only=True):
    """A reference to a symbol defined externally."""

    ref: str
    ext: str
    doc: str = ""


@final
class Any(MLIR, frozen=True, kw_only=True):
    doc: str = ""


@final
class Unknown(MLIR, frozen=True, kw_only=True):
    doc: str = ""


@final
class Builtins(MLIR, frozen=True, kw_only=True):
    types: frozenset[Scalar]
    doc: str = ""


@final
class Literal(MLIR, frozen=True, kw_only=True):
    members: frozenset[jw.Lit | jw.LitBool | None]
    doc: str = ""


@final
class EmptyTuple(MLIR, frozen=True, kw_only=True):
    doc: str = ""


@final
class Field(MLIR, frozen=True, kw_only=True):
    """An entry in a `*Dict` or `NamedTuple`."""

    name: snake_case
    """The name of the field."""
    type: MLIR
    required: bool = False
    doc: str = ""

    @classmethod
    def from_json(
        cls, owner: DefName, name: jw.camelCase, type: jw.JsonWrapper, *, required: bool
    ) -> Field:
        out_name = pascal_to_snake_case(name)
        out_type = from_json(type, owner)
        doc = out_type.doc
        return Field(name=out_name, type=out_type.__replace__(doc=""), required=required, doc=doc)


@final
class NamedTuple(MLIR, frozen=True, kw_only=True):
    fields: tuple[Field, ...]
    doc: str = ""


class _SeqBase[T: MLIR](MLIR, frozen=True, kw_only=True):
    type: Final[T]
    doc: str = ""


@final
class HomogeneousTuple[T: MLIR, N: int](_SeqBase[T], frozen=True, kw_only=True):
    """A sequence where all elements are the same type and has a fixed-length.

    ## Notes
    Python's tuple is *heterogeneous*, but in `mosaic-schema.json` there are no cases of them
    """

    length: N


@final
class VariantHomogeneousTuple[T: MLIR, Ns: tuple[int, ...]](_SeqBase[T], frozen=True, kw_only=True):
    """A sequence where all elements are the same type and has one of the lengths specified in `Ns`.

    ## Notes
    Represents `min: int, max: int`, which in Python means `tuple[T, T] | tuple[T, T, T] | ...`
    """

    lengths: Ns


@final
class Sequence[T: MLIR](_SeqBase[T], frozen=True): ...


@final
class OpenDict(MLIR, frozen=True, kw_only=True):
    """`bases`, `total` will be in the next IR."""

    fields: tuple[Field, ...]
    doc: str = ""


@final
class ClosedDict(MLIR, frozen=True, kw_only=True):
    fields: tuple[Field, ...]
    doc: str = ""


@final
class ExtraDict(MLIR, frozen=True, kw_only=True):
    fields: tuple[Field, ...]
    extra_items: MLIR
    doc: str = ""


@final
class Union(MLIR, frozen=True, kw_only=True):
    members: frozenset[MLIR]
    doc: str = ""


@final
class Root(base.Root[MLIR]):
    @classmethod
    def from_json_wrapper(cls, source: jw.Root, /) -> Root:
        source.ref_unwrap()
        return Root(
            id=source.id,
            definitions={
                name: _from_json_dispatch(schema, name)
                for name, schema in source.definitions.items()
            },
        )


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
    msg = f"Converting {obj.__class__.__name__!r} is not yet implemented, in {owner!r}\n\n{obj!r}"
    raise NotImplementedError(msg)


@_from_json_dispatch.register(jw.EmptySequence)
def _(obj: jw.EmptySequence, _owner: DefName, /) -> EmptyTuple:
    return EmptyTuple(doc=obj.description)


@_from_json_dispatch.register(jw.Unknown)
def _(obj: jw.Unknown, _owner: DefName, /) -> Unknown:
    return Unknown(doc=obj.description)


_POUND_DEFS = "#/definitions/"


@_from_json_dispatch.register(jw.Reference)
def _(obj: jw.Reference, _owner: DefName, /) -> Reference | ExtReference:
    ref = obj.ref
    if ref.startswith(_POUND_DEFS):
        return Reference(ref=ref.removeprefix(_POUND_DEFS), doc=obj.description)
    ext, ref = ref.split(_POUND_DEFS)
    return ExtReference(ref=ref, ext=ext, doc=obj.description)


@_from_json_dispatch.register(jw.Const)
@_from_json_dispatch.register(jw.Enum)
def _(obj: jw.Const | jw.Enum, _owner: DefName, /) -> Literal:
    return Literal(members=frozenset(obj.iter_values()), doc=obj.description)


@_from_json_dispatch.register(jw.Primitive)
@_from_json_dispatch.register(jw.PrimitiveUnion)
def _(obj: jw.Primitive | jw.PrimitiveUnion, _owner: DefName, /) -> Builtins:
    return Builtins(
        types=frozenset(_JSON_PY_SCALAR[t] for t in obj.iter_types()), doc=obj.description
    )


@_from_json_dispatch.register(jw.Sequence)
def _(
    obj: jw.Sequence, owner: DefName, /
) -> Sequence[MLIR] | HomogeneousTuple[MLIR, int] | VariantHomogeneousTuple[MLIR, tuple[int, ...]]:
    doc = obj.description
    type = from_json(obj.items, owner)
    match (obj.min, obj.max):
        case (0, None):
            return Sequence(type=type, doc=doc)
        case (minimum, maximum) if minimum == maximum:
            return HomogeneousTuple(type=type, length=minimum, doc=doc)
        case (minimum, int() as maximum):
            # NOTE: `Lag.lag` should be min 1, max 3 and datamodel-code-generator gets that wrong
            return VariantHomogeneousTuple(
                type=type, lengths=tuple(range(minimum, maximum + 1)), doc=doc
            )
        case _:
            # NOTE: could be representable in python as `tuple[T, Min, *tuple[T, ...]]`
            # We don't have any cases like it yet though
            msg = f"Didn't expect to see ({(obj.min, obj.max)!r}) in {owner!r}\n\n{obj!r}"
            raise NotImplementedError(msg)


@_from_json_dispatch.register(jw.NamedSequence)
def _(obj: jw.NamedSequence, owner: DefName, /) -> NamedTuple:
    fields = tuple(
        Field.from_json(owner, f_name, f_type, required=True)
        for f_name, f_type in obj.fields.items()
    )
    return NamedTuple(fields=fields, doc=obj.description)


@_from_json_dispatch.register(jw.Object)
def _(obj: jw.Object, owner: DefName, /) -> OpenDict | ClosedDict | ExtraDict:
    # Having `required` paired with each field removes a surface to sync
    is_required = frozenset(obj.required).__contains__
    fields = tuple(
        Field.from_json(owner, f_name, f_type, required=is_required(f_name))
        for f_name, f_type in obj.fields.items()
    )
    doc = obj.description
    match obj.closed, obj.extra_items:
        case (None, None):
            return OpenDict(fields=fields, doc=doc)
        case ("closed", None):
            return ClosedDict(fields=fields, doc=doc)
        case (None, extra):
            return ExtraDict(fields=fields, extra_items=from_json(extra, owner), doc=doc)
        case _:
            msg = f"Cannot combine closed={obj.closed!r} and extra_items={obj.extra_items!r} in {owner!r}\n\n{obj!r}"
            raise TypeError(msg)


@_from_json_dispatch.register(jw.Union)
def _(obj: jw.Union, owner: DefName, /) -> Union:
    merge_builtins = set()
    merge_literals = set()
    members = deque[MLIR]()
    for member in obj.members:
        converted = from_json(member, owner)
        if (not converted.doc) and isinstance(converted, (Builtins, Literal)):
            if isinstance(converted, Builtins):
                merge_builtins.update(converted.types)
            else:
                merge_literals.update(converted.members)
        else:
            members.append(converted)
    if merge_builtins:
        members.append(Builtins(types=frozenset(merge_builtins)))
    if merge_literals:
        members.append(Literal(members=frozenset(merge_literals)))
    return Union(members=frozenset(members), doc=obj.description)
