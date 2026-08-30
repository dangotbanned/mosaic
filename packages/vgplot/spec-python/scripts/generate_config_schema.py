# /// script
# requires-python = ">=3.14"
# ///
"""Update the schema that validates `mosaic-spec.toml`.

The initial schema is generated via [`msgspec`] and documentation is improved via [Griffe]'s deeper understanding of docstrings.

[`msgspec`]: https://msgspec.dev/jsonschema
[Griffe]: https://mkdocstrings.github.io/griffe/guide/users/recommendations/docstrings/

## Tip
For IDE support, [install tombi](https://tombi-toml.github.io/tombi/docs/installation).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from tools import fs

if TYPE_CHECKING:
    from pathlib import Path

    import griffe


@dataclass
class GriffeResult:
    schema: dict[str, Any]
    docs_added: list[str]
    docs_missing: list[str]

    def display_report(self) -> None:
        added, missing = self.docs_added, self.docs_missing
        print("Griffe post-processing results:")
        print(f"Added docs ({len(added)}):\n{'\n'.join(f" - '{s}'" for s in added)}")
        print(f"\nUnresolved docs ({len(missing)}):\n{'\n'.join(f" - '{s}'" for s in missing)}")


def main(target: Path, /) -> None:
    from tools import models, serde

    schema = serde.schema(models.config.MosaicSpecToml)
    # https://tombi-toml.github.io/tombi/docs/json-schema#x-tombi-string-formats
    schema |= {
        "x-tombi-string-formats": [
            "uri-reference",
            "date-time",
            "date-time-local",
            "date",
            "time",
            "time-local",
            "regex",
        ]
    }
    result = griffe_enhance(schema)
    serde.write_json(target, result.schema, pretty=True)
    print(f"Generated TOML schema at: {fs.repo_relative_str(target)}")
    result.display_report()


def griffe_load_config_module(tools_path: Path) -> griffe.Module:
    import griffe

    ext = griffe.load_extensions("griffe_inherited_docstrings")
    return griffe.load(tools_path, extensions=ext)["models.config"]


def try_get_doc(module: griffe.Module, member: str) -> str | None:
    griffe_obj: griffe.Class | griffe.Attribute = module[member]
    if (griffe_doc := griffe_obj.docstring) and (parsed := griffe_doc.value):
        return parsed
    return None


_DESC = "description"
_SCOPE_BASE_CLASS = "_BaseScopes"


def griffe_enhance(schema: dict[str, Any]) -> GriffeResult:
    models_config = griffe_load_config_module(fs.SPEC_PYTHON / "tools")
    definitions: dict[str, dict[str, Any]] = schema["$defs"]
    resolved = []
    unresolved = []
    for def_name, def_schema in definitions.items():
        if not def_schema.get(_DESC):
            if (doc := try_get_doc(models_config, def_name)) or (
                def_name.endswith("Scope")
                and (doc := try_get_doc(models_config, _SCOPE_BASE_CLASS))
            ):
                def_schema[_DESC] = doc
                resolved.append(def_name)
            else:
                unresolved.append(def_name)

        for prop_name, prop in def_schema.get("properties", {}).items():
            if prop_name == "action" and "enum" in prop:
                if _DESC not in prop and (description := def_schema.get(_DESC)):
                    prop[_DESC] = description
            elif not prop.get(_DESC):
                prop_path = f"{def_name}.{prop_name}"
                if doc := try_get_doc(models_config, prop_path):
                    prop[_DESC] = doc
                    resolved.append(prop_path)
                else:
                    unresolved.append(prop_path)

    return GriffeResult(schema, sorted(resolved), sorted(unresolved))


if __name__ == "__main__":
    main(fs.MOSAIC_SPEC_TOML_SCHEMA)
