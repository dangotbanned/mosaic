import collections.abc as cabc
import typing as t
from typing import Annotated as A, Literal as L, final

import msgspec
from msgspec import field

from tools.config import scopes
from tools.config.typing import ENTRY_POINT_PATTERN, IterOver
from tools.ident import kebab_case
from tools.models.base import DefName, FrozenStruct, IdName


class _Base[Over: IterOver](
    FrozenStruct,
    frozen=True,
    kw_only=True,
    tag=kebab_case,
    tag_field="action",
    forbid_unknown_fields=True,
):
    """Combines a search space (`scope`) and what to do with it (`action`, ...)."""

    scope: scopes._BaseScopes[Over]


@final
class AsDefs(_Base[L["children"]], frozen=True, kw_only=True, forbid_unknown_fields=True):
    """Lift one or more anonymous types, within a union, into new definitions."""

    scope: scopes.Children = field(default_factory=scopes.Children)
    discriminator: str = ""
    """The name of a discriminator field, if this action targets a [discriminated union][1].

    Each member will be named based on the single literal type allowed for this field.

    [1]: https://www.typescriptlang.org/docs/handbook/2/narrowing.html#discriminated-unions
    """


@final
class AsDefsField(_Base[L["children"]], frozen=True, kw_only=True, forbid_unknown_fields=True):
    """Lift unrepresentable anonymous types from field(s) into definitions.

    Target fields can be selected via `scope.include.child.field_names`.
    """

    scope: scopes.Children = field(default_factory=scopes.Children)


@final
class NewTree(
    _Base[L["definitions", "descendants"]], frozen=True, kw_only=True, forbid_unknown_fields=True
):
    """Derive a new `Root` from another, taking ownership of related definitions.

    This action could be considered taking a cutting from a tree and "re-planting" it.

    ## Notes
    - differs by not requiring 1 `root_name: DefName`, since multiple definitions can match
    - creates a new `mlir.Root` per-action
    """

    scope: scopes.DefsDescendants = field(default_factory=scopes.DefsDescendants)
    id: IdName
    """The name of the new `Root`."""

    into_ext_ref: cabc.Mapping[DefName, IdName] = field(default_factory=dict)
    """If this operation would leave "dangling" references, resolve them using this mapping.

    This option should be reserved for *acknowledging* cyclic definitions.
    """


@final
class Remove(_Base[L["definitions"]], frozen=True, kw_only=True, forbid_unknown_fields=True):
    """Remove matching definitions, without replacement."""

    scope: scopes.Defs = field(default_factory=scopes.Defs)
    # NOTE: Option is a possible candidate for a plugin
    preserve_children: bool = False
    """If the target definition is a union, substitute references to it with refs to the children."""


@final
class RenameFields(_Base[L["definitions"]], frozen=True, kw_only=True, forbid_unknown_fields=True):
    """Rename fields that match a name provided in `overrides`."""

    scope: scopes.Defs = field(default_factory=scopes.Defs)
    overrides: cabc.Mapping[str, str]
    """A mapping from old name to new name."""


@final
class Plugin(_Base[IterOver], frozen=True, kw_only=True, forbid_unknown_fields=True):
    """You're on your own, jim."""

    scope: scopes.Plugin = field(default_factory=scopes.Plugin)
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


type Action = AsDefs | AsDefsField | NewTree | Remove | RenameFields | Plugin
