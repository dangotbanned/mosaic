from __future__ import annotations

import ast
import copy
import dataclasses
from typing import TYPE_CHECKING

from tools import fs
from tools.codemod.common import parse_module

if TYPE_CHECKING:
    from pathlib import Path


@dataclasses.dataclass(slots=True, frozen=True)
class AssignAll:
    node: ast.Assign

    def unparse_value(self) -> str:
        return ast.unparse(self.node.value)

    @staticmethod
    def try_from_module(module: ast.Module) -> AssignAll | None:
        for node in reversed(module.body):
            match node:
                case ast.Assign([ast.Name("__all__")]):
                    return AssignAll(_replace_list_with_tuple(node))
                case _:
                    continue
        return None


def find(source: Path) -> AssignAll:
    """Return the node which makes the `__all__` assignment in `source`."""
    module = parse_module(source)
    if found := AssignAll.try_from_module(module):
        return found
    msg = (
        f"Unable to find an `__all__` in {fs.repo_relative_str(source)!r}, got:\n\n"
        f"```py\n{ast.unparse(module)}\n```"
    )
    raise AttributeError(msg)


def _replace_list_with_tuple(node: ast.Assign) -> ast.Assign:
    # Simpler than version branching (https://github.com/python/typeshed/blob/4b150aed0c3df75d0b3bff63a167d3c666eacb3a/stdlib/ast.pyi#L1179-L1202)
    # Idea stolen from:
    # - https://github.com/python/cpython/blob/3972524c3f28ce03a456410709507092310ff281/Lib/annotationlib.py#L696
    # - https://github.com/python/cpython/blob/3972524c3f28ce03a456410709507092310ff281/Lib/annotationlib.py#L86-L87
    clone = copy.deepcopy(node)
    clone.value.__class__ = ast.Tuple
    return clone
