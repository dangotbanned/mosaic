from __future__ import annotations

import typing as t
from graphlib import TopologicalSorter
from itertools import chain
from pathlib import Path  # ruff: ignore[typing-only-standard-library-import]

import msgspec

from tools.codegen.convert import py_identifier_snake
from tools.common import CanonicalPath, PyIdentifier, PyIdentifierSnake, RichRepr
from tools.ir.pyir import convert
from tools.ir.pyir.base import (
    Definition,
    IterExprs,
    Lines,
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
    from tools.ir.pyir.dependencies import Resolver


@t.final
class Module(base.Root[PyIdentifier | str, Definition], kw_only=True):
    """A representation of a Python module.

    This is a stripped down version of [griffe.Module](https://mkdocstrings.github.io/griffe/reference/api/models/module/#griffe.Module).
    """

    name: PyIdentifierSnake
    filepath: Path
    parent: Module | None = None
    definitions: dict[PyIdentifier | str, Definition] = msgspec.field(default_factory=dict)

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
    def canonical_path(self) -> CanonicalPath:
        result = self.name if self.parent is None else f"{self.parent.canonical_path}.{self.name}"
        return CanonicalPath(result)

    @classmethod
    def from_mlir(cls, source: mlir.Root, parent: Module, /) -> Module:
        it = (convert.from_def(defn, def_name) for def_name, defn in source.def_items())
        return parent.with_child(source.id, it)

    def with_child(self, name: str, definitions: Iterable[Definition]) -> Module:
        """Return a new module, with this package a parent."""
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

    def with_subpackage(self, name: str) -> Module:
        """Return a new subpackage, with this package a parent."""
        name = py_identifier_snake(name)
        if not self.is_init_module:
            msg = f"{self.filepath.name!r} cannot be used as a parent for {name!r}, as it is not a package."
            raise TypeError(msg)
        return Module(name=name, filepath=self.filepath.parent / name / "__init__.py", parent=self)

    def _describe(self, *, length: bool = True, names: bool = True) -> str:
        header = (
            f"<name: {self.name}, defs: {len(self.definitions)}, path:{self.canonical_path}>"
            if length
            else f"<name: {self.name}, path:{self.canonical_path}>"
        )
        if not names:
            return header
        return f"{header}\n    {list(self.definitions)!r}"

    def __rich_repr__(self) -> RichRepr:
        yield "name", self.name
        yield "definitions", self.definitions

    def generate(self, resolver: Resolver) -> Lines:
        get = self.definitions.__getitem__
        yield f"# Generated: {self.canonical_path}"
        yield "from __future__ import annotations\n"
        yield from resolver.iter_imports(self.def_values())
        yield ""
        if self.definitions:
            yield "\n".join(
                chain.from_iterable(
                    get(def_name).iter_lines() for def_name in self.topological_sort()
                )
            )
            yield "\n"
            yield f"__all__ = ({','.join(name.__repr__() for name in self.iter_exports())})\n"

    def topological_sort(self) -> Iterator[PyIdentifier]:
        """Return an iterator over a deterministic, [topological sort] within the bounds of this module.

        In other words, return definition names before the names they depend on;
        ensuring multiple runs produce the same order.

        [topological sort]: https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter
        """
        tps = UntypedRef, TypedRef
        graph = {
            defn.name: sorted({expr.ref for expr in defn.iter_exprs() if isinstance(expr, tps)})
            for defn in self.def_values()
        }
        yield from TopologicalSorter(graph).static_order()

    def with_refs(self, repl: RefRepl, /) -> Module:
        return self.__replace__(
            definitions={def_name: defn.with_refs(repl) for def_name, defn in self.def_items()}
        )

    def iter_exprs(self) -> IterExprs:
        for defn in self.def_values():
            yield from defn.iter_exprs()

    # TODO @dangotbanned: Re-use for package exports
    def iter_exports(self) -> Iterator[str]:
        yield from (name for name in self.def_names() if not name.startswith("_"))

    def unique_refs(self) -> set[UntypedRef]:
        return {expr for expr in self.iter_exprs() if isinstance(expr, UntypedRef)}

    def unique_ext_refs(self) -> set[UntypedExtRef]:
        return {expr for expr in self.iter_exprs() if isinstance(expr, UntypedExtRef)}

    def typed_ref(self, expr: UntypedRef) -> TypedRef:
        """Retrieve the type of a same-module reference."""
        name = expr.ref
        return TypedRef(ref=name, type=type(self[name]))

    def import_ref(self, def_name: PyIdentifier | str, /) -> TypedExtRef:
        """Return a reference that another module can use to refer to a def from here."""
        name = PyIdentifier(def_name)
        return TypedExtRef(ext=self.name, ref=name, type=type(self[name]))

    def depends_ext(self) -> set[PyIdentifierSnake]:
        """Return the set of module names that this one depends on."""
        tps = UntypedExtRef, TypedExtRef
        return {expr.ext for expr in self.iter_exprs() if isinstance(expr, tps)}

    def update_defs(self, definitions: Iterable[Definition], /) -> None:
        """Insert new definitions or overwrite existing ones."""
        self.definitions.update((defn.name, defn) for defn in definitions)
