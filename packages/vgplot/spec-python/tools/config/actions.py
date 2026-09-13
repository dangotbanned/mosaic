import collections.abc as cabc
import typing as t
from typing import Annotated as A, Literal as L, final

import msgspec
from msgspec import field

from tools.config.scopes import (
    ChildrenScope,
    DefsDescendantsScope,
    DefsScope,
    PluginScope,
    _BaseScopes,
)
from tools.config.typing import ENTRY_POINT_PATTERN, IterOver
from tools.models.base import DefName, FrozenStruct, IdName


class _Base[Over: IterOver](
    FrozenStruct,
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
    _Base[L["children"]],
    frozen=True,
    kw_only=True,
    tag="as-defs",
    tag_field="action",
    forbid_unknown_fields=True,
):
    """Lift one or more anonymous types, within a union, into new definitions."""

    scope: ChildrenScope = field(default_factory=ChildrenScope)
    discriminator: str = ""
    """The name of a discriminator field, if this action targets a [discriminated union][1].

    Each member will be named based on the single literal type allowed for this field.

    [1]: https://www.typescriptlang.org/docs/handbook/2/narrowing.html#discriminated-unions
    """


@final
class AsDefsFieldAction(
    _Base[L["children"]],
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
    _Base[L["definitions", "descendants"]],
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
    id: IdName
    """The name of the new `Root`."""

    into_ext_ref: cabc.Mapping[DefName, IdName] = field(default_factory=dict)
    """If this operation would leave "dangling" references, resolve them using this mapping.

    This option should be reserved for *acknowledging* cyclic definitions.
    """


@final
class RemoveAction(
    _Base[L["definitions"]],
    frozen=True,
    kw_only=True,
    tag="remove",
    tag_field="action",
    forbid_unknown_fields=True,
):
    """Remove matching definitions, without replacement."""

    scope: DefsScope = field(default_factory=DefsScope)
    # NOTE: Option is a possible candidate for a plugin
    preserve_children: bool = False
    """If the target definition is a union, substitute references to it with refs to the children."""


@final
class RenameFieldsAction(
    _Base[L["definitions"]],
    frozen=True,
    kw_only=True,
    tag="rename-fields",
    tag_field="action",
    forbid_unknown_fields=True,
):
    """Rename fields that match a name provided in `overrides`."""

    scope: DefsScope = field(default_factory=DefsScope)
    overrides: cabc.Mapping[str, str]
    """A mapping from old name to new name."""


@final
class PluginAction(
    _Base[IterOver],
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
        cabc.Mapping[str, t.Any], msgspec.Meta(extra_json_schema={"additionalProperties": True})
    ] = field(default_factory=dict)
    """Namespace for arbitrary data passed to the plugin."""


type Action = (
    AsDefsAction
    | AsDefsFieldAction
    | NewTreeAction
    | RemoveAction
    | RenameFieldsAction
    | PluginAction
)
