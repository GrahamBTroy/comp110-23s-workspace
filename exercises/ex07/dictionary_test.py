"""EX07 Dictionary Functions tests."""
__author__ = "730561058"

import pytest
from dictionary import invert
from dictionary import favorite_color
from dictionary import count


def test_invert() -> None: 
    """Tests invert."""
    test_dict: dict[str, str] = {'happy': 'bear'}
    end: dict[str, str] = invert(test_dict)
    assert end == {'bear': 'happy'}


def test_to_invert() -> None:
    """Tests invert.""" 
    test_dict: dict[str, str] = {'tall': 'tall'}
    end: dict[str, str] = invert(test_dict)
    assert end == {'tall': 'tall'}


def test_three_invert() -> None: 
    """Tests invert."""
    test_dict: dict[str, str] = {'tall': 'tal', 'tal': "tall"}
    end: dict[str, str] = invert(test_dict)
    assert end == {'tal': 'tall', 'tall': 'tal'}


def test_invert_error() -> None: 
    """Tests invert."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_favorite_color() -> None:
    """Tests favorite color."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_favorite_color_01() -> None:
    """Tests favorite color."""
    assert favorite_color({"red": "yellow", "green": "yellow", "blue": "blue"}) == "yellow"


def test_favorite_color_02() -> None:
    """Tests favorite color."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "red"}) == "yellow"


def test_count() -> None: 
    """Tests count."""
    initial: list(str) = ["Alpha", "Bravo", "Charlie", "Delta"]
    final: dict[str, int] = count(initial)
    assert final == {'Alpha': 1, 'Bravo': 1, 'Charlie': 1, 'Delta': 1}


def test_count_00() -> None: 
    """Tests count."""
    initial: list(str) = ["Alpha", "Alpha", "Alpha", "Delta"]
    final: dict[str, int] = count(initial)
    assert final == {'Alpha': 3, 'Delta': 1}


def test_count_zero() -> None: 
    """Tests count."""
    initial: list(str) = ["1", "2", "3", "3", "44"]
    final: dict[str, int] = count(initial)
    assert final == {'1': 1, '2': 1, '3': 2, '44': 1}
