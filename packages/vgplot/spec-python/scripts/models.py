from collections.abc import Mapping, Sequence  # noqa: I002, TC003
from typing import Any, Literal

from msgspec import UNSET, Struct, UnsetType, field

type Primitive = Literal["array", "boolean", "integer", "null", "number", "object", "string"]
type _JsonSchema = JsonSchema


# TODO @dangotbanned: disable `forbid_unknown_fields=True` after figuring out exactly what isn't used
class JsonSchema(Struct, omit_defaults=True, repr_omit_defaults=True, forbid_unknown_fields=True):
    """The subset of JSON schema used in the spec."""

    schema: str = field(name="$schema", default="")
    ref: str = field(name="$ref", default="")
    title: str = ""
    description: str = ""
    required: Sequence[str] = field(default_factory=list)
    definitions: Mapping[str, _JsonSchema] = field(default_factory=dict)
    properties: Mapping[str, _JsonSchema] = field(default_factory=dict)
    const: str | bool | UnsetType = UNSET
    enum: Sequence[Any] = field(default_factory=list)
    type: Primitive | Sequence[Primitive] = field(default_factory=list)
    any_of: Sequence[_JsonSchema] = field(name="anyOf", default_factory=list)
    format: str = ""
    additional_properties: _JsonSchema | bool = field(name="additionalProperties", default=True)
    items: _JsonSchema | bool | Sequence[_JsonSchema] = True
    min_items: int = field(name="minItems", default=0)
    max_items: int | UnsetType = field(name="maxItems", default=UNSET)

    @property
    def ref_name(self) -> str:
        if ref := self.ref:
            return ref.removeprefix("#/definitions/")
        msg = f"Expected ref, got {self!r}"
        raise TypeError(msg)


class InputSchema(Struct, omit_defaults=True, repr_omit_defaults=True):
    """`mosaic-schema.json`."""

    definitions: Mapping[str, JsonSchema]
    schema: str = field(name="$schema")
    ref: str = field(name="$ref")
