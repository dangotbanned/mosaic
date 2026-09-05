from __future__ import annotations

import typing as t

from tools.codegen.docstrings import doc
from tools.common import copy_replace
from tools.ir.pyir.base import Expr, IterExprs, Lines, PyIR, RefRepl
from tools.ir.pyir.qualifier import Required

if t.TYPE_CHECKING:
    from tools.common import PyIdentifierSnake


_T = t.TypeVar("_T", bound=Expr | Required, default=Expr | Required, covariant=True)


@t.final
class Field(PyIR, t.Generic[_T]):  # ruff: ignore[non-pep695-generic-class]
    name: PyIdentifierSnake
    # NOTE: **Do not upgrade this to PEP 695**.
    # `pyright` is not inferring the variance correctly
    expr: t.Final[_T]
    doc: str = ""

    def iter_lines(self) -> Lines:
        yield f"{self.name}: {self.expr}"
        if self.doc:
            yield doc(self.doc)

    def iter_exprs(self) -> IterExprs:
        yield from self.expr.iter_exprs()  # ty: ignore[invalid-argument-type]

    # NOTE: Captures `NamedTuple` always being `Required`
    @t.overload
    def with_refs(self: Field[Expr], repl: RefRepl, /) -> Field[Expr]: ...
    @t.overload
    def with_refs(self: Field[Required], repl: RefRepl, /) -> Field[Required]: ...
    @t.overload
    def with_refs(self, repl: RefRepl, /) -> Field: ...
    def with_refs(self, repl: RefRepl, /) -> Field:
        current = self.expr
        maybe_changed = self.expr.with_refs(repl)  # ty: ignore[invalid-argument-type]
        if current == maybe_changed:
            return self
        return copy_replace(self, expr=maybe_changed)
