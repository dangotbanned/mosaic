"""Very-intermediate-representation for tagging from schema.

- Iterating over `InputSchema.definitions` to assign these wrappers.
- Then lower into the next IR
"""

from __future__ import annotations

import collections.abc as cabc
from collections.abc import Iterator
from itertools import chain
from typing import (
    TYPE_CHECKING,
    Annotated as A,
    Any,
    Final,
    Literal as L,
    Self,
    TypeIs,
    assert_never,
    final,
)

import msgspec

from tools.models import base
from tools.models.base import DefName
from tools.models.config import ConvertConfig, MosaicSpecToml, ReferenceUnwrap
from tools.models.mosaic import InputSchema, JsonSchema
from tools.serde import convert_json

if TYPE_CHECKING:
    from tools.models import mlir


type Scalar = L["boolean", "integer", "number", "string", "null"]
"""Primitive Json schema types, excluding `"array"` and `"object"`."""

_SCALAR_NAMES: Final = frozenset(("boolean", "integer", "number", "string", "null"))


type Lit = str
"""A schema-static literal string."""

type LitBool = bool
"""A schema-static literal boolean."""

type camelCase = A[str, L["camelCase"]]  # ruff: ignore[mixed-case-variable-in-global-scope, snake-case-type-alias]


def _is_scalar(obj: Any) -> TypeIs[Scalar]:
    return isinstance(obj, str) and obj in _SCALAR_NAMES


def _is_scalar_subset(obj: cabc.Sequence[Any]) -> TypeIs[cabc.Sequence[Scalar]]:
    return _SCALAR_NAMES.issuperset(obj)


class _Tagged(base.Struct, tag=True, tag_field="tag"): ...


_EMPTY_SCHEMA = JsonSchema()


# NOTE: Use `schema` last in the constructor and it will show last in the repr
class JsonWrapper(_Tagged, kw_only=True):
    schema: JsonSchema

    @property
    def description(self) -> str:
        return self.schema.description

    @description.setter
    def description(self, value: str) -> None:
        self.schema.description = value

    @classmethod
    def from_schema(cls, schema: JsonSchema) -> Self:
        """Wrap a json schema, making this layer a tagged union."""
        msg = f"{cls.from_schema.__qualname__}() is not yet implemented"
        raise NotImplementedError(msg)

    def iter_refs(self) -> Iterator[Reference]:
        """Yield all references owned by the current node.

        - If the node is a reference, it will yield itself.
        - References are not resolved.
        """
        yield from ()


@final
class Unknown(JsonWrapper):
    """A schema that does not define validation constraints.

    ## Examples

    The elements in the array allow `Any`:
    ```py
    {"type": "array", "items": {}, "description": "An array of inline data values to visualize."}
    ```

    The object has `extra_items=Any`, in addition to the defined properties.
    ```py
    {
        "type": "object",
        "properties": {...},
        "addditionalProperties": True,
        "description": "Configuration options.",
    }
    ```
    """

    schema: JsonSchema = msgspec.field(default_factory=JsonSchema)

    @classmethod
    def from_schema(cls, schema: JsonSchema) -> Unknown:
        if schema == _EMPTY_SCHEMA:
            return Unknown()
        # quite a hassle to remove defaults, leaving just description
        raw = convert_json(schema, dict[str, Any])
        if raw.keys() == {"description"}:
            return Unknown(schema=schema)
        msg = f"Unexpected schema pattern found: {schema!r}\n{raw!r}"
        raise NotImplementedError(msg)


_POUND_DEFS: Final = "#/definitions/"


@final
class Reference(JsonWrapper):
    """`$ref`."""

    ref: str

    @classmethod
    def from_schema(cls, schema: JsonSchema) -> Reference:
        return Reference(ref=schema.ref, schema=schema)

    def iter_refs(self) -> Iterator[Reference]:
        yield self

    @property
    def def_name(self) -> DefName:
        """Return the name that this reference points to."""
        return self.ref.removeprefix(_POUND_DEFS)


@final
class Union(JsonWrapper):
    """`anyOf`."""

    members: cabc.Sequence[JsonWrapper]

    @classmethod
    def from_schema(cls, schema: JsonSchema) -> Union:
        return Union(members=[_from_schema(m) for m in schema.any_of], schema=schema)

    def iter_refs(self) -> Iterator[Reference]:
        for member in self.members:
            yield from member.iter_refs()

    def __iter__(self) -> Iterator[JsonWrapper]:
        yield from self.members.__iter__()


@final
class Const(JsonWrapper):
    """`Literal[<one>]`."""

    value: Lit | LitBool

    @classmethod
    def from_schema(cls, schema: JsonSchema) -> Const:
        if not isinstance(schema.const, (str, bool)):
            raise _temporary_bad_static_error(schema.type, cls)
        return Const(value=schema.const, schema=schema)

    def iter_values(self) -> Iterator[Lit | LitBool]:
        yield self.value


