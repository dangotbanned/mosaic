# /// script
# requires-python = ">=3.12"
# ///

"""Fix issues in generated code.

Ideally this would not be needed, but codemod is quicker than requesting a feature (for now).
"""

from __future__ import annotations

import ast
import dataclasses
from pathlib import Path

# TODO @dangotbanned: Unbreak path for `../*.ipynb`
try:
    import fs
except ModuleNotFoundError:
    from scripts import fs


@dataclasses.dataclass(slots=True, frozen=True)
class AssignAll:
    node: ast.Assign

    def to_list(self) -> list[str]:
        return self.to_str().split(", ")

    def to_str(self) -> str:
        return ast.unparse(self.node.value).strip("[]").replace("'", "")


def parse_module(source: str | Path) -> ast.Module:
    return ast.parse(Path(source).read_bytes())


def find_dunder_all(source: str | Path) -> AssignAll:
    module = parse_module(source)
    if found := _find_dunder_all(module):
        return found
    msg = (
        f"Unable to find an `__all__` in {fs.repo_relative_str(source)!r}, got:\n\n"
        f"```py\n{ast.unparse(module)}\n```"
    )
    raise AttributeError(msg)


def _find_dunder_all(module: ast.Module) -> AssignAll | None:
    for node in reversed(module.body):
        match node:
            case ast.Assign([ast.Name("__all__")]):
                return AssignAll(node)
            case _:
                continue
    return None


def steal_child_dunder_all(source: Path, target: Path) -> None:
    """Duplicate a child module's `__all__` in-place of a parent.

    This API isn't the goal, but it works for now.

    ## What's missing?
    - [ ] Be more selective about what we re-export
    - [ ] Be more surgical than overwriting an entire file
        - [ ] Would like to write/edit the package docstring inline
        - [ ] Want to be able to export non-generated things here too
    - [ ] Merging multiple `__all__` into a single parent
    """
    source_all = find_dunder_all(source)
    relative = source.relative_to(fs.SRC)
    if relative.name == "__init__.py":
        relative = relative.parent
    import_names = source_all.to_str()
    import_statement = f"from {relative.as_posix().replace('/', '.')} import {import_names}"
    target_contents = f"from __future__ import annotations\n{import_statement}\n__all__ = {tuple(import_names.split(', '))}\n"
    target.write_text(target_contents, "utf8", newline="\n")


if __name__ == "__main__":
    steal_child_dunder_all(fs.MOSAIC_SPEC_GEN_INIT, fs.MOSAIC_SPEC_INIT)
    print(f"Updated `__all__` at: {fs.repo_relative_str(fs.MOSAIC_SPEC_INIT)}")
