from typing import Literal as L, final

from msgspec import field

from tools.common import RichRepr
from tools.config.selectors import Filter
from tools.config.typing import Depth, IterOver
from tools.models.base import FrozenStruct


class _BaseScopes[Over: IterOver](
    FrozenStruct, frozen=True, kw_only=True, forbid_unknown_fields=True
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

    def __rich_repr__(self) -> RichRepr:
        if self.include:
            yield "include", self.include
        if self.exclude:
            yield "exclude", self.exclude
        yield "over", self.over


@final
class Children(_BaseScopes[L["children"]], frozen=True, kw_only=True, forbid_unknown_fields=True):
    over: L["children"] = "children"


@final
class Defs(_BaseScopes[L["definitions"]], frozen=True, kw_only=True, forbid_unknown_fields=True):
    over: L["definitions"] = "definitions"


@final
class DefsDescendants(
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

    def __rich_repr__(self) -> RichRepr:
        yield from super().__rich_repr__()
        if self.ref_follow_depth:
            yield "ref_follow_depth", self.ref_follow_depth


@final
class Plugin(_BaseScopes[IterOver], frozen=True, kw_only=True, forbid_unknown_fields=True):
    over: IterOver = "definitions"
    ref_follow_depth: Depth = 0


type Scopes = Children | Defs | DefsDescendants | Plugin
