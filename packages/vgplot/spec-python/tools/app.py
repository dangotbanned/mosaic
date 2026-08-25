from __future__ import annotations

# ruff: file-ignore[print]
from collections import deque
from typing import TYPE_CHECKING, final

from tools import fs, serde
from tools.ir import json_wrapper as jw, mlir
from tools.models.config import MosaicSpecToml
from tools.models.mosaic import InputSchema

if TYPE_CHECKING:
    from collections.abc import Iterator, Mapping


@final
class App:
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

    def into_mlir(self, *, refresh: bool = False) -> None:
        # NOTE: While these are still being implemented, coupling the steps here ensures an
        # interactive session doesn't re-run on partial data.
        # I don't want to add exception handling (yet)
        if self._mlirs:
            self._mlirs.clear()

        self.into_json_wrapper(refresh=refresh)
        config = self.config.convert.to_mlir
        fn = mlir.Root.from_json_wrapper
        self._mlirs.extend(fn(root, config)[0] for root in self._wrappers)

        self._mlirs = self._run_actions(self._mlirs)

    def _read_sources(self) -> Iterator[InputSchema]:
        if not (sources := self.config.convert.sources):
            msg = "Empty sources"
            raise NotImplementedError(msg)

        for source in sources:
            schema = serde.read_json(source.path, InputSchema)
            schema.id = source.id
            yield schema

    def _run_actions(self, roots: deque[mlir.Root]) -> deque[mlir.Root]:
        for idx, action in self.actions.items():
            print(f"Running action {idx} {action!r}")
            roots = deque(action.run(roots))
            # TODO @dangotbanned: Remove assignment once all actions are working
            # This saves progress for an interactive session
            self._mlirs = roots
        return roots
