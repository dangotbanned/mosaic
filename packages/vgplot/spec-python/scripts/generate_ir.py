# /// script
# requires-python = ">=3.14"
# ///
"""WIP."""

from __future__ import annotations


def main() -> None:
    import argparse
    import dataclasses
    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from collections.abc import Sequence
    from tools.app import App, RunUntil

    @dataclasses.dataclass(kw_only=True)
    class _CLIOptions:
        quiet: bool
        stage: RunUntil
        preview_modules: Sequence[str]

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--quiet", action="store_true", help="Print less to stdout.")
    parser.add_argument(
        "--stage",
        choices=("json_wrapper", "mlir", "pyir", "all"),
        default="all",
        help="Run until the end of a specific conversion stage.",
    )
    parser.add_argument(
        "--preview-modules",
        help="Print the full generated code for these modules to stdout.",
        nargs="+",
        default=(),
    )
    options = parser.parse_args(namespace=_CLIOptions.__new__(_CLIOptions))
    if not options.quiet:
        print("Discovering config")
    app = App.discover()
    app.run(options)


if __name__ == "__main__":
    main()
