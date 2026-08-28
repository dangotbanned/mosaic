from __future__ import annotations

import typing as t
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tools.ir import mlir
    from tools.ir.pyir.base import PyIdentifier
    from tools.ir.pyir.module import Module
    from tools.models.base import DefName

type Incomplete = t.Any


def identifier(name: str) -> PyIdentifier:
    raise NotImplementedError(identifier.__name__)


def from_root(root: mlir.Root) -> Module:
    raise NotImplementedError(from_root.__name__)


def from_def(obj: mlir.Definition[mlir.MLIR], name: DefName) -> Incomplete:
    """`from_def` allows `mlir.*Dict`."""
    raise NotImplementedError(from_def.__name__)


def from_mlir(obj: mlir.MLIR) -> Incomplete:
    """`from_mlir` must reject dicts, since they require a name."""
    raise NotImplementedError(from_mlir.__name__)
