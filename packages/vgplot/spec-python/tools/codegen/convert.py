from __future__ import annotations

import functools
import re
from typing import Final

from tools.common import snake_case

KEYS_REPLACE: Final = {"as": "bind", "from": "source", "for": "plot"}
"""Keys that collide with [`keyword.kwlist`][], but the values are required.

These keys only appear in `"properties"` and `"required"`, the challenge is finding those guys.
"""


_REPL_ADD_UNDERSCORE = r"\g<1>_\g<2>"
_PATTERN_UPPER_LOWER = re.compile(r"([A-Z]+)([A-Z][a-z])")
_PATTERN_LOWER_UPPER = re.compile(r"([a-z])([A-Z])")


@functools.lru_cache(maxsize=1024)
def pascal_to_snake_case(s: str, /) -> snake_case:
    """Convert a PascalCase string to snake_case.

    Adapted from https://github.com/pydantic/pydantic/blob/f7a9b73517afecf25bf898e3b5f591dffe669778/pydantic/alias_generators.py#L43-L62
    """
    s = _PATTERN_UPPER_LOWER.sub(_REPL_ADD_UNDERSCORE, s)
    return snake_case(_PATTERN_LOWER_UPPER.sub(_REPL_ADD_UNDERSCORE, s).lower())
