from __future__ import annotations

import typing as t
from typing import LiteralString as LS

from tools.models import base

if t.TYPE_CHECKING:
    import collections.abc as cabc

    from tools.common import PyIdentifier, PyIdentifierSnake


type Line = str
"""An unindented line of code.

Indents are handled by definitions.
"""

type Lines = cabc.Iterator[Line]
"""The return type of `PyIR.iter_lines`."""

TypeExpr = t.NewType("TypeExpr", str)
"""A rendered type expression."""

type IterExprs = cabc.Iterator[Expr]

if t.TYPE_CHECKING:

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


class Definition(PyIR):
    """A named definition."""

    name: PyIdentifier
    doc: str = ""

    def as_ref(self) -> TypeExpr:
        """Refer to this symbol as a type expression."""
        return TypeExpr(self.name)


class UntypedRef(Expr):
    """Placeholder for `TypedRef`."""

    ref: PyIdentifier


class UntypedExtRef(Expr):
    """Placeholder for `TypedExtRef`."""

    ext: PyIdentifierSnake
    ref: PyIdentifier


class TypedRef[T: PyIR](PyIR):
    """A reference to a resolved `PyIR` type.

    ## Notes
    - The type of references need to be resolved *during* the final stage
    - This doesn't *need* to happen at the beginning of conversion
    - But must be known before trying to synthesize base class typed dicts
    """

    ref: PyIdentifier
    type: type[T]

    def as_base(self) -> str:
        return self.ref

    def iter_exprs(self) -> IterExprs:
        yield from ()


class TypedExtRef[T: PyIR](PyIR):
    """A reference to a resolved `PyIR` type, originated from an external module."""

    ext: PyIdentifierSnake
    ref: PyIdentifier
    type: type[T]

    def as_base(self) -> str:
        return self.ref

    def iter_exprs(self) -> IterExprs:
        yield from ()
