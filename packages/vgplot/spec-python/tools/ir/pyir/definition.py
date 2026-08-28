from __future__ import annotations

import typing as t
from itertools import chain
from typing import Literal as L

from tools.codegen.docstrings import doc
from tools.ir.pyir.base import INDENT, Definition, Expr, Lines, join_comma

if t.TYPE_CHECKING:
    from tools.ir.pyir.field import Field
    from tools.ir.pyir.type_param import TypeVar


@t.final
class TypeAlias(Definition):
    """A representation of a TypeAliasType."""

    expr: Expr
    type_params: tuple[TypeVar, ...] = ()

    _ALIAS: t.ClassVar[L["TypeAliasType"]] = "TypeAliasType"

    def iter_lines(self) -> Lines:
        params = ""
        if type_params := self.type_params:
            params = f", {join_comma(tp.as_ref() for tp in type_params)}"
        yield f"{self.name} = {self._ALIAS}({self.name!r}{params})"
        if self.doc:
            yield doc(self.doc)


@t.final
class NewTypeStr(Definition):
    """A representation of a NewType, where the runtime type is unconditionally `str`.

    `str` is the only use-case I have for `NewType`, so this'll do for now.
    """

    def iter_lines(self) -> Lines:
        yield f"{self.name} = NewType({self.name!r}, str)"
        if self.doc:
            yield doc(self.doc)


@t.final
class NamedTuple(Definition):
    """A representation of a `typing.NamedTuple`."""

    # requires `typing.NamedTuple` import
    fields: tuple[Field[Expr], ...]

    def iter_lines(self) -> Lines:
        yield f"class {self.name}(NamedTuple):"
        if self.doc:
            yield doc(f"{INDENT}{self.doc}")
        for line in chain.from_iterable(fld.iter_lines() for fld in self.fields):
            yield f"{INDENT}{line}"


# TODO @dangotbanned: Dicts (total, bases, TypedDict sf)
class OpenDict: ...


# TODO @dangotbanned: Dicts
class ClosedDict: ...


# TODO @dangotbanned: Dicts
class ExtraDict: ...
