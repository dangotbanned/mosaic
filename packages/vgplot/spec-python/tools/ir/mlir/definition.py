from __future__ import annotations

from typing import Final, final

from tools.ir.mlir.nodes import MLIR, ExtReference, Reference
from tools.models import base


@final
class Definition[T: MLIR](base.Struct, kw_only=True):
    """A top-level (named) node, with pre-computed reference info.

    ## Notes
    - Where are we?
        - Each `Definition` is a graph of immutable nodes (`MLIR`), stored in a mutable structure (dict)
        - That dict provides the `name` and is stored in a mutable struct (`Root`)
    - When a `Definition` requires changes, it must be **replaced**
    - Making sense of that means storing details about references
        - To allow moving node `A` to file x, we need to check for references **to** and **from** `A`
        - This can be computed for the full `definitions` dict on creation
        - Then subsequent changes are incremental
    """

    inner: Final[T]
    refs: set[Reference]
    ext_refs: set[ExtReference]

    @classmethod
    def from_mlir[M: MLIR](cls, defn: M, /) -> Definition[M]:
        return Definition(
            inner=defn, refs=set(defn.iter_refs()), ext_refs=set(defn.iter_ext_refs())
        )

    def has_references(self) -> bool:
        return bool(self.refs or self.ext_refs)
