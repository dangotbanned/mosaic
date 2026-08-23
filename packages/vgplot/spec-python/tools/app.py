from __future__ import annotations

from collections import deque
from typing import TYPE_CHECKING, final

from tools import fs, serde
from tools.ir import json_wrapper as jw, mlir
from tools.ir.mlir.scopes import Matcher
from tools.models.config import MosaicSpecToml
from tools.models.mosaic import InputSchema

if TYPE_CHECKING:
    from collections.abc import Iterator


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

    @staticmethod
    def discover(path: fs.IntoPath = fs.MOSAIC_SPEC_TOML) -> App:
        config = serde.read_toml(path, MosaicSpecToml, contains_paths=True)
        return App(config)

    def read_into_inputs(self, *, refresh: bool = False) -> None:
        if not self._inputs or refresh:
            self._inputs.extend(self._read_sources())

    def into_json_wrapper(self, *, refresh: bool = False) -> None:
        if not self._wrappers or refresh:
            self.read_into_inputs(refresh=refresh)
            self._wrappers.extend(jw.Root.from_input_schema(schema) for schema in self._inputs)

    def into_mlir(self, *, refresh: bool = False) -> None:
        if not self._mlirs or refresh:
            self.into_json_wrapper(refresh=refresh)
            config = self.config.convert.to_mlir
            fn = mlir.Root.from_json_wrapper
            self._mlirs.extend(fn(root, config)[0] for root in self._wrappers)

    def _read_sources(self) -> Iterator[InputSchema]:
        if not (sources := self.config.convert.sources):
            msg = "Empty sources"
            raise NotImplementedError(msg)

        for source in sources:
            schema = serde.read_json(source.path, InputSchema)
            schema.id = source.id
            yield schema

    def _run_actions(self) -> None:
        if not (actions := self.config.convert.to_mlir.actions):
            msg = "Empty actions"
            raise NotImplementedError(msg)
        if not (_roots := self._mlirs):
            msg = "Empty mlirs"
            raise NotImplementedError(msg)

        _jobs = {
            idx: (action, Matcher.from_scopes(action.scope)) for idx, action in enumerate(actions)
        }
        msg_0 = "TODO @dangotbanned: Finish scopes/matcher concept first!"
        raise NotImplementedError(msg_0)
