"""EX05 - `list` Utility Functions."""

__author__ = "730561058"


def only_evens(arguments: list[int]) -> list[int]:
    """Returns if a number is even or not."""
    returns: list[int] = []
    for num in arguments: 
        if num % 2 == 0: 
            returns.append(num)
    return returns


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Returns the combination of two lists."""
    list_three: list[int] = []
    for num in list_one: 
        list_three.append(num)
    for num in list_two: 
        list_three.append(num)
    return list_three


def sub(a_list: list[int], aint: int, bint: int) -> list[int]:
    """List the numbers in a function between two places in the function."""
    if len(a_list) < 1: 
        return []
    if aint < 0: 
        aint = 0
    if aint == len(a_list):
        return []
    if bint > len(a_list): 
        bint = len(a_list)
    section: list[int] = []
    for num in range(aint, bint):
        section.append(a_list[num])
    return section