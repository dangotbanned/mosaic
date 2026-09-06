from __future__ import annotations


def install() -> None:
    """Try to override the default `_colorize` theme, to work better with a dark terminal.

    See [python/cpython#133346] for more info.

    [python/cpython#133346]: https://github.com/python/cpython/issues/133346
    """
    import contextlib

    with contextlib.suppress(ImportError):
        from _colorize import (  # ty: ignore[unresolved-import]  # pyrefly: ignore[missing-import]
            ANSIColors,
            Traceback,
            default_theme,
            set_theme,
        )

        set_theme(
            default_theme.copy_with(
                traceback=Traceback(
                    type=ANSIColors.BOLD_RED,
                    # `MAGENTA` default is bad on dark
                    message=ANSIColors.YELLOW,
                    filename=ANSIColors.BOLD_WHITE,
                    line_no=ANSIColors.BOLD_WHITE,
                    frame=ANSIColors.INTENSE_WHITE,
                )
            )
        )
