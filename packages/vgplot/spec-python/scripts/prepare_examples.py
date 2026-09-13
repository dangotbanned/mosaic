# /// script
# requires-python = ">=3.12"
# ///

from __future__ import annotations

from typing import TYPE_CHECKING

from tools import fs
from tools.codegen.examples import ExamplesGenerator

if TYPE_CHECKING:
    from pathlib import Path


def main(target_dir: Path, /) -> None:
    from tools.app import App

    target_dir.mkdir(parents=True, exist_ok=True)
    package_init = target_dir / "__init__.py"
    if not package_init.exists():
        package_init.touch()

    rename = dict(App.discover()._iter_rename_fields_overrides())
    ExamplesGenerator(fs.EXAMPLES_SPECS_YAML, target_dir, rename).generate_examples()


if __name__ == "__main__":
    main(fs.TESTS / "test_examples")
