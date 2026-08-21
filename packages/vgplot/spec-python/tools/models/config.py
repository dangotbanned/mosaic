"""Configuration via toml."""

import typing
from collections.abc import Mapping, Sequence
from typing import Literal as L, final

import msgspec
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


class InclExcl[T](base.FrozenStruct, frozen=True, forbid_unknown_fields=True):
    """Define `include`/`exclude` filters to match a target."""

    include: frozenset[T] | msgspec.UnsetType = msgspec.UNSET
    exclude: frozenset[T] = field(default_factory=frozenset[T])

    def __bool__(self) -> bool:
        return bool(self.include or self.exclude)


class ParentScope(base.FrozenStruct, frozen=True, kw_only=True, forbid_unknown_fields=True):
    """Limit the search from the full graph.

    This scope filters the `definitions` table, where each entry is considered a *parent*.

    Args:
        definition: Match on the keys of `Root.definitions`.
        node: Match of the type of an entry in `Root.definitions`.
            Has a lower priority than `definition`.
    """

    definition: InclExcl[DefName] = field(default_factory=InclExcl[DefName])
    node: InclExcl[MLIRType] = field(default_factory=InclExcl[MLIRType])

    def __bool__(self) -> bool:
        return bool(self.definition or self.node)


class RefScope(InclExcl[DefName], frozen=True, forbid_unknown_fields=True):
    """What to do when we encounter a `ref`.

    Args:
        follow_depth: Resolve references to a maximum of this depth, before stopping a search.
            By default, refs are left unresolved.
            Each increment above will continue the search if `<current>.ref` leads to another ref when iterating *the ref's children*.
            This model chooses not to support an "unbounded" search.
        include: _description_
        exclude: _description_
    """

    follow_depth: L[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] = 0

    def __bool__(self) -> bool:
        return bool(self.follow_depth or super().__bool__())


class ChildScope(base.FrozenStruct, frozen=True, kw_only=True, forbid_unknown_fields=True):
    """Limit the search from the full graph, after matching on a parent.

    Args:
        node: Match on the type of a definition's children.
        ref: Match on references and decide how deep to resolve them.
    """

    node: InclExcl[MLIRType] = field(default_factory=InclExcl[MLIRType])
    ref: RefScope = field(default_factory=RefScope)
    descend: bool = False  # WIP, basically want a switch for "children means descendants"

    def __bool__(self) -> bool:
        return bool(self.descend or self.node or self.ref)


class Scopes(base.FrozenStruct, frozen=True, kw_only=True, forbid_unknown_fields=True):
    """A search space for an `Action`.

    Args:
        id: Match on `Root.id`.
        parent: Match on `Root.definitions`.
        children: Match on the children of `definitions`.
    """

    id: InclExcl[IdName] = field(default_factory=InclExcl[IdName])
    parent: ParentScope = field(default_factory=ParentScope)
    children: ChildScope = field(default_factory=ChildScope)

    def __bool__(self) -> bool:
        return bool(self.id or self.parent or self.children)


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


class ConvertConfig(base.FrozenStruct, frozen=True, forbid_unknown_fields=True):
    """Top-level config for translation/codegen."""

    to_mlir: JsonWrapperToMLIR = field(default_factory=JsonWrapperToMLIR)


@final
class MosaicSpecToml(base.FrozenStruct, frozen=True, forbid_unknown_fields=True):
    """Top-level config for everything!"""

    convert: ConvertConfig = field(default_factory=ConvertConfig)

    @classmethod
    def discover_config(cls) -> MosaicSpecToml:
        from tools import fs, serde

        return serde.read_toml(fs.MOSAIC_SPEC_TOML, cls)
