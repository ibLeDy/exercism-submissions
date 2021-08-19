COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]
COLORS_MAPPING = {name: idx for idx, name in enumerate(COLORS)}


def color_code(color):
    return COLORS_MAPPING[color]


def colors():
    return COLORS
