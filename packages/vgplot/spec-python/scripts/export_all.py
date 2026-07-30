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
from tools.codemod import common, dunder_all, fragments

if TYPE_CHECKING:
    from pathlib import Path


def steal_child_dunder_all(source: Path, target: Path) -> None:
    import_names = dunder_all.find(source).to_str()
    target_contents = (
        f"{fragments.FUTURE_ANNOTATIONS}\n"
        f"{fragments.import_from(common.dotted_module_name(source), import_names)}\n"
        f"__all__ = {tuple(import_names.split(', '))}\n"
    )
    target.write_text(target_contents, "utf8", newline="\n")


if __name__ == "__main__":
    # TODO @dangotbanned: Check if there was a diff first?
    steal_child_dunder_all(fs.MOSAIC_SPEC_GEN_INIT, fs.MOSAIC_SPEC_INIT)
    print(f"Updated `__all__` at: {fs.repo_relative_str(fs.MOSAIC_SPEC_INIT)}")
