# /// script
# requires-python = ">=3.12"
# ///

from __future__ import annotations

from typing import TYPE_CHECKING

from tools import fs
from tools.codegen.examples import Example

if TYPE_CHECKING:
    from pathlib import Path


def _derive_target_path(target_dir: Path, source: Path) -> Path:
    # kebab-case module names cannot be imported
    valid_stem = source.stem.replace("-", "_")
    target = target_dir / f"test_{valid_stem}.py"
    target.touch()
    return target


def main(target_dir: Path, /) -> None:
    target_dir.mkdir(parents=True, exist_ok=True)
    package_init = target_dir / "__init__.py"
    if not package_init.exists():
        package_init.touch()

    for source in fs.iter_dir(fs.EXAMPLES_SPECS_YAML, ".yaml"):
        rendered = Example.from_path(source).render_test_module()
        _derive_target_path(target_dir, source).write_text(rendered, "utf-8", newline="\n")


if __name__ == "__main__":
    # TODO @dangotbanned: Move handwritten tests out of `test_examples` and use that instead
    target = fs.TESTS / "test_examples_gen"
    main(target)
    print(f"Generated examples at: {fs.repo_relative_str(target)}")
    # TODO @dangotbanned: run ruff on the result
