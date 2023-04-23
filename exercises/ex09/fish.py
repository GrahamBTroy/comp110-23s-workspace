"""File to define Fish class."""

__author__ = "730561058"


class Fish:
    """Is a fish."""
    age: int

    def __init__(self):
        """Makes fish."""
        self.age = 0
        return None
    
    def one_day(self):
        """One day in the life of a fish."""
        self.age += 1
        return None