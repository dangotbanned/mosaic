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
- [x] Merging multiple `__all__` into a single parent
"""

from __future__ import annotations

from collections import deque
from typing import TYPE_CHECKING

from tools import codemod, fs

if TYPE_CHECKING:
    from pathlib import Path


def main(*sources: Path, target: Path) -> None:
    bare_export_tuples = []
    contents: deque[str] = deque((codemod.fragments.FUTURE_ANNOTATIONS,))
    for source in sources:
        names_all = codemod.dunder_all.find(source).unparse_value()
        contents.append(codemod.fragments.import_from(source, names_all.replace("'", "")))
        bare_export_tuples.append(names_all.strip("()"))

    contents.append(f"__all__ = {','.join(bare_export_tuples)}")
    fs.write_lines(target, contents, "Updated `__all__`")


if __name__ == "__main__":
    # TODO @dangotbanned: Check if there was a diff first?
    main(fs.MOSAIC_SPEC_GEN_INIT, fs.MOSAIC_SPEC_INTERSECTION, target=fs.MOSAIC_SPEC_INIT)
