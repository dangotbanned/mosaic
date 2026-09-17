"""Mid-level IR, representing something that's not quite JSON or Python.

## Compared to previous stage

[`tools.ir.json_wrapper`][] retains access to the original schema; whereas here we must peel off
anything that's useful to continue.
While we do that, we crank up the specificity of nodes:

- 11x `JsonWrapper`
- 20x `MLIR`

## Notes

These types begin to look more like python, but permit definitions that the next stage would reject.
This is fine, because we introduce [`actions`][tools.ir.mlir.actions] to smooth out the rough edges.

## Open issues

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
