# /// script
# requires-python = ">=3.12"
# ///
"""Duplicate a child module's `__all__` in-place of a parent.

This API isn't the goal, but it works for now.

## What's missing?
- [ ] Be more selective about what we re-export
- [ ] Be more surgical than overwriting an entire file
    - [ ] Would like to write/edit the package docstring inline
    - [ ] Want to be able to export non-generated things here too
- [ ] Merging multiple `__all__` into a single parent
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from tools import fs
from tools.codemod import dunder_all, fragments

if TYPE_CHECKING:
    from pathlib import Path


def main(source: Path, target: Path) -> None:
    names_all = dunder_all.find(source).unparse_value()
    imports = fragments.import_from(source, names_all.replace("'", ""))
    contents = (fragments.FUTURE_ANNOTATIONS, imports, f"__all__ = {names_all}")
    fs.write_lines(target, contents, "Updated `__all__`")


if __name__ == "__main__":
    # TODO @dangotbanned: Check if there was a diff first?
    main(fs.MOSAIC_SPEC_GEN_INIT, fs.MOSAIC_SPEC_INIT)
