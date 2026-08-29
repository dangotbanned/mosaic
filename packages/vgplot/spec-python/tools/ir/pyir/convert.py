from __future__ import annotations

import typing as t
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tools.ir import mlir, pyir
    from tools.models.base import DefName

type Incomplete = t.Any


def from_def(_obj: mlir.Definition[mlir.MLIR], _name: DefName) -> pyir.Definition:
    """`from_def` allows `mlir.*Dict`."""
    name = f"{from_def.__module__}.{from_def.__name__}"
    msg = f"{name!r} is not yet implemented"
    raise NotImplementedError(msg)


def from_mlir(_obj: mlir.MLIR) -> Incomplete:
    """`from_mlir` must reject dicts, since they require a name."""
    name = f"{from_mlir.__module__}.{from_mlir.__name__}"
    msg = f"{name!r} is not yet implemented"
    raise NotImplementedError(msg)
