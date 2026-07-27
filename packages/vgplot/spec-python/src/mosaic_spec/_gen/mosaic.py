# NOTE: DO NOT EDIT.
# Regenerate with: pnpm generate

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any, Literal, TypeAlias, Union

from typing_extensions import NotRequired, TypedDict


class AggregateExpression(TypedDict, closed=True):
    agg: str
    label: NotRequired[str]


BinInterval: TypeAlias = Literal[
    "date", "number", "millisecond", "second", "minute", "hour", "day", "month", "year"
]


class BrushStyles(TypedDict, closed=True):
    fill: NotRequired[str]
    fill_opacity: NotRequired[float]
    opacity: NotRequired[float]
    stroke: NotRequired[str]
    stroke_dasharray: NotRequired[str]
    stroke_opacity: NotRequired[float]


class CSSStyles(TypedDict, extra_items=str):
    accent_color: NotRequired[str]
    align_content: NotRequired[str]
    align_items: NotRequired[str]
    align_self: NotRequired[str]
    alignment_baseline: NotRequired[str]
    all: NotRequired[str]
    animation: NotRequired[str]
    animation_composition: NotRequired[str]
    animation_delay: NotRequired[str]
    animation_direction: NotRequired[str]
    animation_duration: NotRequired[str]
    animation_fill_mode: NotRequired[str]
    animation_iteration_count: NotRequired[str]
    animation_name: NotRequired[str]
    animation_play_state: NotRequired[str]
    animation_timing_function: NotRequired[str]
    appearance: NotRequired[str]
    aspect_ratio: NotRequired[str]
    backdrop_filter: NotRequired[str]
    backface_visibility: NotRequired[str]
    background: NotRequired[str]
    background_attachment: NotRequired[str]
    background_blend_mode: NotRequired[str]
    background_clip: NotRequired[str]
    background_color: NotRequired[str]
    background_image: NotRequired[str]
    background_origin: NotRequired[str]
    background_position: NotRequired[str]
    background_position_x: NotRequired[str]
    background_position_y: NotRequired[str]
    background_repeat: NotRequired[str]
    background_size: NotRequired[str]
    baseline_shift: NotRequired[str]
    baseline_source: NotRequired[str]
    block_size: NotRequired[str]
    border: NotRequired[str]
    border_block: NotRequired[str]
    border_block_color: NotRequired[str]
    border_block_end: NotRequired[str]
    border_block_end_color: NotRequired[str]
    border_block_end_style: NotRequired[str]
    border_block_end_width: NotRequired[str]
    border_block_start: NotRequired[str]
    border_block_start_color: NotRequired[str]
    border_block_start_style: NotRequired[str]
    border_block_start_width: NotRequired[str]
    border_block_style: NotRequired[str]
    border_block_width: NotRequired[str]
    border_bottom: NotRequired[str]
    border_bottom_color: NotRequired[str]
    border_bottom_left_radius: NotRequired[str]
    border_bottom_right_radius: NotRequired[str]
    border_bottom_style: NotRequired[str]
    border_bottom_width: NotRequired[str]
    border_collapse: NotRequired[str]
    border_color: NotRequired[str]
    border_end_end_radius: NotRequired[str]
    border_end_start_radius: NotRequired[str]
    border_image: NotRequired[str]
    border_image_outset: NotRequired[str]
    border_image_repeat: NotRequired[str]
    border_image_slice: NotRequired[str]
    border_image_source: NotRequired[str]
    border_image_width: NotRequired[str]
    border_inline: NotRequired[str]
    border_inline_color: NotRequired[str]
    border_inline_end: NotRequired[str]
    border_inline_end_color: NotRequired[str]
    border_inline_end_style: NotRequired[str]
    border_inline_end_width: NotRequired[str]
    border_inline_start: NotRequired[str]
    border_inline_start_color: NotRequired[str]
    border_inline_start_style: NotRequired[str]
    border_inline_start_width: NotRequired[str]
    border_inline_style: NotRequired[str]
    border_inline_width: NotRequired[str]
    border_left: NotRequired[str]
    border_left_color: NotRequired[str]
    border_left_style: NotRequired[str]
    border_left_width: NotRequired[str]
    border_radius: NotRequired[str]
    border_right: NotRequired[str]
    border_right_color: NotRequired[str]
    border_right_style: NotRequired[str]
    border_right_width: NotRequired[str]
    border_spacing: NotRequired[str]
    border_start_end_radius: NotRequired[str]
    border_start_start_radius: NotRequired[str]
    border_style: NotRequired[str]
    border_top: NotRequired[str]
    border_top_color: NotRequired[str]
    border_top_left_radius: NotRequired[str]
    border_top_right_radius: NotRequired[str]
    border_top_style: NotRequired[str]
    border_top_width: NotRequired[str]
    border_width: NotRequired[str]
    bottom: NotRequired[str]
    box_decoration_break: NotRequired[str]
    box_shadow: NotRequired[str]
    box_sizing: NotRequired[str]
    break_after: NotRequired[str]
    break_before: NotRequired[str]
    break_inside: NotRequired[str]
    caption_side: NotRequired[str]
    caret_color: NotRequired[str]
    clear: NotRequired[str]
    clip: NotRequired[str]
    clip_path: NotRequired[str]
    clip_rule: NotRequired[str]
    color: NotRequired[str]
    color_interpolation: NotRequired[str]
    color_interpolation_filters: NotRequired[str]
    color_scheme: NotRequired[str]
    column_count: NotRequired[str]
    column_fill: NotRequired[str]
    column_gap: NotRequired[str]
    column_rule: NotRequired[str]
    column_rule_color: NotRequired[str]
    column_rule_style: NotRequired[str]
    column_rule_width: NotRequired[str]
    column_span: NotRequired[str]
    column_width: NotRequired[str]
    columns: NotRequired[str]
    contain: NotRequired[str]
    contain_intrinsic_block_size: NotRequired[str]
    contain_intrinsic_height: NotRequired[str]
    contain_intrinsic_inline_size: NotRequired[str]
    contain_intrinsic_size: NotRequired[str]
    contain_intrinsic_width: NotRequired[str]
    container: NotRequired[str]
    container_name: NotRequired[str]
    container_type: NotRequired[str]
    content: NotRequired[str]
    content_visibility: NotRequired[str]
    counter_increment: NotRequired[str]
    counter_reset: NotRequired[str]
    counter_set: NotRequired[str]
    css_float: NotRequired[str]
    css_text: NotRequired[str]
    cursor: NotRequired[str]
    cx: NotRequired[str]
    cy: NotRequired[str]
    d: NotRequired[str]
    direction: NotRequired[str]
    display: NotRequired[str]
    dominant_baseline: NotRequired[str]
    empty_cells: NotRequired[str]
    fill: NotRequired[str]
    fill_opacity: NotRequired[str]
    fill_rule: NotRequired[str]
    filter: NotRequired[str]
    flex: NotRequired[str]
    flex_basis: NotRequired[str]
    flex_direction: NotRequired[str]
    flex_flow: NotRequired[str]
    flex_grow: NotRequired[str]
    flex_shrink: NotRequired[str]
    flex_wrap: NotRequired[str]
    float: NotRequired[str]
    flood_color: NotRequired[str]
    flood_opacity: NotRequired[str]
    font: NotRequired[str]
    font_family: NotRequired[str]
    font_feature_settings: NotRequired[str]
    font_kerning: NotRequired[str]
    font_optical_sizing: NotRequired[str]
    font_palette: NotRequired[str]
    font_size: NotRequired[str]
    font_size_adjust: NotRequired[str]
    font_stretch: NotRequired[str]
    font_style: NotRequired[str]
    font_synthesis: NotRequired[str]
    font_synthesis_small_caps: NotRequired[str]
    font_synthesis_style: NotRequired[str]
    font_synthesis_weight: NotRequired[str]
    font_variant: NotRequired[str]
    font_variant_alternates: NotRequired[str]
    font_variant_caps: NotRequired[str]
    font_variant_east_asian: NotRequired[str]
    font_variant_ligatures: NotRequired[str]
    font_variant_numeric: NotRequired[str]
    font_variant_position: NotRequired[str]
    font_variation_settings: NotRequired[str]
    font_weight: NotRequired[str]
    forced_color_adjust: NotRequired[str]
    gap: NotRequired[str]
    grid: NotRequired[str]
    grid_area: NotRequired[str]
    grid_auto_columns: NotRequired[str]
    grid_auto_flow: NotRequired[str]
    grid_auto_rows: NotRequired[str]
    grid_column: NotRequired[str]
    grid_column_end: NotRequired[str]
    grid_column_gap: NotRequired[str]
    grid_column_start: NotRequired[str]
    grid_gap: NotRequired[str]
    grid_row: NotRequired[str]
    grid_row_end: NotRequired[str]
    grid_row_gap: NotRequired[str]
    grid_row_start: NotRequired[str]
    grid_template: NotRequired[str]
    grid_template_areas: NotRequired[str]
    grid_template_columns: NotRequired[str]
    grid_template_rows: NotRequired[str]
    height: NotRequired[str]
    hyphenate_character: NotRequired[str]
    hyphenate_limit_chars: NotRequired[str]
    hyphens: NotRequired[str]
    image_orientation: NotRequired[str]
    image_rendering: NotRequired[str]
    inline_size: NotRequired[str]
    inset: NotRequired[str]
    inset_block: NotRequired[str]
    inset_block_end: NotRequired[str]
    inset_block_start: NotRequired[str]
    inset_inline: NotRequired[str]
    inset_inline_end: NotRequired[str]
    inset_inline_start: NotRequired[str]
    isolation: NotRequired[str]
    justify_content: NotRequired[str]
    justify_items: NotRequired[str]
    justify_self: NotRequired[str]
    left: NotRequired[str]
    length: NotRequired[float]
    letter_spacing: NotRequired[str]
    lighting_color: NotRequired[str]
    line_break: NotRequired[str]
    line_height: NotRequired[str]
    list_style: NotRequired[str]
    list_style_image: NotRequired[str]
    list_style_position: NotRequired[str]
    list_style_type: NotRequired[str]
    margin: NotRequired[str]
    margin_block: NotRequired[str]
    margin_block_end: NotRequired[str]
    margin_block_start: NotRequired[str]
    margin_bottom: NotRequired[str]
    margin_inline: NotRequired[str]
    margin_inline_end: NotRequired[str]
    margin_inline_start: NotRequired[str]
    margin_left: NotRequired[str]
    margin_right: NotRequired[str]
    margin_top: NotRequired[str]
    marker: NotRequired[str]
    marker_end: NotRequired[str]
    marker_mid: NotRequired[str]
    marker_start: NotRequired[str]
    mask: NotRequired[str]
    mask_clip: NotRequired[str]
    mask_composite: NotRequired[str]
    mask_image: NotRequired[str]
    mask_mode: NotRequired[str]
    mask_origin: NotRequired[str]
    mask_position: NotRequired[str]
    mask_repeat: NotRequired[str]
    mask_size: NotRequired[str]
    mask_type: NotRequired[str]
    math_depth: NotRequired[str]
    math_style: NotRequired[str]
    max_block_size: NotRequired[str]
    max_height: NotRequired[str]
    max_inline_size: NotRequired[str]
    max_width: NotRequired[str]
    min_block_size: NotRequired[str]
    min_height: NotRequired[str]
    min_inline_size: NotRequired[str]
    min_width: NotRequired[str]
    mix_blend_mode: NotRequired[str]
    object_fit: NotRequired[str]
    object_position: NotRequired[str]
    offset: NotRequired[str]
    offset_anchor: NotRequired[str]
    offset_distance: NotRequired[str]
    offset_path: NotRequired[str]
    offset_position: NotRequired[str]
    offset_rotate: NotRequired[str]
    opacity: NotRequired[str]
    order: NotRequired[str]
    orphans: NotRequired[str]
    outline: NotRequired[str]
    outline_color: NotRequired[str]
    outline_offset: NotRequired[str]
    outline_style: NotRequired[str]
    outline_width: NotRequired[str]
    overflow: NotRequired[str]
    overflow_anchor: NotRequired[str]
    overflow_block: NotRequired[str]
    overflow_clip_margin: NotRequired[str]
    overflow_inline: NotRequired[str]
    overflow_wrap: NotRequired[str]
    overflow_x: NotRequired[str]
    overflow_y: NotRequired[str]
    overscroll_behavior: NotRequired[str]
    overscroll_behavior_block: NotRequired[str]
    overscroll_behavior_inline: NotRequired[str]
    overscroll_behavior_x: NotRequired[str]
    overscroll_behavior_y: NotRequired[str]
    padding: NotRequired[str]
    padding_block: NotRequired[str]
    padding_block_end: NotRequired[str]
    padding_block_start: NotRequired[str]
    padding_bottom: NotRequired[str]
    padding_inline: NotRequired[str]
    padding_inline_end: NotRequired[str]
    padding_inline_start: NotRequired[str]
    padding_left: NotRequired[str]
    padding_right: NotRequired[str]
    padding_top: NotRequired[str]
    page: NotRequired[str]
    page_break_after: NotRequired[str]
    page_break_before: NotRequired[str]
    page_break_inside: NotRequired[str]
    paint_order: NotRequired[str]
    perspective: NotRequired[str]
    perspective_origin: NotRequired[str]
    place_content: NotRequired[str]
    place_items: NotRequired[str]
    place_self: NotRequired[str]
    pointer_events: NotRequired[str]
    position: NotRequired[str]
    print_color_adjust: NotRequired[str]
    quotes: NotRequired[str]
    r: NotRequired[str]
    resize: NotRequired[str]
    right: NotRequired[str]
    rotate: NotRequired[str]
    row_gap: NotRequired[str]
    ruby_align: NotRequired[str]
    ruby_position: NotRequired[str]
    rx: NotRequired[str]
    ry: NotRequired[str]
    scale: NotRequired[str]
    scroll_behavior: NotRequired[str]
    scroll_margin: NotRequired[str]
    scroll_margin_block: NotRequired[str]
    scroll_margin_block_end: NotRequired[str]
    scroll_margin_block_start: NotRequired[str]
    scroll_margin_bottom: NotRequired[str]
    scroll_margin_inline: NotRequired[str]
    scroll_margin_inline_end: NotRequired[str]
    scroll_margin_inline_start: NotRequired[str]
    scroll_margin_left: NotRequired[str]
    scroll_margin_right: NotRequired[str]
    scroll_margin_top: NotRequired[str]
    scroll_padding: NotRequired[str]
    scroll_padding_block: NotRequired[str]
    scroll_padding_block_end: NotRequired[str]
    scroll_padding_block_start: NotRequired[str]
    scroll_padding_bottom: NotRequired[str]
    scroll_padding_inline: NotRequired[str]
    scroll_padding_inline_end: NotRequired[str]
    scroll_padding_inline_start: NotRequired[str]
    scroll_padding_left: NotRequired[str]
    scroll_padding_right: NotRequired[str]
    scroll_padding_top: NotRequired[str]
    scroll_snap_align: NotRequired[str]
    scroll_snap_stop: NotRequired[str]
    scroll_snap_type: NotRequired[str]
    scrollbar_color: NotRequired[str]
    scrollbar_gutter: NotRequired[str]
    scrollbar_width: NotRequired[str]
    shape_image_threshold: NotRequired[str]
    shape_margin: NotRequired[str]
    shape_outside: NotRequired[str]
    shape_rendering: NotRequired[str]
    stop_color: NotRequired[str]
    stop_opacity: NotRequired[str]
    stroke: NotRequired[str]
    stroke_dasharray: NotRequired[str]
    stroke_dashoffset: NotRequired[str]
    stroke_linecap: NotRequired[str]
    stroke_linejoin: NotRequired[str]
    stroke_miterlimit: NotRequired[str]
    stroke_opacity: NotRequired[str]
    stroke_width: NotRequired[str]
    tab_size: NotRequired[str]
    table_layout: NotRequired[str]
    text_align: NotRequired[str]
    text_align_last: NotRequired[str]
    text_anchor: NotRequired[str]
    text_box: NotRequired[str]
    text_box_edge: NotRequired[str]
    text_box_trim: NotRequired[str]
    text_combine_upright: NotRequired[str]
    text_decoration: NotRequired[str]
    text_decoration_color: NotRequired[str]
    text_decoration_line: NotRequired[str]
    text_decoration_skip_ink: NotRequired[str]
    text_decoration_style: NotRequired[str]
    text_decoration_thickness: NotRequired[str]
    text_emphasis: NotRequired[str]
    text_emphasis_color: NotRequired[str]
    text_emphasis_position: NotRequired[str]
    text_emphasis_style: NotRequired[str]
    text_indent: NotRequired[str]
    text_orientation: NotRequired[str]
    text_overflow: NotRequired[str]
    text_rendering: NotRequired[str]
    text_shadow: NotRequired[str]
    text_transform: NotRequired[str]
    text_underline_offset: NotRequired[str]
    text_underline_position: NotRequired[str]
    text_wrap: NotRequired[str]
    text_wrap_mode: NotRequired[str]
    text_wrap_style: NotRequired[str]
    top: NotRequired[str]
    touch_action: NotRequired[str]
    transform: NotRequired[str]
    transform_box: NotRequired[str]
    transform_origin: NotRequired[str]
    transform_style: NotRequired[str]
    transition: NotRequired[str]
    transition_behavior: NotRequired[str]
    transition_delay: NotRequired[str]
    transition_duration: NotRequired[str]
    transition_property: NotRequired[str]
    transition_timing_function: NotRequired[str]
    translate: NotRequired[str]
    unicode_bidi: NotRequired[str]
    user_select: NotRequired[str]
    vector_effect: NotRequired[str]
    vertical_align: NotRequired[str]
    view_transition_class: NotRequired[str]
    view_transition_name: NotRequired[str]
    visibility: NotRequired[str]
    webkit_align_content: NotRequired[str]
    webkit_align_items: NotRequired[str]
    webkit_align_self: NotRequired[str]
    webkit_animation: NotRequired[str]
    webkit_animation_delay: NotRequired[str]
    webkit_animation_direction: NotRequired[str]
    webkit_animation_duration: NotRequired[str]
    webkit_animation_fill_mode: NotRequired[str]
    webkit_animation_iteration_count: NotRequired[str]
    webkit_animation_name: NotRequired[str]
    webkit_animation_play_state: NotRequired[str]
    webkit_animation_timing_function: NotRequired[str]
    webkit_appearance: NotRequired[str]
    webkit_backface_visibility: NotRequired[str]
    webkit_background_clip: NotRequired[str]
    webkit_background_origin: NotRequired[str]
    webkit_background_size: NotRequired[str]
    webkit_border_bottom_left_radius: NotRequired[str]
    webkit_border_bottom_right_radius: NotRequired[str]
    webkit_border_radius: NotRequired[str]
    webkit_border_top_left_radius: NotRequired[str]
    webkit_border_top_right_radius: NotRequired[str]
    webkit_box_align: NotRequired[str]
    webkit_box_flex: NotRequired[str]
    webkit_box_ordinal_group: NotRequired[str]
    webkit_box_orient: NotRequired[str]
    webkit_box_pack: NotRequired[str]
    webkit_box_shadow: NotRequired[str]
    webkit_box_sizing: NotRequired[str]
    webkit_filter: NotRequired[str]
    webkit_flex: NotRequired[str]
    webkit_flex_basis: NotRequired[str]
    webkit_flex_direction: NotRequired[str]
    webkit_flex_flow: NotRequired[str]
    webkit_flex_grow: NotRequired[str]
    webkit_flex_shrink: NotRequired[str]
    webkit_flex_wrap: NotRequired[str]
    webkit_justify_content: NotRequired[str]
    webkit_line_clamp: NotRequired[str]
    webkit_mask: NotRequired[str]
    webkit_mask_box_image: NotRequired[str]
    webkit_mask_box_image_outset: NotRequired[str]
    webkit_mask_box_image_repeat: NotRequired[str]
    webkit_mask_box_image_slice: NotRequired[str]
    webkit_mask_box_image_source: NotRequired[str]
    webkit_mask_box_image_width: NotRequired[str]
    webkit_mask_clip: NotRequired[str]
    webkit_mask_composite: NotRequired[str]
    webkit_mask_image: NotRequired[str]
    webkit_mask_origin: NotRequired[str]
    webkit_mask_position: NotRequired[str]
    webkit_mask_repeat: NotRequired[str]
    webkit_mask_size: NotRequired[str]
    webkit_order: NotRequired[str]
    webkit_perspective: NotRequired[str]
    webkit_perspective_origin: NotRequired[str]
    webkit_text_fill_color: NotRequired[str]
    webkit_text_size_adjust: NotRequired[str]
    webkit_text_stroke: NotRequired[str]
    webkit_text_stroke_color: NotRequired[str]
    webkit_text_stroke_width: NotRequired[str]
    webkit_transform: NotRequired[str]
    webkit_transform_origin: NotRequired[str]
    webkit_transform_style: NotRequired[str]
    webkit_transition: NotRequired[str]
    webkit_transition_delay: NotRequired[str]
    webkit_transition_duration: NotRequired[str]
    webkit_transition_property: NotRequired[str]
    webkit_transition_timing_function: NotRequired[str]
    webkit_user_select: NotRequired[str]
    white_space: NotRequired[str]
    white_space_collapse: NotRequired[str]
    widows: NotRequired[str]
    width: NotRequired[str]
    will_change: NotRequired[str]
    word_break: NotRequired[str]
    word_spacing: NotRequired[str]
    word_wrap: NotRequired[str]
    writing_mode: NotRequired[str]
    x: NotRequired[str]
    y: NotRequired[str]
    z_index: NotRequired[str]
    zoom: NotRequired[str]


Lo: TypeAlias = float


ChannelName: TypeAlias = Literal[
    "ariaLabel",
    "fill",
    "fillOpacity",
    "fontSize",
    "fx",
    "fy",
    "geometry",
    "height",
    "href",
    "length",
    "opacity",
    "path",
    "r",
    "rotate",
    "src",
    "stroke",
    "strokeOpacity",
    "strokeWidth",
    "symbol",
    "text",
    "title",
    "weight",
    "width",
    "x",
    "x1",
    "x2",
    "y",
    "y1",
    "y2",
    "z",
]


