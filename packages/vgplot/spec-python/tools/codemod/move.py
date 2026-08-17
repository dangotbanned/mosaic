from __future__ import annotations

import ast
from collections import deque
from itertools import chain
from typing import TYPE_CHECKING

from tools import fs
from tools.codemod.common import parse_module

if TYPE_CHECKING:
    from pathlib import Path

type Positions = tuple[int, int]


def _get_linenos(node: ast.ClassDef) -> Positions:
    if node.end_lineno is None:
        msg = f"Missing `end_lineno` for {node!r}"
        raise NotImplementedError(msg)
    return (node.lineno - 1, node.end_lineno)


def move_class_defs_to_top(target: Path, *class_names: str) -> None:
    """Rewrite `target` with `class_names` moved to the start of the file.

    The order provided by `class_names` is significant.

    ## Notes
    - Multiple hacks, stacked on top of eachother
    - Gave up on trying to fix this is a reasonable way
        - `MarkOptions` gets defined almost at the bottom of the module
        - it depends on lots of symbols defined in `marks.py`,
          so I don't want to move it to another module just to work around `dcg`
    - ast is enough to find things
        - but it transforms attribute "docstrings" into regular strings
        - so using unparse would be destructive
    - so use the line numbers and then manipulate the lines
    """
    module = parse_module(target)
    original_start = next(node.lineno - 1 for node in module.body if isinstance(node, ast.ClassDef))
    found_positions: dict[str, Positions] = dict.fromkeys(class_names, (0, 0))
    todo = set(class_names)
    for node in reversed(module.body):
        if not todo:
            break
        if isinstance(node, ast.ClassDef) and node.name in todo:
            found_positions[node.name] = _get_linenos(node)
            todo.remove(node.name)

    lines = target.read_text("utf8").splitlines()

    if len(found_positions) == 1:
        start, end = found_positions[class_names[0]]
        lines_reordered = chain(
            lines[:original_start], lines[start:end], lines[original_start:start], lines[end:]
        )
    else:
        # NOTE: surprised this actually worked
        lines_reordered = deque[str]()
        for start, end in sorted(found_positions.values(), reverse=True):
            lines_reordered.extend(lines[start:end].copy())
            del lines[start:end]
        lines_reordered.extendleft(reversed(lines[:original_start]))
        lines_reordered.extend(lines[original_start:])

    fs.write_lines(target, lines_reordered, f"Moved {class_names!r} to top")
