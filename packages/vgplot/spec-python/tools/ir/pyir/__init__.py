"""A limited representation of Python's type system & data model.

## Important
- No classes
- No objects
- No functions/methods/operators
- No AST
- Strictly, things that can be used in the generation of modules containing `TypedDict`s

---

<!--TODO @dangotbanned: Merge above and below into a narrative--->

### Stage 3

- Package: [`tools.ir.pyir`][]
- Root: `pyir.Module` / `pyir.Package`
- Definition: `pyir.Definition`, 7 implementations
- Nodes:
    - `pyir.Expr`, 14 implementations
    - `pyir.PyIR` (other), 9 implementations

---

## Targets

### Python version

Codegen targets the current [minimum supported Python version] (-5 versions).
This is **not planned to be configurable**.

If you want features from a newer version, use Ruff's ([`UP`]) rules on the output:

```terminal
uvx ruff check --extend-select UP --target-version py312 --fix
```

For now, that means:

1. [PEP 695] syntax cannot be used, but type aliases will have the same semantics,
   through the use of [`TypeAliasType`].
2. [PEP 728] features for [`TypedDict`] are used, but depend on either (see [related]):
   i. [`typing_extensions>=4.10.0rc1`]
   ii. [`requires-python>=3.15 `]

[minimum supported Python version]: https://devguide.python.org/versions/#supported-versions
[`UP`]: https://docs.astral.sh/ruff/rules/#pyupgrade-up
[PEP 695]: https://peps.python.org/pep-0695/
[`TypeAliasType`]: https://typing-extensions.readthedocs.io/en/latest/#typing_extensions.TypeAliasType
[PEP 728]: https://peps.python.org/pep-0728/
[`TypedDict`]: https://typing-extensions.readthedocs.io/en/latest/#typing_extensions.TypedDict
[related]: https://discuss.python.org/t/spec-change-proposal-updating-clarifying-rules-for-unpacking-typeddicts-in-function-calls/108582
[`typing_extensions>=4.10.0rc1`]: https://github.com/python/typing_extensions/releases/tag/4.10.0rc1
[`requires-python>=3.15`]: https://docs.python.org/3.15/whatsnew/3.15.html

### Python style

The output is not concerned with linting/formatting behaviors. *This tool* expects that the output
is run through another tool (e.g. [Ruff]) that enforces the conventions of the project.
To that end, *you* should expect the code to be syntactically valid, but ugly.
It is faster to generate code with the knowledge that it will be tidied up elsewhere.

[Ruff]: https://docs.astral.sh/ruff/

#### Non-configurable

These decisions are influenced by a few principles:

- [Nominal] types should be avoided, unless they provide a concrete benefit
- Generated code should take advantage of *language features* [^1] that reduce file size
- Documentation should be local to the member it describes

[Nominal]: https://typing.python.org/en/latest/spec/concepts.html#nominal-and-structural-types

[^1]: "minifying" is not a feature

1. `Enum` -> `Literal`.
2. `dict[str, V]` -> `Mapping[str, V]`.
3. `list[T]` -> `Sequence[T_co]`.
4. `tuple` is used for sequences with a known-length.
5. `total=False` will be preferred for `TypedDict`, *unless* more keys are required than not.
6. [PEP 224]-style "attribute docstrings" will be used whenever possible.

[PEP 224]: https://peps.python.org/pep-0224

#### Potential configuration

These have trade-offs, which should likely be made on a case-by-case basis.

1. Promoting `str` aliases to `NewType`s
   i. `Literal["..."] | str` can mask errors
   ii. `NewType` fixes this, but can be painful to adjust to
2. Promoting "structural named tuple"s to nominal `NamedTuple`s
   i. The former relies on `Annotated`, which may be hidden by a language server
   ii. The latter will reject valid `tuple`(s) and requires the constructor

The default for both is to avoid [nominal] types.

[nominal]: https://typing.python.org/en/latest/spec/concepts.html#nominal-and-structural-types
"""

from __future__ import annotations

import contextlib as _contextlib
from typing import TYPE_CHECKING

from tools.ir.pyir import (
    base,
    convert,
    definition,
    expr,
    field,
    module,
    qualifier,
    special,
    type_param,
    value,
)
from tools.ir.pyir.base import Definition, Expr, ExtRef, PyIR, Ref, TypedExtRef, TypedRef
from tools.ir.pyir.field import Field
from tools.ir.pyir.module import Module, Package

if TYPE_CHECKING:
    from collections.abc import Generator

    from tools import config as _cfg


def _noop[T](obj: T, /) -> T:
    return obj


@_contextlib.contextmanager
def configure(config: _cfg.ToPyIR, /) -> Generator[None]:
    name = config.name
    aliases = name.aliases
    typing = aliases.typing

    expr.Sequence._ALIAS = aliases.collections.abc.Sequence
    expr.Literal._ALIAS = typing.Literal
    expr.Annotated._ALIAS = typing.Annotated
    definition.TypeAlias._ALIAS = typing.TypeAliasType
    definition.OpenDict._FORMAT = name.format_base

    type_config = config.type
    from_def = convert.patch_type_alias_type if type_config.str == "TypeAliasType" else _noop
    into_expr = convert.patch_named_tuple if type_config.NamedTuple == "NamedTuple" else _noop

    try:
        with convert._from_def.context(from_def), convert.into_expr.context(into_expr):
            yield

    finally:
        ...


__all__ = (
    "Definition",
    "Expr",
    "ExtRef",
    "Field",
    "Module",
    "Package",
    "PyIR",
    "Ref",
    "TypedExtRef",
    "TypedRef",
    "base",
    "convert",
    "definition",
    "expr",
    "field",
    "module",
    "qualifier",
    "special",
    "type_param",
    "value",
)
