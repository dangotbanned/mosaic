from __future__ import annotations

from typing import Final, NewType

snake_case = NewType("snake_case", str)
"""A name that has been converted from {camel,Pascal}Case."""

POUND_DEFS: Final = "#/definitions/"
