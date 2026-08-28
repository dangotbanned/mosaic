from __future__ import annotations

import typing as t

from tools.codegen.docstrings import doc
from tools.ir.pyir.base import Definition, Expr, Lines, join_comma


@t.final
class TypeVar(Definition):
    """A representation of a TypeVar."""

    bound: Expr | None = None
    constraints: tuple[Expr, ...] = ()

    def iter_lines(self) -> Lines:
        value = str(bound) if (bound := self.bound) else join_comma(map(str, self.constraints))
        yield f"{self.name} = TypeVar({self.name!r}{value})"
        if self.doc:
            yield doc(self.doc)
