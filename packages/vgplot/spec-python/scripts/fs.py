"""Boring filesystem dances."""

from __future__ import annotations

from pathlib import Path

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

PYPROJECT_TOML = SPEC_PYTHON / "pyproject.toml"
"""`mosaic/packages/vgplot/spec-python/pyproject.toml`"""


def repo_relative_str(source: str | Path) -> str:
    """Return a path representation for errors/logs."""
    return Path(source).relative_to(SPEC_PYTHON).as_posix()
