# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "msgspec>=0.21.1",
# ]
# ///
"""Transform `packages/vgplot/spec/dist/mosaic-schema.json` for use in python."""

from __future__ import annotations

from collections import deque
from pathlib import Path
from typing import TYPE_CHECKING, Final

from tools import fs, serde
from tools.codegen import typed_dict
from tools.codemod import fragments
from tools.models import source as m

if TYPE_CHECKING:
    from collections.abc import Iterable

GENERATED_MODULE_NAME = "mosaic"
SCHEMA_IN = fs.SPEC / "dist/mosaic-schema.json"
SCHEMA_OUT = fs.SPEC_PYTHON / "schema" / f"{GENERATED_MODULE_NAME}.json"


KEYS_REPLACE: Final = {"as": "bind", "from": "source", "for": "plot"}
"""Keys that collide with [`keyword.kwlist`][], but the values are required.

These keys only appear in `"properties"` and `"required"`, the challenge is finding those guys.
"""


def _recursive_replace[T: (m.JsonSchema, m.ItemSchema)](schema: T) -> T:
    """Visit 4 fields at all levels of the schema, renaming matches for [`KEYS_REPLACE`][]."""
    replace = KEYS_REPLACE.get
    recurse = _recursive_replace
    if properties := schema.properties:
        schema.properties = {replace(k, k): (recurse(v)) for k, v in properties.items()}
    if required := schema.required:
        schema.required = [replace(r, r) for r in required]
    if any_of := schema.any_of:
        schema.any_of = [recurse(a) for a in any_of]
    if not isinstance(schema, (m.ItemSchema)) and (items := schema.items) and items is not True:
        if isinstance(items, m.ItemSchema):
            schema.items = recurse(items)
        else:
            schema.items = [recurse(i) for i in items]
    return schema


# TODO @dangotbanned: Use `Spec/Component`
def main(source: str | Path, target: str | Path) -> None:
    print(f"Reading json schema at: {Path(source).relative_to(fs.MONOREPO_ROOT).as_posix()}")
    schema = serde.read_json(source, m.InputSchema)
    definitions = schema.definitions
    _spec_todo = definitions.pop("Spec")
    schema.definitions = {k: _recursive_replace(v) for k, v in definitions.items()}
    print("Finished renaming & Spec removal")

    # TODO @dangotbanned: Fix the order of this so there isn't a need to write to a file
    # Next step is `datamodel-code-generator` -> using
    component_members = schema.flatten_component_union_mut("Component")

    serde.write_json(target, schema)
    print(f"Generated python schema at: {fs.repo_relative_str(target)}")

    serde.write_json(WIP_NAMES, component_members)
    print(f"Generated Component member names at: {fs.repo_relative_str(WIP_NAMES)}")


WIP_NAMES = fs.SPEC_PYTHON / "WIP-Component-names.json"
WIP_SPEC_MODULE = fs.MOSAIC_SPEC / "_spec.py"
SPEC: Final = "Spec"
"""Name of the `Spec` union and prefix for it's members"""

SPEC_HEAD: Final = "SpecHead"
"""Name of the base `TypedDict` for all `Spec` members.

Mixing this into the bases with the `Component` member is a limited form of an intersection type.
"""


def generate_spec_module(component_members: Iterable[str], target: str | Path) -> None:
    spec_fields = (
        typed_dict.Field("config", "Config", "Configuration options."),
        typed_dict.Field("data", "Data", "Dataset definitions."),
        typed_dict.Field("meta", "Meta", "Specification metadata."),
        typed_dict.Field("params", "Params", "Param and Selection definitions."),
        typed_dict.Field(
            "plot_defaults",
            "PlotAttributes",
            "A default set of attributes to apply to all plot components.",
        ),
    )

    module = deque(typed_dict.iter_lines(SPEC_HEAD, spec_fields))
    import_from = fragments.import_from
    module.extendleft(
        (
            import_from(fs.MOSAIC_SPEC / "_typing_compat.py", ("TypedDict", "TypeAliasType")),
            import_from(fs.MOSAIC_SPEC / "_gen" / "mosaic.py", (fld.tp for fld in spec_fields)),
        )
    )

    import_names = deque[str]()
    export_names = deque[str]()

    for base_name in component_members:
        import_names.append(base_name)
        name = f"{SPEC}{base_name}"
        module.extend(typed_dict.iter_lines(name, bases=(SPEC_HEAD, base_name), closed=True))
        export_names.append(name)

    module.append(f"{SPEC} = TypeAliasType({SPEC!r}, {'|'.join(export_names)})")
    export_names.append(SPEC)
    module.appendleft(import_from(fs.MOSAIC_SPEC_GEN_INIT, import_names))
    module.appendleft(fragments.FUTURE_ANNOTATIONS)
    module.append(f"__all__ = {tuple(export_names)}\n")

    target = Path(target)
    target.touch()
    target.write_text("\n".join(module), "utf8", newline="\n")
    print(f"Generated spec module at: {fs.repo_relative_str(target)}")


if __name__ == "__main__":
    main(SCHEMA_IN, SCHEMA_OUT)
    # TODO @dangotbanned: Fix the order!
    # TODO @dangotbanned: Re-enable after resolving typing issues
    REGEN_SPEC_MODULE = False
    if REGEN_SPEC_MODULE:
        comp_members = serde.read_json(WIP_NAMES, list[str])
        generate_spec_module(comp_members, WIP_SPEC_MODULE)
