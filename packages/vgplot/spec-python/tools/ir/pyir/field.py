from __future__ import annotations

import typing as t

from tools.codegen.docstrings import doc
from tools.ir.pyir.base import Expr, Lines, PyIdentifier, PyIR
from tools.ir.pyir.qualifier import NotRequired, Required


@t.final
class Field[T: Expr | Required | NotRequired = Expr | Required | NotRequired](PyIR):
    name: PyIdentifier
    expr: t.Final[T]
    doc: str = ""

    def iter_lines(self) -> Lines:
        yield f"{self.name}: {self.expr}"
        if self.doc:
            yield doc(self.doc)
