"""Boring filesystem dances."""

from __future__ import annotations

# ruff: file-ignore[print,subprocess-without-shell-equals-true]
from pathlib import Path
from typing import TYPE_CHECKING, Any, Final, Literal as L, LiteralString as LS, overload

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

SCHEMA: Final = SPEC_PYTHON / "schema"
"""`mosaic/packages/vgplot/spec-python/schema`.

Output directory for modified schemas.
"""

SCRIPTS = SPEC_PYTHON / "scripts"
"""`mosaic/packages/vgplot/spec-python/scripts`"""

SRC = SPEC_PYTHON / "src"
"""`mosaic/packages/vgplot/spec-python/src`"""

MOSAIC_SPEC = SRC / "mosaic_spec"
"""`mosaic/packages/vgplot/spec-python/src/mosaic_spec`"""

MOSAIC_SPEC_INIT = MOSAIC_SPEC / "__init__.py"
"""`mosaic/packages/vgplot/spec-python/src/mosaic_spec/__init__.py`"""

MOSAIC_SPEC_GEN = MOSAIC_SPEC / "_gen"
"""`mosaic/packages/vgplot/spec-python/src/mosaic_spec/_gen/`"""

MOSAIC_SPEC_GEN_INIT = MOSAIC_SPEC_GEN / "__init__.py"
"""`mosaic/packages/vgplot/spec-python/src/mosaic_spec/_gen/__init__.py`"""


MOSAIC_SPEC_INTERSECTION = MOSAIC_SPEC / "spec.py"
"""`mosaic/packages/vgplot/spec-python/src/mosaic_spec/spec.py`"""

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


type Tool = L["uv", "ruff"]


# TODO @dangotbanned: Change `cwd` to use an enum instead of `None` to represent "leave me alone"
@overload
def run(tool: Tool, *args: LS, output: L["pipe"] = "pipe", cwd: Path | None = ...) -> None: ...
@overload
def run(
    tool: Tool, *args: LS, output: L["capture"], cwd: Path | None = ...
) -> sp.CompletedProcess[str]: ...
def run(
    tool: Tool, *args: LS, output: L["capture", "pipe"] = "pipe", cwd: Path | None = SPEC_PYTHON
) -> sp.CompletedProcess[str] | None:
    """Run a command in a subprocess.

    Args:
        tool: A command-line tool to run.
        *args: Arguments to the tool, where all must be literal strings.
        output: What to do with the output of the command:

            - *"pipe"*: (default) feed it directly into stdout.
            - *"capture"*: wrap it and return the result.
        cwd: Set the current working directory for the subprocess.

            Defaults to `"mosaic/packages/vgplot/spec-python"`

    ## See Also
    [subprocess.run](https://docs.python.org/3/library/subprocess.html#subprocess.run)
    """
    import shutil
    import subprocess as sp

    print(f"$ {' '.join((tool, *args))}")
    args_ = ((shutil.which(tool) or tool), *args)

    if output == "capture":
        return sp.run(args_, check=True, capture_output=True, encoding="utf-8", cwd=cwd)

    with sp.Popen(args_, stdout=sp.PIPE, stderr=sp.STDOUT, encoding="utf-8", cwd=cwd) as process:
        # TODO @dangotbanned: Is there a more direct way to do this?
        if process.stdout is not None:
            for chunk in process.stdout:
                print(chunk, end="")
    if retcode := process.poll():
        # TODO @dangotbanned: Try out raising `SystemExit` instead
        #  `args` and `stderr` have already been displayed at this point
        raise sp.CalledProcessError(retcode, process.args)
    return None
