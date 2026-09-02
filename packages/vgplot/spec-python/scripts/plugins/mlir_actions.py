from __future__ import annotations

from typing import TYPE_CHECKING

from tools.ir import mlir

if TYPE_CHECKING:
    from collections.abc import Iterator


@mlir.actions_plugin
def fix_tip(action: mlir.Plugin, roots: mlir.RootsMut) -> Iterator[mlir.Root]:
    print(f"Landed in {action.entry_point!r}")
    matcher = action.matcher
    for root in roots:
        if matcher.matches_root(root):
            # do something with root ...
            ...
        yield root
