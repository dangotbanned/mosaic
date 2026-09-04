from __future__ import annotations

import typing as t

from tools.codegen.docstrings import doc
from tools.common import copy_replace
from tools.ir.pyir.base import Expr, IterExprs, Lines, PyIR, RefRepl
from tools.ir.pyir.qualifier import NotRequired, Required

if t.TYPE_CHECKING:
    from tools.common import PyIdentifierSnake


@t.final
class Field[T: Expr | Required | NotRequired = Expr | Required | NotRequired](PyIR):
    name: PyIdentifierSnake
    expr: t.Final[T]
    doc: str = ""

    def iter_lines(self) -> Lines:
        yield f"{self.name}: {self.expr}"
        if self.doc:
            yield doc(self.doc)

    def iter_exprs(self) -> IterExprs:
        yield from self.expr.iter_exprs()  # ty: ignore[invalid-argument-type]

    # NOTE: Captures `NamedTuple` not supporting `Required`/`NotRequired`
    @t.overload
    def with_refs(self: Field[Expr], repl: RefRepl, /) -> Field[Expr]: ...
    @t.overload
    def with_refs(self, repl: RefRepl, /) -> Field: ...
    def with_refs(self, repl: RefRepl, /) -> Field[Expr] | Field:
        current = self.expr
        maybe_changed = self.expr.with_refs(repl)  # ty: ignore[invalid-argument-type]
        if current == maybe_changed:
            return self
        return copy_replace(self, expr=maybe_changed)
