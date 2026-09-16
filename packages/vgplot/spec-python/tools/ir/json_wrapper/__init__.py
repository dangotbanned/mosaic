"""The first representation.

The outer container `Root` stores a `definitions` table, much like a JSON Schema:

```py
Root(definitions={"definition_name": JsonWrapper(schema=Schema(...))})
```

The core difference is that each definition *wraps* a `Schema` inside one of 11 distinct node types:

```py
Object(  # < JsonWrapper
    fields={
        "agg": Primitive(  # < JsonWrapper
            type="string",
            schema=Schema(  # < Schema
                description="A SQL expression string to calculate an aggregate value...",
                type="string",
            ),
        ),
        "label": Primitive(  # < JsonWrapper
            type="string",
            schema=Schema(description="A label for this expression....", type="string"),  # < Schema
        ),
    },
    required=["agg"],
    closed="closed",
    extra_items=None,
    schema=Schema(  # < Schema
        description="A custom SQL aggregate expression.",
        type="object",
        additional_properties=False,
        required=["agg"],
        properties={
            "agg": Schema(description="...", type="string"),  # < Schema
            "label": Schema(description="...", type="string"),  # < Schema
        },
    ),
)
```

## Why so many types?

JSON schema has many [keywords] and some are [type-specific].
By contrast, most `JSONWrapper` nodes have a `schema` field and
only require a single additional field for data.

Things that *could be* an optional field are more commonly represented as a distinct type.
Having lots of hyper-specific types pairs nicely with [`@functools.singledispatch`],
which is used heavily for performance.

[keywords]: https://json-schema.org/understanding-json-schema/keywords
[type-specific]: https://json-schema.org/understanding-json-schema/reference/type
[`@functools.singledispatch`]: https://docs.python.org/3/library/functools.html#functools.singledispatch
"""

from __future__ import annotations

from tools.ir.json_wrapper import nodes
from tools.ir.json_wrapper.nodes import JsonWrapper
from tools.ir.json_wrapper.root import Root

__all__ = "JsonWrapper", "Root", "nodes"