ColorScaleType: TypeAlias = Literal[
    "linear",
    "pow",
    "sqrt",
    "log",
    "symlog",
    "utc",
    "time",
    "point",
    "band",
    "ordinal",
    "sequential",
    "cyclical",
    "diverging",
    "diverging-log",
    "diverging-pow",
    "diverging-sqrt",
    "diverging-symlog",
    "categorical",
    "threshold",
    "quantile",
    "quantize",
    "identity",
]


ColorScheme: TypeAlias = (
    Literal[
        "Accent",
        "Category10",
        "Dark2",
        "Observable10",
        "Paired",
        "Pastel1",
        "Pastel2",
        "Set1",
        "Set2",
        "Set3",
        "Tableau10",
        "BrBG",
        "PRGn",
        "PiYG",
        "PuOr",
        "RdBu",
        "RdGy",
        "RdYlBu",
        "RdYlGn",
        "Spectral",
        "BuRd",
        "BuYlRd",
        "Blues",
        "Greens",
        "Greys",
        "Oranges",
        "Purples",
        "Reds",
        "Turbo",
        "Viridis",
        "Magma",
        "Inferno",
        "Plasma",
        "Cividis",
        "Cubehelix",
        "Warm",
        "Cool",
        "BuGn",
        "BuPu",
        "GnBu",
        "OrRd",
        "PuBu",
        "PuBuGn",
        "PuRd",
        "RdPu",
        "YlGn",
        "YlGnBu",
        "YlOrBr",
        "YlOrRd",
        "Rainbow",
        "Sinebow",
    ]
    | Mapping[str, Any]
)


class Config(TypedDict):
    extensions: NotRequired[str | Sequence[str]]


ContinuousScaleType: TypeAlias = Literal[
    "linear", "pow", "sqrt", "log", "symlog", "utc", "time", "identity"
]


CurveName: TypeAlias = Literal[
    "basis",
    "basis-closed",
    "basis-open",
    "bundle",
    "bump-x",
    "bump-y",
    "cardinal",
    "cardinal-closed",
    "cardinal-open",
    "catmull-rom",
    "catmull-rom-closed",
    "catmull-rom-open",
    "linear",
    "linear-closed",
    "monotone-x",
    "monotone-y",
    "natural",
    "step",
    "step-after",
    "step-before",
]


DataArray: TypeAlias = Sequence[Mapping[str, Any]]


class DataCSV(TypedDict, closed=True):
    delimiter: NotRequired[str]
    file: str
    replace: NotRequired[bool]
    sample_size: NotRequired[float]
    select: NotRequired[Sequence[str]]
    temp: NotRequired[bool]
    type: Literal["csv"]
    view: NotRequired[bool]
    where: NotRequired[str | Sequence[str]]


class DataFile(TypedDict, closed=True):
    file: str
    replace: NotRequired[bool]
    select: NotRequired[Sequence[str]]
    temp: NotRequired[bool]
    view: NotRequired[bool]
    where: NotRequired[str | Sequence[str]]


class DataJSON(TypedDict, closed=True):
    file: str
    replace: NotRequired[bool]
    select: NotRequired[Sequence[str]]
    temp: NotRequired[bool]
    type: Literal["json"]
    view: NotRequired[bool]
    where: NotRequired[str | Sequence[str]]


class DataJSONObjects(TypedDict, closed=True):
    data: Sequence[Mapping[str, Any]]
    replace: NotRequired[bool]
    select: NotRequired[Sequence[str]]
    temp: NotRequired[bool]
    type: NotRequired[Literal["json"]]
    view: NotRequired[bool]
    where: NotRequired[str | Sequence[str]]


class DataParquet(TypedDict, closed=True):
    file: str
    replace: NotRequired[bool]
    select: NotRequired[Sequence[str]]
    temp: NotRequired[bool]
    type: Literal["parquet"]
    view: NotRequired[bool]
    where: NotRequired[str | Sequence[str]]


DataQuery: TypeAlias = str


class DataSpatial(TypedDict, closed=True):
    file: str
    layer: NotRequired[str]
    replace: NotRequired[bool]
    select: NotRequired[Sequence[str]]
    temp: NotRequired[bool]
    type: Literal["spatial"]
    view: NotRequired[bool]
    where: NotRequired[str | Sequence[str]]


class DataTable(TypedDict, closed=True):
    query: str
    replace: NotRequired[bool]
    select: NotRequired[Sequence[str]]
    temp: NotRequired[bool]
    type: Literal["table"]
    view: NotRequired[bool]
    where: NotRequired[str | Sequence[str]]


class Days(TypedDict, closed=True):
    days: float


DiscreteScaleType: TypeAlias = Literal["ordinal", "identity"]


Fixed: TypeAlias = Literal["Fixed"]


FrameAnchor: TypeAlias = Literal[
    "middle",
    "top-left",
    "top",
    "top-right",
    "right",
    "bottom-right",
    "bottom",
    "bottom-left",
    "left",
]


GridInterpolate: TypeAlias = Literal["none", "linear", "nearest", "barycentric", "random-walk"]


class HSpace(TypedDict, closed=True):
    hspace: float | str


class Hours(TypedDict, closed=True):
    hours: float


Interpolate: TypeAlias = Literal["number", "rgb", "hsl", "hcl", "lab"]


LabelArrow: TypeAlias = Literal["auto", "up", "right", "down", "left", "none", True, False] | None


MarkerName: TypeAlias = Literal[
    "arrow",
    "arrow-reverse",
    "dot",
    "circle",
    "circle-fill",
    "circle-stroke",
    "tick",
    "tick-x",
    "tick-y",
]


class Options(TypedDict, closed=True):
    label: NotRequired[str]
    value: Any


class Meta(TypedDict):
    credit: NotRequired[str]
    description: NotRequired[str]
    title: NotRequired[str]


class Microseconds(TypedDict, closed=True):
    microseconds: float


class Milliseconds(TypedDict, closed=True):
    milliseconds: float


class Minutes(TypedDict, closed=True):
    minutes: float


class Months(TypedDict, closed=True):
    months: float


class ParamDate(TypedDict, closed=True):
    date: str
    select: NotRequired[Literal["value"]]


ParamLiteral: TypeAlias = str | float | bool | None


ParamValue: TypeAlias = ParamLiteral | Sequence[ParamLiteral | DataQuery]


class Margins(TypedDict, closed=True):
    bottom: NotRequired[float | DataQuery]
    left: NotRequired[float | DataQuery]
    right: NotRequired[float | DataQuery]
    top: NotRequired[float | DataQuery]


Y1: TypeAlias = float | DataQuery


PlotDataInline: TypeAlias = Sequence[Any]


class PlotFrom(TypedDict, closed=True):
    filter_by: NotRequired[DataQuery]
    source: NotRequired[str | DataQuery]
    optimize: NotRequired[bool]


class PlotLegend(TypedDict, closed=True):
    bind: NotRequired[DataQuery]
    columns: NotRequired[float]
    field: NotRequired[str]
    height: NotRequired[float]
    label: NotRequired[str]
    legend: Literal["color", "opacity", "symbol"]
    margin_bottom: NotRequired[float]
    margin_left: NotRequired[float]
    margin_right: NotRequired[float]
    margin_top: NotRequired[float]
    tick_size: NotRequired[float]
    width: NotRequired[float]


PlotMarkData: TypeAlias = PlotDataInline | PlotFrom


PositionScaleType: TypeAlias = Literal[
    "linear",
    "pow",
    "sqrt",
    "log",
    "symlog",
    "utc",
    "time",
    "point",
    "band",
    "threshold",
    "quantile",
    "quantize",
    "identity",
]


ProjectionName: TypeAlias = Literal[
    "albers-usa",
    "albers",
    "azimuthal-equal-area",
    "azimuthal-equidistant",
    "conic-conformal",
    "conic-equal-area",
    "conic-equidistant",
    "equal-earth",
    "equirectangular",
    "gnomonic",
    "identity",
    "reflect-y",
    "mercator",
    "orthographic",
    "stereographic",
    "transverse-mercator",
]


class Format(TypedDict, closed=True):
    aria_label: NotRequired[bool | str | DataQuery]
    fill: NotRequired[bool | str | DataQuery]
    fill_opacity: NotRequired[bool | str | DataQuery]
    font_size: NotRequired[bool | str | DataQuery]
    fx: NotRequired[bool | str | DataQuery]
    fy: NotRequired[bool | str | DataQuery]
    geometry: NotRequired[bool | str | DataQuery]
    height: NotRequired[bool | str | DataQuery]
    href: NotRequired[bool | str | DataQuery]
    length: NotRequired[bool | str | DataQuery]
    opacity: NotRequired[bool | str | DataQuery]
    path: NotRequired[bool | str | DataQuery]
    r: NotRequired[bool | str | DataQuery]
    rotate: NotRequired[bool | str | DataQuery]
    src: NotRequired[bool | str | DataQuery]
    stroke: NotRequired[bool | str | DataQuery]
    stroke_opacity: NotRequired[bool | str | DataQuery]
    stroke_width: NotRequired[bool | str | DataQuery]
    symbol: NotRequired[bool | str | DataQuery]
    text: NotRequired[bool | str | DataQuery]
    title: NotRequired[bool | str | DataQuery]
    weight: NotRequired[bool | str | DataQuery]
    width: NotRequired[bool | str | DataQuery]
    x: NotRequired[bool | str | DataQuery]
    x1: NotRequired[bool | str | DataQuery]
    x2: NotRequired[bool | str | DataQuery]
    y: NotRequired[bool | str | DataQuery]
    y1: NotRequired[bool | str | DataQuery]
    y2: NotRequired[bool | str | DataQuery]
    z: NotRequired[bool | str | DataQuery]


ReducerPercentile: TypeAlias = Literal[
    "p00",
    "p01",
    "p02",
    "p03",
    "p04",
    "p05",
    "p06",
    "p07",
    "p08",
    "p09",
    "p10",
    "p11",
    "p12",
    "p13",
    "p14",
    "p15",
    "p16",
    "p17",
    "p18",
    "p19",
    "p20",
    "p21",
    "p22",
    "p23",
    "p24",
    "p25",
    "p26",
    "p27",
    "p28",
    "p29",
    "p30",
    "p31",
    "p32",
    "p33",
    "p34",
    "p35",
    "p36",
    "p37",
    "p38",
    "p39",
    "p40",
    "p41",
    "p42",
    "p43",
    "p44",
    "p45",
    "p46",
    "p47",
    "p48",
    "p49",
    "p50",
    "p51",
    "p52",
    "p53",
    "p54",
    "p55",
    "p56",
    "p57",
    "p58",
    "p59",
    "p60",
    "p61",
    "p62",
    "p63",
    "p64",
    "p65",
    "p66",
    "p67",
    "p68",
    "p69",
    "p70",
    "p71",
    "p72",
    "p73",
    "p74",
    "p75",
    "p76",
    "p77",
    "p78",
    "p79",
    "p80",
    "p81",
    "p82",
    "p83",
    "p84",
    "p85",
    "p86",
    "p87",
    "p88",
    "p89",
    "p90",
    "p91",
    "p92",
    "p93",
    "p94",
    "p95",
    "p96",
    "p97",
    "p98",
    "p99",
]


class Region(TypedDict, closed=True):
    bind: NotRequired[DataQuery]
    brush: NotRequired[BrushStyles]
    channels: Sequence[str]
    peers: NotRequired[bool]
    select: Literal["region"]


class SQLExpression(TypedDict, closed=True):
    label: NotRequired[str]
    sql: str


ScaleName: TypeAlias = Literal["x", "y", "fx", "fy", "r", "color", "opacity", "symbol", "length"]


class Search(TypedDict, closed=True):
    bind: NotRequired[DataQuery]
    column: NotRequired[str]
    field: NotRequired[str]
    filter_by: NotRequired[DataQuery]
    source: NotRequired[str]
    input: Literal["search"]
    label: NotRequired[str]
    type: NotRequired[Literal["contains", "prefix", "suffix", "regexp"]]


class Seconds(TypedDict, closed=True):
    seconds: float


SelectFilter: TypeAlias = Literal[
    "first", "last", "maxX", "maxY", "minX", "minY", "nearest", "nearestX", "nearestY"
]


class Selection(TypedDict, closed=True):
    cross: NotRequired[bool]
    empty: NotRequired[bool]
    include: NotRequired[DataQuery | Sequence[DataQuery]]
    select: Literal["crossfilter", "intersect", "single", "union"]


class Slider(TypedDict, closed=True):
    bind: NotRequired[DataQuery]
    column: NotRequired[str]
    field: NotRequired[str]
    filter_by: NotRequired[DataQuery]
    source: NotRequired[str]
    input: Literal["slider"]
    label: NotRequired[str]
    max: NotRequired[float]
    min: NotRequired[float]
    select: NotRequired[Literal["point", "interval"]]
    step: NotRequired[float]
    value: NotRequired[float]
    width: NotRequired[float]


class SortOrder2(TypedDict, closed=True):
    channel: NotRequired[
        Literal[
            "-ariaLabel",
            "-fill",
            "-fillOpacity",
            "-fontSize",
            "-fx",
            "-fy",
            "-geometry",
            "-height",
            "-href",
            "-length",
            "-opacity",
            "-path",
            "-r",
            "-rotate",
            "-src",
            "-stroke",
            "-strokeOpacity",
            "-strokeWidth",
            "-symbol",
            "-text",
            "-title",
            "-weight",
            "-width",
            "-x",
            "-x1",
            "-x2",
            "-y",
            "-y1",
            "-y2",
            "-z",
        ]
        | ChannelName
    ]
    order: NotRequired[Literal["ascending", "descending"]]


StackOffsetName: TypeAlias = Literal["center", "normalize", "wiggle"]


StackOrderName: TypeAlias = Literal["value", "x", "y", "z", "sum", "appearance", "inside-out"]


SymbolType: TypeAlias = Literal[
    "asterisk",
    "circle",
    "cross",
    "diamond",
    "diamond2",
    "hexagon",
    "plus",
    "square",
    "square2",
    "star",
    "times",
    "triangle",
    "triangle2",
    "wye",
]


class Table(TypedDict, closed=True):
    align: NotRequired[Mapping[str, Literal["left", "right", "center", "justify"]]]
    bind: NotRequired[DataQuery]
    columns: NotRequired[Sequence[str]]
    filter_by: NotRequired[DataQuery]
    source: NotRequired[str | DataQuery]
    height: NotRequired[float]
    input: Literal["table"]
    max_width: NotRequired[float]
    row_batch: NotRequired[float]
    width: NotRequired[float | Mapping[str, float]]


TimeIntervalName: TypeAlias = Literal[
    "second",
    "minute",
    "hour",
    "day",
    "week",
    "month",
    "quarter",
    "half",
    "year",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
]


TipPointer: TypeAlias = Literal["x", "y", "xy"]


class Toggle(TypedDict, closed=True):
    bind: NotRequired[DataQuery]
    channels: Sequence[str]
    peers: NotRequired[bool]
    select: Literal["toggle"]


class ToggleColor(TypedDict, closed=True):
    bind: NotRequired[DataQuery]
    peers: NotRequired[bool]
    select: Literal["toggleColor"]


class ToggleX(TypedDict, closed=True):
    bind: NotRequired[DataQuery]
    peers: NotRequired[bool]
    select: Literal["toggleX"]


class ToggleY(TypedDict, closed=True):
    bind: NotRequired[DataQuery]
    peers: NotRequired[bool]
    select: Literal["toggleY"]


TransformField: TypeAlias = str | DataQuery


class VSpace(TypedDict, closed=True):
    vspace: float | str


VectorShapeName: TypeAlias = Literal["arrow", "spike"]


class Years(TypedDict, closed=True):
    years: float


class Bin(TypedDict, closed=True):
    bin: str | float | bool | DataQuery | Sequence[str | float | bool | DataQuery]
    interval: NotRequired[BinInterval]
    minstep: NotRequired[float]
    nice: NotRequired[Literal[True]]
    offset: NotRequired[float]
    step: NotRequired[float]
    steps: NotRequired[float]


class Centroid(TypedDict, closed=True):
    centroid: str | float | bool | DataQuery | Sequence[str | float | bool | DataQuery]


class CentroidX(TypedDict, closed=True):
    centroid_x: str | float | bool | DataQuery | Sequence[str | float | bool | DataQuery]


class CentroidY(TypedDict, closed=True):
    centroid_y: str | float | bool | DataQuery | Sequence[str | float | bool | DataQuery]


ChannelDomainValue: TypeAlias = (
    Literal[
        "data",
        "width",
        "height",
        "-ariaLabel",
        "-fill",
        "-fillOpacity",
        "-fontSize",
        "-fx",
        "-fy",
        "-geometry",
        "-height",
        "-href",
        "-length",
        "-opacity",
        "-path",
        "-r",
        "-rotate",
        "-src",
        "-stroke",
        "-strokeOpacity",
        "-strokeWidth",
        "-symbol",
        "-text",
        "-title",
        "-weight",
        "-width",
        "-x",
        "-x1",
        "-x2",
        "-y",
        "-y1",
        "-y2",
        "-z",
        "-data",
    ]
    | ChannelName
    | None
)


class Column(TypedDict, closed=True):
    column: str | float | bool | DataQuery | Sequence[str | float | bool | DataQuery]


Curve: TypeAlias = CurveName


DataDefinition: TypeAlias = (
    DataQuery
    | DataArray
    | DataFile
    | DataTable
    | DataParquet
    | DataCSV
    | DataSpatial
    | DataJSON
    | DataJSONObjects
)


class DateDay(TypedDict, closed=True):
    date_day: str | float | bool | DataQuery | Sequence[str | float | bool | DataQuery]


class DateMonth(TypedDict, closed=True):
    date_month: str | float | bool | DataQuery | Sequence[str | float | bool | DataQuery]


class DateMonthDay(TypedDict, closed=True):
    date_month_day: str | float | bool | DataQuery | Sequence[str | float | bool | DataQuery]


class GeoJSON(TypedDict, closed=True):
    geojson: str | float | bool | DataQuery | Sequence[str | float | bool | DataQuery]


class Highlight(TypedDict, closed=True):
    by: DataQuery
    fill: NotRequired[str]
    fill_opacity: NotRequired[float]
    opacity: NotRequired[float]
    select: Literal["highlight"]
    stroke: NotRequired[str]
    stroke_opacity: NotRequired[float]


IntervalTransform: TypeAlias = (
    Years | Months | Days | Hours | Minutes | Seconds | Milliseconds | Microseconds
)


class IntervalX(TypedDict, closed=True):
    bind: NotRequired[DataQuery]
    brush: NotRequired[BrushStyles]
    field: NotRequired[str]
    peers: NotRequired[bool]
    pixel_size: NotRequired[float]
    select: Literal["intervalX"]


class IntervalXY(TypedDict, closed=True):
    bind: NotRequired[DataQuery]
    brush: NotRequired[BrushStyles]
    peers: NotRequired[bool]
    pixel_size: NotRequired[float]
    select: Literal["intervalXY"]
    xfield: NotRequired[str]
    yfield: NotRequired[str]


class IntervalY(TypedDict, closed=True):
    bind: NotRequired[DataQuery]
    brush: NotRequired[BrushStyles]
    field: NotRequired[str]
    peers: NotRequired[bool]
    pixel_size: NotRequired[float]
    select: Literal["intervalY"]


class Legend(TypedDict, closed=True):
    bind: NotRequired[DataQuery]
    columns: NotRequired[float]
    field: NotRequired[str]
    plot: NotRequired[str]
    height: NotRequired[float]
    label: NotRequired[str]
    legend: Literal["color", "opacity", "symbol"]
    margin_bottom: NotRequired[float]
    margin_left: NotRequired[float]
    margin_right: NotRequired[float]
    margin_top: NotRequired[float]
    tick_size: NotRequired[float]
    width: NotRequired[float]


LiteralTimeInterval: TypeAlias = (
    Literal[
        "3 months",
        "10 years",
        "seconds",
        "minutes",
        "hours",
        "days",
        "weeks",
        "months",
        "quarters",
        "halfs",
        "years",
        "mondays",
        "tuesdays",
        "wednesdays",
        "thursdays",
        "fridays",
        "saturdays",
        "sundays",
    ]
    | TimeIntervalName
    | str
)


class Menu(TypedDict, closed=True):
    bind: NotRequired[DataQuery]
    column: NotRequired[str]
    field: NotRequired[str]
    filter_by: NotRequired[DataQuery]
    source: NotRequired[str]
    input: Literal["menu"]
    label: NotRequired[str]
    list_match: NotRequired[Literal["any", "all"]]
    options: NotRequired[Sequence[Any | Options]]
    value: NotRequired[Any]


class NearestX(TypedDict, closed=True):
    bind: NotRequired[DataQuery]
    channels: NotRequired[Sequence[str]]
    fields: NotRequired[Sequence[str]]
    max_radius: NotRequired[float]
    select: Literal["nearestX"]


class NearestY(TypedDict, closed=True):
    bind: NotRequired[DataQuery]
    channels: NotRequired[Sequence[str]]
    fields: NotRequired[Sequence[str]]
    max_radius: NotRequired[float]
    select: Literal["nearestY"]


class Pan(TypedDict, closed=True):
    select: Literal["pan"]
    x: NotRequired[DataQuery]
    xfield: NotRequired[str]
    y: NotRequired[DataQuery]
    yfield: NotRequired[str]


class PanX(TypedDict, closed=True):
    select: Literal["panX"]
    x: NotRequired[DataQuery]
    xfield: NotRequired[str]
    y: NotRequired[DataQuery]
    yfield: NotRequired[str]


class PanY(TypedDict, closed=True):
    select: Literal["panY"]
    x: NotRequired[DataQuery]
    xfield: NotRequired[str]
    y: NotRequired[DataQuery]
    yfield: NotRequired[str]


class PanZoom(TypedDict, closed=True):
    select: Literal["panZoom"]
    x: NotRequired[DataQuery]
    xfield: NotRequired[str]
    y: NotRequired[DataQuery]
    yfield: NotRequired[str]


class PanZoomX(TypedDict, closed=True):
    select: Literal["panZoomX"]
    x: NotRequired[DataQuery]
    xfield: NotRequired[str]
    y: NotRequired[DataQuery]
    yfield: NotRequired[str]


class PanZoomY(TypedDict, closed=True):
    select: Literal["panZoomY"]
    x: NotRequired[DataQuery]
    xfield: NotRequired[str]
    y: NotRequired[DataQuery]
    yfield: NotRequired[str]


