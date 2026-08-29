from __future__ import annotations

# ruff: file-ignore[print]
from collections import deque
from typing import TYPE_CHECKING, final

from tools import fs, serde
from tools.common import PyIdentifierSnake
from tools.ir import json_wrapper as jw, mlir, pyir
from tools.models.config import MosaicSpecToml
from tools.models.mosaic import InputSchema

if TYPE_CHECKING:
    from collections.abc import Collection, Iterator, Mapping

    from tools.models.base import IdName


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

    *TBD*
    ...

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

    def __init__(self, config: MosaicSpecToml) -> None:
        self.config = config
        self._inputs = deque[InputSchema]()
        self._wrappers = deque[jw.Root]()
        self._mlirs = deque[mlir.Root]()
        self._actions: dict[int, mlir.Action] = {}
        self._mlirs_inv: dict[IdName, int] = {}

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
            self._inputs.extend(self._read_sources())

    def into_json_wrapper(self, *, refresh: bool = False) -> None:
        if not self._wrappers or refresh:
            self.read_into_inputs(refresh=refresh)
            self._wrappers.extend(jw.Root.from_input_schema(schema) for schema in self._inputs)

    def into_mlir(self, *, refresh: bool = False, quiet: bool = False) -> None:
        # NOTE: While these are still being implemented, coupling the steps here ensures an
        # interactive session doesn't re-run on partial data.
        # I don't want to add exception handling (yet)
        if self._mlirs:
            self._mlirs.clear()

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

    def into_pyir(self) -> deque[pyir.Module]:
        """Lower MLIR into PyIR.

        Quite far from having this working, so it's simpler to not have state yet.
        """
        self.into_mlir(refresh=True, quiet=True)
        pkg = pyir.Module(name=PyIdentifierSnake("mosaic_spec"), filepath=fs.MOSAIC_SPEC_INIT)
        sub_pkg = pyir.Module(
            name=PyIdentifierSnake("_gen"), filepath=fs.MOSAIC_SPEC_GEN_INIT, parent=pkg
        )
        modules = deque((pkg, sub_pkg))
        modules.extend(pyir.Module.from_mlir(root, sub_pkg) for root in self._mlirs)
        return modules

    def mlir_root(self, id: IdName, /) -> mlir.Root:
        """Return the `MLIR` representation of module `id`."""
        return self._mlirs[self._mlirs_inv[id]]

    def mlir_root_ids(self) -> Collection[IdName]:
        """Return the names of all `MLIR` modules."""
        return self._mlirs_inv.keys()

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
