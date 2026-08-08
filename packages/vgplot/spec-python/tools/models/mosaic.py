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
import re
from collections.abc import Callable, Iterable, Iterator, Sequence
from typing import Annotated as A, Final, Literal as L, final

from msgspec import field

from tools.models import base

type DefName = str
"""The name that keys the schema in `{"definitions": {<here>: ...}}`"""

type Primitive = L["array", "boolean", "integer", "null", "number", "object", "string"]
type _JsonSchemaFwd = JsonSchema
type NonRecursiveFields = _NonRecursiveFieldsBase
type Ref = str
type Resolved[T] = A[T, L["Resolved"]]


_POUND_DEFS: Final = "#/definitions/"


class XTemplate(
    base.Struct,
    omit_defaults=False,
    forbid_unknown_fields=True,
    kw_only=True,
    tag=functools.partial(re.compile("Template").sub, ""),
    tag_field="tag",
):
    """Helpers for passing in jinja template data when generating typed dicts."""


class SingleTemplate(XTemplate):
    """Generate a single `TypedDict`.

    Which looks like:
    ```py
    class <DefName>(<bases>, <keywords>):
        ... # fields w/ docs are defined here
    """

    bases: str = "TypedDict"
    """The class(es) to use as a base class."""

    keywords: L["total=False", "closed=True", "", "total=False, closed=True"] = "total=False"
    """Keyword arguments for TypedDict's metaclass."""


class ExtraTemplate(XTemplate):
    """Generate two `TypedDict`s.

    Which looks like:
    ```py
    class <base>(<root>, total=False):
        ... # fields w/ docs are defined here

    class <DefName>(<base>, total=False, closed=True):...
    ```
    """

    base: str
    """The name of an extra base TypedDict to generate via [TypedDictBase.jinja2].

    [TypedDictBase.jinja2]: ../../templates/datamodel-code-generator/TypedDictBase.jinja2"""

    root: str = "TypedDict"
    """The base class of `base` itself."""

    @classmethod
    def format(cls, original_name: DefName) -> str:
        return f"_{original_name}Open"

    @classmethod
    def from_name(cls, original_name: DefName, /, root: str) -> ExtraTemplate:
        return cls(base=cls.format(original_name), root=root)


class _NonRecursiveFieldsBase(base.Struct, forbid_unknown_fields=True):
    """Excludes: `"items"`, `"properties"`, `"any_of"`."""

    ref: Ref = field(name="$ref", default="")
    description: str = ""
    title: str = ""
    format: str = ""
    type: Primitive | Sequence[Primitive] | None = None
    const: str | bool | None = None
    enum: Sequence[str | bool | None] = field(default_factory=list)
    additional_properties: NonRecursiveFields | bool = field(
        name="additionalProperties", default=True
    )
    required: Sequence[str] = field(default_factory=list)

    x_template: SingleTemplate | ExtraTemplate | None = field(name="x-template", default=None)
    """See also [`x-` prefix annotations](https://json-schema.org/blog/posts/custom-annotations-will-continue#too-long-read-anyway)"""


    def is_ref(self) -> bool:
        return bool(self.ref)

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

    @property
    def def_name(self) -> DefName:
        if ref := self.ref:
            return ref.removeprefix(_POUND_DEFS)
        msg = f"Expected ref, got {self!r}"
        raise TypeError(msg)

    @classmethod
    def new_ref(cls, name: DefName, /) -> JsonSchema:
        return cls(ref=f"{_POUND_DEFS}{name}")

    def is_union(self) -> bool:
        return bool(self.any_of)

    def remove_properties(self, keys: Iterable[str], /) -> None:
        """Remove a set of *known* keys from `self.properties`."""
        del_item = self.properties.__delitem__
        for key in keys:
            del_item(key)

    def items_schema(self) -> JsonSchema:
        """Ensure `items` contains another `JsonSchema`."""
        items = self.items
        if not isinstance(items, JsonSchema):
            msg = f"Expected a schema in `items` but got {type(items).__name__!r}, in:\n{self!r}"
            raise NotImplementedError(msg)
        return items

    def iter_members(self) -> Iterator[JsonSchema]:
        """Iterate over the members of a union, raising if the assumption that this is a union has changed."""
        if not (members := self.any_of):
            msg = f"Expected a union but `any_of` was empty, got:\n{self!r}"
            raise NotImplementedError(msg)
        yield from members

@final
class InputSchema(base.Struct, kw_only=True):
    """Top level schema for `mosaic-schema.json`."""

    # TODO @dangotbanned: I want to migrate to 2020-12 (2 jumps from draft-07)
    # - docs are easier to read
    # - has examples of multi-file schemas
    # - $id is used frequently
    # - items -> prefixItems
    #   - for this use case, that's not a big deal
    schema: str = field(name="$schema")
    id: str = field(name="$id", default="")
    ref: Ref = field(name="$ref", default="")
    # NOTE: @dangotbanned: would be `"$defs"`
    definitions: dict[DefName, Resolved[JsonSchema]]

    def get(self, target: DefName, /) -> Resolved[JsonSchema]:
        """Get a top-level definition from the schema."""
        return self.definitions[target]

    def pop(self, target: DefName, /) -> Resolved[JsonSchema]:
        """Remove a top-level definition from the schema."""
        return self.definitions.pop(target)

    def insert(self, name: DefName, schema: Resolved[JsonSchema]) -> None:
        """Add a new top-level definition to the schema."""
        self.definitions[name] = schema

    def iter_members_defs(
        self, union: Resolved[JsonSchema], /
    ) -> Iterator[tuple[DefName, Resolved[JsonSchema]]]:
        """Iterate over the definitions ref'd by a union of references.

        Resolves `$ref`s defined at the current level, and raises if either:
        - `union` is not a union
        - each member is not a reference
        """
        for member_ref in union.iter_members():
            name = member_ref.def_name
            yield name, self.get(name)

    def iter_defs(
        self, predicate: Callable[[JsonSchema], bool] | None = None, /
    ) -> Iterator[tuple[DefName, Resolved[JsonSchema]]]:
        it: Iterable[tuple[DefName, Resolved[JsonSchema]]]
        if predicate is None:
            it = self.definitions.items()
        else:
            it = ((name, schema) for name, schema in self.definitions.items() if predicate(schema))
        yield from it


@functools.lru_cache(1024)
def _fix_ambiguous_unicode_characters(string: str, /) -> str:
    """Duplicated from [altair].

    These characters are all over `mosaic/packages/vgplot/spec/src/`, so it seems intentional.

    [altair]: https://github.com/vega/altair/blob/fab318c6c54db07849ec90437efdf20ad431e3a5/tools/markup.py#L133-L134
    """
    string = string.replace("’", "'")  # ruff: ignore[ambiguous-unicode-character-string]
    string = string.replace("–", "-")  # ruff: ignore[ambiguous-unicode-character-string]
    return string  # ruff: ignore[unnecessary-assign]