class Param(TypedDict, closed=True):
    select: NotRequired[Literal["value"]]
    value: ParamValue


ParamDefinition: TypeAlias = ParamValue | Param | ParamDate | Selection


Params: TypeAlias = Mapping[str, ParamDefinition]


PlotInteractor: TypeAlias = (
    Highlight
    | IntervalX
    | IntervalY
    | IntervalXY
    | NearestX
    | NearestY
    | Pan
    | PanX
    | PanY
    | PanZoom
    | PanZoomX
    | PanZoomY
    | Region
    | Toggle
    | ToggleX
    | ToggleY
    | ToggleColor
)


Reducer: TypeAlias = (
    Literal[
        "first",
        "last",
        "identity",
        "count",
        "distinct",
        "sum",
        "proportion",
        "proportion-facet",
        "deviation",
        "min",
        "min-index",
        "max",
        "max-index",
        "mean",
        "median",
        "variance",
        "mode",
    ]
    | ReducerPercentile
)


StackOffset: TypeAlias = StackOffsetName


StackOrder: TypeAlias = (
    Literal["-value", "-x", "-y", "-z", "-sum", "-appearance", "-inside-out"]
    | StackOrderName
    | str
    | Sequence[Any]
)


VectorShape: TypeAlias = VectorShapeName


class ChannelDomainValueSpec1(TypedDict, closed=True):
    limit: NotRequired[float | tuple[Lo, Lo]]
    order: NotRequired[Literal["ascending", "descending"] | None]
    reduce: NotRequired[Reducer | bool | None]
    reverse: NotRequired[bool]
    value: ChannelDomainValue


ChannelDomainValueSpec: TypeAlias = ChannelDomainValue | ChannelDomainValueSpec1


ColumnTransform: TypeAlias = (
    Bin | Column | DateMonth | DateMonthDay | DateDay | Centroid | CentroidX | CentroidY | GeoJSON
)


Data: TypeAlias = Mapping[str, DataDefinition]


FrameValue: TypeAlias = float | IntervalTransform | None


Interval: TypeAlias = LiteralTimeInterval


class Lag(TypedDict, closed=True):
    exclude: NotRequired[
        Literal[
            "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
        ]
    ]
    groups: NotRequired[Sequence[FrameValue] | DataQuery]
    lag: str | float | bool | DataQuery | Sequence[str | float | bool | DataQuery]
    orderby: NotRequired[TransformField | Sequence[TransformField]]
    partitionby: NotRequired[TransformField | Sequence[TransformField]]
    range: NotRequired[Sequence[FrameValue] | DataQuery]
    rows: NotRequired[Sequence[FrameValue] | DataQuery]


class Last(TypedDict, closed=True):
    distinct: NotRequired[bool]
    exclude: NotRequired[
        Literal[
            "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
        ]
    ]
    groups: NotRequired[Sequence[FrameValue] | DataQuery]
    last: str | float | bool | DataQuery | Sequence[str | float | bool | DataQuery]
    orderby: NotRequired[TransformField | Sequence[TransformField]]
    partitionby: NotRequired[TransformField | Sequence[TransformField]]
    range: NotRequired[Sequence[FrameValue] | DataQuery]
    rows: NotRequired[Sequence[FrameValue] | DataQuery]


class LastValue(TypedDict, closed=True):
    exclude: NotRequired[
        Literal[
            "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
        ]
    ]
    groups: NotRequired[Sequence[FrameValue] | DataQuery]
    last_value: str | float | bool | DataQuery | Sequence[str | float | bool | DataQuery]
    orderby: NotRequired[TransformField | Sequence[TransformField]]
    partitionby: NotRequired[TransformField | Sequence[TransformField]]
    range: NotRequired[Sequence[FrameValue] | DataQuery]
    rows: NotRequired[Sequence[FrameValue] | DataQuery]


class Lead(TypedDict, closed=True):
    exclude: NotRequired[
        Literal[
            "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
        ]
    ]
    groups: NotRequired[Sequence[FrameValue] | DataQuery]
    lead: str | float | bool | DataQuery | Sequence[str | float | bool | DataQuery]
    orderby: NotRequired[TransformField | Sequence[TransformField]]
    partitionby: NotRequired[TransformField | Sequence[TransformField]]
    range: NotRequired[Sequence[FrameValue] | DataQuery]
    rows: NotRequired[Sequence[FrameValue] | DataQuery]


class Max(TypedDict, closed=True):
    distinct: NotRequired[bool]
    exclude: NotRequired[
        Literal[
            "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
        ]
    ]
    groups: NotRequired[Sequence[FrameValue] | DataQuery]
    max: str | float | bool | DataQuery | Sequence[str | float | bool | DataQuery]
    orderby: NotRequired[TransformField | Sequence[TransformField]]
    partitionby: NotRequired[TransformField | Sequence[TransformField]]
    range: NotRequired[Sequence[FrameValue] | DataQuery]
    rows: NotRequired[Sequence[FrameValue] | DataQuery]


class Median(TypedDict, closed=True):
    distinct: NotRequired[bool]
    exclude: NotRequired[
        Literal[
            "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
        ]
    ]
    groups: NotRequired[Sequence[FrameValue] | DataQuery]
    median: str | float | bool | DataQuery | Sequence[str | float | bool | DataQuery]
    orderby: NotRequired[TransformField | Sequence[TransformField]]
    partitionby: NotRequired[TransformField | Sequence[TransformField]]
    range: NotRequired[Sequence[FrameValue] | DataQuery]
    rows: NotRequired[Sequence[FrameValue] | DataQuery]


class Min(TypedDict, closed=True):
    distinct: NotRequired[bool]
    exclude: NotRequired[
        Literal[
            "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
        ]
    ]
    groups: NotRequired[Sequence[FrameValue] | DataQuery]
    min: str | float | bool | DataQuery | Sequence[str | float | bool | DataQuery]
    orderby: NotRequired[TransformField | Sequence[TransformField]]
    partitionby: NotRequired[TransformField | Sequence[TransformField]]
    range: NotRequired[Sequence[FrameValue] | DataQuery]
    rows: NotRequired[Sequence[FrameValue] | DataQuery]


class Mode(TypedDict, closed=True):
    distinct: NotRequired[bool]
    exclude: NotRequired[
        Literal[
            "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
        ]
    ]
    groups: NotRequired[Sequence[FrameValue] | DataQuery]
    mode: str | float | bool | DataQuery | Sequence[str | float | bool | DataQuery]
    orderby: NotRequired[TransformField | Sequence[TransformField]]
    partitionby: NotRequired[TransformField | Sequence[TransformField]]
    range: NotRequired[Sequence[FrameValue] | DataQuery]
    rows: NotRequired[Sequence[FrameValue] | DataQuery]


class NTile(TypedDict, closed=True):
    exclude: NotRequired[
        Literal[
            "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
        ]
    ]
    groups: NotRequired[Sequence[FrameValue] | DataQuery]
    ntile: str | float | bool | DataQuery | Sequence[str | float | bool | DataQuery]
    orderby: NotRequired[TransformField | Sequence[TransformField]]
    partitionby: NotRequired[TransformField | Sequence[TransformField]]
    range: NotRequired[Sequence[FrameValue] | DataQuery]
    rows: NotRequired[Sequence[FrameValue] | DataQuery]


class NthValue(TypedDict, closed=True):
    exclude: NotRequired[
        Literal[
            "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
        ]
    ]
    groups: NotRequired[Sequence[FrameValue] | DataQuery]
    nth_value: str | float | bool | DataQuery | Sequence[str | float | bool | DataQuery]
    orderby: NotRequired[TransformField | Sequence[TransformField]]
    partitionby: NotRequired[TransformField | Sequence[TransformField]]
    range: NotRequired[Sequence[FrameValue] | DataQuery]
    rows: NotRequired[Sequence[FrameValue] | DataQuery]


class PercentRank(TypedDict, closed=True):
    exclude: NotRequired[
        Literal[
            "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
        ]
    ]
    groups: NotRequired[Sequence[FrameValue] | DataQuery]
    orderby: NotRequired[TransformField | Sequence[TransformField]]
    partitionby: NotRequired[TransformField | Sequence[TransformField]]
    percent_rank: Sequence[Any] | None
    range: NotRequired[Sequence[FrameValue] | DataQuery]
    rows: NotRequired[Sequence[FrameValue] | DataQuery]


class PlotAttributes(TypedDict, closed=True):
    align: NotRequired[float | DataQuery]
    aria_description: NotRequired[str | None]
    aria_label: NotRequired[str | None]
    aspect_ratio: NotRequired[float | bool | DataQuery | None]
    axis: NotRequired[Literal["top", "right", "bottom", "left", "both"] | bool | DataQuery | None]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    color_base: NotRequired[float | DataQuery]
    color_clamp: NotRequired[bool | DataQuery]
    color_constant: NotRequired[float | DataQuery]
    color_domain: NotRequired[Sequence[Any] | Fixed | DataQuery]
    color_exponent: NotRequired[float | DataQuery]
    color_interpolate: NotRequired[Interpolate | DataQuery]
    color_label: NotRequired[str | DataQuery | None]
    color_n: NotRequired[float | DataQuery]
    color_nice: NotRequired[bool | float | Interval | DataQuery]
    color_percent: NotRequired[bool | DataQuery]
    color_pivot: NotRequired[Any | DataQuery]
    color_range: NotRequired[Sequence[Any] | Fixed | DataQuery]
    color_reverse: NotRequired[bool | DataQuery]
    color_scale: NotRequired[ColorScaleType | DataQuery | None]
    color_scheme: NotRequired[ColorScheme | DataQuery]
    color_symmetric: NotRequired[bool | DataQuery]
    color_tick_format: NotRequired[str | DataQuery | None]
    color_zero: NotRequired[bool | DataQuery]
    facet_grid: NotRequired[bool | str | Interval | Sequence[Any] | DataQuery]
    facet_label: NotRequired[str | DataQuery | None]
    facet_margin: NotRequired[float | DataQuery]
    facet_margin_bottom: NotRequired[float | DataQuery]
    facet_margin_left: NotRequired[float | DataQuery]
    facet_margin_right: NotRequired[float | DataQuery]
    facet_margin_top: NotRequired[float | DataQuery]
    fx_align: NotRequired[float | DataQuery]
    fx_aria_description: NotRequired[str | DataQuery]
    fx_aria_label: NotRequired[str | DataQuery]
    fx_axis: NotRequired[Literal["top", "bottom", "both"] | bool | DataQuery | None]
    fx_domain: NotRequired[Sequence[Any] | Fixed | DataQuery]
    fx_font_variant: NotRequired[str | DataQuery]
    fx_grid: NotRequired[bool | str | Interval | Sequence[Any] | DataQuery]
    fx_inset: NotRequired[float | DataQuery]
    fx_inset_left: NotRequired[float | DataQuery]
    fx_inset_right: NotRequired[float | DataQuery]
    fx_label: NotRequired[str | DataQuery | None]
    fx_label_anchor: NotRequired[Literal["top", "right", "bottom", "left", "center"] | DataQuery]
    fx_label_offset: NotRequired[float | DataQuery]
    fx_line: NotRequired[bool | DataQuery]
    fx_padding: NotRequired[float | DataQuery]
    fx_padding_inner: NotRequired[float | DataQuery]
    fx_padding_outer: NotRequired[float | DataQuery]
    fx_range: NotRequired[Sequence[Any] | Fixed | DataQuery]
    fx_reverse: NotRequired[bool | DataQuery]
    fx_round: NotRequired[bool | DataQuery]
    fx_tick_format: NotRequired[str | DataQuery | None]
    fx_tick_padding: NotRequired[float | DataQuery]
    fx_tick_rotate: NotRequired[float | DataQuery]
    fx_tick_size: NotRequired[float | DataQuery]
    fx_tick_spacing: NotRequired[float | DataQuery]
    fx_ticks: NotRequired[float | Interval | Sequence[Any] | DataQuery]
    fy_align: NotRequired[float | DataQuery]
    fy_aria_description: NotRequired[str | DataQuery]
    fy_aria_label: NotRequired[str | DataQuery]
    fy_axis: NotRequired[Literal["left", "right", "both"] | bool | DataQuery | None]
    fy_domain: NotRequired[Sequence[Any] | Fixed | DataQuery]
    fy_font_variant: NotRequired[str | DataQuery]
    fy_grid: NotRequired[bool | str | Interval | Sequence[Any] | DataQuery]
    fy_inset: NotRequired[float | DataQuery]
    fy_inset_bottom: NotRequired[float | DataQuery]
    fy_inset_top: NotRequired[float | DataQuery]
    fy_label: NotRequired[str | DataQuery | None]
    fy_label_anchor: NotRequired[Literal["top", "right", "bottom", "left", "center"] | DataQuery]
    fy_label_offset: NotRequired[float | DataQuery]
    fy_line: NotRequired[bool | DataQuery]
    fy_padding: NotRequired[float | DataQuery]
    fy_padding_inner: NotRequired[float | DataQuery]
    fy_padding_outer: NotRequired[float | DataQuery]
    fy_range: NotRequired[Sequence[Any] | Fixed | DataQuery]
    fy_reverse: NotRequired[bool | DataQuery]
    fy_round: NotRequired[bool | DataQuery]
    fy_tick_format: NotRequired[str | DataQuery | None]
    fy_tick_padding: NotRequired[float | DataQuery]
    fy_tick_rotate: NotRequired[float | DataQuery]
    fy_tick_size: NotRequired[float | DataQuery]
    fy_tick_spacing: NotRequired[float | DataQuery]
    fy_ticks: NotRequired[float | Interval | Sequence[Any] | DataQuery]
    grid: NotRequired[bool | str | DataQuery]
    height: NotRequired[float | DataQuery]
    inset: NotRequired[float | DataQuery]
    length_base: NotRequired[float | DataQuery]
    length_clamp: NotRequired[Any]
    length_constant: NotRequired[float | DataQuery]
    length_domain: NotRequired[Sequence[Any] | Fixed | DataQuery]
    length_exponent: NotRequired[float | DataQuery]
    length_nice: NotRequired[bool | float | Interval | DataQuery]
    length_percent: NotRequired[bool | DataQuery]
    length_range: NotRequired[Sequence[Any] | Fixed | DataQuery]
    length_scale: NotRequired[ContinuousScaleType | DataQuery | None]
    length_zero: NotRequired[bool | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    margins: NotRequired[Margins]
    name: NotRequired[str]
    opacity_base: NotRequired[float | DataQuery]
    opacity_clamp: NotRequired[bool | DataQuery]
    opacity_constant: NotRequired[float | DataQuery]
    opacity_domain: NotRequired[Sequence[Any] | Fixed | DataQuery]
    opacity_exponent: NotRequired[float | DataQuery]
    opacity_label: NotRequired[str | DataQuery | None]
    opacity_nice: NotRequired[bool | float | Interval | DataQuery]
    opacity_percent: NotRequired[bool | DataQuery]
    opacity_range: NotRequired[Sequence[Any] | Fixed | DataQuery]
    opacity_reverse: NotRequired[bool | DataQuery]
    opacity_scale: NotRequired[ContinuousScaleType | DataQuery | None]
    opacity_tick_format: NotRequired[str | DataQuery | None]
    opacity_zero: NotRequired[bool | DataQuery]
    padding: NotRequired[float | DataQuery]
    projection_clip: NotRequired[bool | float | Literal["frame"] | DataQuery | None]
    projection_domain: NotRequired[Mapping[str, Any] | DataQuery]
    projection_inset: NotRequired[float | DataQuery]
    projection_inset_bottom: NotRequired[float | DataQuery]
    projection_inset_left: NotRequired[float | DataQuery]
    projection_inset_right: NotRequired[float | DataQuery]
    projection_inset_top: NotRequired[float | DataQuery]
    projection_parallels: NotRequired[tuple[Y1, Y1] | DataQuery]
    projection_precision: NotRequired[float | DataQuery]
    projection_rotate: NotRequired[tuple[Y1, Y1, Y1] | DataQuery]
    projection_type: NotRequired[ProjectionName | DataQuery | None]
    r_base: NotRequired[float | DataQuery]
    r_clamp: NotRequired[Any]
    r_constant: NotRequired[float | DataQuery]
    r_domain: NotRequired[Sequence[Any] | Fixed | DataQuery]
    r_exponent: NotRequired[float | DataQuery]
    r_label: NotRequired[str | DataQuery | None]
    r_nice: NotRequired[bool | float | Interval | DataQuery]
    r_percent: NotRequired[bool | DataQuery]
    r_range: NotRequired[Sequence[Any] | Fixed | DataQuery]
    r_scale: NotRequired[ContinuousScaleType | DataQuery | None]
    r_zero: NotRequired[bool | DataQuery]
    style: NotRequired[str | CSSStyles | DataQuery | None]
    symbol_domain: NotRequired[Sequence[Any] | Fixed | DataQuery]
    symbol_range: NotRequired[Sequence[Any] | Fixed | DataQuery]
    symbol_scale: NotRequired[DiscreteScaleType | DataQuery | None]
    width: NotRequired[float | DataQuery]
    x_align: NotRequired[float | DataQuery]
    x_aria_description: NotRequired[str | DataQuery]
    x_aria_label: NotRequired[str | DataQuery]
    x_axis: NotRequired[Literal["top", "bottom", "both"] | bool | DataQuery | None]
    x_base: NotRequired[float | DataQuery]
    x_clamp: NotRequired[bool | DataQuery]
    x_constant: NotRequired[float | DataQuery]
    x_domain: NotRequired[Sequence[Any] | Fixed | DataQuery]
    x_exponent: NotRequired[float | DataQuery]
    x_font_variant: NotRequired[str | DataQuery]
    x_grid: NotRequired[bool | str | Interval | Sequence[Any] | DataQuery]
    x_inset: NotRequired[float | DataQuery]
    x_inset_left: NotRequired[float | DataQuery]
    x_inset_right: NotRequired[float | DataQuery]
    x_label: NotRequired[str | DataQuery | None]
    x_label_anchor: NotRequired[Literal["top", "right", "bottom", "left", "center"] | DataQuery]
    x_label_arrow: NotRequired[LabelArrow | DataQuery]
    x_label_offset: NotRequired[float | DataQuery]
    x_line: NotRequired[bool | DataQuery]
    x_nice: NotRequired[bool | float | Interval | DataQuery]
    x_padding: NotRequired[float | DataQuery]
    x_padding_inner: NotRequired[float | DataQuery]
    x_padding_outer: NotRequired[float | DataQuery]
    x_percent: NotRequired[bool | DataQuery]
    x_range: NotRequired[Sequence[Any] | Fixed | DataQuery]
    x_reverse: NotRequired[bool | DataQuery]
    x_round: NotRequired[bool | DataQuery]
    x_scale: NotRequired[PositionScaleType | DataQuery | None]
    x_tick_format: NotRequired[str | DataQuery | None]
    x_tick_padding: NotRequired[float | DataQuery]
    x_tick_rotate: NotRequired[float | DataQuery]
    x_tick_size: NotRequired[float | DataQuery]
    x_tick_spacing: NotRequired[float | DataQuery]
    x_ticks: NotRequired[float | Interval | Sequence[Any] | DataQuery]
    x_zero: NotRequired[bool | DataQuery]
    xy_domain: NotRequired[Sequence[Any] | Fixed | DataQuery]
    y_align: NotRequired[float | DataQuery]
    y_aria_description: NotRequired[str | DataQuery]
    y_aria_label: NotRequired[str | DataQuery]
    y_axis: NotRequired[Literal["left", "right", "both"] | bool | DataQuery | None]
    y_base: NotRequired[float | DataQuery]
    y_clamp: NotRequired[bool | DataQuery]
    y_constant: NotRequired[float | DataQuery]
    y_domain: NotRequired[Sequence[Any] | Fixed | DataQuery]
    y_exponent: NotRequired[float | DataQuery]
    y_font_variant: NotRequired[str | DataQuery]
    y_grid: NotRequired[bool | str | Interval | Sequence[Any] | DataQuery]
    y_inset: NotRequired[float | DataQuery]
    y_inset_bottom: NotRequired[float | DataQuery]
    y_inset_top: NotRequired[float | DataQuery]
    y_label: NotRequired[str | DataQuery | None]
    y_label_anchor: NotRequired[Literal["top", "right", "bottom", "left", "center"] | DataQuery]
    y_label_arrow: NotRequired[LabelArrow | DataQuery]
    y_label_offset: NotRequired[float | DataQuery]
    y_line: NotRequired[bool | DataQuery]
    y_nice: NotRequired[bool | float | Interval | DataQuery]
    y_padding: NotRequired[float | DataQuery]
    y_padding_inner: NotRequired[float | DataQuery]
    y_padding_outer: NotRequired[float | DataQuery]
    y_percent: NotRequired[bool | DataQuery]
    y_range: NotRequired[Sequence[Any] | Fixed | DataQuery]
    y_reverse: NotRequired[bool | DataQuery]
    y_round: NotRequired[bool | DataQuery]
    y_scale: NotRequired[PositionScaleType | DataQuery | None]
    y_tick_format: NotRequired[str | DataQuery | None]
    y_tick_padding: NotRequired[float | DataQuery]
    y_tick_rotate: NotRequired[float | DataQuery]
    y_tick_size: NotRequired[float | DataQuery]
    y_tick_spacing: NotRequired[float | DataQuery]
    y_ticks: NotRequired[float | Interval | Sequence[Any] | DataQuery]
    y_zero: NotRequired[bool | DataQuery]


class Product(TypedDict, closed=True):
    distinct: NotRequired[bool]
    exclude: NotRequired[
        Literal[
            "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
        ]
    ]
    groups: NotRequired[Sequence[FrameValue] | DataQuery]
    orderby: NotRequired[TransformField | Sequence[TransformField]]
    partitionby: NotRequired[TransformField | Sequence[TransformField]]
    product: str | float | bool | DataQuery | Sequence[str | float | bool | DataQuery]
    range: NotRequired[Sequence[FrameValue] | DataQuery]
    rows: NotRequired[Sequence[FrameValue] | DataQuery]


class Quantile(TypedDict, closed=True):
    distinct: NotRequired[bool]
    exclude: NotRequired[
        Literal[
            "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
        ]
    ]
    groups: NotRequired[Sequence[FrameValue] | DataQuery]
    orderby: NotRequired[TransformField | Sequence[TransformField]]
    partitionby: NotRequired[TransformField | Sequence[TransformField]]
    quantile: Sequence[str | float | bool | DataQuery]
    range: NotRequired[Sequence[FrameValue] | DataQuery]
    rows: NotRequired[Sequence[FrameValue] | DataQuery]


class Rank(TypedDict, closed=True):
    exclude: NotRequired[
        Literal[
            "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
        ]
    ]
    groups: NotRequired[Sequence[FrameValue] | DataQuery]
    orderby: NotRequired[TransformField | Sequence[TransformField]]
    partitionby: NotRequired[TransformField | Sequence[TransformField]]
    range: NotRequired[Sequence[FrameValue] | DataQuery]
    rank: Sequence[Any] | None
    rows: NotRequired[Sequence[FrameValue] | DataQuery]


class RowNumber(TypedDict, closed=True):
    exclude: NotRequired[
        Literal[
            "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
        ]
    ]
    groups: NotRequired[Sequence[FrameValue] | DataQuery]
    orderby: NotRequired[TransformField | Sequence[TransformField]]
    partitionby: NotRequired[TransformField | Sequence[TransformField]]
    range: NotRequired[Sequence[FrameValue] | DataQuery]
    row_number: Sequence[Any] | None
    rows: NotRequired[Sequence[FrameValue] | DataQuery]


class Spec3(TypedDict, closed=True):
    config: NotRequired[Config]
    data: NotRequired[Data]
    hspace: float | str
    meta: NotRequired[Meta]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]


