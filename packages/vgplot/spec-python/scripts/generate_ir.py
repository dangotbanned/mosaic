# /// script
# requires-python = ">=3.14"
# ///
"""Exposes a CLI for `tools.app.App`."""

from __future__ import annotations


def main() -> None:
    import argparse
    import dataclasses
    from typing import get_args

    from tools.app import App, RunUntil

    @dataclasses.dataclass(kw_only=True)
    class _CLIOptions:
        quiet: bool
        stage: RunUntil
        require_unique_module_names: bool = False

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--quiet", action="store_true", help="Print less to stdout.")
    parser.add_argument(
        "--stage",
        choices=get_args(RunUntil.__value__),
        default="lint",
        help="Run until the end of a specific stage.",
    )
    parser.add_argument(
        "--require-unique-module-names",
        action="store_true",
        help="Before codegen, check that every module (regardless of package) has a unique name.\nSee (https://github.com/dangotbanned/mosaic/blob/4c26a5ff88a17663b01ba1b191c0a37480912cb6/packages/vgplot/spec-python/tools/ir/pyir/dependencies.py#L77-L84)",
    )

    options = parser.parse_args(namespace=_CLIOptions.__new__(_CLIOptions))
    if not options.quiet:
        print("Discovering config")
    app = App.discover()
    app.run(options)


if __name__ == "__main__":
    from tools._colorize_install import install

    install()
    main()
