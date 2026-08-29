from __future__ import annotations

import typing as t
from pathlib import Path  # ruff: ignore[typing-only-standard-library-import]

import msgspec

from tools.codegen.convert import py_identifier_snake
from tools.common import PyIdentifier, PyIdentifierSnake
from tools.ir.pyir.base import Definition
from tools.models import base

if t.TYPE_CHECKING:
    from tools.ir import mlir


# TODO @dangotbanned: `PyIR` needs to declare import dependencies
@t.final
class Module(base.Struct, kw_only=True):
    """A representation of a Python module.

    This is a stripped down version of [griffe.Module](https://mkdocstrings.github.io/griffe/reference/api/models/module/#griffe.Module).
    """

    name: PyIdentifierSnake
    filepath: Path
    parent: Module | None = None
    definitions: dict[PyIdentifier, Definition] = msgspec.field(
        default_factory=dict[PyIdentifier, Definition]
    )

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

    @classmethod
    def from_mlir(cls, source: mlir.Root, /) -> Module:
        _name = py_identifier_snake(source.id)
        raise NotImplementedError
