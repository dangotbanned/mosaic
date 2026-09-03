# /// script
# requires-python = ">=3.14"
# ///
"""WIP."""

from __future__ import annotations


def main(*, quiet: bool = False) -> None:
    from tools.app import App

    print("Discovering config")
    app = App.discover()
    print("Generating ...")
    app.into_pyir(quiet=quiet)


if __name__ == "__main__":
    main()
