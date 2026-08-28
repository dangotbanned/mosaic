from __future__ import annotations

from pathlib import Path  # ruff: ignore[typing-only-standard-library-import]

from tools.ir.pyir.base import PyIdentifier  # ruff: ignore[typing-only-first-party-import]
from tools.models import base


# TODO @dangotbanned: `PyIR` needs to declare import dependencies
class Module(base.Struct, kw_only=True):
    """A representation of a Python module.

    This is a stripped down version of [griffe.Module](https://mkdocstrings.github.io/griffe/reference/api/models/module/#griffe.Module).
    """

    name: PyIdentifier
    filepath: Path
    parent: Module | None = None

    @property
    def is_init_module(self) -> bool:
        return self.filepath.stem == "__init__"

    @property
    def is_package(self) -> bool:
        return (not self.parent) and self.is_init_module

    @property
    def is_subpackage(self) -> bool:
        return bool(self.parent) and self.is_init_module

    @property
    def canonical_path(self) -> str:
        if self.parent is None:
            return self.name
        return f"{self.parent.canonical_path}.{self.name}"
