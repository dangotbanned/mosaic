"""Building on top of generated `TypedDict`s.

## Tasks
- [ ] `Spec = SpecHead & Component`
"""

from __future__ import annotations

import dataclasses
import enum
from typing import TYPE_CHECKING, Final, Literal as L, NewType, assert_never

# TODO @dangotbanned: Remove alias after `"pyright>1.1.411"` updates `typing_extensions` stubs
from typing_extensions import Sentinel as sentinel  # ruff: ignore[camelcase-imported-as-lowercase]

from tools.codegen.docstrings import doc

if TYPE_CHECKING:
    from collections.abc import Iterator

PYRIGHT: Final = False
"""In pyroject.toml, this is `tool.pyright.defineConstant = { "PYRIGHT" = true }`"""

if PYRIGHT:
    # NOTE: `Final` is a workaround for https://github.com/microsoft/pyright/issues/10744#issuecomment-5133597898
    # but this breaks `sentinel` for `ty`
    NoTotal: Final = sentinel("NoTotal")
    NoClosed: Final = sentinel("NoClosed")
    NoExtraItems: Final = sentinel("NoExtraItems")
else:
    NoTotal = sentinel("NoTotal")
    NoClosed = sentinel("NoClosed")
    NoExtraItems = sentinel("NoExtraItems")

type TypeExpr = str
"""A string encoding a [type expression][1].

[1]: https://typing.python.org/en/latest/spec/annotations.html#type-and-annotation-expressions
"""

RuntimeTypeExpr = NewType("RuntimeTypeExpr", str)
"""A [type expression][1] that must be valid outside of [Annotation scopes][2].

[1]: https://typing.python.org/en/latest/spec/annotations.html#type-and-annotation-expressions
[2]: https://docs.python.org/3/reference/executionmodel.html#annotation-scopes
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


INDENT: Final = 4 * " "


def iter_lines(
    name: str,
    fields: tuple[Field, ...] = (),
    *,
    bases: tuple[str, ...] = (),
    total: L[False] | NoTotal = NoTotal,
    closed: bool | NoClosed = NoClosed,
    extra_items: RuntimeTypeExpr | NoExtraItems = NoExtraItems,
) -> Iterator[str]:
    # NOTE: Will need to report what has been imported through the duration of writing a module
    bases = bases or ("TypedDict",)
    kwds: dict[str, str | bool] = (
        {} if extra_items is NoExtraItems else {"extra_items": extra_items}
    )

    if closed is not NoClosed:
        if kwds:
            msg = f"Cannot combine closed={closed!r} and extra_items"
            raise TypeError(msg)
        kwds["closed"] = closed

    if total is not NoTotal:
        kwds["total"] = total
        non_default = Qualifier.REQUIRED
    else:
        non_default = Qualifier.DEFAULT

    if fields:
        if total is NoTotal:
            n = len(fields)
            n_required = sum(fld.required for fld in fields)
            if not n_required or n_required <= (n / 2):
                kwds["total"] = False
                non_default = Qualifier.REQUIRED
            elif n_required == n:
                non_default = Qualifier.DEFAULT
            else:
                # NOTE: Might be lucky enough to not hit this
                non_default = Qualifier.NOT_REQUIRED

        kwds_str = ", ".join(f"{k}={v}" for k, v in kwds.items())
        yield f"class {name}({', '.join(bases)}, {kwds_str}):"

        # TODO @dangotbanned: Put the field types somewhere for import deps
        for field in fields:
            for line in field.iter_lines(non_default):
                yield f"{INDENT}{line}"

    else:
        kwds_str = ", ".join(f"{k}={v}" for k, v in kwds.items())
        yield f"class {name}({', '.join(bases)}, {kwds_str}): ..."


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
