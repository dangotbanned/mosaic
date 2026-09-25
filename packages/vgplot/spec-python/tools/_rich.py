"""Configures [rich] for visualizing schemas and other large objects.

[rich]: https://github.com/Textualize/rich
"""

from __future__ import annotations

import typing as t

if t.TYPE_CHECKING:
    from pathlib import Path

    from rich.console import Console

_STYLES: t.Final = {
    "repr.call": "rgb(78,201,176)",
    "repr.attrib_name": "rgb(156,220,254)",
    "repr.str": "rgb(206,145,120)",
    "repr.bool_true": "rgb(86,156,214)",
    "repr.bool_false": "rgb(86,156,214)",
    "repr.bool_none": "rgb(86,156,214)",
    "repr.brace": "rgb(255,215,0)",
    "repr.comma": "rgb(255,215,0)",
    "repr.number": "rgb(181,206,168)",
    "repr.number_complex": "rgb(181,206,168)",
}


_console: Console | None = None


def get_console() -> Console:
    global _console  # ruff: ignore[global-statement]
    if _console is None:
        from rich.console import Console
        from rich.theme import Theme

        _console = Console(theme=Theme(_STYLES))
    return _console


def print_path(message: str, path: Path) -> None:
    """Display a clickable link to a filepath."""
    from rich.style import Style
    from rich.text import Text

    from tools.fs import SPEC_PYTHON

    text = Text(path.relative_to(SPEC_PYTHON).as_posix(), Style(link=path.as_uri()))
    get_console().print(f"{message} at:", text)


def install(
    *,
    crop: bool = False,
    max_length: int | None = 10,
    max_string: int | None = 80,
    max_depth: int | None = 3,
) -> None:
    """Configure [`rich`][] for visualizing schemas and other large objects.

    ## Notes
    - Sets reasonable limits for output size
    - Theme is adapted from [VSCode Dark+ Python Theme](https://github.com/thowitz/dark-plus-python-theme/blob/99ece7cb5ac540cbb28447d401b316fd44230d26/themes/dark-plus-python-theme.json)
    """
    import rich.pretty

    rich.pretty.install(
        get_console(), crop=crop, max_length=max_length, max_string=max_string, max_depth=max_depth
    )
