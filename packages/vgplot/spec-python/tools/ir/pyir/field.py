from __future__ import annotations

import re
import typing as t

from tools.common import copy_replace
from tools.ir.pyir.base import Expr, IterExprs, Lines, PyIR, RefRepl
from tools.ir.pyir.qualifier import Required

if t.TYPE_CHECKING:
    from tools.common import PyIdentifierSnake


_T = t.TypeVar("_T", bound=Expr | Required, default=Expr | Required, covariant=True)


_INDENT = "    "

_THE_INTERVAL_MAY_BE = r"[a-zA-Z ]+"
"""An edge case for [ScaleOptions.interval][1].

[1]: https://github.com/dangotbanned/mosaic/blob/f625cb34644a16b1f55fd9b52eb0706939e33a0e/packages/vgplot/spec/src/spec/marks/Axis.ts#L9-L22
"""

_PATTERN_ONE_OF = re.compile(rf"[\.;,]({_THE_INTERVAL_MAY_BE})? one of:$", re.IGNORECASE)
"""Many (193) docs end with this on their first line.

Following that, there's an unordered list - which may or may not be separated by newlines.
"""

_REPLACE_ONE_OF = f".\n\n{_INDENT}One of:"
"""So we make all variations of it the same."""


@t.final
class Field(PyIR, t.Generic[_T]):  # ruff: ignore[non-pep695-generic-class]
    name: PyIdentifierSnake
    # NOTE: **Do not upgrade this to PEP 695**.
    # `pyright` is not inferring the variance correctly
    expr: t.Final[_T]
    doc: str = ""

    def iter_lines(self) -> Lines:
        yield f"{self.name}: {self.expr}"
        if doc := self.doc:
            lines = doc.splitlines()
            if len(lines) == 1:
                yield f'"""{doc}"""'
            else:
                it = iter(lines)
                first = next(it)
                if _PATTERN_ONE_OF.search(first):
                    yield f'"""{_PATTERN_ONE_OF.sub(_REPLACE_ONE_OF, first)}'
                    if second := next(it):
                        yield second
                else:
                    yield f'"""{first}'
                yield from it
                yield '"""'

    def iter_exprs(self) -> IterExprs:
        yield from self.expr.iter_exprs()  # ty: ignore[invalid-argument-type]

    # NOTE: Captures `NamedTuple` always being `Required`
    @t.overload
    def with_refs(self: Field[Expr], repl: RefRepl, /) -> Field[Expr]: ...
    @t.overload
    def with_refs(self: Field[Required], repl: RefRepl, /) -> Field[Required]: ...
    @t.overload
    def with_refs(self, repl: RefRepl, /) -> Field: ...
    def with_refs(self, repl: RefRepl, /) -> Field:
        current = self.expr
        maybe_changed = self.expr.with_refs(repl)  # ty: ignore[invalid-argument-type]
        if current == maybe_changed:
            return self
        return copy_replace(self, expr=maybe_changed)