@final
class Enum(JsonWrapper):
    """`Literal[...]`."""

    values: cabc.Sequence[Lit | LitBool | None]

    @classmethod
    def from_schema(cls, schema: JsonSchema) -> Enum:
        return Enum(values=schema.enum, schema=schema)

    def iter_values(self) -> Iterator[Lit | LitBool | None]:
        yield from self.values


@final
class Primitive(JsonWrapper):
    """`"type": ~("array" | "object")`."""

    type: Scalar

    @classmethod
    def from_schema(cls, schema: JsonSchema) -> Primitive:
        if not _is_scalar(schema.type):
            raise _temporary_bad_static_error(schema.type, cls)
        return Primitive(type=schema.type, schema=schema)

    def iter_types(self) -> Iterator[Scalar]:
        yield self.type


@final
class PrimitiveUnion(JsonWrapper):
    """`"type": ["null", "string", "number", "boolean"]`.

    Will be lowered into a union later.
    """

    types: cabc.Sequence[Scalar]

    @classmethod
    def from_schema(cls, schema: JsonSchema) -> PrimitiveUnion:
        types = schema.type
        if isinstance(types, (str, type(None))):
            raise _temporary_bad_static_error(types, cls)
        if _is_scalar_subset(types):
            return PrimitiveUnion(types=types, schema=schema)
        msg = f"Unexpected primitive union type: {types!r}, in {schema!r}"
        raise TypeError(msg)

    def iter_types(self) -> Iterator[Scalar]:
        yield from self.types


# NOTE: `tuple[()]`, not `Sequence[Any]`
@final
class EmptySequence(JsonWrapper):
    """`{"maxItems": 0, "minItems": 0, "type": "array"}`."""

    @classmethod
    def from_schema(cls, schema: JsonSchema) -> EmptySequence:
        return EmptySequence(schema=schema)


@final
class NamedSequence(JsonWrapper):
    """Like a `NamedTuple`, but will used `Annotated` on a regular tuple instead."""

    fields: dict[camelCase, JsonWrapper]

    @classmethod
    def from_schema(cls, schema: JsonSchema) -> NamedSequence:
        items = schema.items
        if isinstance(items, (JsonSchema, bool)):
            raise _temporary_bad_static_error(items, cls)
        return NamedSequence(fields={el.title: _from_schema(el) for el in items}, schema=schema)

    def iter_refs(self) -> Iterator[Reference]:
        for field_type in self.fields.values():
            yield from field_type.iter_refs()


@final
class Sequence(JsonWrapper):
    """`"type": "array"`."""

    items: JsonWrapper
    min: int = 0
    max: int | None = None

    @classmethod
    def from_schema(cls, schema: JsonSchema) -> Sequence:
        items = schema.items
        if not isinstance(items, JsonSchema):
            raise _temporary_bad_static_error(items, cls)
        return Sequence(
            items=_from_schema(items), min=schema.min_items, max=schema.max_items, schema=schema
        )

    def iter_refs(self) -> Iterator[Reference]:
        yield from self.items.iter_refs()


type Closed = L["closed"]
"""Until msgspec gets literal bool support"""


@final
class Object(JsonWrapper):
    """`"type": "object"` AKA a class."""

    fields: dict[camelCase, JsonWrapper]
    required: cabc.Sequence[camelCase]
    closed: Closed | None
    extra_items: JsonWrapper | None

    @classmethod
    def from_schema(cls, schema: JsonSchema) -> Object:
        additional = schema.additional_properties
        closed = None
        extra_items = None
        if additional is False:
            closed = "closed"
        elif additional is not True:
            extra_items = _from_schema(convert_json(additional, JsonSchema))
        else:
            extra_items = Unknown()
        return Object(
            fields={k: _from_schema(v) for k, v in schema.properties.items()},
            required=schema.required,
            closed=closed,
            extra_items=extra_items,
            schema=schema,
        )

    def iter_refs(self) -> Iterator[Reference]:
        for field_type in self.fields.values():
            yield from field_type.iter_refs()
        if self.extra_items:
            yield from self.extra_items.iter_refs()


