"""The subset of [Special forms] that cannot be used in type expressions.

[Special forms]: https://typing.python.org/en/latest/spec/glossary.html#term-special-form:
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from tools.ir.pyir.base import PyIR

if TYPE_CHECKING:
    from tools.ir.pyir.type_param import TypeVar


class TypedDict(PyIR):
    """A reference the *name* `TypedDict` in a base class list."""


class Generic(PyIR):
    """A subscript of `Generic` in a base class list."""

    type_params: tuple[TypeVar, ...]