class Spec4(TypedDict, closed=True):
    config: NotRequired[Config]
    data: NotRequired[Data]
    meta: NotRequired[Meta]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    vspace: float | str


class Spec5(TypedDict, closed=True):
    bind: NotRequired[DataQuery]
    column: NotRequired[str]
    config: NotRequired[Config]
    data: NotRequired[Data]
    field: NotRequired[str]
    filter_by: NotRequired[DataQuery]
    source: NotRequired[str]
    input: Literal["menu"]
    label: NotRequired[str]
    list_match: NotRequired[Literal["any", "all"]]
    meta: NotRequired[Meta]
    options: NotRequired[Sequence[Any | Options]]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    value: NotRequired[Any]


class Spec6(TypedDict, closed=True):
    bind: NotRequired[DataQuery]
    column: NotRequired[str]
    config: NotRequired[Config]
    data: NotRequired[Data]
    field: NotRequired[str]
    filter_by: NotRequired[DataQuery]
    source: NotRequired[str]
    input: Literal["search"]
    label: NotRequired[str]
    meta: NotRequired[Meta]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    type: NotRequired[Literal["contains", "prefix", "suffix", "regexp"]]


class Spec7(TypedDict, closed=True):
    bind: NotRequired[DataQuery]
    column: NotRequired[str]
    config: NotRequired[Config]
    data: NotRequired[Data]
    field: NotRequired[str]
    filter_by: NotRequired[DataQuery]
    source: NotRequired[str]
    input: Literal["slider"]
    label: NotRequired[str]
    max: NotRequired[float]
    meta: NotRequired[Meta]
    min: NotRequired[float]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    select: NotRequired[Literal["point", "interval"]]
    step: NotRequired[float]
    value: NotRequired[float]
    width: NotRequired[float]


class Spec8(TypedDict, closed=True):
    align: NotRequired[Mapping[str, Literal["left", "right", "center", "justify"]]]
    bind: NotRequired[DataQuery]
    columns: NotRequired[Sequence[str]]
    config: NotRequired[Config]
    data: NotRequired[Data]
    filter_by: NotRequired[DataQuery]
    source: NotRequired[str | DataQuery]
    height: NotRequired[float]
    input: Literal["table"]
    max_width: NotRequired[float]
    meta: NotRequired[Meta]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    row_batch: NotRequired[float]
    width: NotRequired[float | Mapping[str, float]]


class Spec81(TypedDict, closed=True):
    bind: NotRequired[DataQuery]
    columns: NotRequired[float]
    config: NotRequired[Config]
    data: NotRequired[Data]
    field: NotRequired[str]
    plot: NotRequired[str]
    height: NotRequired[float]
    label: NotRequired[str]
    legend: Literal["color", "opacity", "symbol"]
    margin_bottom: NotRequired[float]
    margin_left: NotRequired[float]
    margin_right: NotRequired[float]
    margin_top: NotRequired[float]
    meta: NotRequired[Meta]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    tick_size: NotRequired[float]
    width: NotRequired[float]


class Stddev(TypedDict, closed=True):
    distinct: NotRequired[bool]
    exclude: NotRequired[
        Literal[
            "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
        ]
    ]
    groups: NotRequired[Sequence[FrameValue] | DataQuery]
    orderby: NotRequired[TransformField | Sequence[TransformField]]
    partitionby: NotRequired[TransformField | Sequence[TransformField]]
    range: NotRequired[Sequence[FrameValue] | DataQuery]
    rows: NotRequired[Sequence[FrameValue] | DataQuery]
    stddev: str | float | bool | DataQuery | Sequence[str | float | bool | DataQuery]


class StddevPop(TypedDict, closed=True):
    distinct: NotRequired[bool]
    exclude: NotRequired[
        Literal[
            "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
        ]
    ]
    groups: NotRequired[Sequence[FrameValue] | DataQuery]
    orderby: NotRequired[TransformField | Sequence[TransformField]]
    partitionby: NotRequired[TransformField | Sequence[TransformField]]
    range: NotRequired[Sequence[FrameValue] | DataQuery]
    rows: NotRequired[Sequence[FrameValue] | DataQuery]
    stddev_pop: str | float | bool | DataQuery | Sequence[str | float | bool | DataQuery]


class Sum(TypedDict, closed=True):
    distinct: NotRequired[bool]
    exclude: NotRequired[
        Literal[
            "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
        ]
    ]
    groups: NotRequired[Sequence[FrameValue] | DataQuery]
    orderby: NotRequired[TransformField | Sequence[TransformField]]
    partitionby: NotRequired[TransformField | Sequence[TransformField]]
    range: NotRequired[Sequence[FrameValue] | DataQuery]
    rows: NotRequired[Sequence[FrameValue] | DataQuery]
    sum: str | float | bool | DataQuery | Sequence[str | float | bool | DataQuery]


class VarPop(TypedDict, closed=True):
    distinct: NotRequired[bool]
    exclude: NotRequired[
        Literal[
            "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
        ]
    ]
    groups: NotRequired[Sequence[FrameValue] | DataQuery]
    orderby: NotRequired[TransformField | Sequence[TransformField]]
    partitionby: NotRequired[TransformField | Sequence[TransformField]]
    range: NotRequired[Sequence[FrameValue] | DataQuery]
    rows: NotRequired[Sequence[FrameValue] | DataQuery]
    var_pop: str | float | bool | DataQuery | Sequence[str | float | bool | DataQuery]


class Variance(TypedDict, closed=True):
    distinct: NotRequired[bool]
    exclude: NotRequired[
        Literal[
            "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
        ]
    ]
    groups: NotRequired[Sequence[FrameValue] | DataQuery]
    orderby: NotRequired[TransformField | Sequence[TransformField]]
    partitionby: NotRequired[TransformField | Sequence[TransformField]]
    range: NotRequired[Sequence[FrameValue] | DataQuery]
    rows: NotRequired[Sequence[FrameValue] | DataQuery]
    variance: str | float | bool | DataQuery | Sequence[str | float | bool | DataQuery]


class Argmax(TypedDict, closed=True):
    argmax: Sequence[str | float | bool | DataQuery]
    distinct: NotRequired[bool]
    exclude: NotRequired[
        Literal[
            "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
        ]
    ]
    groups: NotRequired[Sequence[FrameValue] | DataQuery]
    orderby: NotRequired[TransformField | Sequence[TransformField]]
    partitionby: NotRequired[TransformField | Sequence[TransformField]]
    range: NotRequired[Sequence[FrameValue] | DataQuery]
    rows: NotRequired[Sequence[FrameValue] | DataQuery]


class Argmin(TypedDict, closed=True):
    argmin: Sequence[str | float | bool | DataQuery]
    distinct: NotRequired[bool]
    exclude: NotRequired[
        Literal[
            "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
        ]
    ]
    groups: NotRequired[Sequence[FrameValue] | DataQuery]
    orderby: NotRequired[TransformField | Sequence[TransformField]]
    partitionby: NotRequired[TransformField | Sequence[TransformField]]
    range: NotRequired[Sequence[FrameValue] | DataQuery]
    rows: NotRequired[Sequence[FrameValue] | DataQuery]


class Avg(TypedDict, closed=True):
    avg: str | float | bool | DataQuery | Sequence[str | float | bool | DataQuery]
    distinct: NotRequired[bool]
    exclude: NotRequired[
        Literal[
            "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
        ]
    ]
    groups: NotRequired[Sequence[FrameValue] | DataQuery]
    orderby: NotRequired[TransformField | Sequence[TransformField]]
    partitionby: NotRequired[TransformField | Sequence[TransformField]]
    range: NotRequired[Sequence[FrameValue] | DataQuery]
    rows: NotRequired[Sequence[FrameValue] | DataQuery]


class ChannelDomainSort(TypedDict, closed=True):
    color: NotRequired[ChannelDomainValueSpec]
    fx: NotRequired[ChannelDomainValueSpec]
    fy: NotRequired[ChannelDomainValueSpec]
    length: NotRequired[ChannelDomainValueSpec]
    limit: NotRequired[float | tuple[Lo, Lo]]
    opacity: NotRequired[ChannelDomainValueSpec]
    order: NotRequired[Literal["ascending", "descending"] | None]
    r: NotRequired[ChannelDomainValueSpec]
    reduce: NotRequired[Reducer | bool | None]
    reverse: NotRequired[bool]
    symbol: NotRequired[ChannelDomainValueSpec]
    x: NotRequired[ChannelDomainValueSpec]
    y: NotRequired[ChannelDomainValueSpec]


class Count(TypedDict, closed=True):
    count: (
        Sequence[Any]
        | str
        | float
        | bool
        | DataQuery
        | Sequence[str | float | bool | DataQuery]
        | None
    )
    distinct: NotRequired[bool]
    exclude: NotRequired[
        Literal[
            "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
        ]
    ]
    groups: NotRequired[Sequence[FrameValue] | DataQuery]
    orderby: NotRequired[TransformField | Sequence[TransformField]]
    partitionby: NotRequired[TransformField | Sequence[TransformField]]
    range: NotRequired[Sequence[FrameValue] | DataQuery]
    rows: NotRequired[Sequence[FrameValue] | DataQuery]


class CumeDist(TypedDict, closed=True):
    cume_dist: Sequence[Any] | None
    exclude: NotRequired[
        Literal[
            "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
        ]
    ]
    groups: NotRequired[Sequence[FrameValue] | DataQuery]
    orderby: NotRequired[TransformField | Sequence[TransformField]]
    partitionby: NotRequired[TransformField | Sequence[TransformField]]
    range: NotRequired[Sequence[FrameValue] | DataQuery]
    rows: NotRequired[Sequence[FrameValue] | DataQuery]


class DenseRank(TypedDict, closed=True):
    dense_rank: Sequence[Any] | None
    exclude: NotRequired[
        Literal[
            "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
        ]
    ]
    groups: NotRequired[Sequence[FrameValue] | DataQuery]
    orderby: NotRequired[TransformField | Sequence[TransformField]]
    partitionby: NotRequired[TransformField | Sequence[TransformField]]
    range: NotRequired[Sequence[FrameValue] | DataQuery]
    rows: NotRequired[Sequence[FrameValue] | DataQuery]


class First(TypedDict, closed=True):
    distinct: NotRequired[bool]
    exclude: NotRequired[
        Literal[
            "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
        ]
    ]
    first: str | float | bool | DataQuery | Sequence[str | float | bool | DataQuery]
    groups: NotRequired[Sequence[FrameValue] | DataQuery]
    orderby: NotRequired[TransformField | Sequence[TransformField]]
    partitionby: NotRequired[TransformField | Sequence[TransformField]]
    range: NotRequired[Sequence[FrameValue] | DataQuery]
    rows: NotRequired[Sequence[FrameValue] | DataQuery]


class FirstValue(TypedDict, closed=True):
    exclude: NotRequired[
        Literal[
            "CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"
        ]
    ]
    first_value: str | float | bool | DataQuery | Sequence[str | float | bool | DataQuery]
    groups: NotRequired[Sequence[FrameValue] | DataQuery]
    orderby: NotRequired[TransformField | Sequence[TransformField]]
    partitionby: NotRequired[TransformField | Sequence[TransformField]]
    range: NotRequired[Sequence[FrameValue] | DataQuery]
    rows: NotRequired[Sequence[FrameValue] | DataQuery]


WindowTransform: TypeAlias = (
    RowNumber
    | Rank
    | DenseRank
    | PercentRank
    | CumeDist
    | NTile
    | Lag
    | Lead
    | FirstValue
    | LastValue
    | NthValue
)


AggregateTransform: TypeAlias = (
    Argmax
    | Argmin
    | Avg
    | Count
    | Max
    | Min
    | First
    | Last
    | Median
    | Mode
    | Product
    | Quantile
    | Stddev
    | StddevPop
    | Sum
    | Variance
    | VarPop
)


Transform: TypeAlias = ColumnTransform | AggregateTransform | WindowTransform


ChannelValue: TypeAlias = (
    Sequence[Any] | str | float | bool | Transform | SQLExpression | AggregateExpression | None
)


class ChannelValueIntervalSpec1(TypedDict, closed=True):
    interval: Interval
    value: ChannelValue


class ChannelValueSpec1(TypedDict, closed=True):
    label: NotRequired[str]
    scale: NotRequired[ScaleName | Literal["auto"] | bool | None]
    value: ChannelValue


ChannelValueSpec: TypeAlias = ChannelValue | ChannelValueSpec1


class Tip(TypedDict):
    anchor: NotRequired[FrameAnchor | DataQuery]
    font_family: NotRequired[str | DataQuery]
    font_size: NotRequired[ChannelValue | DataQuery]
    font_style: NotRequired[str | DataQuery]
    font_variant: NotRequired[str | DataQuery]
    font_weight: NotRequired[str | float | DataQuery]
    format: NotRequired[Format]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    line_height: NotRequired[float | DataQuery]
    line_width: NotRequired[float | DataQuery]
    monospace: NotRequired[bool | DataQuery]
    path_filter: NotRequired[str | DataQuery]
    pointer: NotRequired[TipPointer]
    pointer_size: NotRequired[float | DataQuery]
    preferred_anchor: NotRequired[FrameAnchor | DataQuery | None]
    text_anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    text_overflow: NotRequired[
        Literal[
            "clip",
            "ellipsis",
            "clip-start",
            "clip-end",
            "ellipsis-start",
            "ellipsis-middle",
            "ellipsis-end",
        ]
        | DataQuery
        | None
    ]
    text_padding: NotRequired[float | DataQuery]
    x: NotRequired[ChannelValueSpec]
    x1: NotRequired[ChannelValueSpec]
    x2: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    y1: NotRequired[ChannelValueSpec]
    y2: NotRequired[ChannelValueSpec]


class SortOrder1(TypedDict, closed=True):
    order: NotRequired[Literal["ascending", "descending"]]
    value: NotRequired[ChannelValue]


SortOrder: TypeAlias = ChannelValue | SortOrder1 | SortOrder2