@final
class Root(base.Root[JsonWrapper], kw_only=True):
    """Top-level context for `mosaic-schema.json`."""

    id: str = msgspec.field(name="$id", default="")
    ref: str = msgspec.field(name="$ref", default="")
    schema: str = msgspec.field(name="$schema")
    config: ConvertConfig = msgspec.field(default_factory=ConvertConfig)

    @classmethod
    def from_input_schema(cls, source: InputSchema, config: ConvertConfig | None = None) -> Root:
        return Root(
            id=source.id,
            definitions={k: _from_schema(v) for k, v in source.definitions.items()},
            ref=source.ref,
            schema=source.schema,
            # NOTE: At some point this should be less eager and cache based on file info
            # Changing things a lot for now so not worried about perf
            config=config or MosaicSpecToml.discover_config().convert,
        )

    def iter_refs(self) -> Iterator[Reference]:
        """Yield all references within the entire schema."""
        for schema in self.definitions.values():
            yield from schema.iter_refs()

    def get_object(self, name: DefName, /) -> Object:
        return self.get_typed(name, Object)

    def get_union(self, name: DefName, /) -> Union:
        return self.get_typed(name, Union)

    def to_mlir(self) -> tuple[mlir.Root, mlir.ConversionCtx]:
        from tools.models import mlir

        return mlir.Root.from_json_wrapper(self)

    def ref_unwrap(self) -> None:
        """Rewrite top-level references.

        ## Notes
        - Used for 4 reference/(union/literal) pairs:
            - Curve/CurveName
            - Interval/LiteralTimeInterval
            - StackOffset/StackOffsetName
            - VectorShape/VectorShapeName
        - Want to remove the nesting, pick 1 description (they often have 2), update everywhere they are ref'd
        """
        cfg = self.config.to_mlir.ref_unwrap
        ref_unwrap_default = ReferenceUnwrap()
        modified = {}
        to_replace = {}
        for outer_name, outer in self.iter_defs(is_ref):
            inner_name = outer.def_name
            inner = self[inner_name]
            policy = cfg.get(outer_name, ref_unwrap_default)
            if policy.name == "outer":
                final_name = outer_name
            else:
                final_name = _unwrap_pick(policy.name, outer_name, inner_name)

            outer_desc = outer.description
            if policy.description == "outer":
                inner.description = outer_desc
            else:
                inner.description = _unwrap_pick(policy.description, outer_desc, inner.description)
            modified[final_name] = inner
            to_replace[(outer_name, inner_name)] = final_name

        if not to_replace:
            return
        for old in set(chain.from_iterable(to_replace)):
            self.definitions.pop(old)
        self.definitions.update(modified)

        defs = _POUND_DEFS
        repl_table: dict[str, str] = {}
        for (key1, key2), new_name in to_replace.items():
            repl_table[f"{defs}{key1}"] = repl_table[f"{defs}{key2}"] = f"{defs}{new_name}"
        replacement_fn = repl_table.get
        for ref in self.iter_refs():
            if match := replacement_fn(ref.ref):
                ref.ref = match


def _unwrap_pick(policy: L["inner", "longest", "shortest"], outer: str, inner: str) -> str:
    match policy:
        case "inner":
            return inner
        case "longest":
            return max(outer, inner)
        case "shortest":
            return min(outer, inner)
        case _:
            assert_never(policy)


def is_object(obj: Any) -> TypeIs[Object]:
    return isinstance(obj, Object)


def is_union(obj: Any) -> TypeIs[Union]:
    return isinstance(obj, Union)


def is_ref(obj: Any) -> TypeIs[Reference]:
    return isinstance(obj, Reference)


def is_seq(obj: Any) -> TypeIs[Sequence]:
    return isinstance(obj, Sequence)


def is_seq_any(obj: Any) -> TypeIs[Sequence | NamedSequence]:
    return isinstance(obj, (Sequence, NamedSequence, EmptySequence))


def is_seq_named(obj: Any) -> TypeIs[NamedSequence]:
    return isinstance(obj, NamedSequence)


def is_const(obj: Any) -> TypeIs[Const]:
    return isinstance(obj, Const)


def is_enum(obj: Any) -> TypeIs[Enum]:
    return isinstance(obj, Enum)


def _from_schema(schema: JsonSchema) -> JsonWrapper:
    if schema.ref:
        tp = Reference
    elif schema.any_of:
        tp = Union
    elif schema.enum:
        tp = Enum
    elif schema.const:
        tp = Const
    elif schema_type := schema.type:
        if schema_type == "object":
            tp = Object
        elif schema_type == "array":
            return _from_schema_array(schema)
        elif not isinstance(schema_type, str):
            tp = PrimitiveUnion
        else:
            tp = Primitive
    else:
        tp = Unknown
    return tp.from_schema(schema)


def _temporary_bad_static_error(obj: Any, from_type: type[JsonWrapper]) -> TypeError:
    """Return a placeholder error for union narrowing performed in the wrong order.

    None of these should appear, but need to design things differently to avoid the check.
    """
    msg = f"Use `_from_schema` instead. Failed in {from_type.__name__!r}, got {obj!r}"
    return TypeError(msg)


def _from_schema_array(schema: JsonSchema) -> Sequence | NamedSequence | EmptySequence:
    items = schema.items
    if isinstance(items, bool):
        if schema.max_items != 0:
            msg = f"{items=}, in {schema!r}"
            raise TypeError(msg)
        tp = EmptySequence
    else:
        tp = Sequence if isinstance(items, JsonSchema) else NamedSequence
    return tp.from_schema(schema)
