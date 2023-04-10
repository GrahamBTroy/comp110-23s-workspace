"""EX07 Dictionary Functions."""
__author__ = "730561058"


def invert(target: dict[str, str]) -> dict[str, str]:
    """Inverts a given function."""
    end: dict[str, str] = {}
    for i in target:
        if target[i] in end: 
            raise KeyError("KeyError")
        end[target[i]] = i 

    return end


def favorite_color(colors: dict[str, str]) -> str:
    """Lists a most commonly appearing color."""
    color_dict: dict[str, int] = {}
    max_count: int = 0
    fav_color = None

    for key in colors:
        if colors[key] in color_dict:
            color_dict[colors[key]] += 1
        else: 
            color_dict[colors[key]] = 1
        if color_dict[colors[key]] > max_count:
            max_count = color_dict[colors[key]]
            fav_color = colors[key]
    return fav_color


def count(origin: list[str]) -> dict[str, int]: 
    """Makes and prints a dictionary."""
    final: dict[str, int] = {}
    for i in range(len(origin)):
        if origin[i] in final:
            final[origin[i]] += 1
        else: 
            final[origin[i]] = 1
    return final