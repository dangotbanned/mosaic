# /// script
# requires-python = ">=3.14"
# ///
"""Update the schema that validates `mosaic-spec.toml`.

## Tip
For IDE support, [install tombi](https://tombi-toml.github.io/tombi/docs/installation).
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from tools import fs

if TYPE_CHECKING:
    from pathlib import Path


# TODO @dangotbanned: (low priority) Use `griffe` for attribute docstrings -> schema descriptions
# - https://mkdocstrings.github.io/griffe/
# - https://github.com/msgspec/msgspec/blob/f51f378335b01dc0026dc6553a0b9e1915a8edae/src/msgspec/_json_schema.py#L170-L183
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
    serde.write_json(target, schema, pretty=True)
    print(f"Generated TOML schema at: {fs.repo_relative_str(target)}")


if __name__ == "__main__":
    main(fs.MOSAIC_SPEC_TOML_SCHEMA)
