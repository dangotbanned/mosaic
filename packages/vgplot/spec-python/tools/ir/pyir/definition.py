from __future__ import annotations

import typing as t
from itertools import chain
from typing import Literal as L

from tools.codegen.docstrings import doc
from tools.ir.pyir import special as sf
from tools.ir.pyir.base import (
    INDENT,
    Definition,
    Expr,
    IterExprs,
    Lines,
    RuntimeScope,
    TypedExtRef,
    TypedRef,
    join_comma,
)

if t.TYPE_CHECKING:
    from collections.abc import Iterator

    from tools.ir.pyir.field import Field
    from tools.ir.pyir.type_param import TypeVar


@t.final
class TypeAlias[E: Expr = Expr](Definition):
    """A representation of a TypeAliasType."""

    expr: RuntimeScope[E]
    type_params: RuntimeScope[tuple[TypeVar, ...]] = ()

    _ALIAS: t.ClassVar[L["TypeAliasType"]] = "TypeAliasType"

    def iter_lines(self) -> Lines:
        params = f", {self.expr}"
        if type_params := self.type_params:
            params = f", type_params = {join_comma(tp.as_ref() for tp in type_params)}"
        yield f"{self.name} = {self._ALIAS}({self.name!r}{params})"
        if self.doc:
            yield doc(self.doc)

    def iter_exprs(self) -> IterExprs:
        yield from self.expr.iter_exprs()
        for param in self.type_params:
            yield from param.iter_exprs()


@t.final
class NewTypeStr(Definition):
    """A representation of a NewType, where the runtime type is unconditionally `str`.

    `str` is the only use-case I have for `NewType`, so this'll do for now.
    """

    def iter_lines(self) -> Lines:
        yield f"{self.name} = NewType({self.name!r}, str)"
        if self.doc:
            yield doc(self.doc)

    def iter_exprs(self) -> IterExprs:
        yield from ()


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

    def iter_exprs(self) -> IterExprs:
        for f in self.fields:
            yield from f.iter_exprs()


type BaseTD = sf.TypedDict | sf.Generic | TypedRef[OpenDict] | TypedExtRef[OpenDict]
"""Any type that is valid to use in the bases of a `TypedDict`.

Where one or more of these symbols appear as below:

```py
class TD(<BaseTD>, ...):...
```

## Important
This definition is *intentionally narrower* than what [the spec defines][1],
and is aimed to be an easier to understand subset.

In short:

1. By default, the `TypedDict` special-form will be the only type that is present.
2. Synthesizing a generic will add `Generic[T, ...]`.
3. Synthesizing a base class will add `<name of new base>`.

`OpenDict` and `Generic` can only be generated explicitly,
whereas `{Closed,Extra}Dict` are created during conversion of JSON Schema.

[1]: https://typing.python.org/en/latest/spec/typeddict.html#inheritance
"""


class _Dict(Definition):
    fields: tuple[Field, ...]
    bases: RuntimeScope[tuple[BaseTD, ...]] = (sf.TYPED_DICT,)
    total: bool = False

    def keywords(self) -> Iterator[str]:
        """Keyword arguments, as defined [here](https://typing.python.org/en/latest/spec/typeddict.html#class-based-syntax)."""
        if not self.total:
            yield "total=False"

    def iter_lines(self) -> Lines:
        inheritance_list = join_comma(
            chain((base.as_base() for base in self.bases), self.keywords())
        )
        yield f"class {self.name}({inheritance_list}):"
        if self.doc:
            yield doc(f"{INDENT}{self.doc}")
        for line in chain.from_iterable(fld.iter_lines() for fld in self.fields):
            yield f"{INDENT}{line}"

    def iter_exprs(self) -> IterExprs:
        for f in self.fields:
            yield from f.iter_exprs()
        for base in self.bases:
            yield from base.iter_exprs()


@t.final
class OpenDict(_Dict): ...


@t.final
class ClosedDict(_Dict):
    def keywords(self) -> Iterator[str]:
        yield from super().keywords()
        yield "closed=True"


@t.final
class ExtraDict(_Dict):
    extra_items: RuntimeScope[Expr]

    def keywords(self) -> Iterator[str]:
        yield from super().keywords()
        yield from self.extra_items.iter_lines()

    def iter_exprs(self) -> IterExprs:
        yield from super().iter_exprs()
        yield from self.extra_items.iter_exprs()
