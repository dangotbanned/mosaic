from __future__ import annotations

import functools
import re
import string
from keyword import iskeyword as is_keyword
from typing import ClassVar, Final, Self

from tools.common import PyIdentifier, PyIdentifierSnake

KEYS_REPLACE: Final = {"as": "bind", "from": "source", "for": "plot"}
"""Keys that collide with [`keyword.kwlist`][], but the values are required.

These keys only appear in `"properties"` and `"required"`, the challenge is finding those guys.
"""


_REPL_ADD_UNDERSCORE = r"\g<1>_\g<2>"
_REPL_ADD_HYPHEN = r"\g<1>-\g<2>"
_PATTERN_UPPER_LOWER = re.compile(r"([A-Z]+)([A-Z][a-z])")
_PATTERN_LOWER_UPPER = re.compile(r"([a-z])([A-Z])")


@functools.lru_cache(maxsize=1024)
def py_identifier(name: str) -> PyIdentifier:
    """Ensure `name` can be used as an identifier."""
    if name.isidentifier() and not is_keyword(name):
        return PyIdentifier(name)
    raise InvalidIdentifierError.from_name(name)


@functools.lru_cache(maxsize=1024)
def py_identifier_snake(name: str) -> PyIdentifierSnake:
    """Try to coerce `name` into a snake_case identifier.

    Accepts camelCase, PascalCase, kebab-case.
    """
    name = name.replace("-", "_")
    if name.isidentifier() and not is_keyword(name):
        s = _PATTERN_UPPER_LOWER.sub(_REPL_ADD_UNDERSCORE, name)
        s = _PATTERN_LOWER_UPPER.sub(_REPL_ADD_UNDERSCORE, s).lower()
        return PyIdentifierSnake(s)

    raise InvalidIdentifierError.from_name(name)


def kebab_case(name: str) -> str:
    s = _PATTERN_UPPER_LOWER.sub(_REPL_ADD_HYPHEN, name)
    return _PATTERN_LOWER_UPPER.sub(_REPL_ADD_HYPHEN, s).lower()


class InvalidIdentifierError(SyntaxError):
    _URL: ClassVar = (
        "https://docs.python.org/3/reference/lexical_analysis.html#names-identifiers-and-keywords"
    )

    @classmethod
    def from_name(cls, name: str) -> Self:
        if is_keyword(name):
            reason = " as it is a Python keyword."
        elif "-" in name:
            reason = " as it uses kebab-case."
        elif name.startswith(string.digits):
            reason = " as it starts with a number."
        else:
            reason = "."
        msg = (
            f"Cannot use {name!r} as an identifier{reason}\n"
            f"Hint: try picking a different name?\nSee also: {cls._URL}"
        )
        return cls(msg)
