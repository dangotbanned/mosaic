"""Very-intermediate-representation for tagging from schema.

- Iterating over `InputSchema.definitions` to assign these wrappers.
- Then lower into the next IR
"""

import collections.abc as cabc
from typing import Any, Literal as L, Self, final

import msgspec

from tools.models import base
from tools.models.mosaic import DefName, JsonSchema
from tools.serde import convert_json


class _Tagged(base.Struct, tag=True, tag_field="tag"): ...


_EMPTY_SCHEMA = JsonSchema()


# NOTE: Use `schema` last in the constructor and it will show last in the repr
class JsonWrapper(_Tagged, kw_only=True):
    schema: JsonSchema

    @property
    def description(self) -> str:
        return self.schema.description

    @classmethod
    def from_schema(cls, schema: JsonSchema) -> Self:
        """Wrap a json schema, making this layer a tagged union."""
        msg = f"{cls.from_schema.__qualname__}() is not yet implemented"
        raise NotImplementedError(msg)


class _DirectWrapper(JsonWrapper):
    """Doesn't collect any fields yet.

    ## Important
    As soon as a subclass does anything beyond being a tag,
    they should switch to `JsonWrapper` and implement `from_schema` properly.
    """

    @classmethod
    def from_schema(cls, schema: JsonSchema) -> Self:
        return cls(schema=schema)


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


@final
class Reference(JsonWrapper):
    """`$ref`."""

    ref: str

    @classmethod
    def from_schema(cls, schema: JsonSchema) -> Reference:
        return Reference(ref=schema.ref, schema=schema)


@final
class Union(JsonWrapper):
    """`anyOf`."""

    members: cabc.Sequence[JsonWrapper]

    @classmethod
    def from_schema(cls, schema: JsonSchema) -> Union:
        return Union(members=[_from_schema(m) for m in schema.any_of], schema=schema)


@final
class Enum(_DirectWrapper):
    """`Literal[...]`."""


@final
class Const(_DirectWrapper):
    """`Literal[<one>]`."""


@final
class Primitive(_DirectWrapper):
    """`"type": ~("array" | "object")`."""


@final
class PrimitiveUnion(_DirectWrapper):
    """`"type": ["null", "string", "number", "boolean"]`."""


@final
class EmptySequence(_DirectWrapper):
    """`{"maxItems": 0, "minItems": 0, "type": "array"}`."""


@final
class NamedSequence(JsonWrapper):
    """Like a `NamedTuple`, but will used `Annotated` on a regular tuple instead."""

    fields: dict[str, JsonWrapper]

    @classmethod
    def from_schema(cls, schema: JsonSchema) -> NamedSequence:
        items = schema.items
        if isinstance(items, (JsonSchema, bool)):
            msg = "Use `_from_schema` instead"
            raise TypeError(msg)
        return NamedSequence(fields={el.title: _from_schema(el) for el in items}, schema=schema)


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
            msg = "Use `_from_schema` instead"
            raise TypeError(msg)
        return Sequence(
            items=_from_schema(items), min=schema.min_items, max=schema.max_items, schema=schema
        )


type Closed = L["closed"]
"""Until msgspec gets literal bool support"""


@final
class Object(JsonWrapper):
    """`"type": "object"` AKA a class."""

    properties: dict[str, JsonWrapper]
    required: cabc.Sequence[str]
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
            properties={k: _from_schema(v) for k, v in schema.properties.items()},
            required=schema.required,
            closed=closed,
            extra_items=extra_items,
            schema=schema,
        )


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


def from_definitions(definitions: dict[DefName, JsonSchema]) -> dict[DefName, JsonWrapper]:
    return {k: _from_schema(v) for k, v in definitions.items()}
