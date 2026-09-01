from __future__ import annotations

import typing as t
from pathlib import Path  # ruff: ignore[typing-only-standard-library-import]
from typing import Any

import msgspec

from tools.codegen.convert import py_identifier_snake
from tools.common import PyIdentifier, PyIdentifierSnake
from tools.ir.pyir import convert
from tools.ir.pyir.base import Definition
from tools.models import base

if t.TYPE_CHECKING:
    from collections.abc import Iterable

    from tools.ir import mlir


# ruff: file-ignore[print]
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
    def from_mlir(cls, source: mlir.Root, parent: Module, /) -> Module:
        name = py_identifier_snake(source.id)
        if not parent.is_init_module:
            msg = f"{parent.filepath.name!r} cannot be used as a parent for {name!r}, as it is not a package."
            raise TypeError(msg)

        it = (convert.from_def(defn, def_name) for def_name, defn in source.def_items())
        return Module(
            name=name,
            filepath=parent.filepath.parent / f"{name}.py",
            parent=parent,
            definitions={defn.name: defn for defn in it},
        )

    def __repr__(self) -> str:
        return (
            f"Module<name: {self.name}, defs: {len(self.definitions)}, path:{self.canonical_path}>"
        )

    def __rich_repr__(self) -> Iterable[tuple[str, Any]]:
        yield "name", self.name
        yield "definitions", self.definitions

    def preview(self) -> None:
        print(f"# Generated: {self.canonical_path}\n")
        for defn in self.definitions.values():
            print("\n".join(defn.iter_lines()))
            print("\n")
