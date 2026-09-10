from __future__ import annotations

import typing as t
from collections import deque
from collections.abc import Mapping
from graphlib import TopologicalSorter
from itertools import chain
from pathlib import Path  # ruff: ignore[typing-only-standard-library-import]
from typing import Literal as L

import msgspec

from tools.codegen.convert import py_identifier_snake
from tools.common import CanonicalPath, PyIdentifier, PyIdentifierSnake, RichRepr
from tools.ir.pyir.base import Definition, Lines, Ref, TypedExtRef, TypedRef
from tools.models import base

if t.TYPE_CHECKING:
    from collections.abc import Iterable, Iterator

    from tools.ir.pyir.dependencies import Resolver


type ExportKind = L["child-exports", "child-modules"]
"""A filter to apply when determining symbols to re-export in a package.

Either option will implicitly exclude `_`-prefixed names.

- *"child-exports"*: all exports from each child module are re-exported (default).
- *"child-modules"*: only the name of child modules are exported.
"""

type ExportSpec = Mapping[CanonicalPath, ExportKind | tuple[PyIdentifier, ...]]
type PyIdentifierAny = PyIdentifier | PyIdentifierSnake


# NOTE: Why is `Package` separated from `Module`?
# - In Python's data model
#   - A package is a module
#   - but a module is not a package (excluding namespace packages)
# - Griffe models this correctly
#   - but it accounts for scenarios that I will never generate
# - For codegen
#   - A Package does not contain definitions
#   - A Package must have children
#   - The parent of a Module is a Package, and cannot be a Module or None
#   - The parent of a Package is a Package, or None if it is the root
#   - A Module exports all definitions that are not prefixed with `_`
#       - This should be the only mechanism for export control that a Module has
#   - A Package has full control of it's exports
#       - Defaults to the sum of it's children's exports
#       - Optionally, supports exporting Module(s) and subsets of Module exports
@t.final
class Package(base.Struct, kw_only=True):
    """A collection of `Module`s and/or `Package`s."""

    name: PyIdentifierSnake
    filepath: Path
    canonical_path: CanonicalPath

    export_spec: ExportSpec = msgspec.field(default_factory=dict)
    """How to derive names exported from a package."""

    _modules: dict[PyIdentifierSnake, Module] = msgspec.field(default_factory=dict)
    _packages: dict[PyIdentifierSnake, Package] = msgspec.field(default_factory=dict)

    def __repr__(self) -> str:
        # NOTE: Fallback used to keep bound method reprs small
        tp = self.__class__
        return f"pyir.{tp.__name__}<name: {self.name}, modules: {len(self._modules)}, packages: {len(self._packages)}, path: {self.canonical_path}>"

    def __rich_repr__(self) -> RichRepr:
        yield "name", self.name
        if self.export_spec:
            yield "export_spec", self.export_spec
        if self._modules:
            yield "modules", self._modules
        if self._packages:
            yield "packages", self._packages

    def package(self, name: PyIdentifierSnake | str) -> Package:
        parts = t.cast("list[PyIdentifierSnake]", name.split("."))
        if not parts:
            msg = "Empty strings are not a valid identifier"
            raise TypeError(msg)
        package = self
        for part in parts:
            package = package._packages[part]
        return package

    def module(self, name: PyIdentifierSnake | str) -> Module:
        if module := self._modules.get(PyIdentifierSnake(name)):
            return module
        parts = t.cast("list[PyIdentifierSnake]", name.split("."))
        if not parts:
            msg = "Empty strings are not a valid identifier"
            raise TypeError(msg)
        if len(parts) == 2:
            return self._packages[parts[0]]._modules[parts[1]]
        *package_parts, module_name = parts
        package = self
        for part in package_parts:
            package = package._packages[part]
        return package._modules[module_name]

    def iter_modules_descendants(self) -> Iterator[Module]:
        yield from self._modules.values()
        for package in self._packages.values():
            yield from package.iter_modules_descendants()

    def iter_modules_children(self) -> Iterator[Module]:
        yield from self._modules.values()

    def _summarize_into_pyir(self) -> None:
        total_modules = 1
        total_defs = 0
        module_listing = []
        for total_modules, module in enumerate(self.iter_modules_descendants(), 1):  # ruff: ignore[unused-loop-control-variable]
            total_defs += len(module.definitions)
            module_listing.append(f" - {module}")

        print(f"Finished generating with {total_modules} modules(s).")  # ruff: ignore[print]
        print("\n".join(module_listing) + f"\nTotal definitions: {total_defs}")  # ruff: ignore[print]

    @classmethod
    def root_package(
        cls,
        name: PyIdentifierSnake | str,
        filepath: Path,
        /,
        exports: ExportKind | ExportSpec = "child-exports",
    ) -> Package:
        name = py_identifier_snake(name)
        root_name = CanonicalPath(name)
        if not isinstance(exports, Mapping):
            exports = {root_name: exports}
        return Package(name=name, filepath=filepath, export_spec=exports, canonical_path=root_name)

    def with_child(self, name: str, definitions: Iterable[Definition]) -> Module:
        """Return a new module, with this package a parent."""
        name = py_identifier_snake(name)
        canonical_path = CanonicalPath(f"{self.canonical_path}.{name}")
        module = self._modules[name] = Module(
            name=name,
            filepath=self.filepath.parent / f"{name}.py",
            canonical_path=canonical_path,
            definitions={defn.name: defn for defn in definitions},
        )
        return module

    def with_subpackage(self, name: str) -> Package:
        """Return a new subpackage, with this package a parent."""
        name = py_identifier_snake(name)
        canonical_path = CanonicalPath(f"{self.canonical_path}.{name}")
        subpackage = self._packages[name] = Package(
            name=name,
            filepath=self.filepath.parent / name / "__init__.py",
            canonical_path=canonical_path,
        )
        return subpackage

    def generate(self, resolver: Resolver) -> Lines:
        # NOTE: Pretend that this doesn't need to handle `Module`s for now.
        # `Module.generate` is called independently to allow sharing a cache of imports between all modules
        self_canonical = self.canonical_path
        yield f"# Generated: `{self_canonical}`"
        yield "from __future__ import annotations\n"
        exporter = Exporter()
        if not (export_spec := self.export_spec):
            yield from exporter.from_submodules(self)
            yield exporter.dunder_all()
            return

        for canonical, options in export_spec.items():
            if isinstance(options, tuple):
                yield from exporter.import_from(canonical, options)
            elif canonical == self_canonical:
                fn = exporter.submodules if options == "child-modules" else exporter.from_submodules
                yield from fn(self)
            elif child := self._packages.get(_child_package_name(self_canonical, canonical)):
                fn = exporter.submodules if options == "child-modules" else exporter.from_subpackage
                yield from fn(child)
            else:
                msg = f"{options!r} can only be used with a package, but {canonical!r} is a module"
                raise TypeError(msg)


