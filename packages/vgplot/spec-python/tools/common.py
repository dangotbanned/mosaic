from __future__ import annotations

from typing import Final, NewType

PyIdentifier = NewType("PyIdentifier", str)
"""A name that is a [valid python identifier][1].

[1]: https://docs.python.org/3/reference/lexical_analysis.html#names-identifiers-and-keywords
"""

PyIdentifierSnake = NewType("PyIdentifierSnake", str)
"""A snake_case name that is a [valid python identifier][1].

[1]: https://docs.python.org/3/reference/lexical_analysis.html#names-identifiers-and-keywords
"""

POUND_DEFS: Final = "#/definitions/"
