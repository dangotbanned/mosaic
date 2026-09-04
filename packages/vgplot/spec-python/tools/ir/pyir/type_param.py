from __future__ import annotations

import typing as t

from tools.codegen.docstrings import doc
from tools.ir.pyir.base import Definition, Expr, IterExprs, Lines, RefRepl, RuntimeScope, join_comma


@t.final
class TypeVar(Definition):
    """A representation of a TypeVar."""

    bound: RuntimeScope[Expr] | None = None
    constraints: RuntimeScope[tuple[Expr, ...]] = ()

    def iter_lines(self) -> Lines:
        value = str(bound) if (bound := self.bound) else join_comma(map(str, self.constraints))
        yield f"{self.name} = TypeVar({self.name!r}{value})"
        if self.doc:
            yield doc(self.doc)

    def iter_exprs(self) -> IterExprs:
        if bound := self.bound:
            yield from bound.iter_exprs()
        for constraint in self.constraints:
            yield from constraint.iter_exprs()

    def with_refs(self, repl: RefRepl, /) -> TypeVar:
        changes: dict[str, t.Any] = {}
        if bound := self.bound:
            bound_changed = bound.with_refs(repl)
            if bound_changed is not bound:
                changes["bound"] = bound_changed
        constraints_changed = tuple(constraint.with_refs(repl) for constraint in self.constraints)
        if constraints_changed != self.constraints:
            changes["constraints"] = constraints_changed
        if not changes:
            return self
        return self.__replace__(**changes)
