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
from collections.abc import Mapping
from typing import Final, Literal as L, final

from tools.codegen.convert import pascal_to_snake_case
from tools.models import base, json_wrapper as jw
from tools.models.mosaic import DefName  # ruff: ignore[typing-only-first-party-import]

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
    name: str = ""
    types: frozenset[Scalar]
    doc: str = ""


@final
class Literal(MLIR, frozen=True, kw_only=True):
    name: str
    members: frozenset[jw.Lit | jw.LitBool | None]
    doc: str = ""


@final
class EmptyTuple(MLIR, frozen=True, kw_only=True):
    doc: str = ""


_SEQ_TYPE_SUFFIX: Final = "<type>"
_EXTRA_ITEMS_SUFFIX: Final = "<extra_items>"
_FIELD_TYPE_SEP: Final = "-"
"""Every type must have a name.

`Field.type` derives one via:

```py
f"{DefName}-{Field.name}"
```

## Important
This deliberately makes the type name an invalid python identifier.
Synthesized names should never reach generated code *silently*.
"""


@final
class Field(MLIR, frozen=True, kw_only=True):
    """An entry in a `*Dict` or `NamedTuple`."""

    name: snake_case
    type: MLIR
    required: bool = False
    doc: str = ""

    @classmethod
    def from_json(
        cls, owner: DefName, name: jw.camelCase, type: jw.JsonWrapper, *, required: bool
    ) -> Field:
        out_name = pascal_to_snake_case(name)
        out_type = from_json(type, f"{owner}{_FIELD_TYPE_SEP}{out_name}")
        return Field(name=out_name, type=out_type, required=required, doc=out_type.doc)


@final
class NamedTuple(MLIR, frozen=True, kw_only=True):
    name: str
    fields: tuple[Field, ...]
    doc: str = ""


class _SeqBase[T: MLIR](MLIR, frozen=True, kw_only=True):
    name: str
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

    name: str
    fields: tuple[Field, ...]
    doc: str = ""


@final
class ClosedDict(MLIR, frozen=True, kw_only=True):
    name: str
    fields: tuple[Field, ...]
    doc: str = ""


@final
class ExtraDict(MLIR, frozen=True, kw_only=True):
    name: str
    fields: tuple[Field, ...]
    extra_items: MLIR
    doc: str = ""


@final
class Union(MLIR, frozen=True, kw_only=True):
    name: str
    members: frozenset[MLIR]
    doc: str = ""


@final
class Root(base.Struct, kw_only=True):
    id: str = ""
    definitions: dict[DefName, MLIR]

    @classmethod
    def from_json_wrapper(cls, source: jw.Root, /) -> Root:
        source.ref_unwrap()
        return Root(
            id=source.id,
            definitions={
                name: from_json(schema, name) for name, schema in source.definitions.items()
            },
        )


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
    return Literal(name=name, members=frozenset(obj.iter_values()), doc=obj.description)


@from_json.register(jw.Primitive)
@from_json.register(jw.PrimitiveUnion)
def _(obj: jw.Primitive | jw.PrimitiveUnion, name: DefName, /) -> Builtins:
    return Builtins(
        name=name,
        types=frozenset(_JSON_PY_SCALAR[t] for t in obj.iter_types()),
        doc=obj.description,
    )


@from_json.register(jw.Sequence)
def _(
    obj: jw.Sequence, name: DefName, /
) -> Sequence[MLIR] | HomogeneousTuple[MLIR, int] | VariantHomogeneousTuple[MLIR, tuple[int, ...]]:
    doc = obj.description
    type_name = f"{name}{_SEQ_TYPE_SUFFIX}"
    type = from_json(obj.items, type_name)
    match (obj.min, obj.max):
        case (0, None):
            return Sequence(name=name, type=type, doc=doc)
        case (minimum, maximum) if minimum == maximum:
            return HomogeneousTuple(name=name, type=type, length=minimum, doc=doc)
        case (minimum, int() as maximum):
            # NOTE: `Lag.lag` should be min 1, max 3 and datamodel-code-generator gets that wrong
            return VariantHomogeneousTuple(
                name=name, type=type, lengths=tuple(range(minimum, maximum + 1)), doc=doc
            )
        case _:
            # NOTE: could be representable in python as `tuple[T, Min, *tuple[T, ...]]`
            # We don't have any cases like it yet though
            msg = f"Didn't expect to see ({(obj.min, obj.max)!r}) in {name!r}\n\n{obj!r}"
            raise NotImplementedError(msg)


@from_json.register(jw.NamedSequence)
def _(obj: jw.NamedSequence, name: DefName, /) -> NamedTuple:
    fields = tuple(
        Field.from_json(name, f_name, f_type, required=True)
        for f_name, f_type in obj.fields.items()
    )
    return NamedTuple(name=name, fields=fields, doc=obj.description)


@from_json.register(jw.Object)
def _(obj: jw.Object, name: DefName, /) -> OpenDict | ClosedDict | ExtraDict:
    # Having `required` paired with each field removes a surface to sync
    is_required = frozenset(obj.required).__contains__
    fields = tuple(
        Field.from_json(name, f_name, f_type, required=is_required(f_name))
        for f_name, f_type in obj.fields.items()
    )
    doc = obj.description
    match obj.closed, obj.extra_items:
        case (None, None):
            return OpenDict(name=name, fields=fields, doc=doc)
        case ("closed", None):
            return ClosedDict(name=name, fields=fields, doc=doc)
        case (None, extra):
            extra_items = from_json(extra, f"{name}{_EXTRA_ITEMS_SUFFIX}")
            return ExtraDict(name=name, fields=fields, extra_items=extra_items, doc=doc)
        case _:
            msg = f"Cannot combine closed={obj.closed!r} and extra_items={obj.extra_items!r}"
            raise TypeError(msg)


# TODO @dangotbanned: Convert union
@from_json.register(jw.Union)
def _(obj: jw.Union, name: DefName, /) -> Union:
    msg = f"todo: {obj.__class__.__name__!r}"
    raise NotImplementedError(msg)
