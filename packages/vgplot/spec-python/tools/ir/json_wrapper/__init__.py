"""Very-intermediate-representation for tagging *from* a JSON schema.

This layer is about narrowing from the infinite possibilities of JSON schema [keywords]
and [type-specific keywords] into one of 11 distinct node types.

Excluding `Object` and `Sequence`, all nodes have *at-most* 1 attribute.

In this context, *wrapper* means that the original (sub)schema is preserved on each node,
accessible via [`tools.ir.JSONWrapper.schema`][].

[keywords]: https://json-schema.org/understanding-json-schema/keywords
[type-specific keywords]: https://json-schema.org/understanding-json-schema/reference/type
"""

from __future__ import annotations

from tools.ir.json_wrapper import nodes
from tools.ir.json_wrapper.nodes import JsonWrapper
from tools.ir.json_wrapper.root import Root

__all__ = "JsonWrapper", "Root", "nodes"
