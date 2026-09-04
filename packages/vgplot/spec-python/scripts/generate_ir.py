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


if __name__ == "__main__":
    main()