# TODO @dangotbanned: Think about changing `ExportSpec` so that this isn't needed
# - That idea came before the `Package`/`Module` split
# - Now, `CanonicalPath` isn't used as a key - so this is more verbose and requires more work to support
def _child_package_name(parent: CanonicalPath, child: CanonicalPath) -> PyIdentifierSnake:
    child_id = child.removeprefix(parent + ".")
    if child_id == child:
        msg_0 = f"Exports must come from within {parent!r}, but got: {child!r}"
        raise NotImplementedError(msg_0)
    if "." in child_id:
        msg_1 = f"TODO: Handle multiple levels of nesting, got: {child_id!r}"
        raise NotImplementedError(msg_1)

    return py_identifier_snake(child_id)


@t.final
class Module(base.Root[PyIdentifier | str, Definition], kw_only=True):
    """A representation of a Python module.

    This is loosely based on [griffe.Module](https://mkdocstrings.github.io/griffe/reference/api/models/module/#griffe.Module).
    """

    name: PyIdentifierSnake
    filepath: Path
    canonical_path: CanonicalPath
    definitions: dict[PyIdentifier | str, Definition] = msgspec.field(default_factory=dict)

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
        if not self.definitions:
            msg = f"Module {self.canonical_path!r} does not have any definitions to generate."
            raise TypeError(msg)
        get = self.definitions.__getitem__
        yield f"# Generated: `{self.canonical_path}`"
        yield "from __future__ import annotations\n"
        yield from resolver.iter_imports(self.def_values())
        yield ""
        yield "\n".join(
            chain.from_iterable(get(def_name).iter_lines() for def_name in self.topological_sort())
        )
        yield "\n"
        yield f"__all__ = ({','.join(f'"{s}"' for s in self.iter_exports())},)\n"

    def topological_sort(self) -> Iterator[PyIdentifier]:
        """Return an iterator over a deterministic, [topological sort] within the bounds of this module.

        In other words, return definition names before the names they depend on;
        ensuring multiple runs produce the same order.

        [topological sort]: https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter
        """
        tps = Ref, TypedRef
        graph = {
            defn.name: sorted({expr.ref for expr in defn.iter_exprs() if isinstance(expr, tps)})
            for defn in self.def_values()
        }
        yield from TopologicalSorter(graph).static_order()

    def iter_exports(self) -> Iterator[PyIdentifier]:
        yield from (defn.name for defn in self.def_values() if not defn.name.startswith("_"))

    def import_ref(self, def_name: PyIdentifier | str, /) -> TypedExtRef:
        """Return a reference that another module can use to refer to a def from here."""
        name = PyIdentifier(def_name)
        return TypedExtRef(ext=self.name, ref=name, type=type(self[name]))

    def update_defs(self, definitions: Iterable[Definition], /) -> None:
        """Insert new definitions or overwrite existing ones."""
        self.definitions.update((defn.name, defn) for defn in definitions)


class Exporter:
    """Tool for collecting imported names, while generating re-export statements."""

    __slots__ = ("_seen",)

    def __init__(self) -> None:
        self._seen: deque[PyIdentifierAny] = deque()

    def import_from(self, module_name: CanonicalPath, names: Iterable[PyIdentifierAny], /) -> Lines:
        export_names = deque(names)
        self._seen.extend(export_names)
        yield f"from {module_name} import {','.join(export_names)}"

    def from_submodules(self, package: Package, /) -> Lines:
        for module in package.iter_modules_children():
            yield from self.import_from(module.canonical_path, module.iter_exports())

    def from_subpackage(self, sub: Package, /) -> Lines:
        it = chain.from_iterable(m.iter_exports() for m in sub.iter_modules_children())
        yield from self.import_from(sub.canonical_path, it)

    def submodules(self, package: Package, /) -> Lines:
        it = (m.name for m in package.iter_modules_children() if not m.name.startswith("_"))
        yield from self.import_from(package.canonical_path, it)

    def dunder_all(self) -> str:
        return f"\n__all__ = ({','.join(f'"{s}"' for s in self._seen)},)\n"
