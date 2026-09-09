"""External dependencies for a module."""

from __future__ import annotations

import functools
import typing as t
from itertools import chain
from typing import Literal as L

from tools.ir.pyir import definition, expr, special as sf
from tools.ir.pyir.base import (
    Definition,
    Lines,
    PyIR,
    TypedExtRef,
    TypedRef,
    UntypedExtRef,
    UntypedRef,
)
from tools.ir.pyir.definition import ClosedDict, ExtraDict, OpenDict
from tools.ir.pyir.field import Field
from tools.ir.pyir.qualifier import ReadOnly, Required
from tools.ir.pyir.type_param import TypeVar
from tools.models import base, config as cfg

if t.TYPE_CHECKING:
    import collections.abc as cabc

    from tools.common import PyIdentifier, PyIdentifierSnake

__all__ = ("Resolver",)

type CanonicalPath = str
type Dep = StdDep | PartialDep
type Dependencies = cabc.Iterable[Dep]
type _StdModule = L["typing", "collections.abc"]
type _StdName = L[
    "Any",
    "Annotated",
    "Literal",
    "NewType",
    "NamedTuple",
    "TypedDict",
    "Required",
    "ReadOnly",
    "TypeAliasType",
    "TypeVar",
    "Generic",
    "Mapping",
    "Sequence",
]


@t.final
class StdDep(base.FrozenHashableStruct, kw_only=False):
    module: _StdModule
    name: _StdName

    def resolve(self, resolver: Resolver, /) -> str:
        return resolver._resolve_std_dep(self)


@t.final
class PartialDep(base.FrozenHashableStruct, kw_only=False):
    module: PyIdentifierSnake
    name: PyIdentifier

    def resolve(self, resolver: Resolver, /) -> str:
        return resolver._resolve_partial_dep(self)


# TODO @dangotbanned: `_missing_from_data_model` -> derive from some section of `PyIRConfig`
# - Maybe `name`, but could be a new section entirely
# TODO @dangotbanned: finalize attribute names, add `__slots__`
# TODO @dangotbanned: finalize constructor, add to class doc
class Resolver:
    """Resolve the imports required for each module.

    The lifetime of a `Resolved` is tied to a single run of an `App`.
    If any changes are made to a module or configuration, a new `Resolver` should be created to avoid
    invalid cache entries.
    """

    def __init__(
        self, modules: cabc.Mapping[PyIdentifierSnake, CanonicalPath], config: cfg.PyIRNameConfig, /
    ) -> None:
        # NOTE: `(Typed)ExtRef` is lossy
        # - It doesn't include the full canonical path.
        # - Hasn't been an issue for my use case, but would be if any modules shared
        #   the same name (but lived in different sub-packages)
        self._canonical: cabc.Mapping[PyIdentifierSnake, CanonicalPath] = modules
        self._aliases: cfg.PyIRAliases = config.aliases
        self._missing_from_data_model: cabc.Mapping[_StdName, CanonicalPath] = {
            "Required": "mosaic_spec._typing_compat",
            "TypeAliasType": "mosaic_spec._typing_compat",
            "TypeVar": "mosaic_spec._typing_compat",
            "TypedDict": "mosaic_spec._typing_compat",
        }
        self._cache: dict[Dep, str] = {}

    def iter_imports(self, definitions: cabc.Iterable[Definition], /) -> Lines:
        """Yield every unique dependency in `definitions` as an import statement."""
        if deps := frozenset(chain.from_iterable(_find_deps(defn) for defn in definitions)):
            yield from self._iter_resolve(deps)

    def _resolve_partial_dep(self, dep: PartialDep, /) -> str:
        return f"from {self._canonical[dep.module]} import {dep.name}"

    def _resolve_std_dep(self, dep: StdDep, /) -> str:
        name = dep.name
        module = self._missing_from_data_model.get(name, dep.module)
        as_name = self._aliases.get_alias(dep.module, name)
        return f"from {module} import {name}{'' if as_name == name else f' as {as_name}'}"

    def _iter_resolve(self, deps: cabc.Iterable[Dep], /) -> Lines:
        for dep in deps:
            if not (result := self._cache.get(dep)):
                result = self._cache[dep] = dep.resolve(self)
            yield result


_CONSTANT: t.Final[cabc.Mapping[type[PyIR], Dependencies]] = {
    expr.Any: (StdDep("typing", "Any"),),
    sf.TypedDict: (StdDep("typing", "TypedDict"),),
    expr.Literal: (StdDep("typing", "Literal"),),
    definition.NewTypeStr: (StdDep("typing", "NewType"),),
    expr.PyNone: (),
    expr.DynExpr: (),
    TypedRef: (),
    UntypedRef: (),
}
"""Types that always have *the same* dependency.

The question can be answered by the class alone.
"""


