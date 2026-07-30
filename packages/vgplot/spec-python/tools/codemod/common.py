from __future__ import annotations

import ast
from pathlib import Path
from typing import NewType

from tools import fs

DottedName = NewType("DottedName", str)


def parse_module(source: Path) -> ast.Module:
    return ast.parse(Path(source).read_bytes())


def module_name(path: Path, /) -> DottedName:
    """Return the [absolute name][1] of the module at `path`.

    [1]: https://docs.python.org/3/reference/simple_stmts.html#the-import-statement
    """
    relative = path.relative_to(fs.SRC)
    if relative.name == "__init__.py":
        relative = relative.parent
    return DottedName(relative.as_posix().replace("/", "."))
