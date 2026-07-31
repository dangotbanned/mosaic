"""Configures [rich] for visualizing schemas.

This is a noop without `uv <command> --group repl`.

[rich]: https://github.com/Textualize/rich
"""

from __future__ import annotations

_STYLES = {
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


def install(
    *,
    crop: bool = False,
    max_length: int | None = 10,
    max_string: int | None = 80,
    max_depth: int | None = 3,
) -> None:
    """Configure [`rich`][] if available.

    ## Notes
    - Sets reasonable limits for output size
    - Theme is adapted from [VSCode Dark+ Python Theme](https://github.com/thowitz/dark-plus-python-theme/blob/99ece7cb5ac540cbb28447d401b316fd44230d26/themes/dark-plus-python-theme.json)
    """
    import contextlib

    with contextlib.suppress(ImportError):
        import rich.console
        import rich.pretty
        import rich.theme

        console = rich.console.Console(theme=rich.theme.Theme(_STYLES))
        rich.pretty.install(
            console, crop=crop, max_length=max_length, max_string=max_string, max_depth=max_depth
        )
