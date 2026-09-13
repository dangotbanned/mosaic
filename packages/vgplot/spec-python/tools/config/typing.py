from __future__ import annotations

import typing as t
from typing import Literal as L

if t.TYPE_CHECKING:
    import collections.abc as cabc

type MLIRType = L[
    "ClosedDict",
    "EmptyTuple",
    "ExtReference",
    "ExtraDict",
    "Field",
    "HomogeneousTuple",
    "Literal",
    "Mapping",
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
type ActionKind = L["as-defs", "as-defs-field", "rename-fields", "new-tree", "remove", "plugin"]

MLIR_TYPES: t.Final[frozenset[MLIRType]] = frozenset(t.get_args(MLIRType.__value__))
ACTION_KIND: t.Final[tuple[ActionKind, ...]] = t.get_args(ActionKind.__value__)
ENTRY_POINT_PATTERN: t.Final[cabc.Mapping[L["json", "python"], t.LiteralString]] = {
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
OPEN_DICT_BASE_PATTERN: t.Final = r"^([a-zA-Z_]+[a-zA-Z_0-9]*?)?\{name\}([a-zA-Z_0-9]*)?$"
"""Regex pattern for `OpenDict.format`."""
