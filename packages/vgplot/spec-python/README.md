# mosaic-spec

Python typing for authoring [Mosaic](https://idl.uw.edu/mosaic/) visualizations, derived from [Mosaic Spec](https://idl.uw.edu/mosaic/spec/).

> [!WARNING]
> This is highly experimental.  
> See ([#1075](https://github.com/uwdata/mosaic/issues/1075)) for motivation and ([roadmap](./roadmap.md)) for what's next.

## Usage

```py
import mosaic_spec as ms

spec: ms.Spec = {
    "plot": [{"mark": "lineY", "data": {"source": "table"}, "x": "date", "y": "value"}],
    "width": 640,
    "height": 200,
}

spec = ms.spec.Plot(
    plot=[ms.LineY(mark="lineY", data={"source": "table"}, x="date", y="value")],
    width=640,
    height=200,
)
```
