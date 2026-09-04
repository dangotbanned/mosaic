from __future__ import annotations

from typing import TYPE_CHECKING, final

from tools.ir.mlir import convert
from tools.ir.mlir.definition import Definition
from tools.ir.mlir.nodes import MLIR
from tools.models import base

if TYPE_CHECKING:
    from tools.ir import json_wrapper as jw
    from tools.models.base import DefName
    from tools.models.config import JsonWrapperToMLIR


@final
class Root(base.Root[Definition[MLIR]], kw_only=True):
    @classmethod
    def from_json_wrapper(cls, source: jw.Root, config: JsonWrapperToMLIR, /) -> Root:
        source.ref_unwrap(config)
        definitions = {
            name: Definition.from_mlir(convert.from_json(schema, name))
            for name, schema in source.def_items()
        }
        return Root(id=source.id, definitions=definitions)

    def replace(self, name: DefName, node: MLIR, /) -> None:
        """Replace an existing definition with an updated version.

        *Unconditionally* recomputes reference information based on the new version.
        """
        self.definitions[name] = Definition.from_mlir(node)
