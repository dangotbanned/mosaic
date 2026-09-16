"""Mid-level IR, representing something that's not quite JSON or Python.

- Not a full transition to python yet
    - But nodes are not allowed to keep a `schema` field
    - Anything useful must have been peeled off
- Missing things like
    - TypeVar/parameters
    - Type qualifiers
    - Type alias
    - Special forms (well some of them at least)
    - Generics
- Not 100% sure what to call this yet.

---

<!--TODO @dangotbanned: Merge above and below into a narrative--->

### Stage 2

- Package: [`tools.ir.mlir`][]
- Root: `mlir.Root`
- Definition: `mlir.Definition`
- Nodes: `mlir.MLIR`, 20 implementations

#### Open issues

- `ref_unwrap` mutates "Stage 1" to create "Stage 2"
"""

from __future__ import annotations

from tools.ir.mlir import actions, nodes
from tools.ir.mlir.actions import Action, Plugin, RootsMut, actions_plugin
from tools.ir.mlir.common import inner_type_is
from tools.ir.mlir.definition import Definition
from tools.ir.mlir.nodes import MLIR
from tools.ir.mlir.root import Root

__all__ = (
    "MLIR",
    "Action",
    "Definition",
    "Plugin",
    "Root",
    "RootsMut",
    "actions",
    "actions_plugin",
    "inner_type_is",
    "nodes",
)
