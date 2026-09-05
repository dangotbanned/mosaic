from __future__ import annotations

import typing as t
from typing import Self

from tools.common import copy_replace
from tools.ir.pyir.base import Expr, IterExprs, Lines, PyIR, RefRepl, TypeExpr


class Qualifier(PyIR):
    """A type expression wrapped with a [type qualifier][1].

    [1]: https://typing.python.org/en/latest/spec/qualifiers.html#type-qualifiers
    """

    expr: Expr

    def iter_lines(self) -> Lines:
        yield self.__str__()

    def __str__(self) -> TypeExpr:
        return TypeExpr(f"{self.__class__.__name__}[{self.expr}]")

    def iter_exprs(self) -> IterExprs:
        yield from self.expr.iter_exprs()

    def with_refs(self, repl: RefRepl, /) -> Self:
        current = self.expr
        maybe_changed = self.expr.with_refs(repl)
        if current == maybe_changed:
            return self
        return copy_replace(self, expr=maybe_changed)


@t.final
class Required(Qualifier):
    """Marks a Field as required."""



@t.final
class ReadOnly(Qualifier):
    """Marks `extra_items` as read-only."""
