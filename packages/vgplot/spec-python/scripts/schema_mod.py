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
from typing import Final

from tools import fs, serde
from tools.codegen import typed_dict
from tools.codemod import fragments
from tools.models import source as m

GENERATED_MODULE_NAME = "mosaic"
SCHEMA_IN = fs.SPEC / "dist/mosaic-schema.json"
SCHEMA_OUT = fs.SPEC_PYTHON / "schema" / f"{GENERATED_MODULE_NAME}.json"

SPEC_INTERSECTION_MODULE = fs.MOSAIC_SPEC / "_spec.py"

KEYS_REPLACE: Final = {"as": "bind", "from": "source", "for": "plot"}
"""Keys that collide with [`keyword.kwlist`][], but the values are required.

These keys only appear in `"properties"` and `"required"`, the challenge is finding those guys.
"""

SPEC: Final = "Spec"
"""Name of the `Spec` union and prefix for it's members"""

SPEC_HEAD: Final = "SpecHead"
"""Name of the base `TypedDict` for all `Spec` members.

Mixing this into the bases with the `Component` member is a limited form of an intersection type.
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


# TODO @dangotbanned: Fix typing issues in `mosaic_spec/_spec.py`
def generate_python_schema(source: str | Path, target: str | Path) -> None:
    print(f"Reading json schema at: {Path(source).relative_to(fs.MONOREPO_ROOT).as_posix()}")
    schema = serde.read_json(source, m.InputSchema)
    definitions = schema.definitions
    _spec_todo = definitions.pop("Spec")
    schema.definitions = {k: _recursive_replace(v) for k, v in definitions.items()}
    print("Finished renaming & Spec removal")

    schema.flatten_component_union()
    serde.write_json(target, schema)
    print(f"Generated python schema at: {fs.repo_relative_str(target)}")

    components = {name: s for name, s in schema.definitions.items() if s.x_base_open}
    generate_spec_module(components, SPEC_INTERSECTION_MODULE)


def generate_spec_module(components: dict[str, m.JsonSchema], target: str | Path) -> None:
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
    gen_mosaic = fs.MOSAIC_SPEC / "_gen" / "mosaic.py"

    module = deque(typed_dict.iter_lines(SPEC_HEAD, spec_fields))
    import_from = fragments.import_from
    module.extendleft(
        (
            import_from(fs.MOSAIC_SPEC / "_typing_compat.py", ("TypedDict", "TypeAliasType")),
            import_from(gen_mosaic, (fld.tp for fld in spec_fields)),
        )
    )

    import_names = deque[str]()
    export_names = deque[str]()

    for original_name, component in components.items():
        base_open_name = component.x_base_open
        import_names.append(base_open_name)
        name = f"{SPEC}{original_name}"
        module.extend(typed_dict.iter_lines(name, bases=(SPEC_HEAD, base_open_name), closed=True))
        export_names.append(name)

    module.append(f"{SPEC} = TypeAliasType({SPEC!r}, {'|'.join(export_names)})")
    export_names.append(SPEC)
    module.appendleft(import_from(gen_mosaic, import_names))
    module.appendleft(fragments.FUTURE_ANNOTATIONS)
    module.append(f"__all__ = {tuple(export_names)}\n")

    target = Path(target)
    target.touch()
    target.write_text("\n".join(module), "utf8", newline="\n")
    print(f"Generated spec module at: {fs.repo_relative_str(target)}")


if __name__ == "__main__":
    generate_python_schema(SCHEMA_IN, SCHEMA_OUT)
