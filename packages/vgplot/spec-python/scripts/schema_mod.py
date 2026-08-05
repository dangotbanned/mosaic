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

from tools import codemod, fs, serde
from tools.codegen import typed_dict
from tools.codegen.docstrings import doc
from tools.models import mosaic as m

GENERATED_MODULE_NAME = "mosaic"
SCHEMA_IN = fs.SPEC / "dist/mosaic-schema.json"
SCHEMA_OUT = fs.SPEC_PYTHON / "schema" / f"{GENERATED_MODULE_NAME}.json"

GENERATED_MODULE = fs.MOSAIC_SPEC / "_gen" / f"{GENERATED_MODULE_NAME}.py"
TYPING_COMPAT = fs.MOSAIC_SPEC / "_typing_compat.py"

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
SPEC_HEAD_NO_DATA = f"_{SPEC_HEAD}"


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


def generate_python_schema(source: str | Path, target: str | Path) -> tuple[m.InputSchema, str]:
    print(f"Reading json schema at: {Path(source).relative_to(fs.MONOREPO_ROOT).as_posix()}")
    schema = serde.read_json(source, m.InputSchema)
    definitions = schema.definitions

    spec_def = definitions.pop("Spec")
    schema.ref = ""  # Removes `"$ref": "#/definitions/Spec"`
    schema.id = SCHEMA_OUT.name

    schema.definitions = {k: _recursive_replace(v) for k, v in definitions.items()}
    schema.flatten_component_union()
    serde.write_json(target, schema)
    print(f"Generated python schema at: {fs.repo_relative_str(target)}")
    return schema, spec_def.description


def generate_spec_module(
    components: dict[str, m.JsonSchema], spec_doc: str, target: str | Path
) -> None:
    fields_excluding_data = (
        typed_dict.Field("config", "Config", "Configuration options."),
        typed_dict.Field("meta", "Meta", "Specification metadata."),
        typed_dict.Field("params", "Params", "Param and Selection definitions."),
        typed_dict.Field(
            "plot_defaults",
            "PlotAttributes",
            "A default set of attributes to apply to all plot components.",
        ),
    )
    field_data = typed_dict.Field("data", "Data", "Dataset definitions.")
    module = deque(typed_dict.iter_lines(SPEC_HEAD_NO_DATA, fields_excluding_data))
    module.extend(typed_dict.iter_lines(SPEC_HEAD, (field_data,), bases=(SPEC_HEAD_NO_DATA,)))
    import_from = codemod.fragments.import_from
    module.extendleft(
        (
            import_from(TYPING_COMPAT, ("TypedDict", "TypeAliasType")),
            import_from(GENERATED_MODULE, (fld.tp for fld in (*fields_excluding_data, field_data))),
        )
    )

    import_names = deque[str]()
    export_names = deque[str]()

    for original_name, component in components.items():
        base_open_name = component.x_base_open
        import_names.append(base_open_name)
        name = f"{SPEC}{original_name}"
        base_spec = SPEC_HEAD_NO_DATA if "data" in component.properties else SPEC_HEAD
        module.extend(typed_dict.iter_lines(name, bases=(base_spec, base_open_name), closed=True))
        export_names.append(name)

    module.extend((f"{SPEC} = TypeAliasType({SPEC!r}, {'|'.join(export_names)})", doc(spec_doc)))
    export_names.append(SPEC)
    module.appendleft(import_from(GENERATED_MODULE, import_names))
    module.appendleft(codemod.fragments.FUTURE_ANNOTATIONS)
    module.append(f"\n__all__ = {tuple(export_names)}\n")
    fs.write_lines(target, module, "Generated module")


def main() -> None:
    # mosaic -> msgspec -> json -> datamodel-codegen -> back here for more
    schema, spec_doc = generate_python_schema(SCHEMA_IN, SCHEMA_OUT)
    components = {name: s for name, s in schema.definitions.items() if s.x_base_open}
    fs.run("uv", "run", "datamodel-codegen", "--profile=spec")
    print(f"Generated module at: {fs.repo_relative_str(GENERATED_MODULE)}")
    generate_spec_module(components, spec_doc, fs.MOSAIC_SPEC_INTERSECTION)


if __name__ == "__main__":
    main()
