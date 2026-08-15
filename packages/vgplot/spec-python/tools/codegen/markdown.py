"""Markdown tools, targeting docstrings as output."""

from __future__ import annotations

from typing import Final

from tools import fs

_RULE_IGNORE: Final = ("MD041",)
_CONFIG_DOCSTRING: Final = (
    "--config",
    "MD013.line-length=100",
    "--config",
    "MD013.reflow=true",
    "--config",
    "MD054.inline=false",
    "--config",
    "MD054.preferred-style='shortcut'",
)


# TODO @dangotbanned: Start using this on examples after https://github.com/rvben/rumdl/issues/819
def fix(string: str, /) -> str:
    """Lint and perform autofixes using [rumdl](https://rumdl.dev/)."""
    return fs.run(
        "rumdl",
        "check",
        "--fix",
        "--silent",
        "--stdin",  # https://rumdl.dev/usage/cli/#stdinstdout.
        "--disable",
        _RULE_IGNORE[0],
        *_CONFIG_DOCSTRING,
        input=string,
        output="capture",
    ).stdout
