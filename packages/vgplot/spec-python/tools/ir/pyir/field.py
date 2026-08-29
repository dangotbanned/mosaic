from __future__ import annotations

import typing as t

from tools.codegen.docstrings import doc
from tools.ir.pyir.base import Expr, Lines, PyIR
from tools.ir.pyir.qualifier import NotRequired, Required

if t.TYPE_CHECKING:
    from tools.common import PyIdentifierSnake


@t.final
class Field[T: Expr | Required | NotRequired = Expr | Required | NotRequired](PyIR):
    name: PyIdentifierSnake
    expr: t.Final[T]
    doc: str = ""

    def iter_lines(self) -> Lines:
        yield f"{self.name}: {self.expr}"
        if self.doc:
            yield doc(self.doc)
