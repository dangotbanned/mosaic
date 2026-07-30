from __future__ import annotations

import ast
from pathlib import Path

from tools import fs


def parse_module(source: str | Path) -> ast.Module:
    return ast.parse(Path(source).read_bytes())


def dotted_module_name(path: Path, /) -> str:
    """Return the [absolute name][1] of the module at `path`.

    [1]: https://docs.python.org/3/reference/simple_stmts.html#the-import-statement
    """
    relative = path.relative_to(fs.SRC)
    if relative.name == "__init__.py":
        relative = relative.parent
    return relative.as_posix().replace("/", ".")
