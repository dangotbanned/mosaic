"""Design notes.

## Notes
- `msgspec` may be limiting in how much metaprogramming can happen
- would be nice to use descriptors for
    - Is this in annotation scope?
    - Which fields contain expresions?
    - Something like `ExprIR` traversal stuff
"""

from __future__ import annotations

import typing as t
from typing import Annotated as A, Literal as L, LiteralString as LS, Self

import tools.common
from tools.models import base

if t.TYPE_CHECKING:
    import collections.abc as cabc

    from tools.common import PyIdentifier, PyIdentifierSnake

    @t.overload
    def join_comma(iterable: cabc.Iterable[TypeExpr], /) -> TypeExpr: ...
    @t.overload
    def join_comma(iterable: cabc.Iterable[LS], /) -> LS: ...
    @t.overload
    def join_comma(iterable: cabc.Iterable[str], /) -> str: ...
    def join_comma(iterable: cabc.Iterable[str], /) -> str:
        raise NotImplementedError

    join_or = join_comma
else:
    join_comma: t.Final = ",".join
    join_or: t.Final = " | ".join

type Line = str
"""An unindented line of code.

Indents are handled by definitions.
"""

type Lines = cabc.Iterator[Line]
"""The return type of `PyIR.iter_lines`."""

TypeExpr = t.NewType("TypeExpr", str)
"""A rendered type expression."""

type IterExprs = cabc.Iterator[Expr]


type RuntimeScope[T] = A[T, L["runtime"]]
"""Mark a position as being outside of an [annotation scope].

Type expressions in these positions have the following constraints, which all others do not:

1. External references must [^1] use non-`TYPE_CHECKING` imports.
2. Internal references must not refer to to symbols defined *later* in the module.

These rules mean that only a subset of all expressions need to be concerned about
definition order and cyclic references.

[^1]: In some cases a [ForwardRef] is permitted but this doesn't include a base class list.

[annotation scope]: https://docs.python.org/3/reference/executionmodel.html#annotation-scopes
[ForwardRef]: https://docs.python.org/3/library/typing.html#typing.ForwardRef
"""

type RefRepl = tools.common.ReplMap[UntypedRef | UntypedExtRef, TypedRef | TypedExtRef]

INDENT: t.Final = " " * 4


class PyIR(base.FrozenHashableStruct):
    """Python IR, representing anything that can be generated."""

    def iter_lines(self) -> Lines:
        """Yield lines of code that this symbol produces."""
        msg = f"{type(self).__name__}.{self.iter_lines.__name__}() is not yet implemented. Got:\n{self!r}"
        raise NotImplementedError(msg)

    def iter_exprs(self) -> IterExprs:
        """Yield all descendant `Expr`s.

        References are expressions, so we need to traverse to find them.
        """
        msg = f"{type(self).__name__}.{self.iter_exprs.__name__}() is not yet implemented. Got:\n{self!r}"
        raise NotImplementedError(msg)

    def with_refs(self, repl: RefRepl, /) -> Self | PyIR:
        return self


class Expr(PyIR):
    """A [type expression][1].

    [1]: https://typing.python.org/en/latest/spec/annotations.html#type-and-annotation-expressions
    """

    def __str__(self) -> TypeExpr:
        """Render the type expression as a string."""
        msg = f"{type(self).__name__}.{self.__str__.__name__}() is not yet implemented. Got:\n{self!r}"
        raise NotImplementedError(msg)

    def iter_lines(self) -> Lines:
        yield self.__str__()

    def iter_exprs(self) -> IterExprs:
        yield self

    def with_refs(self, repl: RefRepl, /) -> Self | Expr:
        return self


class Definition(PyIR):
    """A named definition."""

    name: PyIdentifier
    doc: str = ""

    def as_ref(self) -> TypeExpr:
        """Refer to this symbol as a type expression."""
        return TypeExpr(self.name)

    def with_refs(self, repl: RefRepl, /) -> Self | Definition:
        return self


class _Ref(Expr):
    ref: PyIdentifier


class _ExtRef(Expr):
    ext: PyIdentifierSnake
    ref: PyIdentifier


class UntypedRef(_Ref, order=True):
    """Placeholder for `TypedRef`."""

    def with_refs(self, repl: RefRepl, /) -> Self | TypedRef | TypedExtRef:
        return repl(self) or self


class UntypedExtRef(_ExtRef, order=True):
    """Placeholder for `TypedExtRef`."""

    def with_refs(self, repl: RefRepl, /) -> Self | TypedRef | TypedExtRef:
        return repl(self) or self


@t.final
class TypedRef[D: Definition = Definition](_Ref):
    """A reference to a resolved `Definition` type.

    ## Notes
    - The type of references need to be resolved *during* the final stage
    - This doesn't *need* to happen at the beginning of conversion
    - But must be known before trying to synthesize base class typed dicts
    """

    type: type[D]

    def as_base(self) -> str:
        return self.ref

    def display(self) -> str:
        """Debug repr."""
        return f"{self.__class__.__name__}[{self.type.__name__}]({self.ref!r})"

    def with_refs(self, repl: RefRepl, /) -> Self:
        return self

    def __str__(self) -> TypeExpr:
        return TypeExpr(self.ref)


@t.final
class TypedExtRef[D: Definition = Definition](_ExtRef):
    """A reference to a resolved `Definition` type, originated from an external module."""

    type: type[D]

    def as_base(self) -> str:
        return self.ref

    def with_refs(self, repl: RefRepl, /) -> Self:
        return self

    def __str__(self) -> TypeExpr:
        # NOTE: later, it might make sense to be smarter about using `ext.ref` to avoid collisions
        return TypeExpr(self.ref)
