from __future__ import annotations


def doc(string: str, /) -> str:
    """Quote a string like a docstring.

    Nothing fancy here.
    """
    return f"'''{string}'''"
