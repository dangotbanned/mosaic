"""Compatibility for `"typing-extensions>=4.16 ; python_full_version < '3.15'"`."""

from __future__ import annotations

import sys

if sys.version_info >= (3, 15):
    from typing import NotRequired, Required, TypeAliasType, TypedDict, TypeVar
else:
    from typing_extensions import NotRequired, Required, TypeAliasType, TypedDict, TypeVar

__all__ = ("NotRequired", "Required", "TypeAliasType", "TypeVar", "TypedDict")
