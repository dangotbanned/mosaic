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
    def from_json_wrapper(
        cls, source: jw.Root, config: JsonWrapperToMLIR, /
    ) -> tuple[Root, convert.ConversionCtx]:
        source.ref_unwrap(config)
        # Probably not gonna go too far into this idea
        ctx = convert.ConversionCtx()
        definitions = {
            name: Definition.from_mlir(convert.from_json(schema, name, ctx))
            for name, schema in source.def_items()
        }
        self = Root(id=source.id, definitions=definitions)
        return self, ctx

    def replace(self, name: DefName, node: MLIR, /) -> None:
        """Replace an existing definition with an updated version.

        *Unconditionally* recomputes reference information based on the new version.
        """
        self.definitions[name] = Definition.from_mlir(node)

    def replace_naive(self, name: DefName, node: MLIR, /) -> None:
        """Replace an existing definition with an updated version.

        *Naive* as we assume that because the definition didn't start with references, it never will.
        """
        current_defn = self[name]
        if current_defn.has_references():
            self.replace(name, node)
        else:
            self.definitions[name] = current_defn.__replace__(inner=node)
