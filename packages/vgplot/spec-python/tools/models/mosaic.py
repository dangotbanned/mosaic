"""[msgspec](https://msgspec.dev/) models for translating the mosaic schema.

# Spec
[Spec]: https://github.com/uwdata/mosaic/blob/e3cb141cfae4a0692990a924c03772956af89f78/packages/vgplot/spec/src/spec/Spec.ts#L34-L70

The current definition of [Spec] does not translate well through JSON schema to `TypedDict`.

## What are `Spec` and `Component`?
Here's a visual to illustrate the complexity

```ts
export type PlotMark = Area | ... | Density | DensityX | DensityY;
//                     ----       ^           --------   --------
//                     |        Union         |          |
//                     Interface              |          |
//                                            Interface(s) intersected with a
//                                            union of 4x anonymous interfaces

export type Component = HConcat | ... | Legend | PlotMark;
//                     --------       ^          --------
//                     |            Union        |
//                     Interface                 Union (65 members)

export type Spec = SpecHead & Component;
//                 -------- ^ ---------|
//                 |   Intersection    |
//                 |                   Union (11 members)
//                 Interface
```

## How does that fit into python?
[Intersection Types]: https://www.typescriptlang.org/docs/handbook/2/objects.html#intersection-types

A **limited form** of [Intersection Types] *are* representable using either `TypedDict` and `Protocol`.

```py
class SpecHead(TypedDict): ...
class HConcat(TypedDict): ...
class Area(TypedDict): ...

class SpecHConcat(SpecHead, HConcat): ...
class SpecArea(SpecHead, Area): ...

type Spec = SpecHConcat | ... | SpecArea
```

Sadly, this doesn't cover intersecting with a union.

## The fix?
- Find all the deeply-nested union members (80-90ish)
    - Includes defining names for those that are anonymous in the schema
- Mix each one with `SpecHead` to create a new TypedDict
    - Revealed issues with intersections allowing `Required & Not Required`
- Union each of those to define `Spec`
"""

import functools
from collections.abc import Sequence
from typing import Literal as L, final

from msgspec import field

from tools.models import base

type Primitive = L["array", "boolean", "integer", "null", "number", "object", "string"]
type _JsonSchemaFwd = JsonSchema
type NonRecursiveFields = _NonRecursiveFieldsBase
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
    additional_properties: NonRecursiveFields | bool = field(
        name="additionalProperties", default=True
    )
    required: Sequence[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if doc := self.description:
            self.description = _fix_ambiguous_unicode_characters(doc)


@final
class JsonSchema(_NonRecursiveFieldsBase, forbid_unknown_fields=True):
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

    properties: dict[str, _JsonSchemaFwd] = field(default_factory=dict)
    any_of: Sequence[_JsonSchemaFwd] = field(name="anyOf", default_factory=list)
    items: _JsonSchemaFwd | Sequence[_JsonSchemaFwd] | bool = True
    min_items: int = field(name="minItems", default=0)
    max_items: int | None = field(name="maxItems", default=None)


@final
class InputSchema(base.RootId[JsonSchema], kw_only=True):
    """Top level schema for `mosaic-schema.json`."""

    # TODO @dangotbanned: I want to migrate to 2020-12 (2 jumps from draft-07)
    # - docs are easier to read
    # - has examples of multi-file schemas
    # - $id is used frequently
    # - items -> prefixItems
    #   - for this use case, that's not a big deal
    # - `"definitions"` -> `"$defs"`
    schema: str = field(name="$schema")
    id: base.IdName = field(name="$id", default=base.IdName(""))
    ref: Ref = field(name="$ref", default="")


@functools.lru_cache(1024)
def _fix_ambiguous_unicode_characters(string: str, /) -> str:
    """Duplicated from [altair].

    These characters are all over `mosaic/packages/vgplot/spec/src/`, so it seems intentional.

    [altair]: https://github.com/vega/altair/blob/fab318c6c54db07849ec90437efdf20ad431e3a5/tools/markup.py#L133-L134
    """
    string = string.replace("’", "'")  # ruff: ignore[ambiguous-unicode-character-string]
    string = string.replace("–", "-")  # ruff: ignore[ambiguous-unicode-character-string]
    return string  # ruff: ignore[unnecessary-assign]
