"""Things that are definitely not type expressions."""

from __future__ import annotations

import typing as t
from typing import ClassVar

from tools.ir.pyir.base import Lines, PyIR


class Value(PyIR):
    value: ClassVar[str]

    def __init_subclass__(cls, value: str, **kwds: t.Any) -> None:
        super().__init_subclass__(**kwds)
        cls.value = value

    def iter_lines(self) -> Lines:
        yield self.value


@t.final
class PyTrue(Value, value="True"): ...


@t.final
class PyFalse(Value, value="False"): ...
