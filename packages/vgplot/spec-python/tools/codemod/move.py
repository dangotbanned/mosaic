from __future__ import annotations

import ast
from itertools import chain
from typing import TYPE_CHECKING

from tools import fs
from tools.codemod.common import parse_module

if TYPE_CHECKING:
    from pathlib import Path


def move_class_to_top(target: Path, class_name: str) -> None:
    """Multiple hacks, stacked on top of eachother.

    ## Notes
    - Giving up on trying to fix this is a reasonable way
        - `MarkOptions` gets defined almost at the bottom of the module
        - it depends on lots of symbols defined in `marks.py`,
          so I don't want to move it to another module just to work around `dcg`
    - ast is enough to find things
        - but it transforms attribute "docstrings" into regular strings
        - so using unparse would be destructive
    - so use the line numbers and then manipulate the lines
    """
    module = parse_module(target)
    start, end = 0, 0

    for node in reversed(module.body):
        if isinstance(node, ast.ClassDef) and node.name == class_name:
            start = node.lineno - 1
            if node.end_lineno is None:
                raise NotImplementedError
            end = node.end_lineno
            break

    move_to = next(node.lineno - 1 for node in module.body if isinstance(node, ast.ClassDef))
    lines = target.read_text("utf8").splitlines()
    lines_reordered = chain(lines[:move_to], lines[start:end], lines[move_to:start], lines[end:])
    fs.write_lines(target, lines_reordered, f"Moved {class_name} to top")
