"""Building on top of generated `TypedDict`s.

## Tasks
- [ ] `Spec = SpecHead & Component`
"""

from __future__ import annotations

from typing import Any, Final, Literal as L, NewType

from typing_extensions import sentinel

NoTotal = sentinel("NoTotal")
NoClosed = sentinel("NoClosed")
NoExtraItems = sentinel("NoExtraItems")

TypeExpr = NewType("TypeExpr", str)
"""A string encoding a [type expression][1].

[1]: https://typing.python.org/en/latest/spec/annotations.html#type-and-annotation-expressions
"""

RuntimeTypeExpr = NewType("RuntimeTypeExpr", TypeExpr)
"""A [type expression][1] that must be valid outside of [Annotation scopes][2].

[1]: https://typing.python.org/en/latest/spec/annotations.html#type-and-annotation-expressions
[2]: https://docs.python.org/3/reference/executionmodel.html#annotation-scopes
"""

type Incomplete = Any

SPEC: Final = "Spec"
"""Name of the `Spec` union and prefix for it's members"""

SPEC_HEAD: Final = "SpecHead"
"""Name of the base `TypedDict` for all `Spec` members.

Mixing this into the bases with the `Component` member is a limited form of an intersection type.
"""


def t_typed_dict(
    name: str,
    fields: tuple[Incomplete, ...] = (),
    *,
    bases: tuple[str, ...] = (),
    total: L[False] | NoTotal = NoTotal,
    closed: bool | NoClosed = NoClosed,
    extra_items: RuntimeTypeExpr | NoExtraItems = NoExtraItems,
) -> str:
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
    kwds_str = ", ".join(f"{k}={v}" for k, v in kwds.items())
    if fields:
        # NOTE:  Will be needed for the general case, but not yet when only dealing with intersections
        msg_0 = "TODO @dangotbanned: Add support for defining new fields"
        raise NotImplementedError(msg_0)
    return f"class {name}({', '.join(bases)}, {kwds_str}): ..."


def t_spec_member(component_name: str) -> str:
    return t_typed_dict(f"{SPEC}{component_name}", bases=(SPEC_HEAD, component_name), closed=True)
