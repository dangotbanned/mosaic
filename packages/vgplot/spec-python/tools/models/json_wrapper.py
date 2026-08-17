"""Very-intermediate-representation for tagging from schema.

- Iterating over `InputSchema.definitions` to assign these wrappers.
- Then lower into the next IR
"""

import collections.abc as cabc
from typing import Any, Literal as L, final

from msgspec.structs import asdict as _asdict

from tools.models import base
from tools.models.mosaic import DefName, JsonSchema
from tools.serde import convert_json


class _Tagged(base.Struct, tag=True, tag_field="tag"): ...


_EMPTY_SCHEMA = JsonSchema()

type JsonWrapper = (
    Reference
    | Union
    | Literal
    | Primitive
    | PrimitiveUnion
    | EmptySequence
    | Sequence
    | Object
    | Unknown
)


@final
class Unknown(_Tagged):
    # `"items": {}, "type": "array"`
    # the inner part is `Any`
    schema: JsonSchema


@final
class Reference(_Tagged):
    # ref
    schema: JsonSchema


@final
class Union(_Tagged):
    # any_of
    schema: JsonSchema
    members: cabc.Sequence[JsonWrapper]

    @classmethod
    def from_schema(cls, schema: JsonSchema) -> Union:
        return Union(schema, [_from_schema(m) for m in schema.any_of])


@final
class Literal(_Tagged):
    # const or enum
    schema: JsonSchema


@final
class Primitive(_Tagged):
    # `"type": "string"`
    schema: JsonSchema


@final
class PrimitiveUnion(_Tagged):
    # `"type": ["null", "string", "number", "boolean"]`
    schema: JsonSchema


@final
class EmptySequence(_Tagged):
    # `{"maxItems": 0, "minItems": 0, "type": "array"}`
    schema: JsonSchema


@final
class Sequence(_Tagged):
    # `"type": "array"`
    # may have `items`, `minItems`, `maxItems`
    schema: JsonSchema
    items: JsonWrapper | cabc.Sequence[JsonWrapper]
    min: int
    max: int | None = None

    @classmethod
    def from_schema(cls, schema: JsonSchema) -> Sequence | EmptySequence:
        items = schema.items
        if isinstance(items, bool):
            if schema.max_items != 0:
                msg = f"{items=}, in {schema!r}"
                raise TypeError(msg)
            return EmptySequence(schema)
        w_items = (
            _from_schema(items)
            if isinstance(items, JsonSchema)
            else [_from_schema(el) for el in items]
        )
        return Sequence(schema, w_items, schema.min_items, schema.max_items)


type Closed = L["closed"]
"""Until msgspec gets literal bool support"""


@final
class Object(_Tagged):
    # `"type": "object"`
    # may have `properties`, `additionalProperties`, `required`
    schema: JsonSchema
    properties: dict[str, JsonWrapper]
    required: cabc.Sequence[str]
    closed: Closed | None
    extra_items: JsonWrapper | None

    @classmethod
    def from_schema(cls, schema: JsonSchema) -> Object:
        props = {k: _from_schema(v) for k, v in schema.properties.items()}
        req = schema.required
        additional = schema.additional_properties
        if additional is False:
            r = Object(schema, props, req, "closed", None)
        elif additional is not True:
            r = Object(schema, props, req, None, _from_schema(JsonSchema(**_asdict(additional))))
        else:
            r = Object(schema, props, req, None, Unknown(_EMPTY_SCHEMA))
        return r


def _from_schema(schema: JsonSchema) -> JsonWrapper:
    if schema.ref:
        r = Reference(schema)
    elif schema.any_of:
        r = Union.from_schema(schema)
    elif schema.const or schema.enum:
        r = Literal(schema)
    elif schema_type := schema.type:
        if schema_type == "object":
            r = Object.from_schema(schema)
        elif schema_type == "array":
            r = Sequence.from_schema(schema)
        elif not isinstance(schema_type, str):
            r = PrimitiveUnion(schema)
        else:
            r = Primitive(schema)
    elif schema == _EMPTY_SCHEMA:
        r = Unknown(schema)
    else:
        # quite a hassle to remove defaults, leaving just description
        raw = convert_json(schema, dict[str, Any])
        if raw.keys() == {"description"}:
            r = Unknown(schema)
        else:
            msg = f"Unexpected schema pattern found: {schema!r}\n{raw!r}"
            raise NotImplementedError(msg)
    return r


def from_definitions(definitions: dict[DefName, JsonSchema]) -> dict[DefName, JsonWrapper]:
    return {k: _from_schema(v) for k, v in definitions.items()}
