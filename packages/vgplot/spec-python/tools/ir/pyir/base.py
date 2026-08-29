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
        msg = f"{type(self).__name__}.{self.iter_lines.__name__}() is not yet implemented"
        raise NotImplementedError(msg)


class Expr(PyIR):
    """A [type expression][1].

    [1]: https://typing.python.org/en/latest/spec/annotations.html#type-and-annotation-expressions
    """

    def __str__(self) -> TypeExpr:
        """Render the type expression as a string."""
        msg = f"{type(self).__name__}.{self.__str__.__name__}() is not yet implemented"
        raise NotImplementedError(msg)

    def iter_lines(self) -> Lines:
        yield self.__str__()


class Definition(PyIR):
    """A named definition."""

    name: PyIdentifier
    doc: str = ""

    def as_ref(self) -> TypeExpr:
        """Refer to this symbol as a type expression."""
        return TypeExpr(self.name)
