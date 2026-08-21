"""Boring filesystem dances."""

from __future__ import annotations

import os
from pathlib import Path
from typing import TYPE_CHECKING, Any, Final, Literal as L, LiteralString as LS, overload

if TYPE_CHECKING:
    import subprocess as sp
    from collections.abc import Iterable, Iterator

# ruff: file-ignore[print,subprocess-without-shell-equals-true]

type IntoPath = str | Path | os.PathLike[str]
"""Anything that can be converted into a [`pathlib.Path`][]."""

type Suffix = L[
    ".css",
    ".csv",
    ".geojson",
    ".js",
    ".json",
    ".md",
    ".parquet",
    ".py",
    ".toml",
    ".ts",
    ".tsv",
    ".yaml",
]
"""Any file extension that would (realistically) be used in this project."""

type Tool = L["uv", "ruff", "rumdl"]

_HERE = Path(__file__)

# NOTE: External paths
MONOREPO_ROOT = _HERE.parent.parent.parent.parent.parent
"""`mosaic`"""

EXAMPLES_SPECS = MONOREPO_ROOT / "specs"
"""`mosaic/specs`.

Monorepo-level directory containing examples for each target format.

## Important
The source for `mosaic/docs/public/specs`.
"""

EXAMPLES_SPECS_YAML = EXAMPLES_SPECS / "yaml"
"""`mosaic/specs/yaml`.

Manually authored examples.

## Important
Everything is generated from yaml.
"""

EXAMPLES_SPECS_PYTHON = EXAMPLES_SPECS / "python"
"""`mosaic/specs/python`.

Generated `vgplot-python` examples, for comparison.
"""

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

MOSAIC_SPEC_TOML = SPEC_PYTHON / "mosaic-spec.toml"
"""`mosaic/packages/vgplot/spec-python/mosaic-spec.toml`.

One day, this file will configure everything.
"""

MOSAIC_SPEC_TOML_SCHEMA = SPEC_PYTHON / "mosaic-spec-toml-schema.json"
"""`mosaic/packages/vgplot/spec-python/mosaic-spec-toml-schema.json`."""

SCHEMA: Final = SPEC_PYTHON / "schema"
"""`mosaic/packages/vgplot/spec-python/schema`.

Output directory for modified schemas.
"""

SCRIPTS = SPEC_PYTHON / "scripts"
"""`mosaic/packages/vgplot/spec-python/scripts`"""

TESTS = SPEC_PYTHON / "tests"
"""`mosaic/packages/vgplot/spec-python/tests`"""

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


def repo_relative_str(source: IntoPath) -> str:
    """Return a path representation for errors/logs."""
    return Path(source).relative_to(SPEC_PYTHON).as_posix()


def read_pyproject() -> dict[str, Any]:
    """`["tool"]["datamodel-codegen"]["profiles"]["spec"]["output"]`."""
    import tomllib

    return tomllib.loads(PYPROJECT_TOML.read_text("utf8"))


def iter_dir(source_dir: IntoPath, *include_suffix: Suffix) -> Iterator[Path]:
    """Iterate over the paths in `source_dir`.

    Args:
        source_dir: The parent directory.
        *include_suffix: Require each result to be a file with one of these extensions.

    ## Notes
    [1]: https://docs.python.org/3/library/pathlib.html#pathlib.Path.iterdir
    [2]: https://docs.python.org/3/library/os.html#os.scandir

    - Faster than [`pathlib.Path.iterdir`][1], but that should be preferred if you
      want to pay for defined behavior in the event a file is [removed/added during iteration][2]
    - Doesn't require re/glob/fnmatch

    ## Examples
    Equivalent glob: `path/to/dir/*`

    >>> files_or_dirs = iter_dir("path/to/dir")

    Equivalent glob: `path/to/dir/*.{yaml,toml}`

    >>> yaml_or_toml = iter_dir("path/to/dir", ".yaml", ".toml")

    The latter is not supported by [python's glob], and is inspired by [globset] syntax.

    [python's glob]: https://docs.python.org/3/library/pathlib.html#pattern-language
    [globset]: https://docs.rs/globset/latest/globset/#syntax
    """
    constructor = type(Path(source_dir))
    for entry in scan_dir(source_dir, *include_suffix):
        yield constructor(entry)


def scan_dir(source_dir: IntoPath, *include_suffix: Suffix) -> Iterator[os.DirEntry[str]]:
    """Iterate over the entries in `source_dir`.

    The lower-level counterpart to [`iter_dir`][].
    """
    with os.scandir(source_dir) as it_scan:
        if not include_suffix:
            yield from it_scan
            return
        for entry in it_scan:
            if entry.is_file() and entry.name.endswith(include_suffix):
                yield entry


def write_lines(target: IntoPath, lines: Iterable[str], /, message: str | None = None) -> None:
    """Join `lines` and write them to `target`."""
    target = Path(target)
    target.touch()
    target.write_text("\n".join(lines), "utf8", newline="\n")
    if message:
        print(f"{message} at: {repo_relative_str(target)}")


# TODO @dangotbanned: Change `cwd` to use an enum instead of `None` to represent "leave me alone"
@overload
def run(tool: Tool, *args: LS, output: L["pipe"] = "pipe", cwd: IntoPath | None = ...) -> None: ...
@overload
def run(
    tool: Tool, *args: LS, input: str | None = ..., output: L["capture"], cwd: IntoPath | None = ...
) -> sp.CompletedProcess[str]: ...
def run(
    tool: Tool,
    *args: LS,
    input: str | None = None,
    output: L["capture", "pipe"] = "pipe",
    cwd: IntoPath | None = SPEC_PYTHON,
) -> sp.CompletedProcess[str] | None:
    """Run a command in a subprocess.

    Args:
        tool: A command-line tool to run.
        *args: Arguments to the tool, where all must be literal strings.
        input: Text to feed into stdin. (Incompatible with `output="pipe"`)
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

    format_cmd = " ".join((tool, *args))
    if len(format_cmd) > 80:
        format_cmd = format_cmd[:50] + "..." + format_cmd[-30:]
    print(f"$ {format_cmd}")
    args_ = ((shutil.which(tool) or tool), *args)

    if output == "capture":
        return sp.run(
            args_, check=True, capture_output=True, encoding="utf-8", cwd=cwd, input=input
        )

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
