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
from collections import deque
from collections.abc import Sequence
from typing import Annotated as A, Any, Final, Literal as L, LiteralString, final

from msgspec import field

from tools.models import base

type Primitive = L["array", "boolean", "integer", "null", "number", "object", "string"]
type _JsonSchemaFwd = JsonSchema
type NonRecursiveFields = _NonRecursiveFieldsBase
type Ref = str
type Resolved[T] = A[T, L["Resolved"]]
type Definitions = dict[Resolved[Ref], Resolved[JsonSchema]]

type DefName = str
"""The name that keys the schema in `{"definitions": {<here>: ...}}`"""

_POUND_DEFS: Final = "#/definitions/"


type Incomplete = Any


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
    x_base_open: bool = field(name="x-base-open", default=False)
    """An extension field marker, to request an extra base class during codegen."""

    def is_ref(self) -> bool:
        return bool(self.ref)

    def __post_init__(self) -> None:
        if doc := self.description:
            self.description = _fix_ambiguous_unicode_characters(doc)


@functools.lru_cache(1024)
def _fix_ambiguous_unicode_characters(string: str, /) -> str:
    """Duplicated from [altair].

    These characters are all over `mosaic/packages/vgplot/spec/src/`, so it seems intentional.

    [altair]: https://github.com/vega/altair/blob/fab318c6c54db07849ec90437efdf20ad431e3a5/tools/markup.py#L133-L134
    """
    string = string.replace("’", "'")  # ruff: ignore[ambiguous-unicode-character-string]
    string = string.replace("–", "-")  # ruff: ignore[ambiguous-unicode-character-string]
    return string  # ruff: ignore[unnecessary-assign]


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

    type: Primitive | Sequence[Primitive] = field(default_factory=list)  # pyright: ignore[reportIncompatibleVariableOverride]
    items: ItemSchema | Sequence[ItemSchema] | bool = True
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


@final
class InputSchema(base.Struct):
    """Top level schema for `mosaic-schema.json`."""

    # NOTE: @dangotbanned: would be `"$defs"`
    definitions: dict[DefName, Resolved[JsonSchema]]

    # TODO @dangotbanned: Since `Spec` is removed, this is now invalid: `"#/definitions/Spec"`
    # Is it just being ignored?
    ref: Ref = field(name="$ref")

    # TODO @dangotbanned: I want to migrate to 2020-12 (2 jumps from draft-07)
    # - docs are easier to read
    # - has examples of multi-file schemas
    # - $id is used frequently
    # - items -> prefixItems
    #   - for this use case, that's not a big deal
    schema: str = field(name="$schema")

    def get(self, target: DefName, /) -> Resolved[JsonSchema]:
        """Get a top-level definition from the schema."""
        return self.definitions[target]

    def insert(self, name: DefName, schema: Resolved[JsonSchema]) -> None:
        """Add a new top-level definition to the schema."""
        self.definitions[name] = schema

    def try_insert(self, name: DefName, schema: Resolved[JsonSchema]) -> DuplicateError | None:
        """Try to add a new definition, returning an error if the name is already in use."""
        if name in self.definitions:
            return DuplicateError.from_try_insert(name, schema, self.get(name))
        return self.insert(name, schema)

    def name_union_members(self, target: DefName, /, fmt: LiteralString = "{target}{idx}") -> None:
        """Lift anonymous members of a union into top-level definitions."""
        union = self.get(target)
        doc = union.description
        member_refs = []
        for idx, member in enumerate(union.any_of, 1):
            member_name = fmt.format(target=target, idx=idx)
            member_refs.append(member.new_ref(member_name))
            if err := self.try_insert(
                member_name, member.__replace__(description=doc, x_base_open=True)
            ):
                raise err
        self.insert(target, union.__replace__(any_of=member_refs))

    # TODO @dangotbanned: Figure out a nicer API for this mess
    # It does too many things
    def flatten_component_union_mut(self, target: DefName | JsonSchema, /) -> deque[DefName]:
        """*'Enhance'* the definition of `Component`.

        See the module doc for a detailed look at this problem.

        ## Notes
        - Mutates `self.definitions`
        - Returns names to use in intersection `TypedDict`s
        """
        if isinstance(target, str):
            target = self.get(target)

        if not target.is_union():
            msg = f"`target` is not a union, got:\n{target!r}"
            raise TypeError(msg)

        # NOTE: Why is this not recursive?
        # It might make sense to do that eventually, but
        # - this shows how many levels of nesting there are.
        # - will raise when expectations change
        member_names: deque[DefName] = deque()
        for member in target.any_of:
            name = member.def_name
            member_resolved = self.get(name)
            if not member_resolved.is_union():
                member_names.append(name)
            else:
                for nested_member in member_resolved.any_of:
                    nested_name = nested_member.def_name
                    nested_member_resolved = self.get(nested_name)
                    if not nested_member_resolved.is_union():
                        member_names.append(nested_name)
                    elif any(deep.is_ref() for deep in nested_member_resolved.any_of):
                        msg_0 = f"TODO @dangotbanned: Expected only anonymous unions at this level, got members: {nested_member_resolved.any_of!r}"
                        raise NotImplementedError(msg_0)
                    else:
                        self.name_union_members(nested_name)
                        member_names.extend(deep.def_name for deep in self.get(nested_name).any_of)
        return member_names


class DuplicateError(ValueError):
    @staticmethod
    def from_try_insert(name: DefName, new: JsonSchema, existing: JsonSchema) -> DuplicateError:
        return DuplicateError(
            f"A definition named {name!r} is already present in the schema.\n"
            f"- To replace {name!r}, use {InputSchema.insert.__qualname__}() instead."
            f"- Otherwise, rename `schema` to avoid a collision.\n\n"
            f"Existing:\n{existing!r}\n\n"
            f"New schema:\n{new!r}"
        )
