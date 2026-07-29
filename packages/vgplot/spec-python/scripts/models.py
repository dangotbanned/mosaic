from collections.abc import Mapping, Sequence
from typing import Annotated as A, Any, Literal as L, final

from msgspec import UNSET, Struct, UnsetType, field

type Primitive = L["array", "boolean", "integer", "null", "number", "object", "string"]
type _JsonSchema = JsonSchema

type Ref = str
type Resolved[T] = A[T, L["Resolved"]]


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

    def flatten_union(
        self, target: Resolved[Ref] | JsonSchema, /
    ) -> dict[Resolved[Ref], Resolved[JsonSchema]]:
        """`Component` flattening.

        ## Notes

        - Might be resuable elsewhere later
        - Only requires 2 levels
            - `Component` -> `(..., PlotMark, ...)`
            - `PlotMark`  -> `(...)`
        - Think I only need the names?
            - Then generate the new `TypedDict`s from imports?
        """
        if isinstance(target, str):
            target = self.get(target)
        match target:
            case JsonSchema(any_of=(_first, *_rest) as union):
                result = {}
                for member in union:
                    name = member.ref_name
                    member_resolved = self.get(name)
                    if not (nested := member_resolved.any_of):
                        result[name] = member_resolved
                    else:
                        for nested_member in nested:
                            name = nested_member.ref_name
                            result[name] = self.get(name)
                return result

            case _:
                msg = f"`target` is not a union, got:\n{target!r}"
                raise TypeError(msg)
