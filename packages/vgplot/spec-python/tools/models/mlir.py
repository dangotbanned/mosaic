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

import functools
import typing
from collections.abc import Mapping
from typing import Final, Literal as L, final

from tools.models import base, json_wrapper as jw
from tools.models.mosaic import DefName  # ruff: ignore[typing-only-first-party-import]

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


class MLIR(base.FrozenStruct, frozen=True, tag=True, tag_field="tag"):
    """Mid-level IR, representing something that's not quite JSON or Python."""


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
class Unknown(MLIR, frozen=True):
    doc: str = ""


@final
class Builtins(MLIR, frozen=True, kw_only=True):
    name: str = ""
    types: frozenset[Scalar]
    doc: str = ""


@final
class Literal(MLIR, frozen=True):
    name: str
    members: frozenset[jw.Lit | jw.LitBool | None]
    doc: str = ""


@final
class EmptyTuple(MLIR, frozen=True):
    doc: str = ""


@final
class Tuple[Items: tuple[MLIR, ...]](MLIR, frozen=True):
    name: str
    items: Items
    doc: str = ""


@final
class Field(MLIR, frozen=True):
    name: str
    type: MLIR
    doc: str = ""


@final
class NamedTuple(MLIR, frozen=True):
    name: str
    fields: tuple[Field, ...]
    doc: str = ""


@final
class Sequence[T: MLIR](MLIR, frozen=True):
    name: str
    type: Final[T]
    doc: str = ""


@final
class OpenDict(MLIR, frozen=True, kw_only=True):
    """`bases` will be in the next IR."""

    name: str
    fields: tuple[Field, ...]
    total: bool = False
    doc: str = ""


@final
class ClosedDict(MLIR, frozen=True, kw_only=True):
    name: str
    fields: tuple[Field, ...]
    total: bool = False
    doc: str = ""


@final
class ExtraDict(MLIR, frozen=True, kw_only=True):
    name: str
    fields: tuple[Field, ...]
    total: bool = False
    extra_items: MLIR
    doc: str = ""


@final
class Union(MLIR, frozen=True):
    name: str
    members: frozenset[MLIR]
    doc: str = ""


@final
class Root(base.Struct, kw_only=True):
    id: str = ""
    definitions: dict[DefName, MLIR]

    @classmethod
    def from_json_wrapper(cls, source: jw.Root, /) -> Root:
        """See for special cases.

        - A `Reference` in `definitions` needs to be unwrapped
            - Curve/CurveName
            - Interval/LiteralTimeInterval
            - StackOffset/StackOffsetName
            - VectorShape/VectorShapeName
        """
        definitions = {}
        for name, schema in source.definitions.items():
            if isinstance(schema, jw.Reference):
                # NOTE: All other (nested) refs can use use singledispatch version
                msg = f"TODO: reference unwrapping + update at end of conversion, got: {name!r}, {schema!r}"
                raise NotImplementedError(msg)
            definitions[name] = from_json(schema, name)
        return Root(id=source.id, definitions=definitions)


@functools.singledispatch
def from_json(obj: jw.JsonWrapper, name: DefName, /) -> MLIR:
    raise NotImplementedError(obj.__class__)


@from_json.register(jw.EmptySequence)
def _(obj: jw.EmptySequence, _name: DefName, /) -> EmptyTuple:
    return EmptyTuple(doc=obj.description)


@from_json.register(jw.Unknown)
def _(obj: jw.Unknown, _name: DefName, /) -> Unknown:
    return Unknown(doc=obj.description)


_POUND_DEFS = "#/definitions/"


@from_json.register(jw.Reference)
def _(obj: jw.Reference, _name: DefName, /) -> Reference | ExtReference:
    ref = obj.ref
    if ref.startswith(_POUND_DEFS):
        return Reference(ref=ref.removeprefix(_POUND_DEFS), doc=obj.description)
    ext, ref = ref.split(_POUND_DEFS)
    return ExtReference(ref=ref, ext=ext, doc=obj.description)


@from_json.register(jw.Const)
@from_json.register(jw.Enum)
def _(obj: jw.Const | jw.Enum, name: DefName, /) -> Literal:
    return Literal(name, frozenset(obj.iter_values()), obj.description)


@from_json.register(jw.Primitive)
@from_json.register(jw.PrimitiveUnion)
def _(obj: jw.Primitive | jw.PrimitiveUnion, name: DefName, /) -> Builtins:
    return Builtins(
        name=name,
        types=frozenset(_JSON_PY_SCALAR[t] for t in obj.iter_types()),
        doc=obj.description,
    )


# TODO @dangotbanned: Convert sequence
# - varied min/max (if exists) will need to be converted into a union
@from_json.register(jw.Sequence)
def _(obj: jw.Sequence, name: DefName, /) -> Tuple[Incomplete] | Sequence[Incomplete] | Union:
    msg = f"todo: {obj.__class__.__name__!r}"
    raise NotImplementedError(msg)


# TODO @dangotbanned: Convert named sequence
@from_json.register(jw.NamedSequence)
def _(obj: jw.NamedSequence, name: DefName, /) -> NamedTuple:
    msg = f"todo: {obj.__class__.__name__!r}"
    raise NotImplementedError(msg)


# TODO @dangotbanned: Convert object
# - pairing required with fields
# - doing something with anonymous field types?
# - branching here on `closed`, `extra_items`
@from_json.register(jw.Object)
def _(obj: jw.Object, name: DefName, /) -> OpenDict | ClosedDict | ExtraDict:
    msg = f"todo: {obj.__class__.__name__!r}"
    raise NotImplementedError(msg)


# TODO @dangotbanned: Convert union
@from_json.register(jw.Union)
def _(obj: jw.Union, name: DefName, /) -> Union:
    msg = f"todo: {obj.__class__.__name__!r}"
    raise NotImplementedError(msg)
