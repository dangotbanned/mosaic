"""Configuration via toml."""

import typing
from collections.abc import Iterable, Mapping, Sequence
from pathlib import Path
from typing import Annotated as A, Final, Literal as L, final

import msgspec
from msgspec import field

from tools.models import base
from tools.models.base import DefName

type MLIRType = L[
    "ClosedDict",
    "EmptyTuple",
    "ExtReference",
    "ExtraDict",
    "Field",
    "HomogeneousTuple",
    "Literal",
    "NamedTuple",
    "OpenDict",
    "PyBool",
    "PyFloat",
    "PyInt",
    "PyNone",
    "PyStr",
    "Reference",
    "Sequence",
    "Union",
    "Unknown",
    "VariantHomogeneousTuple",
]

type UnwrapPolicy = L["longest", "shortest", "inner", "outer"]
type Depth = L[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


type IterOver = L["definitions", "children", "descendants"]
"""The kind of traversal to perform.

- *"definitions"*: Visit top-level definitions only.
- *"children"*: Visit the children of top-level definitions.
- *"descendants"*: Visit top-level definitions, then their children, recursively.
"""

ENTRY_POINT_PATTERN: Final[Mapping[L["json", "python"], typing.LiteralString]] = {
    "json": r"([\w.]+)\s*(:\s*([\w.]+)\s*)$",
    "python": r"(?P<module>[\w.]+)\s*(:\s*(?P<attr>[\w.]+)\s*)$",
}
"""A pair of regex patterns to validate and parse an entry point.

The python version is semantically the same, but uses named capture groups.

```py
"module" # the fully qualified module path
"attr"   # the function to call inside it
```
"""


class ReferenceUnwrap(base.FrozenStruct, frozen=True, forbid_unknown_fields=True):
    """Override how each attribute is chosen when unwraping a ref.

    ## Notes
    Both `name` and `description` are resolved independently. Here they are referred to as **value**.

    - *"longest"*: pick the longest value
    - *"shortest"*: pick the shortest value
        - **note**: The default description is `""`
    - *"outer"*: use the value of the definition with a `"$ref"` field
    - *"inner"*: use the value of the definition without a `"$ref"` field

    ## Examples
    `"Curve"` does not add much value to `"CurveName"`, but it has a different name and description:

    ```py
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "definitions": {
            "Curve": {
                "$ref": "#/definitions/CurveName",
                "description": "How to interpolate between control points.",
            },
            "CurveName": {
                "description": "The built-in curve implementations.",
                "enum": ["basis", "basis-closed", "basis-open"],
                "type": "string",
            },
        },
    }
    ```

    By default, `schema` will be simplified using the `"outer"` name (`"Curve"`)
    and the `"longest"` description (`"CurveName"`)

    ```py
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "definitions": {
            "Curve": {
                "description": "How to interpolate between control points.",
                "enum": ["basis", "basis-closed", "basis-open"],
                "type": "string",
            }
        },
    }
    ```
    """

    name: UnwrapPolicy = "outer"
    description: UnwrapPolicy = "longest"


class Child(base.FrozenStruct, frozen=True, forbid_unknown_fields=True):
    """Match on the contents of a definition's children."""

    nodes: frozenset[MLIRType] = field(default_factory=frozenset[MLIRType])
    """Match on the type of a child node."""
    field_names: frozenset[str] = field(default_factory=frozenset[str])
    """Match on the name of a field.

    **Implies that the parent has fields**.
    """

    def __bool__(self) -> bool:
        return bool(self.nodes or self.field_names)

    def __rich_repr__(self) -> Iterable[base.Entry[typing.Any]]:
        if self.nodes:
            yield "nodes", self.nodes
        if self.field_names:
            yield "field_names", self.field_names


class NamesNodes(base.FrozenStruct, frozen=True, forbid_unknown_fields=True):
    """Match on the name or type of a definition."""

    names: frozenset[DefName] = field(default_factory=frozenset[DefName])
    nodes: frozenset[MLIRType] = field(default_factory=frozenset[MLIRType])

    def __bool__(self) -> bool:
        return bool(self.names or self.nodes)

    def __rich_repr__(self) -> Iterable[base.Entry[typing.Any]]:
        if self.names:
            yield "names", self.names
        if self.nodes:
            yield "nodes", self.nodes


class Filter(base.FrozenStruct, frozen=True, forbid_unknown_fields=True):
    """A specification for matching against a graph.

    Each parameter constrains the search in the priority order of:

    ```
    id -> definition -> child
    ```
    """

    id: frozenset[base.IdName] = field(default_factory=frozenset[base.IdName])
    """Match on the name of a module (`Root.id`)."""
    definition: NamesNodes = field(default_factory=NamesNodes)
    """Match on a named symbol within a module (`Root.definitions`)."""
    child: Child = field(default_factory=Child)
    """Match on an anonymous symbol within a definition."""

    def __bool__(self) -> bool:
        return bool(self.id or self.definition or self.child)

    def __rich_repr__(self) -> Iterable[base.Entry[typing.Any]]:
        if self.id:
            yield "id", self.id
        if self.definition:
            yield "definition", self.definition
        if self.child:
            yield "child", self.child


class _BaseScopes[Over: IterOver](
    base.FrozenStruct, frozen=True, kw_only=True, forbid_unknown_fields=True
):
    """A search space for an `Action`.

    ## Notes
    The algorithm for resolving `include` and `exclude` is *roughly*:

    ```py
    everything = set()
    include = set()
    exclude = set()

    neither = everything
    include_only = everything.intersection(include)
    exclude_only = everything.difference(exclude)
    include_exclude = everything.intersection(include).difference(exclude)
    ```
    """

    include: Filter = field(default_factory=Filter)
    """Require matches to meet these constraints for inclusion.

    By default, the search includes all roots, definitions and their children.
    """
    exclude: Filter = field(default_factory=Filter)
    """Reject candidates that meet these constraints.

    By default, the search does not exclude.
    """
    over: Over
    """The kind of traversal to perform.

    - *"definitions"*: Visit top-level definitions only.
    - *"children"*: Visit the children of top-level definitions.
    - *"descendants"*: Visit top-level definitions, then their children, recursively.
    """

    def __bool__(self) -> bool:
        return bool(self.include or self.exclude)

    def __rich_repr__(self) -> Iterable[base.Entry[typing.Any]]:
        if self.include:
            yield "include", self.include
        if self.exclude:
            yield "exclude", self.exclude
        yield "over", self.over


@final
class ChildrenScope(
    _BaseScopes[L["children"]], frozen=True, kw_only=True, forbid_unknown_fields=True
):
    over: L["children"] = "children"


@final
class DefsScope(
    _BaseScopes[L["definitions"]], frozen=True, kw_only=True, forbid_unknown_fields=True
):
    over: L["definitions"] = "definitions"


@final
class DefsDescendantsScope(
    _BaseScopes[L["definitions", "descendants"]],
    frozen=True,
    kw_only=True,
    forbid_unknown_fields=True,
):
    over: L["definitions", "descendants"] = "definitions"
    ref_follow_depth: Depth = 0
    """Resolve references to a maximum of this depth, before stopping a search.

    By default, refs are left unresolved.
    Each increment above will continue the search if `<current>.ref` leads to another ref when iterating *the ref's children*.
    This model chooses not to support an "unbounded" search.
    """

    def __bool__(self) -> bool:
        return bool(self.ref_follow_depth or self.include or self.exclude)

    def __rich_repr__(self) -> Iterable[base.Entry[typing.Any]]:
        yield from super().__rich_repr__()
        if self.ref_follow_depth:
            yield "ref_follow_depth", self.ref_follow_depth


class PluginScope(_BaseScopes[IterOver], frozen=True, kw_only=True, forbid_unknown_fields=True):
    over: IterOver = "definitions"
    ref_follow_depth: Depth = 0


class _BaseAction[Over: IterOver](
    base.FrozenStruct,
    frozen=True,
    kw_only=True,
    tag=True,
    tag_field="action",
    forbid_unknown_fields=True,
):
    """Combines a search space (`scope`) and what to do with it (`action`, ...)."""

    scope: _BaseScopes[Over]


@final
class AsDefsAction(
    _BaseAction[L["children"]],
    frozen=True,
    kw_only=True,
    tag="as-defs",
    tag_field="action",
    forbid_unknown_fields=True,
):
    """Lift one or more anonymous types, within a union, into new definitions."""

    scope: ChildrenScope = field(default_factory=ChildrenScope)


@final
class AsDefsFieldAction(
    _BaseAction[L["children"]],
    frozen=True,
    kw_only=True,
    tag="as-defs-field",
    tag_field="action",
    forbid_unknown_fields=True,
):
    """Lift unrepresentable anonymous types from field(s) into definitions.

    Target fields can be selected via `scope.include.child.field_names`.
    """

    scope: ChildrenScope = field(default_factory=ChildrenScope)


@final
class NewTreeAction(
    _BaseAction[L["definitions", "descendants"]],
    frozen=True,
    kw_only=True,
    tag="new-tree",
    tag_field="action",
    forbid_unknown_fields=True,
):
    """Derive a new `Root` from another, taking ownership of related definitions.

    This action could be considered taking a cutting from a tree and "re-planting" it.

    ## Notes
    - differs by not requiring 1 `root_name: DefName`, since multiple definitions can match
    - creates a new `mlir.Root` per-action
    """

    scope: DefsDescendantsScope = field(default_factory=DefsDescendantsScope)
    id: base.IdName
    """The name of the new `Root`."""

    into_ext_ref: Mapping[DefName, base.IdName] = field(default_factory=dict)
    """If this operation would leave "dangling" references, resolve them using this mapping.

    This option should be reserved for *acknowledging* cyclic definitions.
    """


@final
class RemoveAction(
    _BaseAction[L["definitions"]],
    frozen=True,
    kw_only=True,
    tag="remove",
    tag_field="action",
    forbid_unknown_fields=True,
):
    """Remove matching definitions, without replacement."""

    scope: DefsScope = field(default_factory=DefsScope)


@final
class RenameFieldsAction(
    _BaseAction[L["definitions"]],
    frozen=True,
    kw_only=True,
    tag="rename-fields",
    tag_field="action",
    forbid_unknown_fields=True,
):
    """Rename fields that match a name provided in `overrides`."""

    scope: DefsScope = field(default_factory=DefsScope)
    overrides: Mapping[str, str]
    """A mapping from old name to new name."""


class PluginAction(
    _BaseAction[IterOver],
    frozen=True,
    kw_only=True,
    tag="plugin",
    tag_field="action",
    forbid_unknown_fields=True,
):
    """You're on your own, jim."""

    scope: PluginScope = field(default_factory=PluginScope)
    entry_point: A[str, msgspec.Meta(pattern=ENTRY_POINT_PATTERN["json"])]
    """The path to the plugin definition.

    Uses a pattern adapted from [entry-points], restricted to the following forms:

    ```py
    "package.module:attribute"
    "package.module:object.attribute"
    ```

    [entry-points]: https://packaging.python.org/en/latest/specifications/entry-points/
    """
    extra: A[
        Mapping[str, typing.Any], msgspec.Meta(extra_json_schema={"additionalProperties": True})
    ] = field(default_factory=dict)
    """Namespace for arbitrary data passed to the plugin."""


type ActionKind = L["as-defs", "as-defs-field", "rename-fields", "new-tree", "remove", "plugin"]
type Action = (
    AsDefsAction
    | AsDefsFieldAction
    | NewTreeAction
    | RemoveAction
    | RenameFieldsAction
    | PluginAction
)
type Scopes = ChildrenScope | DefsScope | DefsDescendantsScope | PluginScope

_ACTION_KIND: typing.Final[tuple[ActionKind, ...]] = typing.get_args(ActionKind.__value__)


class JsonWrapperToMLIR(base.FrozenStruct, frozen=True, forbid_unknown_fields=True):
    """Configure converting from json schema.

    Represents the first conversion stage.
    """

    ref_unwrap: Mapping[DefName, ReferenceUnwrap] = field(default_factory=dict)
    """Mapping from the outer ("$ref"-defining) definition name to a policy table."""

    actions: Sequence[Action] = field(default_factory=list[Action])

    @property
    def ref_unwrap_default(self) -> ReferenceUnwrap:
        return ReferenceUnwrap()


class SourceConfig(base.FrozenStruct, frozen=True, forbid_unknown_fields=True):
    """A schema source for conversion."""

    path: Path
    """A relative path to the schema, resolved against the location of `mosaic-spec.toml`."""
    id: base.IdName
    """A unique identifier for the loaded result.

    In the final representation, `id` is used for the name of a python module.
    """


class ConvertConfig(base.FrozenStruct, frozen=True, forbid_unknown_fields=True):
    """Top-level config for translation/codegen."""

    sources: Sequence[SourceConfig] = field(default_factory=list[SourceConfig])
    to_mlir: JsonWrapperToMLIR = field(default_factory=JsonWrapperToMLIR)


@final
class MosaicSpecToml(base.FrozenStruct, frozen=True, forbid_unknown_fields=True):
    """Top-level config for everything!"""

    convert: ConvertConfig = field(default_factory=ConvertConfig)
