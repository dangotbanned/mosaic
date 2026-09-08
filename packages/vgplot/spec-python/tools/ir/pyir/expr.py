from __future__ import annotations

import typing as t
from typing import Literal as L, Self

from tools.common import copy_replace
from tools.ir.pyir.base import Expr, IterExprs, RefRepl, TypeExpr, join_comma, join_or
from tools.models import base

if t.TYPE_CHECKING:
    from tools.common import PyIdentifierSnake
    from tools.ir.pyir import value
    from tools.ir.pyir.field import Field


@t.final
class DynExpr(Expr, kw_only=False):
    """A simple, lightweight expression that has zero dependencies."""

    tp_expr: TypeExpr

    def __str__(self) -> TypeExpr:
        return self.tp_expr


@t.final
class Any(Expr):
    # NOTE: required `typing.Any`
    _tp_expr: t.ClassVar[TypeExpr] = TypeExpr("Any")

    def __str__(self) -> TypeExpr:
        return self._tp_expr


EMPTY_TUPLE: t.Final = DynExpr(TypeExpr("tuple[()]"))
STR: t.Final = DynExpr(TypeExpr("str"))
INT: t.Final = DynExpr(TypeExpr("int"))
FLOAT: t.Final = DynExpr(TypeExpr("float"))
BOOL: t.Final = DynExpr(TypeExpr("bool"))
ANY: t.Final = Any()


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
    """A representation of a `typing.Literal`.

    This form is more restricted than [Legal parameters for `Literal` at type check time][1].

    [1]: https://typing.python.org/en/latest/spec/literal.html#legal-parameters-for-literal-at-type-check-time
    """

    members: tuple[LiteralMember, ...]

    _ALIAS: t.ClassVar[L["Literal", "L", "Lit"]] = "Literal"

    def __str__(self) -> TypeExpr:
        members = sorted(repr(m) if isinstance(m, str) else m.value for m in self.members)
        return TypeExpr(f"{self._ALIAS}[{join_comma(members)}]")

    @classmethod
    def from_name(cls, name: PyIdentifierSnake, /) -> Literal:
        return Literal(members=(base.Lit(name),))


@t.final
class Union(Expr):
    """A representation of an implicit `typing.Union`."""

    # this will get the converted `VariantHomogeneousTuple`
    members: tuple[Expr, ...]

    def __str__(self) -> TypeExpr:
        return join_or(m.__str__() for m in self.members)

    def iter_exprs(self) -> IterExprs:
        yield self
        for m in self.members:
            yield from m.iter_exprs()

    def with_refs(self, repl: RefRepl, /) -> Union:
        new_members = tuple(member.with_refs(repl) for member in self.members)
        if self.members == new_members:
            return self
        return self.__replace__(members=new_members)


class _HasExpr(Expr):
    expr: Expr

    def iter_exprs(self) -> IterExprs:
        yield self
        yield from self.expr.iter_exprs()

    def with_refs(self, repl: RefRepl, /) -> Self:
        current = self.expr
        maybe_changed = self.expr.with_refs(repl)
        if current == maybe_changed:
            return self
        return copy_replace(self, expr=maybe_changed)


@t.final
class Mapping(_HasExpr):
    """A representation of a `collections.abc.Mapping`, with str keys."""

    def __str__(self) -> TypeExpr:
        return TypeExpr(f"Mapping[str, {self.expr}]")


@t.final
class Sequence(_HasExpr):
    """A representation of a `collections.abc.Sequence`."""

    _ALIAS: t.ClassVar[L["Sequence", "Seq"]] = "Sequence"

    def __str__(self) -> TypeExpr:
        return TypeExpr(f"{self._ALIAS}[{self.expr}]")


@t.final
class HomogeneousTuple(_HasExpr):
    length: int

    def __str__(self) -> TypeExpr:
        tp = self.expr.__str__()
        return TypeExpr(f"tuple[{join_comma(tp for _ in range(self.length))}]")


@t.final
class Annotated(Expr):
    """A representation of a `typing.Annotated`."""

    origin: Expr
    metadata: tuple[Expr, ...]

    _ALIAS: t.ClassVar[L["Annotated", "A", "An", "Ann"]] = "Annotated"

    def __str__(self) -> TypeExpr:
        return TypeExpr(
            f"{self._ALIAS}[{self.origin}, {join_comma(m.__str__() for m in self.metadata)}]"
        )

    def iter_exprs(self) -> IterExprs:
        yield self
        yield from self.origin.iter_exprs()
        for m in self.metadata:
            yield from m.iter_exprs()

    def with_refs(self, repl: RefRepl, /) -> Annotated:
        changes: dict[str, t.Any] = {}
        origin_changed = self.origin.with_refs(repl)
        if origin_changed is not self.origin:
            changes["origin"] = origin_changed
        metadata_changed = tuple(m.with_refs(repl) for m in self.metadata)
        if self.metadata != metadata_changed:
            changes["metadata"] = metadata_changed
        if not changes:
            return self
        return self.__replace__(**changes)


# TODO @dangotbanned: Need to redo this entirely, it complicates dependencies, that it does a transform later
# TODO @dangotbanned: Fix the field order being broken from the first `FrozenMap`
# - Can't sort the keys to fix, because their initial order is significant
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

    def iter_exprs(self) -> IterExprs:
        yield self
        for f in self.fields:
            yield from f.iter_exprs()

    def with_refs(self, repl: RefRepl, /) -> NamedTuple:
        changed = tuple(f.with_refs(repl) for f in self.fields)
        if self.fields == changed:
            return self
        return self.__replace__(fields=changed)


@t.final
class ForwardRef(_HasExpr):
    """A [stringified][1] type expression.

    [1]: https://typing.python.org/en/latest/spec/annotations.html#string-annotations
    """

    def __str__(self) -> TypeExpr:
        return TypeExpr(f'"{self.expr}"')
