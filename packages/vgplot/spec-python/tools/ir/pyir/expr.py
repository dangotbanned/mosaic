from __future__ import annotations

import typing as t
from typing import Literal as L

from tools.ir.pyir.base import Expr, TypeExpr, join_comma, join_or
from tools.models import base

if t.TYPE_CHECKING:
    from tools.common import PyIdentifierSnake
    from tools.ir.pyir import value
    from tools.ir.pyir.field import Field


@t.final
class DynExpr(Expr):
    """A simple, lightweight expression.

    Represents some stdlib type with 0 or minimal configuration.
    """

    tp_expr: TypeExpr
    requires: tuple[str, ...] = ()

    def __str__(self) -> TypeExpr:
        return self.tp_expr


def _expr(s: str, *requires: str) -> DynExpr:
    return DynExpr(tp_expr=TypeExpr(s), requires=requires)


EMPTY_TUPLE: t.Final = _expr("tuple[()]")
ANY: t.Final = _expr("Any", "typing.Any")
STR: t.Final = _expr("str")
INT: t.Final = _expr("int")
FLOAT: t.Final = _expr("float")
BOOL: t.Final = _expr("bool")
MAPPING_STR_ANY: t.Final = _expr("Mapping[str, Any]", "collections.abc.Mapping", "typing.Any")
MAPPING_STR_STR: t.Final = _expr("Mapping[str, str]", "collections.abc.Mapping")


@t.final
class PyNone(Expr):
    _tp_expr: t.ClassVar[TypeExpr] = TypeExpr("None")

    def __str__(self) -> TypeExpr:
        return self._tp_expr

    @property
    def value(self) -> str:
        return self._tp_expr


type LiteralMember = base.Lit | value.PyTrue | value.PyFalse | PyNone


# technically a special-form
@t.final
class Literal(Expr):
    """A representation of an `typing.Literal`."""

    members: tuple[LiteralMember, ...]

    _ALIAS: t.ClassVar[L["Literal", "L", "Lit"]] = "L"

    def __str__(self) -> TypeExpr:
        members = sorted(repr(m) if isinstance(m, str) else m.value for m in self.members)
        return TypeExpr(f"{self._ALIAS}[{join_comma(members)}]")

    @classmethod
    def from_name(cls, name: PyIdentifierSnake, /) -> Literal:
        return Literal(members=(base.Lit(name),))


class Union(Expr):
    """A representation of an implicit `typing.Union`."""

    # this will get the converted `VariantHomogeneousTuple`
    members: tuple[Expr, ...]

    def __str__(self) -> TypeExpr:
        return join_or(m.__str__() for m in self.members)


@t.final
class Sequence(Expr):
    """A representation of a `collections.abc.Sequence`."""

    expr: Expr
    _ALIAS: t.ClassVar[L["Sequence"]] = "Sequence"

    def __str__(self) -> TypeExpr:
        return TypeExpr(f"{self._ALIAS}[{self.expr}]")


@t.final
class HomogeneousTuple(Expr):
    expr: Expr
    length: int

    def __str__(self) -> TypeExpr:
        tp = self.expr.__str__()
        return TypeExpr(f"tuple[{join_comma(tp for _ in range(self.length))}]")


@t.final
class Annotated(Expr):
    """A representation of an `typing.Annotated`."""

    origin: Expr
    metadata: tuple[Expr, ...]

    _ALIAS: t.ClassVar[L["Annotated", "A", "An", "Ann"]] = "A"

    def __str__(self) -> TypeExpr:
        return TypeExpr(
            f"{self._ALIAS}[{self.origin}, {join_comma(m.__str__() for m in self.metadata)}]"
        )


# NOTE: A new invention?
@t.final
class NamedTuple(Expr):
    """A structural named tuple.

    You could think of this as similar to `typing.NamedTuple`, but it doesn't have a name *itself* and
    the "field names" are merely annotations.

    ## Examples
    Full verbosity version:

    ```py
    class ChannelDomainSort(TypedDict, total=False, closed=True):
        limit: float | tuple[Annotated[float, Literal["lo"]], Annotated[float, Literal["hi"]]]
    ```

    With single character aliases:

    ```py
    class ChannelDomainSort(TypedDict, total=False, closed=True):
        limit: float | tuple[A[float, L["lo"]], A[float, L["hi"]]]
    ```
    With an additional helper alias (`Field`), to lookcloser to `name: ann`:

    ```py
    class ChannelDomainSort(TypedDict, total=False, closed=True):
        limit: float | tuple[Field[L["lo"], float], Field[L["hi"], float]]


    # impl
    _Name = TypeVar("_Name", bound=LiteralString)
    _T = TypeVar("_T")
    Field = TypeAliasType("Field", A[_T, _Name], type_params=(_Name, _T))
    ```
    """

    fields: tuple[Field[Expr], ...]

    def __str__(self) -> TypeExpr:
        exprs = (
            Annotated(origin=fld.expr, metadata=(Literal.from_name(fld.name),))
            for fld in self.fields
        )
        return TypeExpr(f"tuple[{join_comma(e.__str__() for e in exprs)}]")


@t.final
class ForwardRef(Expr):
    """A [stringified][1] type expression.

    [1]: https://typing.python.org/en/latest/spec/annotations.html#string-annotations
    """

    expr: Expr

    def __str__(self) -> TypeExpr:
        return TypeExpr(f'"{self.expr}"')
