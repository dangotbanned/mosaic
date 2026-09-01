from __future__ import annotations

import typing as t
from typing import Literal as L

from tools.ir.mlir.nodes import MLIR, ExtReference, Field, Reference
from tools.models import base

if t.TYPE_CHECKING:
    from collections.abc import Callable


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

    def has_references(self) -> bool:
        return bool(self.refs or self.ext_refs)

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


def inner_type_is[M: MLIR](
    inner_type: type[M], /
) -> Callable[[Definition[t.Any]], t.TypeIs[Definition[M]]]:
    """Generate a typeguard to pass to [`mlir.Root.iter_defs`][].

    Args:
        inner_type: A single `MLIR` class to check against `Definition.inner`.

    ## Examples
    ```py
    from typing import assert_type

    from tools.ir import mlir
    from tools.ir.mlir.nodes import ClosedDict


    def func(root: mlir.Root) -> None:
        _, first_closed_dict = next(root.iter_defs(mlir.inner_type_is(ClosedDict)))
        assert_type(first_closed_dict, mlir.Definition[ClosedDict])  # OK
    ```
    """

    def guard(obj: Definition[t.Any], /) -> t.TypeIs[Definition[M]]:
        return isinstance(obj.inner, inner_type)

    return guard
