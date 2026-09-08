"""Builder API."""

from __future__ import annotations

import collections.abc as _cabc
import typing as _t
from typing import TYPE_CHECKING, Literal as L

from tools import ds as _ds
from tools.codegen import convert as _name
from tools.ir.pyir import definition as _defn, expr as _e, qualifier as _q, special as _sf
from tools.ir.pyir.definition import Source
from tools.ir.pyir.field import Field as _Field

if TYPE_CHECKING:
    from tools.ir.pyir import base as _base
    from tools.ir.pyir.definition import ClosedDict as _Closed, OpenDict as _Open

__all__ = "Source", "alias", "dict", "field", "required", "supertype"


type _Ref[D: _base.Definition = _base.Definition] = _base.TypedRef[D] | _base.TypedExtRef[D]
type OneOrIterable[T] = T | _cabc.Iterable[T]
required = _q.Required


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


def alias(name: str, *exprs: _base.Expr, doc: str = "") -> _defn.TypeAlias[_base.Expr | _e.Union]:
    expr_ = exprs[0] if len(exprs) == 1 else _e.Union(members=exprs)
    return _defn.TypeAlias(name=_name.py_identifier(name), expr=expr_, doc=doc)


def supertype(
    name: str,
    definitions: _cabc.Iterable[_Closed],
    *,
    doc: str = "",
    bases: tuple[_defn.BaseTD, ...] = (_sf.TYPED_DICT,),
    exclude: OneOrIterable[str] = frozenset(),
) -> _Open:
    """Approximate a base class that all members of `definitions` can inherit from.

    ## Notes
    - This operation only makes sense if the common fields are non-generic
    - `exclude` should be used for discriminator/generic fields to preserve in children
        - For `MarkOptions`-derived, each `mark` field has unique documentation to preserve
    """
    it = iter(definitions)
    fields = next(it).fields
    first = frozenset(fields)
    common = set(first.difference(exclude if not isinstance(exclude, str) else (exclude,)))
    common.intersection_update(*(defn.fields for defn in it))
    if not common:
        msg = "`definitions` have 0 common fields"
        if isinstance(definitions, _cabc.Collection):
            msg += f", got:\n{definitions!r}"
        raise TypeError(msg)
    fields = _ds.frozenmap((k, v) for k, v in fields.items() if k in common)
    return _defn.OpenDict(name=_name.py_identifier(name), fields=fields, bases=bases, doc=doc)
