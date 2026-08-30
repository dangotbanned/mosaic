"""Markdown tools, targeting docstrings as output."""

from __future__ import annotations

import subprocess
from typing import Final

from tools import fs

_no_emphasis_as_heading = "MD036"
_first_line_heading = "MD041"
_RULE_IGNORE: Final = (_no_emphasis_as_heading, _first_line_heading)
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
_COMMA: Final = ","


def fix(string: str, /, *, debug: bool = False) -> str:
    """Lint and perform autofixes using [rumdl](https://rumdl.dev/).

    Args:
        string: A fragment of markdown.
        debug: Request and capture *stderr*.

    ## See Also
    https://rumdl.dev/usage/cli/#stdinstdout
    """
    args = ("check", "--fix", "--stdin", "--disable", _COMMA.join(_RULE_IGNORE), *_CONFIG_DOCSTRING)
    if debug:
        try:
            return fs.run("rumdl", *args, input=string, output="capture").stdout
        except subprocess.CalledProcessError as err:
            err.add_note(err.stderr)
            raise
    else:
        return fs.run("rumdl", *args, "--silent", input=string, output="capture").stdout
