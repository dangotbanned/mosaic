# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "msgspec>=0.21.1",
# ]
# ///
"""Transform `packages/vgplot/spec/dist/mosaic-schema.json` for use in python."""

from __future__ import annotations

from pathlib import Path
from typing import Final

# TODO @dangotbanned: Unbreak path for `../*.ipynb`
try:
    import tools.models.source as models
    from tools import serde

    import fs
except ModuleNotFoundError:
    import sys

    sys.path.append(str(Path(__file__).parent.parent))
    from tools import serde
    from tools.models import source as models

    from scripts import fs


GENERATED_MODULE_NAME = "mosaic"
SCHEMA_IN = fs.SPEC / "dist/mosaic-schema.json"
SCHEMA_OUT = fs.SPEC_PYTHON / "schema" / f"{GENERATED_MODULE_NAME}.json"


KEYS_REPLACE: Final = {"as": "bind", "from": "source", "for": "plot"}
"""Keys that collide with [`keyword.kwlist`][], but the values are required.

These keys only appear in `"properties"` and `"required"`, the challenge is finding those guys.
"""


def _recursive_replace[T: (models.JsonSchema, models.ItemSchema)](schema: T) -> T:
    """Visit 4 fields at all levels of the schema, renaming matches for [`KEYS_REPLACE`][]."""
    replace = KEYS_REPLACE.get
    m = models
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
    schema = serde.read_json(source, models.InputSchema)
    definitions = schema.definitions
    _spec_todo = definitions.pop("Spec")
    schema.definitions = {k: _recursive_replace(v) for k, v in definitions.items()}
    serde.write_json(target, schema)
    print(f"Generated python schema at: {fs.repo_relative_str(target)}")


if __name__ == "__main__":
    main(SCHEMA_IN, SCHEMA_OUT)
