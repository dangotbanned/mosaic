"""[msgspec](https://msgspec.dev/) models for translating the mosaic schema.

## Notes
- Defines a greatly-reduced subset of JSON schema
- Structs act **both** as filters (undeclared fields are skipped)
  and validators (unexpected types within them raise during serde).
- `forbid_unknown_fields=True` can be used to determine if it is safe to remove a field,
  or to check a new schema hasn't introduced something unhandled
"""

from collections import deque
from collections.abc import Sequence
from typing import Annotated as A, Literal as L, final

from msgspec import field

from tools.models import base

type Primitive = L["array", "boolean", "integer", "null", "number", "object", "string"]
type _JsonSchemaFwd = JsonSchema
type NonRecursiveFields = _NonRecursiveFieldsBase
type Ref = str
type Resolved[T] = A[T, L["Resolved"]]
type Definitions = dict[Resolved[Ref], Resolved[JsonSchema]]


class _NonRecursiveFieldsBase(base.Struct, forbid_unknown_fields=True):
    """Excludes: `"items"`, `"properties"`, `"any_of"`."""

    ref: Ref = field(name="$ref", default="")
    description: str = ""
    title: str = ""
    format: str = ""
    type: Primitive | None = None
    const: str | bool | None = None
    enum: Sequence[str | bool | None] = field(default_factory=list)
    additional_properties: NonRecursiveFields | bool = field(
        name="additionalProperties", default=True
    )
    required: Sequence[str] = field(default_factory=list)


class _RecursePropsUnionBase(_NonRecursiveFieldsBase, forbid_unknown_fields=True):
    properties: dict[str, _JsonSchemaFwd] = field(default_factory=dict)
    any_of: Sequence[_JsonSchemaFwd] = field(name="anyOf", default_factory=list)


@final
class ItemSchema(_RecursePropsUnionBase, forbid_unknown_fields=True):
    """An element in `"items"`.

    Excludes: `"items"`.

    There are never 2 in a row:

        {"items": {"items": ...}}
    """


@final
class JsonSchema(_RecursePropsUnionBase, forbid_unknown_fields=True):
    """The (useful) subset of JSON schema used in `"definitions"`.

    Excludes `"$schema"` from all `Spec` members, while leaving a single version at the top-level.
    """

    type: Primitive | Sequence[Primitive] = field(default_factory=list)  # pyright: ignore[reportIncompatibleVariableOverride]
    items: ItemSchema | Sequence[ItemSchema] | bool = True
    min_items: int = field(name="minItems", default=0)
    max_items: int | None = field(name="maxItems", default=None)

    @property
    def ref_name(self) -> Resolved[Ref]:
        if ref := self.ref:
            return ref.removeprefix("#/definitions/")
        msg = f"Expected ref, got {self!r}"
        raise TypeError(msg)


@final
class InputSchema(base.Struct):
    """Top level schema for `mosaic-schema.json`."""

    definitions: Definitions
    ref: Ref = field(name="$ref")
    schema: str = field(name="$schema")

    def get(self, target: Resolved[Ref], /) -> Resolved[JsonSchema]:
        return self.definitions[target]

    def flatten_union(self, target: Resolved[Ref] | JsonSchema, /) -> deque[Resolved[Ref]]:
        """`Component` flattening.

        ## Notes
        - Might be resuable elsewhere later
        - Only requires 2 levels
            - `Component` -> `(..., PlotMark, ...)`
            - `PlotMark`  -> `(...)`
        - Then generate the new `TypedDict`s from imports using names
        """
        if isinstance(target, str):
            target = self.get(target)
        if not (union := target.any_of):
            msg = f"`target` is not a union, got:\n{target!r}"
            raise TypeError(msg)
        member_names: deque[Resolved[Ref]] = deque()
        for member in union:
            name = member.ref_name
            member_resolved = self.get(name)
            if not (nested := member_resolved.any_of):
                member_names.append(name)
            else:
                member_names.extend(nested_member.ref_name for nested_member in nested)
        return member_names
