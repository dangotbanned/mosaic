"""A limited representation of Python's type system & data model.

## Important
- No classes
- No objects
- No functions/methods/operators
- No AST
- Strictly, things that can be used in the generation of modules containing `TypedDict`s
"""

from __future__ import annotations

from tools.ir.pyir import base, convert, definition, expr, field, module, qualifier, value
from tools.ir.pyir.base import Expr, PyIdentifier, PyIR
from tools.ir.pyir.definition import Definition
from tools.ir.pyir.field import Field
from tools.ir.pyir.module import Module

__all__ = (
    "Definition",
    "Expr",
    "Field",
    "Module",
    "PyIR",
    "PyIdentifier",
    "base",
    "convert",
    "definition",
    "expr",
    "field",
    "module",
    "qualifier",
    "value",
)
