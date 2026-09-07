from __future__ import annotations

import typing as t
from graphlib import TopologicalSorter
from pathlib import Path  # ruff: ignore[typing-only-standard-library-import]

import msgspec

from tools.codegen.convert import py_identifier_snake
from tools.common import PyIdentifier, PyIdentifierSnake, RichRepr
from tools.ir.pyir import convert
from tools.ir.pyir.base import (
    Definition,
    IterExprs,
    RefRepl,
    TypedExtRef,
    TypedRef,
    UntypedExtRef,
    UntypedRef,
)
from tools.models import base

if t.TYPE_CHECKING:
    from collections.abc import Iterable, Iterator

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
        it = (convert.from_def(defn, def_name) for def_name, defn in source.def_items())
        return parent.child(source.id, it)

    def child(self, name: str, definitions: Iterable[Definition]) -> Module:
        """Add a new module to this package."""
        name = py_identifier_snake(name)
        if not self.is_init_module:
            msg = f"{self.filepath.name!r} cannot be used as a parent for {name!r}, as it is not a package."
            raise TypeError(msg)
        return Module(
            name=name,
            filepath=self.filepath.parent / f"{name}.py",
            parent=self,
            definitions={defn.name: defn for defn in definitions},
        )

    def __repr__(self) -> str:
        return (
            f"Module<name: {self.name}, defs: {len(self.definitions)}, path:{self.canonical_path}>"
        )

    def __rich_repr__(self) -> RichRepr:
        yield "name", self.name
        yield "definitions", self.definitions

    def preview(self) -> None:
        print(f"# Generated: {self.canonical_path}\n")
        get = self.definitions.__getitem__
        for def_name in self.topological_sort():
            print("\n".join(get(def_name).iter_lines()))
            print("\n")

    def topological_sort(self) -> Iterator[PyIdentifier]:
        """Return an iterator over a deterministic, [topological sort] within the bounds of this module.

        In other words, return definition names before the names they depend on;
        ensuring multiple runs produce the same order.

        [topological sort]: https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter
        """
        tps = UntypedRef, TypedRef
        graph = {
            defn.name: sorted({expr.ref for expr in defn.iter_exprs() if isinstance(expr, tps)})
            for defn in self.definitions.values()
        }
        yield from TopologicalSorter(graph).static_order()

    def with_refs(self, repl: RefRepl, /) -> Module:
        return self.__replace__(
            definitions={
                def_name: defn.with_refs(repl) for def_name, defn in self.definitions.items()
            }
        )

    def iter_exprs(self) -> IterExprs:
        for defn in self.definitions.values():
            yield from defn.iter_exprs()

    def unique_refs(self) -> set[UntypedRef]:
        return {expr for expr in self.iter_exprs() if isinstance(expr, UntypedRef)}

    def unique_ext_refs(self) -> set[UntypedExtRef]:
        return {expr for expr in self.iter_exprs() if isinstance(expr, UntypedExtRef)}

    def typed_ref(self, expr: UntypedRef) -> TypedRef:
        """Retrieve the type of a same-module reference."""
        name = expr.ref
        return TypedRef(ref=name, type=type(self.definitions[name]))

    def import_ref(self, def_name: PyIdentifier | str, /) -> TypedExtRef:
        """Return a reference that another module can use to refer to a def from here."""
        name = PyIdentifier(def_name)
        return TypedExtRef(ext=self.name, ref=name, type=type(self.definitions[name]))

    def depends_ext(self) -> set[PyIdentifierSnake]:
        """Return the set of module names that this one depends on."""
        tps = UntypedExtRef, TypedExtRef
        return {expr.ext for expr in self.iter_exprs() if isinstance(expr, tps)}

    def update_defs(self, definitions: Iterable[Definition], /) -> None:
        """Insert new definitions or overwrite existing ones."""
        self.definitions.update((defn.name, defn) for defn in definitions)
