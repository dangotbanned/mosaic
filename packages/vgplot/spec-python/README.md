# mosaic-spec

Python typing for authoring [Mosaic] visualizations, derived from [Mosaic Spec].

[Mosaic]: https://idl.uw.edu/mosaic/
[Mosaic Spec]: https://idl.uw.edu/mosaic/spec/

> [!CAUTION]
> This API is experimental and breaking changes should be expected.  
> See ([#1075]) for motivation and ([roadmap]) for what's next.

[#1075]: https://github.com/uwdata/mosaic/issues/1075
[roadmap]: ./roadmap.md

## Usage

[Typed dictionaries]: https://typing.python.org/en/latest/spec/typeddict.html
[Type aliases]: https://typing.python.org/en/latest/spec/aliases.html

[`vgplot/spec/src/spec/Spec.ts`]: ../spec/src/spec/Spec.ts

`mosaic_spec` exports [Typed dictionaries] and [Type aliases] describing the
full public interface of [`vgplot/spec/src/spec/Spec.ts`].  
These symbols can be used in annotations to provide type checking for `dict`
literals:

```py
import mosaic_spec as ms

spec: ms.Spec = {
    "plot": [{"mark": "lineY", "data": {"source": "table"}, "x": "date", "y": "value"}],
    "width": 640,
    "height": 200,
}
```

Each `TypedDict` can be used directly, providing inline docs on hover:

```py
ms.LineY(
    data=[{"i": i, "u": u} for i, u in zip(range(8), "ABCDEFGH")],
    x="u",
    y="v",
    stroke="steelblue",
    curve="monotone-x",
    # ^ The curve (interpolation) method for connecting adjacent points. One of ...
    marker="circle",
    mark="lineY",
)
```

[`mosaic_spec.spec`]: ./src/mosaic_spec/spec.py
[Intersection Types]: https://www.typescriptlang.org/docs/handbook/2/objects.html#intersection-types

The [`mosaic_spec.spec`] namespace provides an entrypoint for each of the 81
plot, input widget, or layout components - as a means to represent TypeScript's
[Intersection Types]:

```py
spec = ms.spec.Plot(
    plot=[ms.LineY(mark="lineY", data={"source": "table"}, x="date", y="value")],
    width=640,
    height=200,
)
```

<!--TODO @dangotbanned: Missing bits

- [Unpack for keyword arguments](https://typing.python.org/en/latest/spec/callables.html#unpack-for-keyword-arguments)
  - Use case is "build your own builder"
  - Need to add another layer without discriminator fields
    - `transform.py` (e.g. `FirstValue` -> `first_value=...` ) require args in a key repeating their name
    - `marks.py` (e.g. `AreaX` -> `mark="areaX"` ) require a camelCase value in mark
        - `MarkOptions` partially addresses this one
    - As-is, the `Required` fields propagate to `**kwds` which is the part you'd want to avoid
- Converting to `vgplot` and/or `mosaic_widget`
  - There's an issue with reversing `{"for": "plot"}`
--->
