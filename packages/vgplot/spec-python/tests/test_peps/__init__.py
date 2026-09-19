"""Handwritten test suite, inspired by related [Typing PEPs] [^1].

[^1]: *PEP* stands for Python Enhancement Proposal.

The goal is to provide project-specific coverage, which we can't get from [`tests/test_examples/`] alone.

Also it should easier to spot regressions within these more focused cases
vs a needle in a more [complex example].

## [`TypedDict`]

### Finished PEPs (done, with a stable interface)

- [x] [PEP 589] - TypedDict: Type Hints for Dictionaries with a Fixed Set of Keys
- [x] [PEP 655] - Marking individual TypedDict items as required or potentially-missing
- [x] [PEP 692] - Using TypedDict for more precise **kwargs typing.
- [ ] [PEP 728] - TypedDict with Typed Extra Items

Another good source for cases are the [Type System Conformance] tests.

### Open PEPs (under consideration)

Covering these is a much lower priority.
We also need to wait for reference implementations to become available:

- [ ] [PEP 764] - Inline typed dictionaries
  - `ty` marks this syntax as `@Todo`
  - `pyright` seems to ignore it
- [ ] [PEP 821] - Support for unpacking TypedDicts in Callable type hints


## Related

- [ ] [PEP 695] - Type Parameter Syntax
  - Just the `TypeAliasType` part
- [ ] [PEP 747] - Annotating Type Forms
- [ ] [PEP 827] - Type Manipulation
  - Covers significantly more than just [`TypedDict`]
  - Includes a [`NewTypedDict`] operator
  - Demonstrates reproducing [TypeScript-style "Utility Types"]

[`tests/test_examples/`]: https://github.com/dangotbanned/mosaic/blob/spec-python/hand-rolled/packages/vgplot/spec-python/tests/test_examples
[complex example]: https://github.com/dangotbanned/mosaic/blob/spec-python/hand-rolled/packages/vgplot/spec-python/tests/test_examples/test_splom.py
[Typing PEPs]: https://peps.python.org/topic/typing
[`TypedDict`]: https://typing.python.org/en/latest/spec/typeddict.html
[Type System Conformance]: https://github.com/python/typing/tree/main/conformance/tests
[PEP 589]: https://peps.python.org/pep-0589/
[PEP 655]: https://peps.python.org/pep-0655/
[PEP 692]: https://peps.python.org/pep-0692/
[PEP 695]: https://peps.python.org/pep-0695/
[PEP 728]: https://peps.python.org/pep-0728/
[PEP 747]: https://peps.python.org/pep-0747/
[PEP 764]: https://peps.python.org/pep-0764/
[PEP 821]: https://peps.python.org/pep-0821/
[PEP 827]: https://peps.python.org/pep-0827/
[`NewTypedDict`]: https://peps.python.org/pep-0827/#object-creation
[TypeScript-style "Utility Types"]: https://peps.python.org/pep-0827/#typescript-style-utility-types
"""
