from msgspec import field

from tools.common import RichRepr
from tools.config.typing import MLIRType
from tools.models.base import DefName, FrozenStruct, IdName


class Child(FrozenStruct, frozen=True, forbid_unknown_fields=True):
    """Match on the contents of a definition's children."""

    nodes: frozenset[MLIRType] = field(default_factory=frozenset[MLIRType])
    """Match on the type of a child node."""
    field_names: frozenset[str] = field(default_factory=frozenset[str])
    """Match on the name of a field.

    **Implies that the parent has fields**.
    """

    def __bool__(self) -> bool:
        return bool(self.nodes or self.field_names)

    def __rich_repr__(self) -> RichRepr:
        if self.nodes:
            yield "nodes", self.nodes
        if self.field_names:
            yield "field_names", self.field_names


class NamesNodes(FrozenStruct, frozen=True, forbid_unknown_fields=True):
    """Match on the name or type of a definition."""

    names: frozenset[DefName] = field(default_factory=frozenset[DefName])
    nodes: frozenset[MLIRType] = field(default_factory=frozenset[MLIRType])

    def __bool__(self) -> bool:
        return bool(self.names or self.nodes)

    def __rich_repr__(self) -> RichRepr:
        if self.names:
            yield "names", self.names
        if self.nodes:
            yield "nodes", self.nodes


class Filter(FrozenStruct, frozen=True, forbid_unknown_fields=True):
    """A specification for matching against a graph.

    Each parameter constrains the search in the priority order of:

    ```
    id -> definition -> child
    ```
    """

    id: frozenset[IdName] = field(default_factory=frozenset[IdName])
    """Match on the name of a module (`Root.id`)."""
    definition: NamesNodes = field(default_factory=NamesNodes)
    """Match on a named symbol within a module (`Root.definitions`)."""
    child: Child = field(default_factory=Child)
    """Match on an anonymous symbol within a definition."""

    def __bool__(self) -> bool:
        return bool(self.id or self.definition or self.child)

    def __rich_repr__(self) -> RichRepr:
        if self.id:
            yield "id", self.id
        if self.definition:
            yield "definition", self.definition
        if self.child:
            yield "child", self.child
