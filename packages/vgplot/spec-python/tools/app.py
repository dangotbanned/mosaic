from __future__ import annotations

# ruff: file-ignore[print]
from collections import Counter, deque
from typing import TYPE_CHECKING, Literal as L, Protocol, final

from tools import fs, serde
from tools.common import CanonicalPath, PyIdentifier, PyIdentifierSnake
from tools.config import MosaicSpecToml
from tools.ir import json_wrapper as jw, mlir, pyir
from tools.ir.pyir.dependencies import Resolver

if TYPE_CHECKING:
    from collections.abc import Iterator, Mapping


type RunUntil = L["json_wrapper", "mlir", "pyir", "codegen", "lint"]


class CLIOptions(Protocol):
    stage: RunUntil
    """Run until the end of a specific conversion stage."""
    quiet: bool
    "Print less to stdout."
    require_unique_module_names: bool
    """Before codegen, check that every module (regardless of package) has a unique name.

    See [related](https://github.com/dangotbanned/mosaic/blob/4c26a5ff88a17663b01ba1b191c0a37480912cb6/packages/vgplot/spec-python/tools/ir/pyir/dependencies.py#L77-L84)
    """


@final
class App:
    """Application context for multi-stage IR conversion."""

    config: MosaicSpecToml
    _wrappers: deque[jw.Root]
    _mlirs: deque[mlir.Root]
    _package: pyir.Package

    def __init__(self, config: MosaicSpecToml) -> None:
        self.config = config
        self._wrappers = deque[jw.Root]()
        self._mlirs = deque[mlir.Root]()
        self._actions: dict[int, mlir.Action] = {}

    @staticmethod
    def discover(path: fs.IntoPath = fs.MOSAIC_SPEC_TOML) -> App:
        config = serde.read_toml(path, MosaicSpecToml, contains_paths=True)
        return App(config)

    def run(self, options: CLIOptions) -> None:
        method = {
            "json_wrapper": self.into_json_wrapper,
            "mlir": self.into_mlir,
            "pyir": self.into_pyir,
            "codegen": self.codegen,
            "lint": self.lint,
        }[options.stage]
        method(options)

    @property
    def actions(self) -> Mapping[int, mlir.Action]:
        if actions := self._actions:
            return actions
        if actions_cfg := self.config.convert.to_mlir.actions:
            self._actions = dict(mlir.actions.from_config(actions_cfg))
            return self._actions
        msg = "Empty actions"
        raise NotImplementedError(msg)

    def into_json_wrapper(self, options: CLIOptions) -> None:
        """Deserialize source schema(s) and wrap them in `JSONWrapper` nodes."""
        if not (sources := self.config.sources):
            msg = "Empty sources"
            raise NotImplementedError(msg)
        self._wrappers = deque(jw.Root.from_json(source.path, source.id) for source in sources)

    def into_mlir(self, options: CLIOptions) -> None:
        """Convert `JSONWrapper` into `MLIR`, running actions on the result."""
        self.into_json_wrapper(options)
        config = self.config.convert.to_mlir
        fn = mlir.Root.from_json_wrapper
        self._mlirs = deque(fn(root, config) for root in self._wrappers)
        quiet = options.quiet
        if not quiet:
            print(f"Starting {len(self.actions)} actions on {len(self._mlirs)} root(s).")
        self._mlirs = self._run_actions(self._mlirs, quiet=quiet)
        if not quiet:
            print(f"Finished actions with {len(self._mlirs)} root(s).")
            print("\n".join(root._describe() for root in self._mlirs))

    def into_pyir(self, options: CLIOptions) -> None:
        """Convert `MLIR` into `PyIR`."""
        self.into_mlir(options)
        quiet = options.quiet
        if not quiet:
            print(f"Generating module representation from {len(self._mlirs)} root(s).")

        self._package = pyir.Package.root_package(
            "mosaic_spec",
            fs.MOSAIC_SPEC_INIT,
            exports={
                CanonicalPath("mosaic_spec"): "child-modules",
                CanonicalPath("mosaic_spec._gen"): "child-exports",
                CanonicalPath("mosaic_spec.spec"): (PyIdentifier("Spec"),),
            },
        )
        sub_pkg = self._package.with_subpackage("_gen")

        if not quiet:
            print("Added 2 packages.")
        with pyir.configure(self.config.convert.to_pyir):
            for root in self._mlirs:
                # TODO @dangotbanned: Either bake `ext` here or make everything walkable?
                sub_pkg.with_child(
                    root.id,
                    (pyir.convert.from_def(defn, def_name) for def_name, defn in root.def_items()),
                )
            if not quiet:
                self._package._summarize_into_pyir()
            self._run_pyir_plugins(quiet=quiet)

    def _ensure_unique_module_names(self, n_unique: int, /) -> None:
        module_names = [module.name for module in self._iter_modules()]
        if n_unique == len(module_names):
            return
        duplicates = "\n".join(
            f"- Got {name!r} {count} times"
            for name, count in Counter(module_names).items()
            if count > 1
        )
        msg = (
            f"Multiple modules with the same name are not yet supported:\n{duplicates}.\n\n"
            f"See (https://github.com/dangotbanned/mosaic/blob/4c26a5ff88a17663b01ba1b191c0a37480912cb6/packages/vgplot/spec-python/tools/ir/pyir/dependencies.py#L77-L84)"
        )
        raise NotImplementedError(msg)

    def codegen(self, options: CLIOptions) -> None:
        self.into_pyir(options)
        quiet = options.quiet
        if not quiet:
            print("Starting codegen")

        # TODO @dangotbanned: remove the need for expanding the names here.
        # Likely need to do this during `into_pyir` when the parent is accessible
        expand_to_canonical_path = {
            module.name: module.canonical_path for module in self._iter_modules()
        }
        if options.require_unique_module_names:
            self._ensure_unique_module_names(len(expand_to_canonical_path))
        resolver = Resolver(expand_to_canonical_path, self.config.convert.to_pyir.name)
        messages = {
            True: (None, None, None),
            False: ("Generated module", "Generated subpackage", "Generated package"),
        }[quiet]

        for module in self._iter_modules():
            fs.write_lines(module.filepath, module.generate(resolver), messages[0])

        root = self._package
        for package in root._packages.values():
            fs.write_lines(package.filepath, package.generate(resolver), messages[1])

        fs.write_lines(root.filepath, root.generate(resolver), messages[2])

    def lint(self, options: CLIOptions) -> None:
        self.codegen(options)
        quiet = options.quiet
        output = "quiet" if quiet else "pipe"
        fs.run("uv", "run", "ruff", "check", output=output)
        fs.run("uv", "run", "ruff", "format", output=output)

    def package(self, name: PyIdentifierSnake | str = "mosaic_spec") -> pyir.Package:
        """Return the `PyIR` representation of package `name`."""
        if name == "mosaic_spec":
            return self._package
        return self._package.package(name.removeprefix("mosaic_spec."))

    def module(self, name: str) -> pyir.Module:
        """Return the `PyIR` representation of module `name`."""
        return self._package.module(name.removeprefix("mosaic_spec."))

    def _iter_modules(self) -> Iterator[pyir.Module]:
        return self._package.iter_modules_descendants()

    def _run_actions(self, roots: deque[mlir.Root], *, quiet: bool) -> deque[mlir.Root]:
        for idx, action in self.actions.items():
            if not quiet:
                print(f"  Running action {idx} {action!r}")
            roots = deque(action.run(roots))
        return roots

    def _run_pyir_plugins(self, *, quiet: bool = False) -> None:
        import scripts.plugins.pyir_actions

        if not quiet:
            print("Running pyir plugins")
        scripts.plugins.pyir_actions.run(self)
        if not quiet:
            print("Finished pyir plugins")

    def _iter_rename_fields_overrides(self) -> Iterator[tuple[str, str]]:
        """Yield `action = "rename-fields"` overrides.

        Maps from old name to new name.
        """
        from tools.config.actions import RenameFields

        for action in self.config.convert.to_mlir.actions:
            if isinstance(action, RenameFields):
                yield from action.overrides.items()
