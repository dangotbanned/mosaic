"""Building on top of generated `TypedDict`s."""

from __future__ import annotations

import dataclasses
import enum
from itertools import chain
from typing import TYPE_CHECKING, Final, Literal as L, assert_never

from tools.codegen.docstrings import doc

if TYPE_CHECKING:
    from collections.abc import Iterator, Sequence


type TypeExpr = str
"""A string encoding a [type expression][1].

[1]: https://typing.python.org/en/latest/spec/annotations.html#type-and-annotation-expressions
"""

type Line = str
"""An unindented line of code."""


class Qualifier(enum.Enum):
    # there's `ReadOnly` too, but doesn't fit this use-case
    DEFAULT = "{0}"
    """Use when all are required"""

    REQUIRED = "Required[{0}]"
    """Use this when `total=False`/less than half are required"""

    NOT_REQUIRED = "NotRequired[{0}]"
    """Use this when `total` isn't provided/more than half are required"""

    @classmethod
    def from_fields(cls, fields: Sequence[Field], /) -> Qualifier:
        n = len(fields)
        n_required = sum(fld.required for fld in fields)
        if not n_required or n_required <= (n / 2):
            return Qualifier.REQUIRED
        if n_required != n:
            return Qualifier.NOT_REQUIRED
        return Qualifier.DEFAULT


INDENT: Final = 4 * " "


def _join_keywords(kwds: dict[str, str | bool | None]) -> str:
    """Drop everything that is a default."""
    return ", ".join(f"{k}={v}" for k, v in kwds.items() if v is not None)


def iter_lines(
    name: str,
    fields: tuple[Field, ...] = (),
    *,
    bases: tuple[str, ...] = ("TypedDict",),
    total: L[False] | None = None,
    closed: L[True] | None = None,
    extra_items: TypeExpr | None = None,
) -> Iterator[str]:
    if closed and extra_items:
        msg = f"Cannot combine closed={closed!r} and extra_items={extra_items!r}"
        raise TypeError(msg)
    kwds = {"total": total, "closed": closed, "extra_items": extra_items}
    if not fields:
        yield f"class {name}({', '.join(bases)}, {_join_keywords(kwds)}): ..."
        return
    if total is False:
        non_default = Qualifier.REQUIRED
    else:
        non_default = Qualifier.from_fields(fields)
        if non_default is Qualifier.REQUIRED:
            kwds["total"] = False
    yield f"class {name}({', '.join(bases)}, {_join_keywords(kwds)}):"
    for line in chain.from_iterable(fld.iter_lines(non_default) for fld in fields):
        yield f"{INDENT}{line}"


Q = Qualifier


@dataclasses.dataclass(slots=True)
class Field:
    name: str
    tp: TypeExpr

    description: str = ""
    _: dataclasses.KW_ONLY
    required: bool = False

    def iter_lines(self, base_q: Qualifier) -> Iterator[Line]:
        # base_q is the one that needs to be shown, because the default is the opposite
        self_q = Q.REQUIRED if self.required else Q.NOT_REQUIRED
        match (self_q, base_q):
            case (_, Q.DEFAULT) | (Q.NOT_REQUIRED, Q.REQUIRED) | (Q.REQUIRED, Q.NOT_REQUIRED):
                ann = self.tp
            case (q, _):
                ann = q.value.format(self.tp)
            case _:
                assert_never((self_q, base_q))

        yield f"{self.name}: {ann}"
        if desc := self.description:
            yield doc(desc)
