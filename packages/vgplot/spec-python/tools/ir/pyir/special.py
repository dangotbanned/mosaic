"""The subset of [Special forms] that cannot be used in type expressions.

[Special forms]: https://typing.python.org/en/latest/spec/glossary.html#term-special-form:
"""

from __future__ import annotations

import typing as t
from typing import Literal as L

from tools.ir.pyir.base import IterExprs, PyIR, RefRepl, RuntimeScope, join_comma

if t.TYPE_CHECKING:
    from tools.ir.pyir.type_param import TypeVar


@t.final
class TypedDict(PyIR):
    """A reference the *name* `TypedDict` in a base class list."""

    def as_base(self) -> L["TypedDict"]:
        return "TypedDict"

    def iter_exprs(self) -> IterExprs:
        yield from ()

    def with_refs(self, repl: RefRepl, /) -> TypedDict:
        return self


TYPED_DICT: t.Final = TypedDict()


@t.final
class Generic(PyIR):
    """A subscript of `Generic` in a base class list."""

    type_params: RuntimeScope[tuple[TypeVar, ...]]

    def as_base(self) -> str:
        return f"Generic[{join_comma(tp.as_ref() for tp in self.type_params)}]"

    def iter_exprs(self) -> IterExprs:
        for param in self.type_params:
            yield from param.iter_exprs()

    def with_refs(self, repl: RefRepl, /) -> Generic:
        params_changed = tuple(p.with_refs(repl) for p in self.type_params)
        if params_changed != self.type_params:
            return self.__replace__(type_params=params_changed)
        return self
