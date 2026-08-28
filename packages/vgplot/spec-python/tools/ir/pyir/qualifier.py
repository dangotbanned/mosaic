from __future__ import annotations

import typing as t

from tools.ir.pyir.base import Expr, Lines, PyIR, TypeExpr


class Qualifier(PyIR):
    """A type expression wrapped with a [type qualifier][1].

    [1]: https://typing.python.org/en/latest/spec/qualifiers.html#type-qualifiers
    """

    expr: Expr

    def iter_lines(self) -> Lines:
        yield self.__str__()

    def __str__(self) -> TypeExpr:
        return TypeExpr(f"{self.__class__.__name__}[{self.expr}]")


@t.final
class Required(Qualifier):
    """Marks a Field as required."""


@t.final
class NotRequired(Qualifier):
    """Marks a Field as not required."""


@t.final
class ReadOnly(Qualifier):
    """Marks `extra_items` as read-only."""
