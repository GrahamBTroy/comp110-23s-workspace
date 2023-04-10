"""EX05 test - Method of testing utility functions."""
__author__ = "730561058"

from utils import only_evens

from utils import concat

from utils import sub 


def test_only_evenss() -> None: 
    """Simple test."""
    arguments: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(arguments) == [2, 4]


def test_only_evens2() -> None:
    """Simple test."""
    arguments: list[int] = [10, 21, 34, 47, 63]
    assert only_evens(arguments) == [10, 34]


def test_only_evens3() -> None: 
    """Simple test."""
    arguments: list[int] = [1066, 2199, 3433, 476, 6301010, 9999, 8]
    assert only_evens(arguments) == [1066, 476, 6301010, 8]


def test_concat0() -> None: 
    """Simple test."""
    list_one: list[int] = [1, 2, 3]
    list_two: list[int] = [4, 5, 6]
    assert concat(list_one, list_two) == [1, 2, 3, 4, 5, 6]


def test_concat2() -> None: 
    """Simple test."""
    list_one: list[int] = [7, 6, 5]
    list_two: list[int] = [8, 9, 10]
    assert concat(list_one, list_two) == [7, 6, 5, 8, 9, 10]


def test_concat3() -> None: 
    """Simple test."""
    list_one: list[int] = []
    list_two: list[int] = []
    assert concat(list_one, list_two) == []


def test_sub1() -> None: 
    """Simple test."""
    a_list: list[int] = [1, 3, 3, 6, 5]
    aint = 1
    bint = 4
    assert sub(a_list, aint, bint) == [3, 3, 6]


def test_sub2() -> None: 
    """Simple test."""
    a_list: list[int] = [1, 3, 3, 6, 5]
    aint = 1
    bint = 2
    assert sub(a_list, aint, bint) == [3]


def test_sub3() -> None: 
    """Simple test."""
    a_list: list[int] = [1, 2, 3, 7, 5, 9]
    aint = 1
    bint = 5
    assert sub(a_list, aint, bint) == [2, 3, 7, 5]
    