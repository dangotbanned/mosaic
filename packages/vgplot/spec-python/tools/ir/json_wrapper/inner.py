"""Direct representation of `mosaic-schema.json`.

Describes a subset of [JSON Schema draft-07] that is produced by [ts-json-schema-generator].

[JSON Schema draft-07]: https://json-schema.org/draft-07/schema
[ts-json-schema-generator]: https://github.com/vega/ts-json-schema-generator
"""

from __future__ import annotations

from collections.abc import Sequence  # ruff: ignore[typing-only-standard-library-import]
from typing import Literal as L, final

from msgspec import field

from tools.common import fix_ambiguous_unicode_characters
from tools.models import base

type Primitive = L["array", "boolean", "integer", "null", "number", "object", "string"]
type _SchemaFwd = Schema
type _AdditionalProperties = _NonRecursiveFieldsBase
type Ref = str


class _NonRecursiveFieldsBase(base.Struct, forbid_unknown_fields=True):
    """Excludes: `"items"`, `"properties"`, `"any_of"`."""

    ref: Ref = field(name="$ref", default="")
    description: str = ""
    title: str = ""
    format: str = ""
    type: Primitive | Sequence[Primitive] | None = None
    const: base.Lit | bool | None = None
    enum: Sequence[base.Lit | bool | None] = field(default_factory=list)
    additional_properties: _AdditionalProperties | bool = field(
        name="additionalProperties", default=True
    )
    required: Sequence[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if doc := self.description:
            self.description = fix_ambiguous_unicode_characters(doc)


@final
class Schema(_NonRecursiveFieldsBase, forbid_unknown_fields=True):
    """The (useful) subset of JSON schema used in `"definitions"`.

    ## Notes
    - Defines a greatly-reduced subset of JSON schema
        - Excludes `"$schema"` from all `Spec` members, while leaving a single version at the top-level.
        - Exludes all unused keywords
        - Narrows some types of the remaining parts
    - Structs act **both** as filters (undeclared fields are skipped)
      and validators (unexpected types within them raise during serde).
    - `forbid_unknown_fields=True` can be used to determine if it is safe to remove a field,
      or to check a new schema hasn't introduced something unhandled
    """

    properties: dict[str, _SchemaFwd] = field(default_factory=dict)
    any_of: Sequence[_SchemaFwd] = field(name="anyOf", default_factory=list)
    items: _SchemaFwd | Sequence[_SchemaFwd] | bool = True
    min_items: int = field(name="minItems", default=0)
    max_items: int | None = field(name="maxItems", default=None)


@final
class Mosaic(base.RootId[Schema], kw_only=True):
    """Top level schema for `mosaic-schema.json`."""

    schema: str = field(name="$schema")
    id: base.IdName = field(name="$id", default=base.IdName(""))
    ref: Ref = field(name="$ref", default="")
