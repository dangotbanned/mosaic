# NOTE: DO NOT EDIT.
# Regenerate with: pnpm generate

from __future__ import annotations

from typing import Literal

from mosaic_spec._typing_compat import TypeAliasType

ColorScheme = TypeAliasType(
    "ColorScheme",
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
    ],
)
"""The built-in color schemes. For categorical data, one of:

- *Accent* - eight colors
- *Category10* - ten colors
- *Dark2* - eight colors
- *Observable10* (default) - ten colors
- *Paired* - twelve paired colors
- *Pastel1* - nine colors
- *Pastel2* - eight colors
- *Set1* - nine colors
- *Set2* - eight colors
- *Set3* - twelve colors
- *Tableau10* - ten colors

For diverging data, one of:

- *BrBG* - from brown to white to blue-green
- *PRGn* - from purple to white to green
- *PiYG* - from pink to white to yellow-green
- *PuOr* - from purple to white to orange
- *RdBu* (default) - from red to white to blue
- *RdGy* - from red to white to gray
- *RdYlBu* - from red to yellow to blue
- *RdYlGn* - from red to yellow to green
- *Spectral* - from red to blue, through the spectrum
- *BuRd* - from blue to white to red
- *BuYlRd* - from blue to yellow to red

For sequential data, one of:

- *Blues* - from white to blue
- *Greens* - from white to green
- *Greys* - from white to gray
- *Oranges* - from white to orange
- *Purples* - from white to purple
- *Reds* - from white to red
- *Turbo* (default) - from blue to red, through the spectrum
- *Viridis* - from blue to green to yellow
- *Magma* - from purple to orange to yellow
- *Inferno* - from purple to orange to yellow
- *Plasma* - from purple to orange to yellow
- *Cividis* - from blue to yellow
- *Cubehelix* - from black to white, rotating hue
- *Warm* - from purple to green, through warm hues
- *Cool* - from green to to purple, through cool hues
- *BuGn* - from light blue to dark green
- *BuPu* - from light blue to dark purple
- *GnBu* - from light green to dark blue
- *OrRd* - from light orange to dark red
- *PuBu* - from light purple to dark blue
- *PuBuGn* - from light purple to blue to dark green
- *PuRd* - from light purple to dark red
- *RdPu* - from light red to dark purple
- *YlGn* - from light yellow to dark green
- *YlGnBu* - from light yellow to green to dark blue
- *YlOrBr* - from light yellow to orange to dark brown
- *YlOrRd* - from light yellow to orange to dark red

For cyclical data, one of:

- *Rainbow* (default) - the less-angry rainbow color scheme
- *Sinebow* - Bumgardner and Loyd's “sinebow” scheme"""


TimeIntervalName = TypeAliasType(
    "TimeIntervalName",
    Literal[
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
    ],
)
"""The built-in time intervals; UTC or local time, depending on context. The
*week* interval is an alias for *sunday*. The *quarter* interval is every three months, and the *half* interval is every six months, aligned at the start of the year."""


Interval = TypeAliasType(
    "Interval",
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
    | str,
)
"""How to partition a continuous range into discrete intervals; one of:

- a named time interval such as *day* (for date intervals)
- a number (for number intervals), defining intervals at integer multiples of *n*"""
