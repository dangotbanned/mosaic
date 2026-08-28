"""The subset of [Special forms] that cannot be used in type expressions.

[Special forms]: https://typing.python.org/en/latest/spec/glossary.html#term-special-form:
"""

from __future__ import annotations

from tools.ir.pyir.base import PyIR


class TypedDict(PyIR):
    """A reference the *name* `TypedDict` in a base class list."""


# TODO @dangotbanned: `type_params: tuple[TypeVar, ...]`
class Generic(PyIR):
    """A subscript of `Generic` in a base class list."""
