"""File to define Bear class."""

__author__ = "730561058"


class Bear:
    """Is a bear!""" 
    age: int
    hunger_score: int
    
    def __init__(self):
        """Constructor."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """One day for a bear."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Bear gotta eat."""
        self.hunger_score = self.hunger_score + num_fish

    