_CONSTANT_PLUS_DESCENDANTS: t.Final[cabc.Mapping[type[PyIR], StdDep]] = {
    expr.Mapping: StdDep("collections.abc", "Mapping"),
    expr.Sequence: StdDep("collections.abc", "Sequence"),
    Required: StdDep("typing", "Required"),
    ReadOnly: StdDep("typing", "ReadOnly"),
    sf.Generic: StdDep("typing", "Generic"),
    definition.TypeAlias: StdDep("typing", "TypeAliasType"),
    TypeVar: StdDep("typing", "TypeVar"),
    definition.NamedTuple: StdDep("typing", "NamedTuple"),
    expr.Annotated: StdDep("typing", "Annotated"),
}
"""Types that introduce a constant dependency via the class and variable via the instance's descendants."""


@functools.singledispatch
def _find_deps(node: PyIR) -> Dependencies:
    msg = f"_find_deps() is not yet implemented for {type(node).__name__}, got:\n{node!r}"
    raise NotImplementedError(msg)


def _const(node: PyIR) -> Dependencies:
    return _CONSTANT[node.__class__]


for _tp in _CONSTANT:
    _find_deps.register(_tp, _const)


@_find_deps.register(ReadOnly)
@_find_deps.register(Required)
@_find_deps.register(expr.Sequence)
@_find_deps.register(expr.Mapping)
def _(node: expr.Mapping | expr.Sequence | Required | ReadOnly) -> Dependencies:
    yield _CONSTANT_PLUS_DESCENDANTS[node.__class__]
    yield from _find_deps(node.expr)


@_find_deps.register(definition.TypeAlias)
def _(node: definition.TypeAlias) -> Dependencies:
    yield _CONSTANT_PLUS_DESCENDANTS[node.__class__]
    yield from _find_deps(node.expr)
    for param in node.type_params:
        yield from _find_deps(param)


@_find_deps.register(sf.Generic)
def _(node: sf.Generic) -> Dependencies:
    yield _CONSTANT_PLUS_DESCENDANTS[node.__class__]
    for param in node.type_params:
        yield from _find_deps(param)


@functools.cache
def _from_ext_ref(node: UntypedExtRef | TypedExtRef, /) -> PartialDep:
    return PartialDep(node.ext, node.ref)


@_find_deps.register(TypedExtRef)
@_find_deps.register(UntypedExtRef)
def _(node: UntypedExtRef | TypedExtRef) -> Dependencies:
    yield _from_ext_ref(node)


@_find_deps.register(expr.ForwardRef)
@_find_deps.register(Field)
@_find_deps.register(expr.HomogeneousTuple)
def _(node: expr.HomogeneousTuple | Field | expr.ForwardRef) -> Dependencies:
    return _find_deps(node.expr)


@_find_deps.register(expr.Union)
def _(node: expr.Union) -> Dependencies:
    for m in node.members:
        yield from _find_deps(m)


@_find_deps.register(expr.NamedTuple)
def _(node: expr.NamedTuple) -> Dependencies:
    # NOTE: complicated, this does a transformation at render-time
    # that was clever, but not consistent with how I handled `VariantHomogeneousTuple` expansion
    yield from (StdDep("typing", "Annotated"), StdDep("typing", "Literal"))
    for f in node.fields:
        yield from _find_deps(f.expr)


@_find_deps.register(definition.NamedTuple)
def _(node: definition.NamedTuple) -> Dependencies:
    yield _CONSTANT_PLUS_DESCENDANTS[node.__class__]
    for f in node.fields:
        yield from _find_deps(f.expr)


@_find_deps.register(TypeVar)
def _(node: TypeVar) -> Dependencies:
    yield _CONSTANT_PLUS_DESCENDANTS[node.__class__]
    if bound := node.bound:
        yield from _find_deps(bound)
    for con in node.constraints:
        yield from _find_deps(con)


@_find_deps.register(expr.Annotated)
def _(node: expr.Annotated) -> Dependencies:
    yield _CONSTANT_PLUS_DESCENDANTS[node.__class__]
    yield from _find_deps(node.origin)
    for m in node.metadata:
        yield from _find_deps(m)


@_find_deps.register(ClosedDict)
@_find_deps.register(OpenDict)
def _find_deps_dict(node: OpenDict | ClosedDict | ExtraDict) -> Dependencies:
    for f in node.fields.values():
        yield from _find_deps(f.expr)
    for b in node.bases:
        yield from _find_deps(b)


@_find_deps.register(ExtraDict)
def _(node: ExtraDict) -> Dependencies:
    yield from _find_deps_dict(node)
    yield from _find_deps(node.extra_items)
