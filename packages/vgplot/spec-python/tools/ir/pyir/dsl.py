"""Builder API."""

from __future__ import annotations

import typing as _t
from typing import TYPE_CHECKING, Literal as L

from tools import ds as _ds
from tools.codegen import convert as _name
from tools.ir.pyir import definition as _defn, qualifier as _q, special as _sf
from tools.ir.pyir.field import Field as _Field

if TYPE_CHECKING:
    from tools.ir.pyir import base as _base
    from tools.ir.pyir.definition import ClosedDict as _Closed, OpenDict as _Open

required = _q.Required
type _Ref[D: _base.Definition = _base.Definition] = _base.TypedRef[D] | _base.TypedExtRef[D]


def field[E: _base.Expr | _q.Required](name: str, expr: E, doc: str = "") -> _Field[E]:
    return _Field(name=_name.py_identifier_snake(name), expr=expr, doc=doc)


@_t.overload
def dict[E: _base.Expr | _q.Required](
    name: str,
    *fields: _Field[E],
    closed: L[False] = False,
    total: bool = False,
    bases: tuple[_Ref[_Open], ...] = (),
    doc: str = "",
) -> _Open: ...
@_t.overload
def dict[E: _base.Expr | _q.Required](
    name: str,
    *fields: _Field[E],
    closed: L[True],
    total: bool = False,
    bases: tuple[_Ref[_Open], ...] = (),
    doc: str = "",
) -> _Closed: ...
def dict[E: _base.Expr | _q.Required](
    name: str,
    *fields: _Field[E],
    closed: bool = False,
    total: bool = False,
    bases: tuple[_Ref[_Open], ...] = (),
    doc: str = "",
) -> _Open | _Closed:
    tp_result = _defn.ClosedDict if closed else _defn.OpenDict
    return tp_result(
        name=_name.py_identifier(name),
        fields=_ds.frozenmap((f.name, f) for f in fields),
        bases=bases or (_sf.TYPED_DICT,),
        total=total,
        doc=doc,
    )
