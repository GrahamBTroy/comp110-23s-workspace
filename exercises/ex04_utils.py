"""EX04 - `list` Utility Functions."""
__author__ = "730561058"
input = 1


def all(ts: list[int], input: int) -> bool:
    """This function determines if the list is entirely composed of an input."""
    same: bool = True
    count = 0
    if len(ts) == 0:
        same = False
    while count <= len(ts) - 1: 
        if input != ts[count]: 
            same = False
        count += 1
    return same


def max(input: list[int]) -> int: 
    """This function determines what the largest number in the list is."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    big = input[0]
    count = 0
    while count < len(input):
        if big < input[count]:
            big = input[count]
        count += 1
    return big


def is_equal(a: list[int], b: list[int]) -> bool:
    """This function determines if two lists are exactly the same."""
    count = 0
    if len(a) != len(b):
        return False
    while count < len(a): 
        if a[count] != b[count]: 
            return False
        count += 1
    return True