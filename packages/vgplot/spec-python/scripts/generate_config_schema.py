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

from tools import _rich, fs, serde

if TYPE_CHECKING:
    from pathlib import Path
    from types import GenericAlias

    import griffe

_DESC = "description"
_SCOPES_PREFIX = "scopes."
_SCOPE_BASE_CLASS = "scopes._BaseScopes"
_CONFIG_PACKAGE_PREFIX = "tools.config."
_ACTION_TAG = "action"


def _patched_msgspec_json_schema_get_class_name(cls: GenericAlias | Any) -> Any:
    """Monkeypatched version of [msgspec._json_schema._get_class_name].

    ## Notes
    - The original function controls the name used in `"$defs"`, but is deeply nested in private calls
    - We need control of the name, because without a module-qualifier, we cannot easily find it using Griffe

    [msgspec._json_schema._get_class_name]: https://github.com/msgspec/msgspec/blob/c5c30121cd7e1da7b7e115ce947982f51589491a/src/msgspec/_json_schema.py#L162-L167
    """
    if hasattr(cls, "__origin__"):
        name = cls.__origin__.__name__
        args = ", ".join(a.__name__ if isinstance(a, type) else repr(a) for a in cls.__args__)
        return f"{name}[{args}]"
    return f"{cls.__module__.removeprefix(_CONFIG_PACKAGE_PREFIX)}.{cls.__name__}"


def _generate_msgspec() -> dict[str, Any]:
    import msgspec._json_schema

    from tools.config import MosaicSpecToml

    # NOTE: Yes, this is pretty gnarly ...
    setattr(msgspec._json_schema, "_get_class_name", _patched_msgspec_json_schema_get_class_name)  # ruff: ignore[set-attr-with-constant]

    schema = serde.schema(MosaicSpecToml)
    defs: dict[str, dict[str, Any]] = schema["$defs"]
    for defn in defs.values():
        title: str = defn["title"]
        defn["title"] = title.rsplit(".", maxsplit=1)[-1]

    schema |= {
        "title": "MosaicSpecToml",
        # https://tombi-toml.github.io/tombi/docs/json-schema#x-tombi-string-formats
        "x-tombi-string-formats": [
            "uri-reference",
            "date-time",
            "date-time-local",
            "date",
            "time",
            "time-local",
            "regex",
        ],
    }
    return schema


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
    schema = _generate_msgspec()
    result = griffe_enhance(schema)
    serde.write_json(target, result.schema, pretty=True)
    _rich.print_path("Generated TOML schema", target)
    result.display_report()


def griffe_load_config_package(tools_path: Path) -> griffe.Module:
    import griffe

    ext = griffe.load_extensions("griffe_inherited_docstrings")
    return griffe.load(tools_path, extensions=ext)["config"]


def try_get_doc(package: griffe.Module, member: str) -> str | None:
    griffe_obj: griffe.Class | griffe.Attribute = package[member]
    if (griffe_doc := griffe_obj.docstring) and (parsed := griffe_doc.value):
        return parsed
    return None


def griffe_enhance(schema: dict[str, Any]) -> GriffeResult:
    models_config = griffe_load_config_package(fs.SPEC_PYTHON / "tools")
    definitions: dict[str, dict[str, Any]] = schema["$defs"]
    resolved = []
    unresolved = []
    for def_name, def_schema in definitions.items():
        if not def_schema.get(_DESC):
            if (doc := try_get_doc(models_config, def_name)) or (
                def_name.startswith(_SCOPES_PREFIX)
                and (doc := try_get_doc(models_config, _SCOPE_BASE_CLASS))
            ):
                def_schema[_DESC] = doc
                resolved.append(def_name)
            else:
                unresolved.append(def_name)

        for prop_name, prop in def_schema.get("properties", {}).items():
            if prop_name == _ACTION_TAG and "enum" in prop:
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
    from tools._colorize_install import install

    install()
    main(fs.MOSAIC_SPEC_TOML_SCHEMA)
