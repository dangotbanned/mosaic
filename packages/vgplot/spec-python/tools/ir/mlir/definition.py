from __future__ import annotations

import typing as t
from typing import Literal as L

from tools.ir.mlir.nodes import MLIR, ExtReference, Field, Reference
from tools.models import base


@t.final
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

    inner: t.Final[T]
    refs: set[Reference]
    ext_refs: set[ExtReference]

    @classmethod
    def from_mlir[M: MLIR](cls, defn: M, /) -> Definition[M]:
        return Definition(
            inner=defn, refs=set(defn.iter_refs()), ext_refs=set(defn.iter_ext_refs())
        )

    @t.overload
    def field(self, name: str, /, *, allow_missing: L[False] = False) -> Field: ...
    @t.overload
    def field(self, name: str, /, *, allow_missing: L[True]) -> Field | None: ...
    def field(self, name: str, /, *, allow_missing: bool = False) -> Field | None:
        if field := self.inner.get_field(name):
            return field
        if allow_missing:
            return None
        inner = self.inner
        if not hasattr(inner, "fields"):
            msg = f"{inner.__class__.__name__!r} is not a type that defines fields, got:\n{inner!r}"
            raise TypeError(msg)
        msg = f"Field {name!r} is not present in:\n{inner!r}"
        raise KeyError(msg)
