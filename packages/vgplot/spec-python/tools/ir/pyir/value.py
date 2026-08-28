"""Things that are definitely not type expressions."""

from __future__ import annotations

import typing as t
from typing import ClassVar

from tools.ir.pyir.base import Lines, PyIR


class Value(PyIR):
    value: ClassVar[str]

    def iter_lines(self) -> Lines:
        yield self.value


@t.final
class PyTrue(Value):
    value: ClassVar[str] = "True"


@t.final
class PyFalse(Value):
    value: ClassVar[str] = "False"
