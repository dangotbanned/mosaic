# ruff: noqa: I002, TC003, N817
from collections.abc import Mapping, Sequence
from typing import Annotated as An
from typing import Any, final
from typing import Literal as L

from msgspec import UNSET, Struct, UnsetType, field

type Primitive = L["array", "boolean", "integer", "null", "number", "object", "string"]
type _JsonSchema = JsonSchema

type Ref = str
type Resolved[T] = An[T, L["Resolved"]]
type Unresolved[T] = An[T, L["Unresolved"]]


# TODO @dangotbanned: disable `forbid_unknown_fields=True` after figuring out exactly what isn't used
@final
class JsonSchema(Struct, omit_defaults=True, repr_omit_defaults=True, forbid_unknown_fields=True):
    """The subset of JSON schema used in the spec."""

    ref: Ref = field(name="$ref", default="")
    title: str = ""
    description: str = ""
    type: Primitive | Sequence[Primitive] = field(default_factory=list)
    any_of: Sequence[_JsonSchema] = field(name="anyOf", default_factory=list)
    required: Sequence[str] = field(default_factory=list)
    properties: Mapping[str, _JsonSchema] = field(default_factory=dict)
    const: str | bool | UnsetType = UNSET
    enum: Sequence[Any] = field(default_factory=list)
    additional_properties: _JsonSchema | bool = field(name="additionalProperties", default=True)
    items: _JsonSchema | bool | Sequence[_JsonSchema] = True
    min_items: int = field(name="minItems", default=0)
    max_items: int | UnsetType = field(name="maxItems", default=UNSET)
    format: str = ""
    schema: str = field(name="$schema", default="")

    @property
    def ref_name(self) -> Resolved[Ref]:
        if ref := self.ref:
            return ref.removeprefix("#/definitions/")
        msg = f"Expected ref, got {self!r}"
        raise TypeError(msg)


class InputSchema(Struct, omit_defaults=True, repr_omit_defaults=True):
    """`mosaic-schema.json`."""

    definitions: Mapping[Resolved[Ref], Resolved[JsonSchema]]
    ref: Ref = field(name="$ref")
    schema: str = field(name="$schema")

    def get(self, target: Resolved[Ref], /) -> Resolved[JsonSchema]:
        return self.definitions[target]

