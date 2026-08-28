from __future__ import annotations

import typing as t
from typing import Literal as L

from tools.ir.pyir.base import Expr, PyIdentifier, TypeExpr, join_comma
from tools.models import base

if t.TYPE_CHECKING:
    from tools.ir.pyir import value
    from tools.ir.pyir.field import Field


class _Singleton(Expr):
    _tp_expr: t.ClassVar[TypeExpr]

    def __str__(self) -> TypeExpr:
        return self._tp_expr


@t.final
class EmptyTuple(_Singleton):
    _tp_expr: t.ClassVar[TypeExpr] = TypeExpr("tuple[()]")


@t.final
class Any(_Singleton):
    _tp_expr: t.ClassVar[TypeExpr] = TypeExpr("Any")


@t.final
class PyStr(_Singleton):
    _tp_expr: t.ClassVar[TypeExpr] = TypeExpr("str")


@t.final
class PyInt(_Singleton):
    _tp_expr: t.ClassVar[TypeExpr] = TypeExpr("int")


@t.final
class PyFloat(_Singleton):
    _tp_expr: t.ClassVar[TypeExpr] = TypeExpr("float")


@t.final
class PyBool(_Singleton):
    _tp_expr = TypeExpr("bool")


@t.final
class PyNone(_Singleton):
    _tp_expr = TypeExpr("None")

    @property
    def value(self) -> str:
        return self._tp_expr


# technically a special-form
@t.final
class Literal(Expr):
    """A representation of an `typing.Literal`."""

    members: tuple[base.Lit | value.PyTrue | value.PyFalse | PyNone, ...]

    _ALIAS: t.ClassVar[L["Literal", "L", "Lit"]] = "L"

    def __str__(self) -> TypeExpr:
        members = sorted(repr(m) if isinstance(m, str) else m.value for m in self.members)
        return TypeExpr(f"{self._ALIAS}[{join_comma(members)}]")

    @classmethod
    def from_name(cls, name: PyIdentifier, /) -> Literal:
        return Literal(members=(base.Lit(name),))


class Union(Expr):
    """A representation of an implicit `typing.Union`."""

    # this will get the converted `VariantHomogeneousTuple`
    members: tuple[Expr, ...]

    def __str__(self) -> TypeExpr:
        return TypeExpr(" | ".join(m.__str__() for m in self.members))


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
