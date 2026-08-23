"""Configuration via toml."""

import typing
from collections.abc import Iterable, Mapping, Sequence
from pathlib import Path
from typing import Literal as L, final

from msgspec import field

from tools.models import base

type IdName = str
"""The unique name for a `Root`."""

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

type Todo = typing.Any
"""Defining this type requires a refactor to prevent forward refs.

Doing that is a good idea, so this marker is a reminder.
"""

type UnwrapPolicy = L["longest", "shortest", "inner", "outer"]
type DefName = str
type Depth = L[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


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


class Nodes(base.FrozenStruct, frozen=True, kw_only=True, forbid_unknown_fields=True):
    """Match on the type of a node."""

    nodes: frozenset[MLIRType] = field(default_factory=frozenset[MLIRType])

    def __bool__(self) -> bool:
        return bool(self.nodes)


class Names(base.FrozenStruct, frozen=True, kw_only=True, forbid_unknown_fields=True):
    """Match on the name of a definition."""

    names: frozenset[DefName] = field(default_factory=frozenset[DefName])

    def __bool__(self) -> bool:
        return bool(self.names)


class NamesNodes(base.FrozenStruct, frozen=True, kw_only=True, forbid_unknown_fields=True):
    """Match on the name or type of a definition."""

    names: frozenset[DefName] = field(default_factory=frozenset[DefName])
    nodes: frozenset[MLIRType] = field(default_factory=frozenset[MLIRType])

    def __bool__(self) -> bool:
        return bool(self.names or self.nodes)


class Filter(base.FrozenStruct, frozen=True, kw_only=True, forbid_unknown_fields=True):
    """A specification for matching against a graph.

    Each parameter constrains the search in the priority order of:

    ```
    id -> definition -> child -> ref
    ```

    Args:
        id: Match on the name of a module (`Root.id`).
        definition: Match on a named symbol within a module (`Root.definitions`).
        child: Match on an anonymous symbol within a definition.
        ref: Match on the subset of `child`, which is a reference to named definition.
    """

    id: frozenset[IdName] = field(default_factory=frozenset[IdName])
    definition: NamesNodes = field(default_factory=NamesNodes)
    child: Nodes = field(default_factory=Nodes)
    ref: Names = field(default_factory=Names)

    def __bool__(self) -> bool:
        return bool(self.id or self.definition or self.child or self.ref)

    def __rich_repr__(self) -> Iterable[base.Entry[typing.Any]]:
        if self.id:
            yield "id", self.id
        if self.definition:
            yield "definition", self.definition
        if self.child:
            yield "child", self.child
        if self.ref:
            yield "ref", self.ref


class Scopes(base.FrozenStruct, frozen=True, kw_only=True, forbid_unknown_fields=True):
    """A search space for an `Action`.

    Args:
        include: Require matches to meet these constraints for inclusion.
            By default, the search includes all roots, definitions and their children.
        exclude: Reject candidates that meet these constraints.
            By default, the search does not exclude.
        descend: _todo_description_
        ref_follow_depth: Resolve references to a maximum of this depth, before stopping a search.
            By default, refs are left unresolved.
            Each increment above will continue the search if `<current>.ref` leads to another ref when iterating *the ref's children*.
            This model chooses not to support an "unbounded" search.

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
    exclude: Filter = field(default_factory=Filter)
    descend: bool = False  # WIP, basically want a switch for "children means descendants"
    ref_follow_depth: Depth = 0

    def __bool__(self) -> bool:
        return bool(self.descend or self.ref_follow_depth or self.include or self.exclude)

    def __rich_repr__(self) -> Iterable[base.Entry[typing.Any]]:
        if self.include:
            yield "include", self.include
        if self.exclude:
            yield "exclude", self.exclude
        if self.descend:
            yield "descend", self.descend
        if self.ref_follow_depth:
            yield "ref_follow_depth", self.ref_follow_depth


class _BaseAction(
    base.FrozenStruct,
    frozen=True,
    kw_only=True,
    tag=True,
    tag_field="action",
    forbid_unknown_fields=True,
):
    """Combines a search space (`scope`) and what to do with it (`action`, ...)."""

    scope: Scopes = field(default_factory=Scopes)


@final
class AsRefAction(
    _BaseAction,
    frozen=True,
    kw_only=True,
    tag="as-ref",
    tag_field="action",
    forbid_unknown_fields=True,
):
    """Replace all anonymous matches with a reference to this new definition.

    Aiming to do the heavy lifting for de-duplicating anonymous unions.
    """

    name: DefName
    """The name of the new definition."""
    type: Todo
    """The new definition itself.

    Will appear as a new entry in `definitions`.
    """
    match_doc: bool = False
    """Require `type.doc == candidate.doc` for a successful match.

    By default, action can define a new `doc` and match anonymous types which never had one.

    However, `True` may make sense when a `doc` exists due to obfuscation
    (e.g. `--expose=export` in [ts-json-schema-generator][1]).

    [1]: https://github.com/vega/ts-json-schema-generator#options
    """


@final
class NewTreeAction(
    _BaseAction,
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

    id: IdName  # (currently) the stem of filename
    """The name of the new `Root`."""


type Action = AsRefAction | NewTreeAction


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
    """A schema source for conversion.

    Args:
        path: A relative path to the schema, resolved against the location of `mosaic-spec.toml`.
        id: A unique identifier for the loaded result.
    """

    path: Path
    id: IdName


class ConvertConfig(base.FrozenStruct, frozen=True, forbid_unknown_fields=True):
    """Top-level config for translation/codegen."""

    sources: Sequence[SourceConfig] = field(default_factory=list[SourceConfig])
    to_mlir: JsonWrapperToMLIR = field(default_factory=JsonWrapperToMLIR)


@final
class MosaicSpecToml(base.FrozenStruct, frozen=True, forbid_unknown_fields=True):
    """Top-level config for everything!"""

    convert: ConvertConfig = field(default_factory=ConvertConfig)
