# /// script
# requires-python = ">=3.14"
# ///
"""WIP."""

from __future__ import annotations

import dataclasses
from typing import Literal as L


@dataclasses.dataclass(kw_only=True)
class _Options:
    quiet: bool
    stage: L["json_wrapper", "mlir", "pyir", "all"]


def main(options: _Options) -> None:
    from tools.app import App

    quiet = options.quiet
    if not quiet:
        print("Discovering config")
    app = App.discover()
    if not quiet:
        print("Generating ...")

    if options.stage == "all":
        app.into_pyir(quiet=options.quiet)

        # NOTE: All experimental stuff, which depends on `pyir`
        print()
        print("Unique typed references:")
        for module in app._modules.values():
            unique_refs = sorted(module.unique_refs())
            print(f"{module.canonical_path} ({len(unique_refs)}):")
            if unique_refs:
                print("\n".join(f"  {module.typed_ref(ref).display()}" for ref in unique_refs))
            print()

        print("Module dependencies:")
        for module in app._modules.values():
            depends = module.depends_ext()
            print(f"{module.canonical_path} ({len(depends)}):")
            if depends:
                print("\n".join(f"  {s}" for s in sorted(depends)))
            print()

        print("Resolving all dependency types")
        app.resolve_all_references()
    elif options.stage == "pyir":
        app.into_pyir(quiet=options.quiet)
    elif options.stage == "mlir":
        app.into_mlir(quiet=options.quiet)
    else:
        app.into_json_wrapper(quiet=options.quiet)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--quiet", action="store_true", help="Print less to stdout.")
    parser.add_argument(
        "--stage",
        choices=("json_wrapper", "mlir", "pyir", "all"),
        default="all",
        help="Run until the end of a specific conversion stage.",
    )
    main(parser.parse_args(namespace=_Options.__new__(_Options)))
