from __future__ import annotations

# ruff: file-ignore[print]
from collections import deque
from typing import TYPE_CHECKING, Literal as L, Protocol, final

from tools import fs, serde
from tools.common import CanonicalPath, PyIdentifier, PyIdentifierSnake
from tools.ir import json_wrapper as jw, mlir, pyir
from tools.ir.pyir.dependencies import Resolver
from tools.models.config import MosaicSpecToml

if TYPE_CHECKING:
    from collections.abc import Collection, Iterator, Mapping, Sequence

    from tools.models.base import IdName


type RunUntil = L["json_wrapper", "mlir", "pyir", "codegen", "lint"]


class CLIOptions(Protocol):
    stage: RunUntil
    """Run until the end of a specific conversion stage."""
    quiet: bool
    "Print less to stdout."
    preview_modules: Sequence[str | L["all"]]
    "Print the full generated code for these modules to stdout."


@final
class App:
    """Application context for multi-stage IR conversion.

    ## Important

    Configured via `spec-python/mosaic-spec.toml`.
    Install [tombi] for schema-driven IDE support.

    [tombi]: https://tombi-toml.github.io/tombi/docs/installation

    ## Sources

    Takes one or more JSON Schema as input.

    ## Stages

    Each stage has a common pattern of one or more "root" containers storing a table of "definitions".

    ### Stage 1

    - Package: [`tools.ir.json_wrapper`][]
    - Root: `json_wrapper.Root`
    - Nodes: `json_wrapper.JsonWrapper`, 11 implementations

    The raw schema cannot deserialize into this representation directly (see [msgspec/msgspec#982]).

    This stage begins with a re-wrapping of a representation that *can*, stored on the `schema` field of each node.

    [msgspec/msgspec#982]: https://github.com/msgspec/msgspec/issues/982

    ### Stage 2

    - Package: [`tools.ir.mlir`][]
    - Root: `mlir.Root`
    - Definition: `mlir.Definition`
    - Nodes: `mlir.MLIR`, 20 implementations

    #### Open issues

    - `ref_unwrap` mutates "Stage 1" to create "Stage 2"

    ### Stage 3

    - Package: [`tools.ir.pyir`][]
    - Root: `pyir.Module` / `pyir.Package`
    - Definition: `pyir.Definition`, 7 implementations
    - Nodes:
        - `pyir.Expr`, 14 implementations
        - `pyir.PyIR` (other), 9 implementations

    ## Targets

    ### Python version

    Codegen targets the current [minimum supported Python version] (-5 versions).
    This is **not planned to be configurable**.

    If you want features from a newer version, use Ruff's ([`UP`]) rules on the output:

    ```terminal
    uvx ruff check --extend-select UP --target-version py312 --fix
    ```

    For now, that means:

    1. [PEP 695] syntax cannot be used, but type aliases will have the same semantics,
       through the use of [`TypeAliasType`].
    2. [PEP 728] features for [`TypedDict`] are used, but depend on either (see [related]):
       i. [`typing_extensions>=4.10.0rc1`]
       ii. [`requires-python>=3.15 `]

    [minimum supported Python version]: https://devguide.python.org/versions/#supported-versions
    [`UP`]: https://docs.astral.sh/ruff/rules/#pyupgrade-up
    [PEP 695]: https://peps.python.org/pep-0695/
    [`TypeAliasType`]: https://typing-extensions.readthedocs.io/en/latest/#typing_extensions.TypeAliasType
    [PEP 728]: https://peps.python.org/pep-0728/
    [`TypedDict`]: https://typing-extensions.readthedocs.io/en/latest/#typing_extensions.TypedDict
    [related]: https://discuss.python.org/t/spec-change-proposal-updating-clarifying-rules-for-unpacking-typeddicts-in-function-calls/108582
    [`typing_extensions>=4.10.0rc1`]: https://github.com/python/typing_extensions/releases/tag/4.10.0rc1
    [`requires-python>=3.15`]: https://docs.python.org/3.15/whatsnew/3.15.html

    ### Python style

    The output is not concerned with linting/formatting behaviors. *This tool* expects that the output
    is run through another tool (e.g. [Ruff]) that enforces the conventions of the project.
    To that end, *you* should expect the code to be syntactically valid, but ugly.
    It is faster to generate code with the knowledge that it will be tidied up elsewhere.

    [Ruff]: https://docs.astral.sh/ruff/

    #### Non-configurable

    These decisions are influenced by a few principles:

    - [Nominal] types should be avoided, unless they provide a concrete benefit
    - Generated code should take advantage of *language features* [^1] that reduce file size
    - Documentation should be local to the member it describes

    [Nominal]: https://typing.python.org/en/latest/spec/concepts.html#nominal-and-structural-types

    [^1]: "minifying" is not a feature

    1. `Enum` -> `Literal`.
    2. `dict[str, V]` -> `Mapping[str, V]`.
    3. `list[T]` -> `Sequence[T_co]`.
    4. `tuple` is used for sequences with a known-length.
    5. `total=False` will be preferred for `TypedDict`, *unless* more keys are required than not.
    6. [PEP 224]-style "attribute docstrings" will be used whenever possible.

    [PEP 224]: https://peps.python.org/pep-0224

    #### Potential configuration

    These have trade-offs, which should likely be made on a case-by-case basis.

    1. Promoting `str` aliases to `NewType`s
       i. `Literal["..."] | str` can mask errors
       ii. `NewType` fixes this, but can be painful to adjust to
    2. Promoting "structural named tuple"s to nominal `NamedTuple`s
       i. The former relies on `Annotated`, which may be hidden by a language server
       ii. The latter will reject valid `tuple`(s) and requires the constructor

    The default for both is to avoid [nominal] types.

    [nominal]: https://typing.python.org/en/latest/spec/concepts.html#nominal-and-structural-types
    """

    config: MosaicSpecToml
    _wrappers: deque[jw.Root]
    _mlirs: deque[mlir.Root]
    _package: pyir.Package

    def __init__(self, config: MosaicSpecToml) -> None:
        self.config = config
        self._wrappers = deque[jw.Root]()
        self._mlirs = deque[mlir.Root]()
        self._actions: dict[int, mlir.Action] = {}
        self._mlirs_inv: dict[IdName, int] = {}

    @staticmethod
    def discover(path: fs.IntoPath = fs.MOSAIC_SPEC_TOML) -> App:
        config = serde.read_toml(path, MosaicSpecToml, contains_paths=True)
        return App(config)

    def run(self, options: CLIOptions) -> None:
        stage = options.stage
        quiet = options.quiet
        if options.preview_modules:
            self.preview_modules(*options.preview_modules, quiet=quiet)
            return
        method = {
            "json_wrapper": self.into_json_wrapper,
            "mlir": self.into_mlir,
            "pyir": self.into_pyir,
            "codegen": self.codegen,
            "lint": self.lint,
        }[stage]
        method(quiet=quiet)

    @property
    def actions(self) -> Mapping[int, mlir.Action]:
        if actions := self._actions:
            return actions
        if actions_cfg := self.config.convert.to_mlir.actions:
            self._actions = dict(mlir.actions.from_config(actions_cfg))
            return self._actions
        msg = "Empty actions"
        raise NotImplementedError(msg)

    def into_json_wrapper(self, *, quiet: bool = False) -> None:
        """Deserialize source schema(s) and wrap them in `JSONWrapper` nodes."""
        if not (sources := self.config.convert.sources):
            msg = "Empty sources"
            raise NotImplementedError(msg)
        self._wrappers = deque(jw.Root.from_json(source.path, source.id) for source in sources)

    def into_mlir(self, *, quiet: bool = False) -> None:
        """Convert `JSONWrapper` into `MLIR`, running actions on the result."""
        self.into_json_wrapper()
        config = self.config.convert.to_mlir
        fn = mlir.Root.from_json_wrapper
        self._mlirs = deque(fn(root, config) for root in self._wrappers)
        if not quiet:
            print(f"Starting {len(self.actions)} actions on {len(self._mlirs)} root(s).")
        self._mlirs = self._run_actions(self._mlirs, quiet=quiet)
        self._mlirs_inv = {root.id: idx for idx, root in enumerate(self._mlirs)}
        if not quiet:
            print(f"Finished actions with {len(self._mlirs)} root(s).")
            print("\n".join(root._describe() for root in self._mlirs))

    def into_pyir(self, *, quiet: bool = False) -> None:
        """Convert `MLIR` into `PyIR`."""
        self.into_mlir(quiet=quiet)
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
                sub_pkg.with_child(
                    root.id,
                    (pyir.convert.from_def(defn, def_name) for def_name, defn in root.def_items()),
                )
            if not quiet:
                self._package._summarize_into_pyir()
            self._run_pyir_plugins(quiet=quiet)

    def preview_modules(self, *names: str, quiet: bool = False) -> None:
        self.into_pyir(quiet=quiet)
        if "all" in names:
            names = tuple(module.name for module in self._iter_modules())
        if not quiet:
            print(f"Previewing modules: {list(names)!r}")

        # NOTE: `quiet=True` will only silence previous steps, this one is about displaying stuff
        resolver = Resolver(
            {module.name: module.canonical_path for module in self._iter_modules()},
            self.config.convert.to_pyir.name,
        )
        multiple_modules = len(names) > 1
        for module in self._iter_modules():
            if module.name in names:
                print("\n".join(module.generate(resolver)))
                if multiple_modules:
                    print("-" * 100)

    def codegen(self, *, quiet: bool = False) -> None:
        self.into_pyir(quiet=quiet)
        if not quiet:
            print("Starting codegen")

        resolver = Resolver(
            {module.name: module.canonical_path for module in self._iter_modules()},
            self.config.convert.to_pyir.name,
        )
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

    def lint(self, *, quiet: bool = False) -> None:
        self.codegen(quiet=quiet)
        output = "quiet" if quiet else "pipe"
        fs.run("uv", "run", "ruff", "check", output=output)
        fs.run("uv", "run", "ruff", "format", output=output)

    def mlir_root(self, id: IdName, /) -> mlir.Root:
        """Return the `MLIR` representation of module `id`."""
        return self._mlirs[self._mlirs_inv[id]]

    def mlir_root_ids(self) -> Collection[IdName]:
        """Return the names of all `MLIR` modules."""
        return self._mlirs_inv.keys()

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
