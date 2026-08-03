"""Boring filesystem dances."""

from __future__ import annotations

# ruff: file-ignore[print,subprocess-without-shell-equals-true]
from pathlib import Path
from typing import TYPE_CHECKING, Any, LiteralString

if TYPE_CHECKING:
    import subprocess as sp
    from collections.abc import Iterable


_HERE = Path(__file__)

# NOTE: External paths
MONOREPO_ROOT = _HERE.parent.parent.parent.parent.parent
"""`mosaic`"""

PACKAGES = MONOREPO_ROOT / "packages"
"""`mosaic/packages`"""

VGPLOT_PACKAGE = PACKAGES / "vgplot"
"""`mosaic/packages/vgplot`"""

SPEC = VGPLOT_PACKAGE / "spec"
"""`mosaic/packages/vgplot/spec`"""

VGPLOT_PYTHON = VGPLOT_PACKAGE / "vgplot-python"
"""`mosaic/packages/vgplot/vgplot-python`"""

WIDGET = VGPLOT_PACKAGE / "widget"
"""`mosaic/packages/vgplot/widget`"""


# NOTE: Local paths
SPEC_PYTHON = _HERE.parent.parent
"""`mosaic/packages/vgplot/spec-python`"""

SCRIPTS = SPEC_PYTHON / "scripts"
"""`mosaic/packages/vgplot/spec-python/scripts`"""

SRC = SPEC_PYTHON / "src"
"""`mosaic/packages/vgplot/spec-python/src`"""

MOSAIC_SPEC = SRC / "mosaic_spec"
"""`mosaic/packages/vgplot/spec-python/src/mosaic_spec`"""

MOSAIC_SPEC_INIT = MOSAIC_SPEC / "__init__.py"
"""`mosaic/packages/vgplot/spec-python/src/mosaic_spec/__init__.py`"""

MOSAIC_SPEC_GEN_INIT = MOSAIC_SPEC / "_gen" / "__init__.py"
"""`mosaic/packages/vgplot/spec-python/src/mosaic_spec/_gen/__init__.py`"""

PYPROJECT_TOML = SPEC_PYTHON / "pyproject.toml"
"""`mosaic/packages/vgplot/spec-python/pyproject.toml`"""


def repo_relative_str(source: str | Path) -> str:
    """Return a path representation for errors/logs."""
    return Path(source).relative_to(SPEC_PYTHON).as_posix()


def read_pyproject() -> dict[str, Any]:
    """`["tool"]["datamodel-codegen"]["profiles"]["spec"]["output"]`."""
    import tomllib

    return tomllib.loads(PYPROJECT_TOML.read_text("utf8"))


def write_lines(target: str | Path, lines: Iterable[str], /, message: str | None = None) -> None:
    """Join `lines` and write them to `target`."""
    target = Path(target)
    target.touch()
    target.write_text("\n".join(lines), "utf8", newline="\n")
    if message:
        print(f"{message} at: {repo_relative_str(target)}")


def run(*args: LiteralString, cwd: Path | None = SPEC_PYTHON) -> sp.CompletedProcess[str]:
    """Run a command in a [subprocess], capturing and decoding output.

    [subprocess]: https://docs.python.org/3/library/subprocess.html#subprocess.run
    """
    import subprocess as sp

    print(f"$ {' '.join(args)}")
    return sp.run(args, check=True, capture_output=True, encoding="utf-8", cwd=cwd)