class Spec10(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    curve: NotRequired[Curve | DataQuery]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["area"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    offset: NotRequired[StackOffset | DataQuery | None]
    opacity: NotRequired[ChannelValueSpec]
    order: NotRequired[StackOrder | DataQuery | None]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x1: NotRequired[ChannelValueSpec]
    x2: NotRequired[ChannelValueSpec]
    y1: NotRequired[ChannelValueSpec]
    y2: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec11(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    curve: NotRequired[Curve | DataQuery]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["areaX"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    offset: NotRequired[StackOffset | DataQuery | None]
    opacity: NotRequired[ChannelValueSpec]
    order: NotRequired[StackOrder | DataQuery | None]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    x1: NotRequired[ChannelValueSpec]
    x2: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec12(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    curve: NotRequired[Curve | DataQuery]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["areaY"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    offset: NotRequired[StackOffset | DataQuery | None]
    opacity: NotRequired[ChannelValueSpec]
    order: NotRequired[StackOrder | DataQuery | None]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    y1: NotRequired[ChannelValueSpec]
    y2: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec13(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bend: NotRequired[float | bool | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    head_angle: NotRequired[float | DataQuery]
    head_length: NotRequired[float | DataQuery]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_end: NotRequired[float | DataQuery]
    inset_start: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["arrow"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    sweep: NotRequired[Literal["+x", "-x", "+y", "-y"] | float | DataQuery]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    x1: NotRequired[ChannelValueSpec]
    x2: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    y1: NotRequired[ChannelValueSpec]
    y2: NotRequired[ChannelValueSpec]


class Spec14(TypedDict, closed=True):
    anchor: NotRequired[Literal["top", "right", "bottom", "left"] | DataQuery]
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    color: NotRequired[ChannelValueSpec | DataQuery]
    config: NotRequired[Config]
    data: NotRequired[Data]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    font_family: NotRequired[str | DataQuery]
    font_size: NotRequired[ChannelValue | DataQuery]
    font_style: NotRequired[str | DataQuery]
    font_variant: NotRequired[str | DataQuery]
    font_weight: NotRequired[str | float | DataQuery]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    label: NotRequired[str | DataQuery | None]
    label_anchor: NotRequired[Literal["top", "right", "bottom", "left", "center"] | DataQuery]
    label_arrow: NotRequired[
        Literal["auto", "up", "right", "down", "left", "none", True, False] | DataQuery | None
    ]
    label_offset: NotRequired[float | DataQuery]
    line_anchor: NotRequired[Literal["top", "middle", "bottom"] | DataQuery]
    line_height: NotRequired[float | DataQuery]
    line_width: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["axisX"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    monospace: NotRequired[bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    text: NotRequired[ChannelValue]
    text_anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    text_overflow: NotRequired[
        Literal[
            "clip",
            "ellipsis",
            "clip-start",
            "clip-end",
            "ellipsis-start",
            "ellipsis-middle",
            "ellipsis-end",
        ]
        | DataQuery
        | None
    ]
    text_stroke: NotRequired[ChannelValueSpec | DataQuery]
    text_stroke_opacity: NotRequired[ChannelValueSpec]
    text_stroke_width: NotRequired[ChannelValueSpec]
    tick_format: NotRequired[str | DataQuery | None]
    tick_padding: NotRequired[float | DataQuery]
    tick_rotate: NotRequired[float | DataQuery]
    tick_size: NotRequired[float | DataQuery]
    tick_spacing: NotRequired[float | DataQuery]
    ticks: NotRequired[float | Interval | Sequence[Any] | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec15(TypedDict, closed=True):
    anchor: NotRequired[Literal["top", "right", "bottom", "left"] | DataQuery]
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    color: NotRequired[ChannelValueSpec | DataQuery]
    config: NotRequired[Config]
    data: NotRequired[Data]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    font_family: NotRequired[str | DataQuery]
    font_size: NotRequired[ChannelValue | DataQuery]
    font_style: NotRequired[str | DataQuery]
    font_variant: NotRequired[str | DataQuery]
    font_weight: NotRequired[str | float | DataQuery]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    label: NotRequired[str | DataQuery | None]
    label_anchor: NotRequired[Literal["top", "right", "bottom", "left", "center"] | DataQuery]
    label_arrow: NotRequired[
        Literal["auto", "up", "right", "down", "left", "none", True, False] | DataQuery | None
    ]
    label_offset: NotRequired[float | DataQuery]
    line_anchor: NotRequired[Literal["top", "middle", "bottom"] | DataQuery]
    line_height: NotRequired[float | DataQuery]
    line_width: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["axisY"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    monospace: NotRequired[bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    text: NotRequired[ChannelValue]
    text_anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    text_overflow: NotRequired[
        Literal[
            "clip",
            "ellipsis",
            "clip-start",
            "clip-end",
            "ellipsis-start",
            "ellipsis-middle",
            "ellipsis-end",
        ]
        | DataQuery
        | None
    ]
    text_stroke: NotRequired[ChannelValueSpec | DataQuery]
    text_stroke_opacity: NotRequired[ChannelValueSpec]
    text_stroke_width: NotRequired[ChannelValueSpec]
    tick_format: NotRequired[str | DataQuery | None]
    tick_padding: NotRequired[float | DataQuery]
    tick_rotate: NotRequired[float | DataQuery]
    tick_size: NotRequired[float | DataQuery]
    tick_spacing: NotRequired[float | DataQuery]
    ticks: NotRequired[float | Interval | Sequence[Any] | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec16(TypedDict, closed=True):
    anchor: NotRequired[Literal["top", "right", "bottom", "left"] | DataQuery]
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    color: NotRequired[ChannelValueSpec | DataQuery]
    config: NotRequired[Config]
    data: NotRequired[Data]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    font_family: NotRequired[str | DataQuery]
    font_size: NotRequired[ChannelValue | DataQuery]
    font_style: NotRequired[str | DataQuery]
    font_variant: NotRequired[str | DataQuery]
    font_weight: NotRequired[str | float | DataQuery]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    label: NotRequired[str | DataQuery | None]
    label_anchor: NotRequired[Literal["top", "right", "bottom", "left", "center"] | DataQuery]
    label_arrow: NotRequired[
        Literal["auto", "up", "right", "down", "left", "none", True, False] | DataQuery | None
    ]
    label_offset: NotRequired[float | DataQuery]
    line_anchor: NotRequired[Literal["top", "middle", "bottom"] | DataQuery]
    line_height: NotRequired[float | DataQuery]
    line_width: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["axisFx"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    monospace: NotRequired[bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    text: NotRequired[ChannelValue]
    text_anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    text_overflow: NotRequired[
        Literal[
            "clip",
            "ellipsis",
            "clip-start",
            "clip-end",
            "ellipsis-start",
            "ellipsis-middle",
            "ellipsis-end",
        ]
        | DataQuery
        | None
    ]
    text_stroke: NotRequired[ChannelValueSpec | DataQuery]
    text_stroke_opacity: NotRequired[ChannelValueSpec]
    text_stroke_width: NotRequired[ChannelValueSpec]
    tick_format: NotRequired[str | DataQuery | None]
    tick_padding: NotRequired[float | DataQuery]
    tick_rotate: NotRequired[float | DataQuery]
    tick_size: NotRequired[float | DataQuery]
    tick_spacing: NotRequired[float | DataQuery]
    ticks: NotRequired[float | Interval | Sequence[Any] | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec17(TypedDict, closed=True):
    anchor: NotRequired[Literal["top", "right", "bottom", "left"] | DataQuery]
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    color: NotRequired[ChannelValueSpec | DataQuery]
    config: NotRequired[Config]
    data: NotRequired[Data]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    font_family: NotRequired[str | DataQuery]
    font_size: NotRequired[ChannelValue | DataQuery]
    font_style: NotRequired[str | DataQuery]
    font_variant: NotRequired[str | DataQuery]
    font_weight: NotRequired[str | float | DataQuery]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    label: NotRequired[str | DataQuery | None]
    label_anchor: NotRequired[Literal["top", "right", "bottom", "left", "center"] | DataQuery]
    label_arrow: NotRequired[
        Literal["auto", "up", "right", "down", "left", "none", True, False] | DataQuery | None
    ]
    label_offset: NotRequired[float | DataQuery]
    line_anchor: NotRequired[Literal["top", "middle", "bottom"] | DataQuery]
    line_height: NotRequired[float | DataQuery]
    line_width: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["axisFy"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    monospace: NotRequired[bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    text: NotRequired[ChannelValue]
    text_anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    text_overflow: NotRequired[
        Literal[
            "clip",
            "ellipsis",
            "clip-start",
            "clip-end",
            "ellipsis-start",
            "ellipsis-middle",
            "ellipsis-end",
        ]
        | DataQuery
        | None
    ]
    text_stroke: NotRequired[ChannelValueSpec | DataQuery]
    text_stroke_opacity: NotRequired[ChannelValueSpec]
    text_stroke_width: NotRequired[ChannelValueSpec]
    tick_format: NotRequired[str | DataQuery | None]
    tick_padding: NotRequired[float | DataQuery]
    tick_rotate: NotRequired[float | DataQuery]
    tick_size: NotRequired[float | DataQuery]
    tick_spacing: NotRequired[float | DataQuery]
    ticks: NotRequired[float | Interval | Sequence[Any] | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec24(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["cell"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rx: NotRequired[float | str | DataQuery]
    ry: NotRequired[float | str | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class Spec25(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["cellX"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rx: NotRequired[float | str | DataQuery]
    ry: NotRequired[float | str | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class Spec26(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["cellY"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rx: NotRequired[float | str | DataQuery]
    ry: NotRequired[float | str | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class Spec27(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bandwidth: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    height: NotRequired[float | DataQuery]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    interpolate: NotRequired[GridInterpolate | DataQuery | None]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["contour"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    pad: NotRequired[float | DataQuery]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    pixel_size: NotRequired[float | DataQuery]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    thresholds: NotRequired[float | Sequence[float] | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    width: NotRequired[float | DataQuery]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class Spec28(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    curve: NotRequired[Curve | DataQuery]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["delaunayLink"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec29(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    curve: NotRequired[Curve | DataQuery]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["delaunayMesh"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec30(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    curve: NotRequired[Curve | DataQuery]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["hull"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec31(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    curve: NotRequired[Curve | DataQuery]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["voronoi"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec32(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    curve: NotRequired[Curve | DataQuery]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["voronoiMesh"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec33(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bandwidth: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    height: NotRequired[float | DataQuery]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    image_rendering: NotRequired[str | DataQuery]
    interpolate: NotRequired[GridInterpolate | DataQuery | None]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["denseLine"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    normalize: NotRequired[bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    pad: NotRequired[float | DataQuery]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    pixel_size: NotRequired[float | DataQuery]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    width: NotRequired[float | DataQuery]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec34(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bandwidth: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    font_family: NotRequired[str | DataQuery]
    font_size: NotRequired[ChannelValue | DataQuery]
    font_style: NotRequired[str | DataQuery]
    font_variant: NotRequired[str | DataQuery]
    font_weight: NotRequired[str | float | DataQuery]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    height: NotRequired[float | DataQuery]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    interpolate: NotRequired[GridInterpolate | DataQuery | None]
    line_height: NotRequired[float | DataQuery]
    line_width: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["density"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    monospace: NotRequired[bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    pad: NotRequired[float | DataQuery]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    pixel_size: NotRequired[float | DataQuery]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    r: NotRequired[ChannelValueSpec | float | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | float | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    symbol: NotRequired[ChannelValueSpec | SymbolType | DataQuery]
    target: NotRequired[str | DataQuery]
    text_anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    text_overflow: NotRequired[
        Literal[
            "clip",
            "ellipsis",
            "clip-start",
            "clip-end",
            "ellipsis-start",
            "ellipsis-middle",
            "ellipsis-end",
        ]
        | DataQuery
        | None
    ]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    type: NotRequired[Literal["dot", "circle", "hexagon", "cell", "text"] | DataQuery]
    width: NotRequired[float | DataQuery]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec35(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bandwidth: NotRequired[float | DataQuery]
    bins: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    curve: NotRequired[Curve | DataQuery]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["densityX"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    normalize: NotRequired[Literal["max", "sum", "none"] | bool | DataQuery]
    offset: NotRequired[StackOffset | DataQuery | None]
    opacity: NotRequired[ChannelValueSpec]
    order: NotRequired[StackOrder | DataQuery | None]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stack: NotRequired[bool | DataQuery]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    type: Literal["areaX"]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec36(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bandwidth: NotRequired[float | DataQuery]
    bins: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    curve: NotRequired[Curve | Literal["auto"] | DataQuery]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["densityX"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    normalize: NotRequired[Literal["max", "sum", "none"] | bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    type: Literal["lineX"]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec37(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bandwidth: NotRequired[float | DataQuery]
    bins: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["densityX"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    normalize: NotRequired[Literal["max", "sum", "none"] | bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    r: NotRequired[ChannelValueSpec | float | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | float | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    symbol: NotRequired[ChannelValueSpec | SymbolType | DataQuery]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    type: Literal["dotX"]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec38(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bandwidth: NotRequired[float | DataQuery]
    bins: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    font_family: NotRequired[str | DataQuery]
    font_size: NotRequired[ChannelValue | DataQuery]
    font_style: NotRequired[str | DataQuery]
    font_variant: NotRequired[str | DataQuery]
    font_weight: NotRequired[str | float | DataQuery]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    line_anchor: NotRequired[Literal["top", "middle", "bottom"] | DataQuery]
    line_height: NotRequired[float | DataQuery]
    line_width: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["densityX"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    monospace: NotRequired[bool | DataQuery]
    normalize: NotRequired[Literal["max", "sum", "none"] | bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    text: NotRequired[ChannelValue]
    text_anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    text_overflow: NotRequired[
        Literal[
            "clip",
            "ellipsis",
            "clip-start",
            "clip-end",
            "ellipsis-start",
            "ellipsis-middle",
            "ellipsis-end",
        ]
        | DataQuery
        | None
    ]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    type: Literal["textX"]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec39(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bandwidth: NotRequired[float | DataQuery]
    bins: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    curve: NotRequired[Curve | DataQuery]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["densityY"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    normalize: NotRequired[Literal["max", "sum", "none"] | bool | DataQuery]
    offset: NotRequired[StackOffset | DataQuery | None]
    opacity: NotRequired[ChannelValueSpec]
    order: NotRequired[StackOrder | DataQuery | None]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stack: NotRequired[bool | DataQuery]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    type: NotRequired[Literal["areaY"]]
    x: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec40(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bandwidth: NotRequired[float | DataQuery]
    bins: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    curve: NotRequired[Curve | Literal["auto"] | DataQuery]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["densityY"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    normalize: NotRequired[Literal["max", "sum", "none"] | bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    type: Literal["lineY"]
    x: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec41(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bandwidth: NotRequired[float | DataQuery]
    bins: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["densityY"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    normalize: NotRequired[Literal["max", "sum", "none"] | bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    r: NotRequired[ChannelValueSpec | float | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | float | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    symbol: NotRequired[ChannelValueSpec | SymbolType | DataQuery]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    type: Literal["dot", "dotY", "circle", "hexagon"]
    x: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec42(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bandwidth: NotRequired[float | DataQuery]
    bins: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    font_family: NotRequired[str | DataQuery]
    font_size: NotRequired[ChannelValue | DataQuery]
    font_style: NotRequired[str | DataQuery]
    font_variant: NotRequired[str | DataQuery]
    font_weight: NotRequired[str | float | DataQuery]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    line_anchor: NotRequired[Literal["top", "middle", "bottom"] | DataQuery]
    line_height: NotRequired[float | DataQuery]
    line_width: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["densityY"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    monospace: NotRequired[bool | DataQuery]
    normalize: NotRequired[Literal["max", "sum", "none"] | bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    text: NotRequired[ChannelValue]
    text_anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    text_overflow: NotRequired[
        Literal[
            "clip",
            "ellipsis",
            "clip-start",
            "clip-end",
            "ellipsis-start",
            "ellipsis-middle",
            "ellipsis-end",
        ]
        | DataQuery
        | None
    ]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    type: Literal["text", "textY"]
    x: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec43(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["dot"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    r: NotRequired[ChannelValueSpec | float | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | float | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    symbol: NotRequired[ChannelValueSpec | SymbolType | DataQuery]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec46(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["circle"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    r: NotRequired[ChannelValueSpec | float | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | float | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    symbol: NotRequired[ChannelValueSpec | SymbolType | DataQuery]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec47(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["hexagon"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    r: NotRequired[ChannelValueSpec | float | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | float | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    symbol: NotRequired[ChannelValueSpec | SymbolType | DataQuery]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec48(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    ci: NotRequired[float | DataQuery]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["errorbarX"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: ChannelValueSpec
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec49(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    ci: NotRequired[float | DataQuery]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["errorbarY"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: ChannelValueSpec
    z: NotRequired[ChannelValue]


class Spec50(TypedDict, closed=True):
    anchor: NotRequired[Literal["top", "right", "bottom", "left"] | DataQuery | None]
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: NotRequired[Data]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["frame"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rx: NotRequired[float | str | DataQuery]
    ry: NotRequired[float | str | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]


class Spec51(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    geometry: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["geo"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    r: NotRequired[ChannelValueSpec | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]


class Spec52(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: NotRequired[Data]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["graticule"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]


class Spec53(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: NotRequired[Data]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["sphere"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]


class Spec54(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bin_width: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    font_family: NotRequired[str | DataQuery]
    font_size: NotRequired[ChannelValue | DataQuery]
    font_style: NotRequired[str | DataQuery]
    font_variant: NotRequired[str | DataQuery]
    font_weight: NotRequired[str | float | DataQuery]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    line_height: NotRequired[float | DataQuery]
    line_width: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["hexbin"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    monospace: NotRequired[bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    r: NotRequired[ChannelValueSpec | float | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | float | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    symbol: NotRequired[ChannelValueSpec | SymbolType | DataQuery]
    target: NotRequired[str | DataQuery]
    text_anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    text_overflow: NotRequired[
        Literal[
            "clip",
            "ellipsis",
            "clip-start",
            "clip-end",
            "ellipsis-start",
            "ellipsis-middle",
            "ellipsis-end",
        ]
        | DataQuery
        | None
    ]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    type: NotRequired[Literal["dot", "circle", "hexagon", "text"] | DataQuery]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec55(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bin_width: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: NotRequired[Data]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["hexgrid"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]


class Spec56(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    cross_origin: NotRequired[str | DataQuery]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    height: NotRequired[ChannelValue | DataQuery]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    image_rendering: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["image"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    preserve_aspect_ratio: NotRequired[str | DataQuery]
    r: NotRequired[ChannelValue | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    src: NotRequired[ChannelValue | DataQuery]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    width: NotRequired[ChannelValue | DataQuery]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class Spec57(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    curve: NotRequired[Curve | Literal["auto"] | DataQuery]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["line"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec58(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    curve: NotRequired[Curve | Literal["auto"] | DataQuery]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["lineX"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec59(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    curve: NotRequired[Curve | Literal["auto"] | DataQuery]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["lineY"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec60(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    curve: NotRequired[Curve | Literal["auto"] | DataQuery]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["link"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    x1: NotRequired[ChannelValueSpec]
    x2: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    y1: NotRequired[ChannelValueSpec]
    y2: NotRequired[ChannelValueSpec]


class Spec61(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bandwidth: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    height: NotRequired[float | DataQuery]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    image_rendering: NotRequired[str | DataQuery]
    interpolate: NotRequired[GridInterpolate | DataQuery | None]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["raster"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    pad: NotRequired[float | DataQuery]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    pixel_size: NotRequired[float | DataQuery]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    width: NotRequired[float | DataQuery]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class Spec62(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bandwidth: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    height: NotRequired[float | DataQuery]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    image_rendering: NotRequired[str | DataQuery]
    interpolate: NotRequired[GridInterpolate | DataQuery | None]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["heatmap"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    pad: NotRequired[float | DataQuery]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    pixel_size: NotRequired[float | DataQuery]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    width: NotRequired[float | DataQuery]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class Spec63(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bandwidth: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    height: NotRequired[float | DataQuery]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    image_rendering: NotRequired[str | DataQuery]
    interpolate: NotRequired[GridInterpolate | DataQuery | None]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["rasterTile"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    origin: NotRequired[Sequence[float] | DataQuery]
    pad: NotRequired[float | DataQuery]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    pixel_size: NotRequired[float | DataQuery]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    width: NotRequired[float | DataQuery]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class Spec67(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    ci: NotRequired[float | DataQuery]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["regressionY"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    precision: NotRequired[float | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec70(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: NotRequired[Data]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    font_family: NotRequired[str | DataQuery]
    font_size: NotRequired[ChannelValue | DataQuery]
    font_style: NotRequired[str | DataQuery]
    font_variant: NotRequired[str | DataQuery]
    font_weight: NotRequired[str | float | DataQuery]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    line_anchor: NotRequired[Literal["top", "middle", "bottom"] | DataQuery]
    line_height: NotRequired[float | DataQuery]
    line_width: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["text"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    monospace: NotRequired[bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    text: NotRequired[ChannelValue]
    text_anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    text_overflow: NotRequired[
        Literal[
            "clip",
            "ellipsis",
            "clip-start",
            "clip-end",
            "ellipsis-start",
            "ellipsis-middle",
            "ellipsis-end",
        ]
        | DataQuery
        | None
    ]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec73(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["tickX"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class Spec74(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["tickY"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class Spec75(TypedDict, closed=True):
    anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    length: NotRequired[ChannelValueSpec]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["vector"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    r: NotRequired[float | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue]
    select: NotRequired[SelectFilter]
    shape: NotRequired[VectorShape | DataQuery]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class Spec76(TypedDict, closed=True):
    anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    length: NotRequired[ChannelValueSpec]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["vectorX"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    r: NotRequired[float | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue]
    select: NotRequired[SelectFilter]
    shape: NotRequired[VectorShape | DataQuery]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class Spec77(TypedDict, closed=True):
    anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    length: NotRequired[ChannelValueSpec]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["vectorY"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    r: NotRequired[float | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue]
    select: NotRequired[SelectFilter]
    shape: NotRequired[VectorShape | DataQuery]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class Spec78(TypedDict, closed=True):
    anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    length: NotRequired[ChannelValueSpec]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["spike"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    r: NotRequired[float | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue]
    select: NotRequired[SelectFilter]
    shape: NotRequired[VectorShape | DataQuery]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class Sphere(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["sphere"]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]


class Spike(TypedDict, closed=True):
    anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    length: NotRequired[ChannelValueSpec]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["spike"]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    r: NotRequired[float | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue]
    select: NotRequired[SelectFilter]
    shape: NotRequired[VectorShape | DataQuery]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class Text(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: NotRequired[PlotMarkData]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    font_family: NotRequired[str | DataQuery]
    font_size: NotRequired[ChannelValue | DataQuery]
    font_style: NotRequired[str | DataQuery]
    font_variant: NotRequired[str | DataQuery]
    font_weight: NotRequired[str | float | DataQuery]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    line_anchor: NotRequired[Literal["top", "middle", "bottom"] | DataQuery]
    line_height: NotRequired[float | DataQuery]
    line_width: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["text"]
    mix_blend_mode: NotRequired[str | DataQuery]
    monospace: NotRequired[bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    text: NotRequired[ChannelValue]
    text_anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    text_overflow: NotRequired[
        Literal[
            "clip",
            "ellipsis",
            "clip-start",
            "clip-end",
            "ellipsis-start",
            "ellipsis-middle",
            "ellipsis-end",
        ]
        | DataQuery
        | None
    ]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class TickX(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["tickX"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class TickY(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["tickY"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class Vector(TypedDict, closed=True):
    anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    length: NotRequired[ChannelValueSpec]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["vector"]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    r: NotRequired[float | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue]
    select: NotRequired[SelectFilter]
    shape: NotRequired[VectorShape | DataQuery]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class VectorX(TypedDict, closed=True):
    anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    length: NotRequired[ChannelValueSpec]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["vectorX"]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    r: NotRequired[float | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue]
    select: NotRequired[SelectFilter]
    shape: NotRequired[VectorShape | DataQuery]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class VectorY(TypedDict, closed=True):
    anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    length: NotRequired[ChannelValueSpec]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["vectorY"]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    r: NotRequired[float | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue]
    select: NotRequired[SelectFilter]
    shape: NotRequired[VectorShape | DataQuery]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class Voronoi(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    curve: NotRequired[Curve | DataQuery]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["voronoi"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class VoronoiMesh(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    curve: NotRequired[Curve | DataQuery]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["voronoiMesh"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Area(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    curve: NotRequired[Curve | DataQuery]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["area"]
    mix_blend_mode: NotRequired[str | DataQuery]
    offset: NotRequired[StackOffset | DataQuery | None]
    opacity: NotRequired[ChannelValueSpec]
    order: NotRequired[StackOrder | DataQuery | None]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x1: NotRequired[ChannelValueSpec]
    x2: NotRequired[ChannelValueSpec]
    y1: NotRequired[ChannelValueSpec]
    y2: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class AreaX(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    curve: NotRequired[Curve | DataQuery]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["areaX"]
    mix_blend_mode: NotRequired[str | DataQuery]
    offset: NotRequired[StackOffset | DataQuery | None]
    opacity: NotRequired[ChannelValueSpec]
    order: NotRequired[StackOrder | DataQuery | None]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    x1: NotRequired[ChannelValueSpec]
    x2: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class AreaY(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    curve: NotRequired[Curve | DataQuery]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["areaY"]
    mix_blend_mode: NotRequired[str | DataQuery]
    offset: NotRequired[StackOffset | DataQuery | None]
    opacity: NotRequired[ChannelValueSpec]
    order: NotRequired[StackOrder | DataQuery | None]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    y1: NotRequired[ChannelValueSpec]
    y2: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Arrow(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bend: NotRequired[float | bool | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    head_angle: NotRequired[float | DataQuery]
    head_length: NotRequired[float | DataQuery]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_end: NotRequired[float | DataQuery]
    inset_start: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["arrow"]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    sweep: NotRequired[Literal["+x", "-x", "+y", "-y"] | float | DataQuery]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    x1: NotRequired[ChannelValueSpec]
    x2: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    y1: NotRequired[ChannelValueSpec]
    y2: NotRequired[ChannelValueSpec]


class AxisFx(TypedDict, closed=True):
    anchor: NotRequired[Literal["top", "right", "bottom", "left"] | DataQuery]
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    color: NotRequired[ChannelValueSpec | DataQuery]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    font_family: NotRequired[str | DataQuery]
    font_size: NotRequired[ChannelValue | DataQuery]
    font_style: NotRequired[str | DataQuery]
    font_variant: NotRequired[str | DataQuery]
    font_weight: NotRequired[str | float | DataQuery]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    label: NotRequired[str | DataQuery | None]
    label_anchor: NotRequired[Literal["top", "right", "bottom", "left", "center"] | DataQuery]
    label_arrow: NotRequired[
        Literal["auto", "up", "right", "down", "left", "none", True, False] | DataQuery | None
    ]
    label_offset: NotRequired[float | DataQuery]
    line_anchor: NotRequired[Literal["top", "middle", "bottom"] | DataQuery]
    line_height: NotRequired[float | DataQuery]
    line_width: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["axisFx"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    mix_blend_mode: NotRequired[str | DataQuery]
    monospace: NotRequired[bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    text: NotRequired[ChannelValue]
    text_anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    text_overflow: NotRequired[
        Literal[
            "clip",
            "ellipsis",
            "clip-start",
            "clip-end",
            "ellipsis-start",
            "ellipsis-middle",
            "ellipsis-end",
        ]
        | DataQuery
        | None
    ]
    text_stroke: NotRequired[ChannelValueSpec | DataQuery]
    text_stroke_opacity: NotRequired[ChannelValueSpec]
    text_stroke_width: NotRequired[ChannelValueSpec]
    tick_format: NotRequired[str | DataQuery | None]
    tick_padding: NotRequired[float | DataQuery]
    tick_rotate: NotRequired[float | DataQuery]
    tick_size: NotRequired[float | DataQuery]
    tick_spacing: NotRequired[float | DataQuery]
    ticks: NotRequired[float | Interval | Sequence[Any] | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class AxisFy(TypedDict, closed=True):
    anchor: NotRequired[Literal["top", "right", "bottom", "left"] | DataQuery]
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    color: NotRequired[ChannelValueSpec | DataQuery]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    font_family: NotRequired[str | DataQuery]
    font_size: NotRequired[ChannelValue | DataQuery]
    font_style: NotRequired[str | DataQuery]
    font_variant: NotRequired[str | DataQuery]
    font_weight: NotRequired[str | float | DataQuery]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    label: NotRequired[str | DataQuery | None]
    label_anchor: NotRequired[Literal["top", "right", "bottom", "left", "center"] | DataQuery]
    label_arrow: NotRequired[
        Literal["auto", "up", "right", "down", "left", "none", True, False] | DataQuery | None
    ]
    label_offset: NotRequired[float | DataQuery]
    line_anchor: NotRequired[Literal["top", "middle", "bottom"] | DataQuery]
    line_height: NotRequired[float | DataQuery]
    line_width: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["axisFy"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    mix_blend_mode: NotRequired[str | DataQuery]
    monospace: NotRequired[bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    text: NotRequired[ChannelValue]
    text_anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    text_overflow: NotRequired[
        Literal[
            "clip",
            "ellipsis",
            "clip-start",
            "clip-end",
            "ellipsis-start",
            "ellipsis-middle",
            "ellipsis-end",
        ]
        | DataQuery
        | None
    ]
    text_stroke: NotRequired[ChannelValueSpec | DataQuery]
    text_stroke_opacity: NotRequired[ChannelValueSpec]
    text_stroke_width: NotRequired[ChannelValueSpec]
    tick_format: NotRequired[str | DataQuery | None]
    tick_padding: NotRequired[float | DataQuery]
    tick_rotate: NotRequired[float | DataQuery]
    tick_size: NotRequired[float | DataQuery]
    tick_spacing: NotRequired[float | DataQuery]
    ticks: NotRequired[float | Interval | Sequence[Any] | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class AxisX(TypedDict, closed=True):
    anchor: NotRequired[Literal["top", "right", "bottom", "left"] | DataQuery]
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    color: NotRequired[ChannelValueSpec | DataQuery]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    font_family: NotRequired[str | DataQuery]
    font_size: NotRequired[ChannelValue | DataQuery]
    font_style: NotRequired[str | DataQuery]
    font_variant: NotRequired[str | DataQuery]
    font_weight: NotRequired[str | float | DataQuery]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    label: NotRequired[str | DataQuery | None]
    label_anchor: NotRequired[Literal["top", "right", "bottom", "left", "center"] | DataQuery]
    label_arrow: NotRequired[
        Literal["auto", "up", "right", "down", "left", "none", True, False] | DataQuery | None
    ]
    label_offset: NotRequired[float | DataQuery]
    line_anchor: NotRequired[Literal["top", "middle", "bottom"] | DataQuery]
    line_height: NotRequired[float | DataQuery]
    line_width: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["axisX"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    mix_blend_mode: NotRequired[str | DataQuery]
    monospace: NotRequired[bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    text: NotRequired[ChannelValue]
    text_anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    text_overflow: NotRequired[
        Literal[
            "clip",
            "ellipsis",
            "clip-start",
            "clip-end",
            "ellipsis-start",
            "ellipsis-middle",
            "ellipsis-end",
        ]
        | DataQuery
        | None
    ]
    text_stroke: NotRequired[ChannelValueSpec | DataQuery]
    text_stroke_opacity: NotRequired[ChannelValueSpec]
    text_stroke_width: NotRequired[ChannelValueSpec]
    tick_format: NotRequired[str | DataQuery | None]
    tick_padding: NotRequired[float | DataQuery]
    tick_rotate: NotRequired[float | DataQuery]
    tick_size: NotRequired[float | DataQuery]
    tick_spacing: NotRequired[float | DataQuery]
    ticks: NotRequired[float | Interval | Sequence[Any] | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class AxisY(TypedDict, closed=True):
    anchor: NotRequired[Literal["top", "right", "bottom", "left"] | DataQuery]
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    color: NotRequired[ChannelValueSpec | DataQuery]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    font_family: NotRequired[str | DataQuery]
    font_size: NotRequired[ChannelValue | DataQuery]
    font_style: NotRequired[str | DataQuery]
    font_variant: NotRequired[str | DataQuery]
    font_weight: NotRequired[str | float | DataQuery]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    label: NotRequired[str | DataQuery | None]
    label_anchor: NotRequired[Literal["top", "right", "bottom", "left", "center"] | DataQuery]
    label_arrow: NotRequired[
        Literal["auto", "up", "right", "down", "left", "none", True, False] | DataQuery | None
    ]
    label_offset: NotRequired[float | DataQuery]
    line_anchor: NotRequired[Literal["top", "middle", "bottom"] | DataQuery]
    line_height: NotRequired[float | DataQuery]
    line_width: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["axisY"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    mix_blend_mode: NotRequired[str | DataQuery]
    monospace: NotRequired[bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    text: NotRequired[ChannelValue]
    text_anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    text_overflow: NotRequired[
        Literal[
            "clip",
            "ellipsis",
            "clip-start",
            "clip-end",
            "ellipsis-start",
            "ellipsis-middle",
            "ellipsis-end",
        ]
        | DataQuery
        | None
    ]
    text_stroke: NotRequired[ChannelValueSpec | DataQuery]
    text_stroke_opacity: NotRequired[ChannelValueSpec]
    text_stroke_width: NotRequired[ChannelValueSpec]
    tick_format: NotRequired[str | DataQuery | None]
    tick_padding: NotRequired[float | DataQuery]
    tick_rotate: NotRequired[float | DataQuery]
    tick_size: NotRequired[float | DataQuery]
    tick_spacing: NotRequired[float | DataQuery]
    ticks: NotRequired[float | Interval | Sequence[Any] | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Cell(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["cell"]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rx: NotRequired[float | str | DataQuery]
    ry: NotRequired[float | str | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class CellX(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["cellX"]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rx: NotRequired[float | str | DataQuery]
    ry: NotRequired[float | str | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class CellY(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["cellY"]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rx: NotRequired[float | str | DataQuery]
    ry: NotRequired[float | str | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


ChannelValueIntervalSpec: TypeAlias = ChannelValueSpec | ChannelValueIntervalSpec1


class Circle(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["circle"]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    r: NotRequired[ChannelValueSpec | float | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | float | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    symbol: NotRequired[ChannelValueSpec | SymbolType | DataQuery]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Contour(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bandwidth: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    height: NotRequired[float | DataQuery]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    interpolate: NotRequired[GridInterpolate | DataQuery | None]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["contour"]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    pad: NotRequired[float | DataQuery]
    paint_order: NotRequired[str | DataQuery]
    pixel_size: NotRequired[float | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    thresholds: NotRequired[float | Sequence[float] | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    width: NotRequired[float | DataQuery]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class DelaunayLink(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    curve: NotRequired[Curve | DataQuery]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["delaunayLink"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class DelaunayMesh(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    curve: NotRequired[Curve | DataQuery]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["delaunayMesh"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class DenseLine(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bandwidth: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    height: NotRequired[float | DataQuery]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    image_rendering: NotRequired[str | DataQuery]
    interpolate: NotRequired[GridInterpolate | DataQuery | None]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["denseLine"]
    mix_blend_mode: NotRequired[str | DataQuery]
    normalize: NotRequired[bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    pad: NotRequired[float | DataQuery]
    paint_order: NotRequired[str | DataQuery]
    pixel_size: NotRequired[float | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    width: NotRequired[float | DataQuery]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Density(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bandwidth: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    font_family: NotRequired[str | DataQuery]
    font_size: NotRequired[ChannelValue | DataQuery]
    font_style: NotRequired[str | DataQuery]
    font_variant: NotRequired[str | DataQuery]
    font_weight: NotRequired[str | float | DataQuery]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    height: NotRequired[float | DataQuery]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    interpolate: NotRequired[GridInterpolate | DataQuery | None]
    line_height: NotRequired[float | DataQuery]
    line_width: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["density"]
    mix_blend_mode: NotRequired[str | DataQuery]
    monospace: NotRequired[bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    pad: NotRequired[float | DataQuery]
    paint_order: NotRequired[str | DataQuery]
    pixel_size: NotRequired[float | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    r: NotRequired[ChannelValueSpec | float | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | float | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    symbol: NotRequired[ChannelValueSpec | SymbolType | DataQuery]
    target: NotRequired[str | DataQuery]
    text_anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    text_overflow: NotRequired[
        Literal[
            "clip",
            "ellipsis",
            "clip-start",
            "clip-end",
            "ellipsis-start",
            "ellipsis-middle",
            "ellipsis-end",
        ]
        | DataQuery
        | None
    ]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    type: NotRequired[Literal["dot", "circle", "hexagon", "cell", "text"] | DataQuery]
    width: NotRequired[float | DataQuery]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class DensityXAreaX(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bandwidth: NotRequired[float | DataQuery]
    bins: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    curve: NotRequired[Curve | DataQuery]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["densityX"]
    mix_blend_mode: NotRequired[str | DataQuery]
    normalize: NotRequired[Literal["max", "sum", "none"] | bool | DataQuery]
    offset: NotRequired[StackOffset | DataQuery | None]
    opacity: NotRequired[ChannelValueSpec]
    order: NotRequired[StackOrder | DataQuery | None]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stack: NotRequired[bool | DataQuery]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    type: Literal["areaX"]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class DensityXLineX(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bandwidth: NotRequired[float | DataQuery]
    bins: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    curve: NotRequired[Curve | Literal["auto"] | DataQuery]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["densityX"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    mix_blend_mode: NotRequired[str | DataQuery]
    normalize: NotRequired[Literal["max", "sum", "none"] | bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    type: Literal["lineX"]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class DensityXDotX(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bandwidth: NotRequired[float | DataQuery]
    bins: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["densityX"]
    mix_blend_mode: NotRequired[str | DataQuery]
    normalize: NotRequired[Literal["max", "sum", "none"] | bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    r: NotRequired[ChannelValueSpec | float | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | float | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    symbol: NotRequired[ChannelValueSpec | SymbolType | DataQuery]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    type: Literal["dotX"]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class DensityXTextX(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bandwidth: NotRequired[float | DataQuery]
    bins: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    font_family: NotRequired[str | DataQuery]
    font_size: NotRequired[ChannelValue | DataQuery]
    font_style: NotRequired[str | DataQuery]
    font_variant: NotRequired[str | DataQuery]
    font_weight: NotRequired[str | float | DataQuery]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    line_anchor: NotRequired[Literal["top", "middle", "bottom"] | DataQuery]
    line_height: NotRequired[float | DataQuery]
    line_width: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["densityX"]
    mix_blend_mode: NotRequired[str | DataQuery]
    monospace: NotRequired[bool | DataQuery]
    normalize: NotRequired[Literal["max", "sum", "none"] | bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    text: NotRequired[ChannelValue]
    text_anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    text_overflow: NotRequired[
        Literal[
            "clip",
            "ellipsis",
            "clip-start",
            "clip-end",
            "ellipsis-start",
            "ellipsis-middle",
            "ellipsis-end",
        ]
        | DataQuery
        | None
    ]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    type: Literal["textX"]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


DensityX: TypeAlias = DensityXAreaX | DensityXLineX | DensityXDotX | DensityXTextX


class DensityY1(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bandwidth: NotRequired[float | DataQuery]
    bins: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    curve: NotRequired[Curve | DataQuery]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["densityY"]
    mix_blend_mode: NotRequired[str | DataQuery]
    normalize: NotRequired[Literal["max", "sum", "none"] | bool | DataQuery]
    offset: NotRequired[StackOffset | DataQuery | None]
    opacity: NotRequired[ChannelValueSpec]
    order: NotRequired[StackOrder | DataQuery | None]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stack: NotRequired[bool | DataQuery]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    type: NotRequired[Literal["areaY"]]
    x: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class DensityY2(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bandwidth: NotRequired[float | DataQuery]
    bins: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    curve: NotRequired[Curve | Literal["auto"] | DataQuery]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["densityY"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    mix_blend_mode: NotRequired[str | DataQuery]
    normalize: NotRequired[Literal["max", "sum", "none"] | bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    type: Literal["lineY"]
    x: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class DensityY3(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bandwidth: NotRequired[float | DataQuery]
    bins: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["densityY"]
    mix_blend_mode: NotRequired[str | DataQuery]
    normalize: NotRequired[Literal["max", "sum", "none"] | bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    r: NotRequired[ChannelValueSpec | float | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | float | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    symbol: NotRequired[ChannelValueSpec | SymbolType | DataQuery]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    type: Literal["dot", "dotY", "circle", "hexagon"]
    x: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class DensityY4(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bandwidth: NotRequired[float | DataQuery]
    bins: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    font_family: NotRequired[str | DataQuery]
    font_size: NotRequired[ChannelValue | DataQuery]
    font_style: NotRequired[str | DataQuery]
    font_variant: NotRequired[str | DataQuery]
    font_weight: NotRequired[str | float | DataQuery]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    line_anchor: NotRequired[Literal["top", "middle", "bottom"] | DataQuery]
    line_height: NotRequired[float | DataQuery]
    line_width: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["densityY"]
    mix_blend_mode: NotRequired[str | DataQuery]
    monospace: NotRequired[bool | DataQuery]
    normalize: NotRequired[Literal["max", "sum", "none"] | bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    text: NotRequired[ChannelValue]
    text_anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    text_overflow: NotRequired[
        Literal[
            "clip",
            "ellipsis",
            "clip-start",
            "clip-end",
            "ellipsis-start",
            "ellipsis-middle",
            "ellipsis-end",
        ]
        | DataQuery
        | None
    ]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    type: Literal["text", "textY"]
    x: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


DensityY: TypeAlias = DensityY1 | DensityY2 | DensityY3 | DensityY4


class Dot(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["dot"]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    r: NotRequired[ChannelValueSpec | float | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | float | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    symbol: NotRequired[ChannelValueSpec | SymbolType | DataQuery]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class DotX(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["dotX"]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    r: NotRequired[ChannelValueSpec | float | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | float | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    symbol: NotRequired[ChannelValueSpec | SymbolType | DataQuery]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueIntervalSpec]
    z: NotRequired[ChannelValue]


class DotY(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["dotY"]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    r: NotRequired[ChannelValueSpec | float | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | float | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    symbol: NotRequired[ChannelValueSpec | SymbolType | DataQuery]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueIntervalSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class ErrorBarX(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    ci: NotRequired[float | DataQuery]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["errorbarX"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: ChannelValueSpec
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class ErrorBarY(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    ci: NotRequired[float | DataQuery]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["errorbarY"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: ChannelValueSpec
    z: NotRequired[ChannelValue]


class Frame(TypedDict, closed=True):
    anchor: NotRequired[Literal["top", "right", "bottom", "left"] | DataQuery | None]
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["frame"]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rx: NotRequired[float | str | DataQuery]
    ry: NotRequired[float | str | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]


class Geo(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    geometry: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["geo"]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    r: NotRequired[ChannelValueSpec | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]


class Graticule(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["graticule"]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]


class GridFx(TypedDict, closed=True):
    anchor: NotRequired[Literal["top", "right", "bottom", "left"] | DataQuery]
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    color: NotRequired[ChannelValueSpec | DataQuery]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["gridFx"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tick_spacing: NotRequired[float | DataQuery]
    ticks: NotRequired[float | Interval | Sequence[Any] | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueIntervalSpec]
    y1: NotRequired[ChannelValueSpec]
    y2: NotRequired[ChannelValueSpec]


class GridFy(TypedDict, closed=True):
    anchor: NotRequired[Literal["top", "right", "bottom", "left"] | DataQuery]
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    color: NotRequired[ChannelValueSpec | DataQuery]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["gridFy"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tick_spacing: NotRequired[float | DataQuery]
    ticks: NotRequired[float | Interval | Sequence[Any] | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueIntervalSpec]
    x1: NotRequired[ChannelValueSpec]
    x2: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class GridX(TypedDict, closed=True):
    anchor: NotRequired[Literal["top", "right", "bottom", "left"] | DataQuery]
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    color: NotRequired[ChannelValueSpec | DataQuery]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["gridX"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tick_spacing: NotRequired[float | DataQuery]
    ticks: NotRequired[float | Interval | Sequence[Any] | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueIntervalSpec]
    y1: NotRequired[ChannelValueSpec]
    y2: NotRequired[ChannelValueSpec]


class GridY(TypedDict, closed=True):
    anchor: NotRequired[Literal["top", "right", "bottom", "left"] | DataQuery]
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    color: NotRequired[ChannelValueSpec | DataQuery]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["gridY"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tick_spacing: NotRequired[float | DataQuery]
    ticks: NotRequired[float | Interval | Sequence[Any] | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueIntervalSpec]
    x1: NotRequired[ChannelValueSpec]
    x2: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class Heatmap(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bandwidth: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    height: NotRequired[float | DataQuery]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    image_rendering: NotRequired[str | DataQuery]
    interpolate: NotRequired[GridInterpolate | DataQuery | None]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["heatmap"]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    pad: NotRequired[float | DataQuery]
    paint_order: NotRequired[str | DataQuery]
    pixel_size: NotRequired[float | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    width: NotRequired[float | DataQuery]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class Hexagon(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["hexagon"]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    r: NotRequired[ChannelValueSpec | float | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | float | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    symbol: NotRequired[ChannelValueSpec | SymbolType | DataQuery]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Hexbin(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bin_width: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    font_family: NotRequired[str | DataQuery]
    font_size: NotRequired[ChannelValue | DataQuery]
    font_style: NotRequired[str | DataQuery]
    font_variant: NotRequired[str | DataQuery]
    font_weight: NotRequired[str | float | DataQuery]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    line_height: NotRequired[float | DataQuery]
    line_width: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["hexbin"]
    mix_blend_mode: NotRequired[str | DataQuery]
    monospace: NotRequired[bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    r: NotRequired[ChannelValueSpec | float | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | float | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    symbol: NotRequired[ChannelValueSpec | SymbolType | DataQuery]
    target: NotRequired[str | DataQuery]
    text_anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    text_overflow: NotRequired[
        Literal[
            "clip",
            "ellipsis",
            "clip-start",
            "clip-end",
            "ellipsis-start",
            "ellipsis-middle",
            "ellipsis-end",
        ]
        | DataQuery
        | None
    ]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    type: NotRequired[Literal["dot", "circle", "hexagon", "text"] | DataQuery]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Hexgrid(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bin_width: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["hexgrid"]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]


class Hull(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    curve: NotRequired[Curve | DataQuery]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["hull"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Image(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    cross_origin: NotRequired[str | DataQuery]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    height: NotRequired[ChannelValue | DataQuery]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    image_rendering: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["image"]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    preserve_aspect_ratio: NotRequired[str | DataQuery]
    r: NotRequired[ChannelValue | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    src: NotRequired[ChannelValue | DataQuery]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    width: NotRequired[ChannelValue | DataQuery]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class Line(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    curve: NotRequired[Curve | Literal["auto"] | DataQuery]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["line"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class LineX(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    curve: NotRequired[Curve | Literal["auto"] | DataQuery]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["lineX"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class LineY(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    curve: NotRequired[Curve | Literal["auto"] | DataQuery]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["lineY"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Link(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    curve: NotRequired[Curve | Literal["auto"] | DataQuery]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["link"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tension: NotRequired[float | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    x1: NotRequired[ChannelValueSpec]
    x2: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    y1: NotRequired[ChannelValueSpec]
    y2: NotRequired[ChannelValueSpec]


class Raster(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bandwidth: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    height: NotRequired[float | DataQuery]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    image_rendering: NotRequired[str | DataQuery]
    interpolate: NotRequired[GridInterpolate | DataQuery | None]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["raster"]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    pad: NotRequired[float | DataQuery]
    paint_order: NotRequired[str | DataQuery]
    pixel_size: NotRequired[float | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    width: NotRequired[float | DataQuery]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class RasterTile(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    bandwidth: NotRequired[float | DataQuery]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    height: NotRequired[float | DataQuery]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    image_rendering: NotRequired[str | DataQuery]
    interpolate: NotRequired[GridInterpolate | DataQuery | None]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["rasterTile"]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    origin: NotRequired[Sequence[float] | DataQuery]
    pad: NotRequired[float | DataQuery]
    paint_order: NotRequired[str | DataQuery]
    pixel_size: NotRequired[float | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    width: NotRequired[float | DataQuery]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class Rect(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["rect"]
    mix_blend_mode: NotRequired[str | DataQuery]
    offset: NotRequired[StackOffset | DataQuery | None]
    opacity: NotRequired[ChannelValueSpec]
    order: NotRequired[StackOrder | DataQuery | None]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rx: NotRequired[float | str | DataQuery]
    ry: NotRequired[float | str | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueIntervalSpec]
    x1: NotRequired[ChannelValueSpec]
    x2: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueIntervalSpec]
    y1: NotRequired[ChannelValueSpec]
    y2: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class RectX(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["rectX"]
    mix_blend_mode: NotRequired[str | DataQuery]
    offset: NotRequired[StackOffset | DataQuery | None]
    opacity: NotRequired[ChannelValueSpec]
    order: NotRequired[StackOrder | DataQuery | None]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rx: NotRequired[float | str | DataQuery]
    ry: NotRequired[float | str | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    x1: NotRequired[ChannelValueSpec]
    x2: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueIntervalSpec]
    y1: NotRequired[ChannelValueSpec]
    y2: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class RectY(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["rectY"]
    mix_blend_mode: NotRequired[str | DataQuery]
    offset: NotRequired[StackOffset | DataQuery | None]
    opacity: NotRequired[ChannelValueSpec]
    order: NotRequired[StackOrder | DataQuery | None]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rx: NotRequired[float | str | DataQuery]
    ry: NotRequired[float | str | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueIntervalSpec]
    x1: NotRequired[ChannelValueSpec]
    x2: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    y1: NotRequired[ChannelValueSpec]
    y2: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class RegressionY(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    ci: NotRequired[float | DataQuery]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["regressionY"]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    precision: NotRequired[float | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class RuleX(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: NotRequired[PlotMarkData]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["ruleX"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueIntervalSpec]
    y1: NotRequired[ChannelValueSpec]
    y2: NotRequired[ChannelValueSpec]


class RuleY(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: NotRequired[PlotMarkData]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["ruleY"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueIntervalSpec]
    y1: NotRequired[ChannelValueSpec]
    y2: NotRequired[ChannelValueSpec]


class Spec18(TypedDict, closed=True):
    anchor: NotRequired[Literal["top", "right", "bottom", "left"] | DataQuery]
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    color: NotRequired[ChannelValueSpec | DataQuery]
    config: NotRequired[Config]
    data: NotRequired[Data]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["gridX"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tick_spacing: NotRequired[float | DataQuery]
    ticks: NotRequired[float | Interval | Sequence[Any] | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueIntervalSpec]
    y1: NotRequired[ChannelValueSpec]
    y2: NotRequired[ChannelValueSpec]


class Spec19(TypedDict, closed=True):
    anchor: NotRequired[Literal["top", "right", "bottom", "left"] | DataQuery]
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    color: NotRequired[ChannelValueSpec | DataQuery]
    config: NotRequired[Config]
    data: NotRequired[Data]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["gridY"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tick_spacing: NotRequired[float | DataQuery]
    ticks: NotRequired[float | Interval | Sequence[Any] | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueIntervalSpec]
    x1: NotRequired[ChannelValueSpec]
    x2: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class Spec20(TypedDict, closed=True):
    anchor: NotRequired[Literal["top", "right", "bottom", "left"] | DataQuery]
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    color: NotRequired[ChannelValueSpec | DataQuery]
    config: NotRequired[Config]
    data: NotRequired[Data]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["gridFx"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tick_spacing: NotRequired[float | DataQuery]
    ticks: NotRequired[float | Interval | Sequence[Any] | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueIntervalSpec]
    y1: NotRequired[ChannelValueSpec]
    y2: NotRequired[ChannelValueSpec]


class Spec21(TypedDict, closed=True):
    anchor: NotRequired[Literal["top", "right", "bottom", "left"] | DataQuery]
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    color: NotRequired[ChannelValueSpec | DataQuery]
    config: NotRequired[Config]
    data: NotRequired[Data]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["gridFy"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tick_spacing: NotRequired[float | DataQuery]
    ticks: NotRequired[float | Interval | Sequence[Any] | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueIntervalSpec]
    x1: NotRequired[ChannelValueSpec]
    x2: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]


class Spec22(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["barX"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    offset: NotRequired[StackOffset | DataQuery | None]
    opacity: NotRequired[ChannelValueSpec]
    order: NotRequired[StackOrder | DataQuery | None]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rx: NotRequired[float | str | DataQuery]
    ry: NotRequired[float | str | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueIntervalSpec]
    x1: NotRequired[ChannelValueSpec]
    x2: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec23(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["barY"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    offset: NotRequired[StackOffset | DataQuery | None]
    opacity: NotRequired[ChannelValueSpec]
    order: NotRequired[StackOrder | DataQuery | None]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rx: NotRequired[float | str | DataQuery]
    ry: NotRequired[float | str | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueIntervalSpec]
    y1: NotRequired[ChannelValueSpec]
    y2: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec44(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["dotX"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    r: NotRequired[ChannelValueSpec | float | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | float | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    symbol: NotRequired[ChannelValueSpec | SymbolType | DataQuery]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueIntervalSpec]
    z: NotRequired[ChannelValue]


class Spec45(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["dotY"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    r: NotRequired[ChannelValueSpec | float | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | float | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    symbol: NotRequired[ChannelValueSpec | SymbolType | DataQuery]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueIntervalSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec64(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["rect"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    offset: NotRequired[StackOffset | DataQuery | None]
    opacity: NotRequired[ChannelValueSpec]
    order: NotRequired[StackOrder | DataQuery | None]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rx: NotRequired[float | str | DataQuery]
    ry: NotRequired[float | str | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueIntervalSpec]
    x1: NotRequired[ChannelValueSpec]
    x2: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueIntervalSpec]
    y1: NotRequired[ChannelValueSpec]
    y2: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec65(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["rectX"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    offset: NotRequired[StackOffset | DataQuery | None]
    opacity: NotRequired[ChannelValueSpec]
    order: NotRequired[StackOrder | DataQuery | None]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rx: NotRequired[float | str | DataQuery]
    ry: NotRequired[float | str | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    x1: NotRequired[ChannelValueSpec]
    x2: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueIntervalSpec]
    y1: NotRequired[ChannelValueSpec]
    y2: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec66(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["rectY"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    offset: NotRequired[StackOffset | DataQuery | None]
    opacity: NotRequired[ChannelValueSpec]
    order: NotRequired[StackOrder | DataQuery | None]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rx: NotRequired[float | str | DataQuery]
    ry: NotRequired[float | str | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueIntervalSpec]
    x1: NotRequired[ChannelValueSpec]
    x2: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    y1: NotRequired[ChannelValueSpec]
    y2: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec68(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: NotRequired[Data]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["ruleX"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueIntervalSpec]
    y1: NotRequired[ChannelValueSpec]
    y2: NotRequired[ChannelValueSpec]


class Spec69(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: NotRequired[Data]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["ruleY"]
    marker: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_end: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_mid: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    marker_start: NotRequired[MarkerName | Literal["none"] | bool | DataQuery | None]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueIntervalSpec]
    y1: NotRequired[ChannelValueSpec]
    y2: NotRequired[ChannelValueSpec]


class Spec71(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: NotRequired[Data]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    font_family: NotRequired[str | DataQuery]
    font_size: NotRequired[ChannelValue | DataQuery]
    font_style: NotRequired[str | DataQuery]
    font_variant: NotRequired[str | DataQuery]
    font_weight: NotRequired[str | float | DataQuery]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    line_anchor: NotRequired[Literal["top", "middle", "bottom"] | DataQuery]
    line_height: NotRequired[float | DataQuery]
    line_width: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["textX"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    monospace: NotRequired[bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    text: NotRequired[ChannelValue]
    text_anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    text_overflow: NotRequired[
        Literal[
            "clip",
            "ellipsis",
            "clip-start",
            "clip-end",
            "ellipsis-start",
            "ellipsis-middle",
            "ellipsis-end",
        ]
        | DataQuery
        | None
    ]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueIntervalSpec]
    z: NotRequired[ChannelValue]


class Spec72(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: NotRequired[Data]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    font_family: NotRequired[str | DataQuery]
    font_size: NotRequired[ChannelValue | DataQuery]
    font_style: NotRequired[str | DataQuery]
    font_variant: NotRequired[str | DataQuery]
    font_weight: NotRequired[str | float | DataQuery]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    interval: NotRequired[Interval]
    line_anchor: NotRequired[Literal["top", "middle", "bottom"] | DataQuery]
    line_height: NotRequired[float | DataQuery]
    line_width: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["textY"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    monospace: NotRequired[bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    text: NotRequired[ChannelValue]
    text_anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    text_overflow: NotRequired[
        Literal[
            "clip",
            "ellipsis",
            "clip-start",
            "clip-end",
            "ellipsis-start",
            "ellipsis-middle",
            "ellipsis-end",
        ]
        | DataQuery
        | None
    ]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueIntervalSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec79(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    gap: NotRequired[float | DataQuery]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["waffleX"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    multiple: NotRequired[float | DataQuery]
    offset: NotRequired[StackOffset | DataQuery | None]
    opacity: NotRequired[ChannelValueSpec]
    order: NotRequired[StackOrder | DataQuery | None]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    round: NotRequired[bool | DataQuery]
    rx: NotRequired[float | str | DataQuery]
    ry: NotRequired[float | str | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    unit: NotRequired[float | DataQuery]
    x: NotRequired[ChannelValueIntervalSpec]
    x1: NotRequired[ChannelValueSpec]
    x2: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class Spec80(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    config: NotRequired[Config]
    data: Data
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    gap: NotRequired[float | DataQuery]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["waffleY"]
    meta: NotRequired[Meta]
    mix_blend_mode: NotRequired[str | DataQuery]
    multiple: NotRequired[float | DataQuery]
    offset: NotRequired[StackOffset | DataQuery | None]
    opacity: NotRequired[ChannelValueSpec]
    order: NotRequired[StackOrder | DataQuery | None]
    paint_order: NotRequired[str | DataQuery]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    round: NotRequired[bool | DataQuery]
    rx: NotRequired[float | str | DataQuery]
    ry: NotRequired[float | str | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    unit: NotRequired[float | DataQuery]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueIntervalSpec]
    y1: NotRequired[ChannelValueSpec]
    y2: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class TextX(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: NotRequired[PlotMarkData]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    font_family: NotRequired[str | DataQuery]
    font_size: NotRequired[ChannelValue | DataQuery]
    font_style: NotRequired[str | DataQuery]
    font_variant: NotRequired[str | DataQuery]
    font_weight: NotRequired[str | float | DataQuery]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    line_anchor: NotRequired[Literal["top", "middle", "bottom"] | DataQuery]
    line_height: NotRequired[float | DataQuery]
    line_width: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["textX"]
    mix_blend_mode: NotRequired[str | DataQuery]
    monospace: NotRequired[bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    text: NotRequired[ChannelValue]
    text_anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    text_overflow: NotRequired[
        Literal[
            "clip",
            "ellipsis",
            "clip-start",
            "clip-end",
            "ellipsis-start",
            "ellipsis-middle",
            "ellipsis-end",
        ]
        | DataQuery
        | None
    ]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueIntervalSpec]
    z: NotRequired[ChannelValue]


class TextY(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: NotRequired[PlotMarkData]
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    font_family: NotRequired[str | DataQuery]
    font_size: NotRequired[ChannelValue | DataQuery]
    font_style: NotRequired[str | DataQuery]
    font_variant: NotRequired[str | DataQuery]
    font_weight: NotRequired[str | float | DataQuery]
    frame_anchor: NotRequired[FrameAnchor | DataQuery]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    interval: NotRequired[Interval]
    line_anchor: NotRequired[Literal["top", "middle", "bottom"] | DataQuery]
    line_height: NotRequired[float | DataQuery]
    line_width: NotRequired[float | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["textY"]
    mix_blend_mode: NotRequired[str | DataQuery]
    monospace: NotRequired[bool | DataQuery]
    opacity: NotRequired[ChannelValueSpec]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rotate: NotRequired[ChannelValue | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    text: NotRequired[ChannelValue]
    text_anchor: NotRequired[Literal["start", "middle", "end"] | DataQuery]
    text_overflow: NotRequired[
        Literal[
            "clip",
            "ellipsis",
            "clip-start",
            "clip-end",
            "ellipsis-start",
            "ellipsis-middle",
            "ellipsis-end",
        ]
        | DataQuery
        | None
    ]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueIntervalSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class WaffleX(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    gap: NotRequired[float | DataQuery]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["waffleX"]
    mix_blend_mode: NotRequired[str | DataQuery]
    multiple: NotRequired[float | DataQuery]
    offset: NotRequired[StackOffset | DataQuery | None]
    opacity: NotRequired[ChannelValueSpec]
    order: NotRequired[StackOrder | DataQuery | None]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    round: NotRequired[bool | DataQuery]
    rx: NotRequired[float | str | DataQuery]
    ry: NotRequired[float | str | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    unit: NotRequired[float | DataQuery]
    x: NotRequired[ChannelValueIntervalSpec]
    x1: NotRequired[ChannelValueSpec]
    x2: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class WaffleY(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    gap: NotRequired[float | DataQuery]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["waffleY"]
    mix_blend_mode: NotRequired[str | DataQuery]
    multiple: NotRequired[float | DataQuery]
    offset: NotRequired[StackOffset | DataQuery | None]
    opacity: NotRequired[ChannelValueSpec]
    order: NotRequired[StackOrder | DataQuery | None]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    round: NotRequired[bool | DataQuery]
    rx: NotRequired[float | str | DataQuery]
    ry: NotRequired[float | str | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    unit: NotRequired[float | DataQuery]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueIntervalSpec]
    y1: NotRequired[ChannelValueSpec]
    y2: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class BarX(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["barX"]
    mix_blend_mode: NotRequired[str | DataQuery]
    offset: NotRequired[StackOffset | DataQuery | None]
    opacity: NotRequired[ChannelValueSpec]
    order: NotRequired[StackOrder | DataQuery | None]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rx: NotRequired[float | str | DataQuery]
    ry: NotRequired[float | str | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueIntervalSpec]
    x1: NotRequired[ChannelValueSpec]
    x2: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


class BarY(TypedDict, closed=True):
    aria_description: NotRequired[str | DataQuery]
    aria_hidden: NotRequired[str | DataQuery]
    aria_label: NotRequired[ChannelValue]
    channels: NotRequired[Mapping[str, str]]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    data: PlotMarkData
    dx: NotRequired[float | DataQuery]
    dy: NotRequired[float | DataQuery]
    facet: NotRequired[Literal["auto", "include", "exclude", "super"] | bool | DataQuery | None]
    facet_anchor: NotRequired[
        Literal[
            "top",
            "right",
            "bottom",
            "left",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "top-empty",
            "right-empty",
            "bottom-empty",
            "left-empty",
            "empty",
        ]
        | DataQuery
        | None
    ]
    fill: NotRequired[ChannelValueSpec | DataQuery]
    fill_opacity: NotRequired[ChannelValueSpec | DataQuery]
    filter: NotRequired[ChannelValue]
    fx: NotRequired[ChannelValue]
    fy: NotRequired[ChannelValue]
    href: NotRequired[ChannelValue]
    image_filter: NotRequired[str | DataQuery]
    inset: NotRequired[float | DataQuery]
    inset_bottom: NotRequired[float | DataQuery]
    inset_left: NotRequired[float | DataQuery]
    inset_right: NotRequired[float | DataQuery]
    inset_top: NotRequired[float | DataQuery]
    interval: NotRequired[Interval | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    mark: Literal["barY"]
    mix_blend_mode: NotRequired[str | DataQuery]
    offset: NotRequired[StackOffset | DataQuery | None]
    opacity: NotRequired[ChannelValueSpec]
    order: NotRequired[StackOrder | DataQuery | None]
    paint_order: NotRequired[str | DataQuery]
    pointer_events: NotRequired[str | DataQuery]
    reverse: NotRequired[bool | DataQuery]
    rx: NotRequired[float | str | DataQuery]
    ry: NotRequired[float | str | DataQuery]
    select: NotRequired[SelectFilter]
    shape_rendering: NotRequired[str | DataQuery]
    sort: NotRequired[SortOrder | ChannelDomainSort]
    stroke: NotRequired[ChannelValueSpec | DataQuery]
    stroke_dasharray: NotRequired[str | float | DataQuery]
    stroke_dashoffset: NotRequired[str | float | DataQuery]
    stroke_linecap: NotRequired[str | DataQuery]
    stroke_linejoin: NotRequired[str | DataQuery]
    stroke_miterlimit: NotRequired[float | DataQuery]
    stroke_opacity: NotRequired[ChannelValueSpec]
    stroke_width: NotRequired[ChannelValueSpec]
    target: NotRequired[str | DataQuery]
    tip: NotRequired[bool | TipPointer | Tip | DataQuery]
    title: NotRequired[ChannelValue]
    x: NotRequired[ChannelValueSpec]
    y: NotRequired[ChannelValueIntervalSpec]
    y1: NotRequired[ChannelValueSpec]
    y2: NotRequired[ChannelValueSpec]
    z: NotRequired[ChannelValue]


PlotMark: TypeAlias = (
    Area
    | AreaX
    | AreaY
    | Arrow
    | AxisX
    | AxisY
    | AxisFx
    | AxisFy
    | GridX
    | GridY
    | GridFx
    | GridFy
    | BarX
    | BarY
    | Cell
    | CellX
    | CellY
    | Contour
    | DelaunayLink
    | DelaunayMesh
    | Hull
    | Voronoi
    | VoronoiMesh
    | DenseLine
    | Density
    | DensityX
    | DensityY
    | Dot
    | DotX
    | DotY
    | Circle
    | Hexagon
    | ErrorBarX
    | ErrorBarY
    | Frame
    | Geo
    | Graticule
    | Sphere
    | Hexbin
    | Hexgrid
    | Image
    | Line
    | LineX
    | LineY
    | Link
    | Raster
    | Heatmap
    | RasterTile
    | Rect
    | RectX
    | RectY
    | RegressionY
    | RuleX
    | RuleY
    | Text
    | TextX
    | TextY
    | TickX
    | TickY
    | Vector
    | VectorX
    | VectorY
    | Spike
    | WaffleX
    | WaffleY
)


class Spec9(TypedDict, closed=True):
    align: NotRequired[float | DataQuery]
    aria_description: NotRequired[str | None]
    aria_label: NotRequired[str | None]
    aspect_ratio: NotRequired[float | bool | DataQuery | None]
    axis: NotRequired[Literal["top", "right", "bottom", "left", "both"] | bool | DataQuery | None]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    color_base: NotRequired[float | DataQuery]
    color_clamp: NotRequired[bool | DataQuery]
    color_constant: NotRequired[float | DataQuery]
    color_domain: NotRequired[Sequence[Any] | Fixed | DataQuery]
    color_exponent: NotRequired[float | DataQuery]
    color_interpolate: NotRequired[Interpolate | DataQuery]
    color_label: NotRequired[str | DataQuery | None]
    color_n: NotRequired[float | DataQuery]
    color_nice: NotRequired[bool | float | Interval | DataQuery]
    color_percent: NotRequired[bool | DataQuery]
    color_pivot: NotRequired[Any | DataQuery]
    color_range: NotRequired[Sequence[Any] | Fixed | DataQuery]
    color_reverse: NotRequired[bool | DataQuery]
    color_scale: NotRequired[ColorScaleType | DataQuery | None]
    color_scheme: NotRequired[ColorScheme | DataQuery]
    color_symmetric: NotRequired[bool | DataQuery]
    color_tick_format: NotRequired[str | DataQuery | None]
    color_zero: NotRequired[bool | DataQuery]
    config: NotRequired[Config]
    data: NotRequired[Data]
    facet_grid: NotRequired[bool | str | Interval | Sequence[Any] | DataQuery]
    facet_label: NotRequired[str | DataQuery | None]
    facet_margin: NotRequired[float | DataQuery]
    facet_margin_bottom: NotRequired[float | DataQuery]
    facet_margin_left: NotRequired[float | DataQuery]
    facet_margin_right: NotRequired[float | DataQuery]
    facet_margin_top: NotRequired[float | DataQuery]
    fx_align: NotRequired[float | DataQuery]
    fx_aria_description: NotRequired[str | DataQuery]
    fx_aria_label: NotRequired[str | DataQuery]
    fx_axis: NotRequired[Literal["top", "bottom", "both"] | bool | DataQuery | None]
    fx_domain: NotRequired[Sequence[Any] | Fixed | DataQuery]
    fx_font_variant: NotRequired[str | DataQuery]
    fx_grid: NotRequired[bool | str | Interval | Sequence[Any] | DataQuery]
    fx_inset: NotRequired[float | DataQuery]
    fx_inset_left: NotRequired[float | DataQuery]
    fx_inset_right: NotRequired[float | DataQuery]
    fx_label: NotRequired[str | DataQuery | None]
    fx_label_anchor: NotRequired[Literal["top", "right", "bottom", "left", "center"] | DataQuery]
    fx_label_offset: NotRequired[float | DataQuery]
    fx_line: NotRequired[bool | DataQuery]
    fx_padding: NotRequired[float | DataQuery]
    fx_padding_inner: NotRequired[float | DataQuery]
    fx_padding_outer: NotRequired[float | DataQuery]
    fx_range: NotRequired[Sequence[Any] | Fixed | DataQuery]
    fx_reverse: NotRequired[bool | DataQuery]
    fx_round: NotRequired[bool | DataQuery]
    fx_tick_format: NotRequired[str | DataQuery | None]
    fx_tick_padding: NotRequired[float | DataQuery]
    fx_tick_rotate: NotRequired[float | DataQuery]
    fx_tick_size: NotRequired[float | DataQuery]
    fx_tick_spacing: NotRequired[float | DataQuery]
    fx_ticks: NotRequired[float | Interval | Sequence[Any] | DataQuery]
    fy_align: NotRequired[float | DataQuery]
    fy_aria_description: NotRequired[str | DataQuery]
    fy_aria_label: NotRequired[str | DataQuery]
    fy_axis: NotRequired[Literal["left", "right", "both"] | bool | DataQuery | None]
    fy_domain: NotRequired[Sequence[Any] | Fixed | DataQuery]
    fy_font_variant: NotRequired[str | DataQuery]
    fy_grid: NotRequired[bool | str | Interval | Sequence[Any] | DataQuery]
    fy_inset: NotRequired[float | DataQuery]
    fy_inset_bottom: NotRequired[float | DataQuery]
    fy_inset_top: NotRequired[float | DataQuery]
    fy_label: NotRequired[str | DataQuery | None]
    fy_label_anchor: NotRequired[Literal["top", "right", "bottom", "left", "center"] | DataQuery]
    fy_label_offset: NotRequired[float | DataQuery]
    fy_line: NotRequired[bool | DataQuery]
    fy_padding: NotRequired[float | DataQuery]
    fy_padding_inner: NotRequired[float | DataQuery]
    fy_padding_outer: NotRequired[float | DataQuery]
    fy_range: NotRequired[Sequence[Any] | Fixed | DataQuery]
    fy_reverse: NotRequired[bool | DataQuery]
    fy_round: NotRequired[bool | DataQuery]
    fy_tick_format: NotRequired[str | DataQuery | None]
    fy_tick_padding: NotRequired[float | DataQuery]
    fy_tick_rotate: NotRequired[float | DataQuery]
    fy_tick_size: NotRequired[float | DataQuery]
    fy_tick_spacing: NotRequired[float | DataQuery]
    fy_ticks: NotRequired[float | Interval | Sequence[Any] | DataQuery]
    grid: NotRequired[bool | str | DataQuery]
    height: NotRequired[float | DataQuery]
    inset: NotRequired[float | DataQuery]
    length_base: NotRequired[float | DataQuery]
    length_clamp: NotRequired[Any]
    length_constant: NotRequired[float | DataQuery]
    length_domain: NotRequired[Sequence[Any] | Fixed | DataQuery]
    length_exponent: NotRequired[float | DataQuery]
    length_nice: NotRequired[bool | float | Interval | DataQuery]
    length_percent: NotRequired[bool | DataQuery]
    length_range: NotRequired[Sequence[Any] | Fixed | DataQuery]
    length_scale: NotRequired[ContinuousScaleType | DataQuery | None]
    length_zero: NotRequired[bool | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    margins: NotRequired[Margins]
    meta: NotRequired[Meta]
    name: NotRequired[str]
    opacity_base: NotRequired[float | DataQuery]
    opacity_clamp: NotRequired[bool | DataQuery]
    opacity_constant: NotRequired[float | DataQuery]
    opacity_domain: NotRequired[Sequence[Any] | Fixed | DataQuery]
    opacity_exponent: NotRequired[float | DataQuery]
    opacity_label: NotRequired[str | DataQuery | None]
    opacity_nice: NotRequired[bool | float | Interval | DataQuery]
    opacity_percent: NotRequired[bool | DataQuery]
    opacity_range: NotRequired[Sequence[Any] | Fixed | DataQuery]
    opacity_reverse: NotRequired[bool | DataQuery]
    opacity_scale: NotRequired[ContinuousScaleType | DataQuery | None]
    opacity_tick_format: NotRequired[str | DataQuery | None]
    opacity_zero: NotRequired[bool | DataQuery]
    padding: NotRequired[float | DataQuery]
    params: NotRequired[Params]
    plot: Sequence[PlotMark | PlotInteractor | PlotLegend]
    plot_defaults: NotRequired[PlotAttributes]
    projection_clip: NotRequired[bool | float | Literal["frame"] | DataQuery | None]
    projection_domain: NotRequired[Mapping[str, Any] | DataQuery]
    projection_inset: NotRequired[float | DataQuery]
    projection_inset_bottom: NotRequired[float | DataQuery]
    projection_inset_left: NotRequired[float | DataQuery]
    projection_inset_right: NotRequired[float | DataQuery]
    projection_inset_top: NotRequired[float | DataQuery]
    projection_parallels: NotRequired[tuple[Y1, Y1] | DataQuery]
    projection_precision: NotRequired[float | DataQuery]
    projection_rotate: NotRequired[tuple[Y1, Y1, Y1] | DataQuery]
    projection_type: NotRequired[ProjectionName | DataQuery | None]
    r_base: NotRequired[float | DataQuery]
    r_clamp: NotRequired[Any]
    r_constant: NotRequired[float | DataQuery]
    r_domain: NotRequired[Sequence[Any] | Fixed | DataQuery]
    r_exponent: NotRequired[float | DataQuery]
    r_label: NotRequired[str | DataQuery | None]
    r_nice: NotRequired[bool | float | Interval | DataQuery]
    r_percent: NotRequired[bool | DataQuery]
    r_range: NotRequired[Sequence[Any] | Fixed | DataQuery]
    r_scale: NotRequired[ContinuousScaleType | DataQuery | None]
    r_zero: NotRequired[bool | DataQuery]
    style: NotRequired[str | CSSStyles | DataQuery | None]
    symbol_domain: NotRequired[Sequence[Any] | Fixed | DataQuery]
    symbol_range: NotRequired[Sequence[Any] | Fixed | DataQuery]
    symbol_scale: NotRequired[DiscreteScaleType | DataQuery | None]
    width: NotRequired[float | DataQuery]
    x_align: NotRequired[float | DataQuery]
    x_aria_description: NotRequired[str | DataQuery]
    x_aria_label: NotRequired[str | DataQuery]
    x_axis: NotRequired[Literal["top", "bottom", "both"] | bool | DataQuery | None]
    x_base: NotRequired[float | DataQuery]
    x_clamp: NotRequired[bool | DataQuery]
    x_constant: NotRequired[float | DataQuery]
    x_domain: NotRequired[Sequence[Any] | Fixed | DataQuery]
    x_exponent: NotRequired[float | DataQuery]
    x_font_variant: NotRequired[str | DataQuery]
    x_grid: NotRequired[bool | str | Interval | Sequence[Any] | DataQuery]
    x_inset: NotRequired[float | DataQuery]
    x_inset_left: NotRequired[float | DataQuery]
    x_inset_right: NotRequired[float | DataQuery]
    x_label: NotRequired[str | DataQuery | None]
    x_label_anchor: NotRequired[Literal["top", "right", "bottom", "left", "center"] | DataQuery]
    x_label_arrow: NotRequired[LabelArrow | DataQuery]
    x_label_offset: NotRequired[float | DataQuery]
    x_line: NotRequired[bool | DataQuery]
    x_nice: NotRequired[bool | float | Interval | DataQuery]
    x_padding: NotRequired[float | DataQuery]
    x_padding_inner: NotRequired[float | DataQuery]
    x_padding_outer: NotRequired[float | DataQuery]
    x_percent: NotRequired[bool | DataQuery]
    x_range: NotRequired[Sequence[Any] | Fixed | DataQuery]
    x_reverse: NotRequired[bool | DataQuery]
    x_round: NotRequired[bool | DataQuery]
    x_scale: NotRequired[PositionScaleType | DataQuery | None]
    x_tick_format: NotRequired[str | DataQuery | None]
    x_tick_padding: NotRequired[float | DataQuery]
    x_tick_rotate: NotRequired[float | DataQuery]
    x_tick_size: NotRequired[float | DataQuery]
    x_tick_spacing: NotRequired[float | DataQuery]
    x_ticks: NotRequired[float | Interval | Sequence[Any] | DataQuery]
    x_zero: NotRequired[bool | DataQuery]
    xy_domain: NotRequired[Sequence[Any] | Fixed | DataQuery]
    y_align: NotRequired[float | DataQuery]
    y_aria_description: NotRequired[str | DataQuery]
    y_aria_label: NotRequired[str | DataQuery]
    y_axis: NotRequired[Literal["left", "right", "both"] | bool | DataQuery | None]
    y_base: NotRequired[float | DataQuery]
    y_clamp: NotRequired[bool | DataQuery]
    y_constant: NotRequired[float | DataQuery]
    y_domain: NotRequired[Sequence[Any] | Fixed | DataQuery]
    y_exponent: NotRequired[float | DataQuery]
    y_font_variant: NotRequired[str | DataQuery]
    y_grid: NotRequired[bool | str | Interval | Sequence[Any] | DataQuery]
    y_inset: NotRequired[float | DataQuery]
    y_inset_bottom: NotRequired[float | DataQuery]
    y_inset_top: NotRequired[float | DataQuery]
    y_label: NotRequired[str | DataQuery | None]
    y_label_anchor: NotRequired[Literal["top", "right", "bottom", "left", "center"] | DataQuery]
    y_label_arrow: NotRequired[LabelArrow | DataQuery]
    y_label_offset: NotRequired[float | DataQuery]
    y_line: NotRequired[bool | DataQuery]
    y_nice: NotRequired[bool | float | Interval | DataQuery]
    y_padding: NotRequired[float | DataQuery]
    y_padding_inner: NotRequired[float | DataQuery]
    y_padding_outer: NotRequired[float | DataQuery]
    y_percent: NotRequired[bool | DataQuery]
    y_range: NotRequired[Sequence[Any] | Fixed | DataQuery]
    y_reverse: NotRequired[bool | DataQuery]
    y_round: NotRequired[bool | DataQuery]
    y_scale: NotRequired[PositionScaleType | DataQuery | None]
    y_tick_format: NotRequired[str | DataQuery | None]
    y_tick_padding: NotRequired[float | DataQuery]
    y_tick_rotate: NotRequired[float | DataQuery]
    y_tick_size: NotRequired[float | DataQuery]
    y_tick_spacing: NotRequired[float | DataQuery]
    y_ticks: NotRequired[float | Interval | Sequence[Any] | DataQuery]
    y_zero: NotRequired[bool | DataQuery]


class Plot(TypedDict, closed=True):
    align: NotRequired[float | DataQuery]
    aria_description: NotRequired[str | None]
    aria_label: NotRequired[str | None]
    aspect_ratio: NotRequired[float | bool | DataQuery | None]
    axis: NotRequired[Literal["top", "right", "bottom", "left", "both"] | bool | DataQuery | None]
    clip: NotRequired[Literal["frame", "sphere"] | bool | DataQuery | None]
    color_base: NotRequired[float | DataQuery]
    color_clamp: NotRequired[bool | DataQuery]
    color_constant: NotRequired[float | DataQuery]
    color_domain: NotRequired[Sequence[Any] | Fixed | DataQuery]
    color_exponent: NotRequired[float | DataQuery]
    color_interpolate: NotRequired[Interpolate | DataQuery]
    color_label: NotRequired[str | DataQuery | None]
    color_n: NotRequired[float | DataQuery]
    color_nice: NotRequired[bool | float | Interval | DataQuery]
    color_percent: NotRequired[bool | DataQuery]
    color_pivot: NotRequired[Any | DataQuery]
    color_range: NotRequired[Sequence[Any] | Fixed | DataQuery]
    color_reverse: NotRequired[bool | DataQuery]
    color_scale: NotRequired[ColorScaleType | DataQuery | None]
    color_scheme: NotRequired[ColorScheme | DataQuery]
    color_symmetric: NotRequired[bool | DataQuery]
    color_tick_format: NotRequired[str | DataQuery | None]
    color_zero: NotRequired[bool | DataQuery]
    facet_grid: NotRequired[bool | str | Interval | Sequence[Any] | DataQuery]
    facet_label: NotRequired[str | DataQuery | None]
    facet_margin: NotRequired[float | DataQuery]
    facet_margin_bottom: NotRequired[float | DataQuery]
    facet_margin_left: NotRequired[float | DataQuery]
    facet_margin_right: NotRequired[float | DataQuery]
    facet_margin_top: NotRequired[float | DataQuery]
    fx_align: NotRequired[float | DataQuery]
    fx_aria_description: NotRequired[str | DataQuery]
    fx_aria_label: NotRequired[str | DataQuery]
    fx_axis: NotRequired[Literal["top", "bottom", "both"] | bool | DataQuery | None]
    fx_domain: NotRequired[Sequence[Any] | Fixed | DataQuery]
    fx_font_variant: NotRequired[str | DataQuery]
    fx_grid: NotRequired[bool | str | Interval | Sequence[Any] | DataQuery]
    fx_inset: NotRequired[float | DataQuery]
    fx_inset_left: NotRequired[float | DataQuery]
    fx_inset_right: NotRequired[float | DataQuery]
    fx_label: NotRequired[str | DataQuery | None]
    fx_label_anchor: NotRequired[Literal["top", "right", "bottom", "left", "center"] | DataQuery]
    fx_label_offset: NotRequired[float | DataQuery]
    fx_line: NotRequired[bool | DataQuery]
    fx_padding: NotRequired[float | DataQuery]
    fx_padding_inner: NotRequired[float | DataQuery]
    fx_padding_outer: NotRequired[float | DataQuery]
    fx_range: NotRequired[Sequence[Any] | Fixed | DataQuery]
    fx_reverse: NotRequired[bool | DataQuery]
    fx_round: NotRequired[bool | DataQuery]
    fx_tick_format: NotRequired[str | DataQuery | None]
    fx_tick_padding: NotRequired[float | DataQuery]
    fx_tick_rotate: NotRequired[float | DataQuery]
    fx_tick_size: NotRequired[float | DataQuery]
    fx_tick_spacing: NotRequired[float | DataQuery]
    fx_ticks: NotRequired[float | Interval | Sequence[Any] | DataQuery]
    fy_align: NotRequired[float | DataQuery]
    fy_aria_description: NotRequired[str | DataQuery]
    fy_aria_label: NotRequired[str | DataQuery]
    fy_axis: NotRequired[Literal["left", "right", "both"] | bool | DataQuery | None]
    fy_domain: NotRequired[Sequence[Any] | Fixed | DataQuery]
    fy_font_variant: NotRequired[str | DataQuery]
    fy_grid: NotRequired[bool | str | Interval | Sequence[Any] | DataQuery]
    fy_inset: NotRequired[float | DataQuery]
    fy_inset_bottom: NotRequired[float | DataQuery]
    fy_inset_top: NotRequired[float | DataQuery]
    fy_label: NotRequired[str | DataQuery | None]
    fy_label_anchor: NotRequired[Literal["top", "right", "bottom", "left", "center"] | DataQuery]
    fy_label_offset: NotRequired[float | DataQuery]
    fy_line: NotRequired[bool | DataQuery]
    fy_padding: NotRequired[float | DataQuery]
    fy_padding_inner: NotRequired[float | DataQuery]
    fy_padding_outer: NotRequired[float | DataQuery]
    fy_range: NotRequired[Sequence[Any] | Fixed | DataQuery]
    fy_reverse: NotRequired[bool | DataQuery]
    fy_round: NotRequired[bool | DataQuery]
    fy_tick_format: NotRequired[str | DataQuery | None]
    fy_tick_padding: NotRequired[float | DataQuery]
    fy_tick_rotate: NotRequired[float | DataQuery]
    fy_tick_size: NotRequired[float | DataQuery]
    fy_tick_spacing: NotRequired[float | DataQuery]
    fy_ticks: NotRequired[float | Interval | Sequence[Any] | DataQuery]
    grid: NotRequired[bool | str | DataQuery]
    height: NotRequired[float | DataQuery]
    inset: NotRequired[float | DataQuery]
    length_base: NotRequired[float | DataQuery]
    length_clamp: NotRequired[Any]
    length_constant: NotRequired[float | DataQuery]
    length_domain: NotRequired[Sequence[Any] | Fixed | DataQuery]
    length_exponent: NotRequired[float | DataQuery]
    length_nice: NotRequired[bool | float | Interval | DataQuery]
    length_percent: NotRequired[bool | DataQuery]
    length_range: NotRequired[Sequence[Any] | Fixed | DataQuery]
    length_scale: NotRequired[ContinuousScaleType | DataQuery | None]
    length_zero: NotRequired[bool | DataQuery]
    margin: NotRequired[float | DataQuery]
    margin_bottom: NotRequired[float | DataQuery]
    margin_left: NotRequired[float | DataQuery]
    margin_right: NotRequired[float | DataQuery]
    margin_top: NotRequired[float | DataQuery]
    margins: NotRequired[Margins]
    name: NotRequired[str]
    opacity_base: NotRequired[float | DataQuery]
    opacity_clamp: NotRequired[bool | DataQuery]
    opacity_constant: NotRequired[float | DataQuery]
    opacity_domain: NotRequired[Sequence[Any] | Fixed | DataQuery]
    opacity_exponent: NotRequired[float | DataQuery]
    opacity_label: NotRequired[str | DataQuery | None]
    opacity_nice: NotRequired[bool | float | Interval | DataQuery]
    opacity_percent: NotRequired[bool | DataQuery]
    opacity_range: NotRequired[Sequence[Any] | Fixed | DataQuery]
    opacity_reverse: NotRequired[bool | DataQuery]
    opacity_scale: NotRequired[ContinuousScaleType | DataQuery | None]
    opacity_tick_format: NotRequired[str | DataQuery | None]
    opacity_zero: NotRequired[bool | DataQuery]
    padding: NotRequired[float | DataQuery]
    plot: Sequence[PlotMark | PlotInteractor | PlotLegend]
    projection_clip: NotRequired[bool | float | Literal["frame"] | DataQuery | None]
    projection_domain: NotRequired[Mapping[str, Any] | DataQuery]
    projection_inset: NotRequired[float | DataQuery]
    projection_inset_bottom: NotRequired[float | DataQuery]
    projection_inset_left: NotRequired[float | DataQuery]
    projection_inset_right: NotRequired[float | DataQuery]
    projection_inset_top: NotRequired[float | DataQuery]
    projection_parallels: NotRequired[tuple[Y1, Y1] | DataQuery]
    projection_precision: NotRequired[float | DataQuery]
    projection_rotate: NotRequired[tuple[Y1, Y1, Y1] | DataQuery]
    projection_type: NotRequired[ProjectionName | DataQuery | None]
    r_base: NotRequired[float | DataQuery]
    r_clamp: NotRequired[Any]
    r_constant: NotRequired[float | DataQuery]
    r_domain: NotRequired[Sequence[Any] | Fixed | DataQuery]
    r_exponent: NotRequired[float | DataQuery]
    r_label: NotRequired[str | DataQuery | None]
    r_nice: NotRequired[bool | float | Interval | DataQuery]
    r_percent: NotRequired[bool | DataQuery]
    r_range: NotRequired[Sequence[Any] | Fixed | DataQuery]
    r_scale: NotRequired[ContinuousScaleType | DataQuery | None]
    r_zero: NotRequired[bool | DataQuery]
    style: NotRequired[str | CSSStyles | DataQuery | None]
    symbol_domain: NotRequired[Sequence[Any] | Fixed | DataQuery]
    symbol_range: NotRequired[Sequence[Any] | Fixed | DataQuery]
    symbol_scale: NotRequired[DiscreteScaleType | DataQuery | None]
    width: NotRequired[float | DataQuery]
    x_align: NotRequired[float | DataQuery]
    x_aria_description: NotRequired[str | DataQuery]
    x_aria_label: NotRequired[str | DataQuery]
    x_axis: NotRequired[Literal["top", "bottom", "both"] | bool | DataQuery | None]
    x_base: NotRequired[float | DataQuery]
    x_clamp: NotRequired[bool | DataQuery]
    x_constant: NotRequired[float | DataQuery]
    x_domain: NotRequired[Sequence[Any] | Fixed | DataQuery]
    x_exponent: NotRequired[float | DataQuery]
    x_font_variant: NotRequired[str | DataQuery]
    x_grid: NotRequired[bool | str | Interval | Sequence[Any] | DataQuery]
    x_inset: NotRequired[float | DataQuery]
    x_inset_left: NotRequired[float | DataQuery]
    x_inset_right: NotRequired[float | DataQuery]
    x_label: NotRequired[str | DataQuery | None]
    x_label_anchor: NotRequired[Literal["top", "right", "bottom", "left", "center"] | DataQuery]
    x_label_arrow: NotRequired[LabelArrow | DataQuery]
    x_label_offset: NotRequired[float | DataQuery]
    x_line: NotRequired[bool | DataQuery]
    x_nice: NotRequired[bool | float | Interval | DataQuery]
    x_padding: NotRequired[float | DataQuery]
    x_padding_inner: NotRequired[float | DataQuery]
    x_padding_outer: NotRequired[float | DataQuery]
    x_percent: NotRequired[bool | DataQuery]
    x_range: NotRequired[Sequence[Any] | Fixed | DataQuery]
    x_reverse: NotRequired[bool | DataQuery]
    x_round: NotRequired[bool | DataQuery]
    x_scale: NotRequired[PositionScaleType | DataQuery | None]
    x_tick_format: NotRequired[str | DataQuery | None]
    x_tick_padding: NotRequired[float | DataQuery]
    x_tick_rotate: NotRequired[float | DataQuery]
    x_tick_size: NotRequired[float | DataQuery]
    x_tick_spacing: NotRequired[float | DataQuery]
    x_ticks: NotRequired[float | Interval | Sequence[Any] | DataQuery]
    x_zero: NotRequired[bool | DataQuery]
    xy_domain: NotRequired[Sequence[Any] | Fixed | DataQuery]
    y_align: NotRequired[float | DataQuery]
    y_aria_description: NotRequired[str | DataQuery]
    y_aria_label: NotRequired[str | DataQuery]
    y_axis: NotRequired[Literal["left", "right", "both"] | bool | DataQuery | None]
    y_base: NotRequired[float | DataQuery]
    y_clamp: NotRequired[bool | DataQuery]
    y_constant: NotRequired[float | DataQuery]
    y_domain: NotRequired[Sequence[Any] | Fixed | DataQuery]
    y_exponent: NotRequired[float | DataQuery]
    y_font_variant: NotRequired[str | DataQuery]
    y_grid: NotRequired[bool | str | Interval | Sequence[Any] | DataQuery]
    y_inset: NotRequired[float | DataQuery]
    y_inset_bottom: NotRequired[float | DataQuery]
    y_inset_top: NotRequired[float | DataQuery]
    y_label: NotRequired[str | DataQuery | None]
    y_label_anchor: NotRequired[Literal["top", "right", "bottom", "left", "center"] | DataQuery]
    y_label_arrow: NotRequired[LabelArrow | DataQuery]
    y_label_offset: NotRequired[float | DataQuery]
    y_line: NotRequired[bool | DataQuery]
    y_nice: NotRequired[bool | float | Interval | DataQuery]
    y_padding: NotRequired[float | DataQuery]
    y_padding_inner: NotRequired[float | DataQuery]
    y_padding_outer: NotRequired[float | DataQuery]
    y_percent: NotRequired[bool | DataQuery]
    y_range: NotRequired[Sequence[Any] | Fixed | DataQuery]
    y_reverse: NotRequired[bool | DataQuery]
    y_round: NotRequired[bool | DataQuery]
    y_scale: NotRequired[PositionScaleType | DataQuery | None]
    y_tick_format: NotRequired[str | DataQuery | None]
    y_tick_padding: NotRequired[float | DataQuery]
    y_tick_rotate: NotRequired[float | DataQuery]
    y_tick_size: NotRequired[float | DataQuery]
    y_tick_spacing: NotRequired[float | DataQuery]
    y_ticks: NotRequired[float | Interval | Sequence[Any] | DataQuery]
    y_zero: NotRequired[bool | DataQuery]


Component: TypeAlias = Union[
    "HConcat", "VConcat", HSpace, VSpace, Menu, Search, Slider, Table, Plot, PlotMark, Legend
]


class HConcat(TypedDict, closed=True):
    hconcat: Sequence[Component]


class Spec1(TypedDict, closed=True):
    config: NotRequired[Config]
    data: NotRequired[Data]
    hconcat: Sequence[Component]
    meta: NotRequired[Meta]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]


class Spec2(TypedDict, closed=True):
    config: NotRequired[Config]
    data: NotRequired[Data]
    meta: NotRequired[Meta]
    params: NotRequired[Params]
    plot_defaults: NotRequired[PlotAttributes]
    vconcat: Sequence[Component]


Spec: TypeAlias = (
    Spec1
    | Spec2
    | Spec3
    | Spec4
    | Spec5
    | Spec6
    | Spec7
    | Spec8
    | Spec9
    | Spec10
    | Spec11
    | Spec12
    | Spec13
    | Spec14
    | Spec15
    | Spec16
    | Spec17
    | Spec18
    | Spec19
    | Spec20
    | Spec21
    | Spec22
    | Spec23
    | Spec24
    | Spec25
    | Spec26
    | Spec27
    | Spec28
    | Spec29
    | Spec30
    | Spec31
    | Spec32
    | Spec33
    | Spec34
    | Spec35
    | Spec36
    | Spec37
    | Spec38
    | Spec39
    | Spec40
    | Spec41
    | Spec42
    | Spec43
    | Spec44
    | Spec45
    | Spec46
    | Spec47
    | Spec48
    | Spec49
    | Spec50
    | Spec51
    | Spec52
    | Spec53
    | Spec54
    | Spec55
    | Spec56
    | Spec57
    | Spec58
    | Spec59
    | Spec60
    | Spec61
    | Spec62
    | Spec63
    | Spec64
    | Spec65
    | Spec66
    | Spec67
    | Spec68
    | Spec69
    | Spec70
    | Spec71
    | Spec72
    | Spec73
    | Spec74
    | Spec75
    | Spec76
    | Spec77
    | Spec78
    | Spec79
    | Spec80
    | Spec81
)


class VConcat(TypedDict, closed=True):
    vconcat: Sequence[Component]
