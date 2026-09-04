from __future__ import annotations

import functools

# ruff: file-ignore[print]
from collections import deque
from typing import TYPE_CHECKING, final

from tools import fs, serde
from tools.common import PyIdentifierSnake, into_repl_map
from tools.ir import json_wrapper as jw, mlir, pyir
from tools.models.config import MosaicSpecToml
from tools.models.mosaic import InputSchema

if TYPE_CHECKING:
    from collections.abc import Collection, Iterator, Mapping

    from tools.models.base import IdName

type CanonicalPath = str

type _PyIRRefMap = dict[pyir.UntypedRef | pyir.UntypedExtRef, pyir.TypedRef | pyir.TypedExtRef]
"""Very long, unfortunate type."""


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

    - Module: `tools.models.mosaic`
    - Root: `mosaic.InputSchema`
    - Nodes: `mosaic.JsonSchema`, `mosaic.NonRecursiveFields`

    Raw files are **strictly** parsed into a reduced subset of [JSON Schema draft-07],
    based on patterns observed from [ts-json-schema-generator]'s output.

    [JSON Schema draft-07]: https://json-schema.org/draft-07/schema
    [ts-json-schema-generator]: https://github.com/vega/ts-json-schema-generator

    #### Open issues

    - Most of what this representation does is related to `scripts/schema_mod.py`
    - The naming of the types & module location are not consistent with `tools.ir.*`
    - `description` is cleaned on creation

    ### Stage 2

    - Package: `tools.ir.json_wrapper`
    - Root: `json_wrapper.Root`
    - Nodes: `json_wrapper.JsonWrapper`, 11 implementations

    #### Open issues

    - Would really like to deserialize into this directly, but (https://github.com/msgspec/msgspec/issues/982)

    ### Stage 3

    - Package: `tools.ir.mlir`
    - Root: `mlir.Root`
    - Definition: `mlir.Definition`
    - Nodes: `mlir.MLIR`, 20 implementations

    #### Open issues

    - `ref_unwrap` mutates "Stage 2" to create "Stage 3"

    ### Stage 4

    - Package: `tools.ir.pyir`
    - Root: `pyir.Module`
    - Definition: `pyir.Definition`, 7 implementations
    - Nodes:
        - `pyir.Expr`, 14 implementations
        - `pyir.PyIR` (other), 9 implementations

    #### Open issues

    - Some deeply nested edge cases are not converted yet (`expr.Unresolved`)
    - Reference typing, for inheritance lists

    ## Targets

    *This section is a goal, but entirely unimplemented and depends on the output of **Stage 4***.

    ### Python version

    Output is for the current [minimum supported Python version] (-5 versions).
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
    _inputs: deque[InputSchema]
    _wrappers: deque[jw.Root]
    _mlirs: deque[mlir.Root]
    _modules: dict[CanonicalPath, pyir.Module]

    def __init__(self, config: MosaicSpecToml) -> None:
        self.config = config
        self._inputs = deque[InputSchema]()
        self._wrappers = deque[jw.Root]()
        self._mlirs = deque[mlir.Root]()
        self._actions: dict[int, mlir.Action] = {}
        self._mlirs_inv: dict[IdName, int] = {}
        self._modules: dict[CanonicalPath, pyir.Module] = {}

    @staticmethod
    def discover(path: fs.IntoPath = fs.MOSAIC_SPEC_TOML) -> App:
        config = serde.read_toml(path, MosaicSpecToml, contains_paths=True)
        return App(config)

    @property
    def actions(self) -> Mapping[int, mlir.Action]:
        if actions := self._actions:
            return actions
        if actions_cfg := self.config.convert.to_mlir.actions:
            self._actions = dict(mlir.actions.from_config(actions_cfg))
            return self._actions
        msg = "Empty actions"
        raise NotImplementedError(msg)

    def read_into_inputs(self, *, refresh: bool = False) -> None:
        if not self._inputs or refresh:
            it = self._read_sources()
            if refresh:
                self._inputs.clear()
            self._inputs.extend(it)

    def into_json_wrapper(self, *, refresh: bool = False) -> None:
        if not self._wrappers or refresh:
            self.read_into_inputs(refresh=refresh)
            it = (jw.Root.from_input_schema(schema) for schema in self._inputs)
            if refresh:
                self._wrappers.clear()
            self._wrappers.extend(it)

    def into_mlir(self, *, refresh: bool = False, quiet: bool = False) -> None:
        if not self._mlirs or refresh:
            if self._mlirs:
                self._mlirs.clear()
                self._mlirs_inv.clear()
            self.into_json_wrapper(refresh=refresh)
            config = self.config.convert.to_mlir
            fn = mlir.Root.from_json_wrapper
            self._mlirs.extend(fn(root, config) for root in self._wrappers)
            if not quiet:
                print(f"Starting {len(self.actions)} actions on {len(self._mlirs)} root(s).")
            self._mlirs = self._run_actions(self._mlirs, quiet=quiet)
            self._mlirs_inv = {root.id: idx for idx, root in enumerate(self._mlirs)}
            if not quiet:
                print(f"Finished actions with {len(self._mlirs)} root(s).")
                print("\n".join(root._describe() for root in self._mlirs))

    def into_pyir(self, *, refresh: bool = False, quiet: bool = False) -> None:
        """Lower MLIR into PyIR."""
        self.into_mlir(refresh=refresh, quiet=quiet)
        if not quiet:
            print(f"Generating module representation from {len(self._mlirs)} root(s).")
        pkg = pyir.Module(name=PyIdentifierSnake("mosaic_spec"), filepath=fs.MOSAIC_SPEC_INIT)
        sub_pkg = pyir.Module(
            name=PyIdentifierSnake("_gen"), filepath=fs.MOSAIC_SPEC_GEN_INIT, parent=pkg
        )

        self._modules = {pkg.canonical_path: pkg, sub_pkg.canonical_path: sub_pkg}
        if not quiet:
            print(f"Added {len(self._modules)} packages.")
        it = (pyir.Module.from_mlir(root, sub_pkg) for root in self._mlirs)
        self._modules.update((module.canonical_path, module) for module in it)
        if not quiet:
            print(f"Finished generating with {len(self._modules)} modules(s).")
            print("\n".join(f" - {m}" for m in self._modules))
            print(f"Total definitions: {sum(len(m.definitions) for m in self._modules.values())}")

    def mlir_root(self, id: IdName, /) -> mlir.Root:
        """Return the `MLIR` representation of module `id`."""
        return self._mlirs[self._mlirs_inv[id]]

    def mlir_root_ids(self) -> Collection[IdName]:
        """Return the names of all `MLIR` modules."""
        return self._mlirs_inv.keys()

    def module(self, name: CanonicalPath | str, /) -> pyir.Module:
        """Return the `PyIR` representation of module `name`."""
        return self._modules[canonical_path(name)]

    def resolve_all_references(self) -> None:
        """Convert all untyped references to typed references.

        After this operation, every `PyIR` can be rendered.

        ## Notes
        - This is the most expensive version of what this *could be*
            - **Takes around 20ms**
        - Most places where it is *expected* to be needed are not ready yet
            - `TypeVar`
            - `TypedDict` bases
            - `TypeAliasType` type params
        """
        modules = self._modules
        done = {}
        # typing is not strictly accurate, but this pleases invariance
        resolved_ext_refs: _PyIRRefMap = {}
        for canonical_path, module in modules.items():
            # Fast path 1
            if not module.definitions:
                done[canonical_path] = module
                continue

            replace: _PyIRRefMap = {}
            unique_refs = module.unique_refs()
            unique_ext_refs = module.unique_ext_refs()
            replace.update((ref, module.typed_ref(ref)) for ref in unique_refs)
            if unique_ext_refs:
                # NOTE: Takes advantage of dependencies being repetitive
                # - 6 have no dependencies
                # - 5 only depend on `params.ParamRef`
                # - 4 remain (mosaic, marks, plot, layout)
                replace_ext: _PyIRRefMap = {
                    ref: resolved_ext_refs.get(ref) or typed_ext_ref(modules, ref)
                    for ref in unique_ext_refs
                }
                replace.update(replace_ext)
                resolved_ext_refs.update(replace_ext)

            # Fast path 2
            if not replace:
                done[canonical_path] = module
                continue

            # NOTE: We have *some* work to do
            done[canonical_path] = module.with_refs(into_repl_map(replace))

        self._modules = done

    def _read_sources(self) -> Iterator[InputSchema]:
        if not (sources := self.config.convert.sources):
            msg = "Empty sources"
            raise NotImplementedError(msg)

        for source in sources:
            schema = serde.read_json(source.path, InputSchema)
            schema.id = source.id
            yield schema

    def _run_actions(self, roots: deque[mlir.Root], *, quiet: bool) -> deque[mlir.Root]:
        for idx, action in self.actions.items():
            if not quiet:
                print(f"  Running action {idx} {action!r}")
            roots = deque(action.run(roots))
        return roots


@functools.cache
def canonical_path(name: CanonicalPath | str, /) -> CanonicalPath:
    return name if name.startswith("mosaic_spec") else f"mosaic_spec._gen.{name}"


def typed_ext_ref(
    modules: dict[CanonicalPath, pyir.Module], expr: pyir.UntypedExtRef, /
) -> pyir.TypedExtRef:
    ref = expr.ref
    ext = expr.ext
    ext_module = modules[canonical_path(ext)]
    return pyir.TypedExtRef(ext=ext, ref=ref, type=type(ext_module.definitions[ref]))
