from __future__ import annotations

from collections.abc import Collection, Sequence
from datetime import date
from typing import TYPE_CHECKING, Any, Literal, TypeAlias, TypedDict, TypeVar, overload

if TYPE_CHECKING:
    from typing_extensions import Unpack


_T = TypeVar("_T")

ParamLiteral: TypeAlias = str | float | bool | None
"""Literal Param values."""

ParamDate: TypeAlias = dict[Literal["date"], str]


@overload
def _resolve(v: None, param_names: dict[int, str]) -> None: ...
@overload
def _resolve(v: list[Any], param_names: dict[int, str]) -> list[Any]: ...
@overload
def _resolve(
    v: dict[str, Any] | _SelectionOpts, param_names: dict[int, str]
) -> dict[str, Any]: ...
@overload
def _resolve(v: _ParamBase, param_names: dict[int, str]) -> str | _ParamBase: ...
@overload
def _resolve(v: _T, param_names: dict[int, str]) -> _T: ...
def _resolve(
    v: _T | Any, param_names: dict[int, str]
) -> str | _ParamBase | list[Any] | dict[str, Any] | _T | None:
    """Recursively resolve _ParamBase objects to "$name" ref strings."""
    if isinstance(v, _ParamBase):
        name = param_names.get(id(v))
        return f"${name}" if name is not None else v
    if isinstance(v, list):
        return [_resolve(x, param_names) for x in v]
    if isinstance(v, dict):
        return {k: _resolve(val, param_names) for k, val in v.items()}  # ty: ignore[invalid-return-type]
    return v


class _ParamBase:
    """Base for Param and Selection instances used as param ref tokens."""

    def param_def(self, *, param_names: dict[int, str]) -> Any:
        raise NotImplementedError


class ParamValue(_ParamBase):
    def __init__(self, value: ParamLiteral | ParamDate = None) -> None:
        self._value: ParamLiteral | ParamDate = value

    def param_def(self, *, param_names: dict[int, str]) -> ParamLiteral | ParamDate:
        if isinstance(self._value, date):
            return {"date": self._value.isoformat()}

    def __repr__(self) -> str:
        return f"param.value({self._value!r})"


class ParamArray(_ParamBase):
    def __init__(self, values: IntoParamArray) -> None:
        self._values: list[ParamLiteral | IntoParamRef] = list(values)

    def param_def(self, *, param_names: dict[int, str]) -> list[Any]:
        return [_resolve(v, param_names) for v in self._values]

    def __repr__(self) -> str:
        return f"param.array({self._values!r})"


# NOTE: `"value"` is mentioned in the docs, but not the type?
_Select: TypeAlias = Literal["crossfilter", "intersect", "single", "union"]
"""The type of reactive parameter.

One of:
- `"intersect"` for a `Selection` that intersects clauses (logical "and")
- `"union"` for a `Selection` that unions clauses (logical "or")
- `"single"` for a `Selection` that retains a single clause only
- `"crossfilter"` for a cross-filtered intersection `Selection`
"""


class _SelectionOpts(TypedDict, total=False):
    cross: bool
    """A flag for cross-filtering, where selections made in a plot filter others but not oneself.

    (default `False`, except for `crossfilter` selections).
    """

    empty: bool
    """A flag for setting an initial empty selection state.

    - If `True`, a selection with no clauses corresponds to an empty selection with no records.
    - If `False`, a selection with no clauses selects all values.
    """

    include: IntoParamRef | Collection[IntoParamRef]
    """Upstream selections whose clauses should be included as part of this selection.

    Any clauses or activations published to the upstream selections will be relayed to this selection.
    """


class SelectionDef(_ParamBase):
    def __init__(self, select: _Select, **opts: Unpack[_SelectionOpts]) -> None:
        self._select: _Select = select
        self._opts: _SelectionOpts = opts

    def param_def(self, *, param_names: dict[int, str]) -> dict[str, str | Any]:
        d = {"select": self._select}
        d.update(_resolve(self._opts, param_names))
        return d

    def __repr__(self) -> str:
        opts = ", ".join(f"{k}={v!r}" for k, v in self._opts.items())
        return f"selection.{self._select}({opts})"


ParamDef: TypeAlias = ParamValue | ParamArray | SelectionDef
"""A Param or Selection definition."""


# TODO @dangotbanned: Figure out if this is before/after `$`-prefixing
ParamRef: TypeAlias = str

IntoParamRef: TypeAlias = ParamDef | ParamRef
"""Anything that can be resolved into a `ParamRef`."""

IntoParamArray: TypeAlias = Sequence[ParamLiteral | IntoParamRef]


# TODO @dangotbanned: Make `Param*` generic?
@overload
def param(value: ParamLiteral | ParamDate = None) -> ParamValue: ...
@overload
def param(value: IntoParamArray) -> ParamArray: ...
@overload
def param(
    value: ParamLiteral | ParamDate | IntoParamArray,
) -> ParamArray | ParamValue: ...
def param(
    value: ParamLiteral | ParamDate | IntoParamArray = None,
) -> ParamArray | ParamValue:
    if isinstance(value, Sequence) and not isinstance(value, str):
        # NOTE: Not sure how `int` got in there?
        #   `int & Sequence[object]`
        return ParamArray(value)  # ty: ignore[invalid-argument-type]
    return ParamValue(value)


class selection:
    """Namespace for creating selection params."""

    @staticmethod
    def intersect(**opts: Unpack[_SelectionOpts]) -> SelectionDef:
        return SelectionDef("intersect", **opts)

    @staticmethod
    def crossfilter(**opts: Unpack[_SelectionOpts]) -> SelectionDef:
        return SelectionDef("crossfilter", **opts)

    @staticmethod
    def union(**opts: Unpack[_SelectionOpts]) -> SelectionDef:
        return SelectionDef("union", **opts)

    @staticmethod
    def single(**opts: Unpack[_SelectionOpts]) -> SelectionDef:
        return SelectionDef("single", **opts)
