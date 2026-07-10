"""A fluent take on `plot.py`."""

from __future__ import annotations

from typing import Any, TypeAlias

from vgplot.params_alt import _ParamValue

Incomplete: TypeAlias = Any


class Plot:
    def mark(self) -> Incomplete:
        raise NotImplementedError

    def mark_mapping(self) -> Incomplete:
        raise NotImplementedError

    def directive(self) -> Incomplete:
        raise NotImplementedError

    def view(self) -> Incomplete:
        raise NotImplementedError


class _InteractorSugar(_ParamValue[Incomplete]):
    __slots__ = ()

    def _interactor(self, select: str | Incomplete, **kwds: Any) -> Incomplete: ...
