# NOTE: DO NOT EDIT MANUALLY.
# Regenerate with: pnpm generate
from __future__ import annotations

from mosaic_spec._gen.expression import SQLExpression
from mosaic_spec._gen.params import ParamRef
from mosaic_spec._typing_compat import TypeAliasType

TransformField = TypeAliasType("TransformField", ParamRef | SQLExpression | str)
"""A field argument to a data transform."""


__all__ = ("TransformField",)
