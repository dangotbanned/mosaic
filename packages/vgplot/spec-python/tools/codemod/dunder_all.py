from __future__ import annotations

import ast
import dataclasses
from typing import TYPE_CHECKING

from tools import fs
from tools.codemod.common import parse_module

if TYPE_CHECKING:
    from pathlib import Path


@dataclasses.dataclass(slots=True, frozen=True)
class AssignAll:
    node: ast.Assign

    def to_str(self) -> str:
        return ast.unparse(self.node.value).strip("[]").replace("'", "")

    @staticmethod
    def try_from_module(module: ast.Module) -> AssignAll | None:
        for node in reversed(module.body):
            match node:
                case ast.Assign([ast.Name("__all__")]):
                    return AssignAll(node)
                case _:
                    continue
        return None


def find(source: str | Path) -> AssignAll:
    """Return the node which makes the `__all__` assignment in `source`."""
    module = parse_module(source)
    if found := AssignAll.try_from_module(module):
        return found
    msg = (
        f"Unable to find an `__all__` in {fs.repo_relative_str(source)!r}, got:\n\n"
        f"```py\n{ast.unparse(module)}\n```"
    )
    raise AttributeError(msg)
