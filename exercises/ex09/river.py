"""File to define River class."""

__author__ = "730561058"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """River."""
    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())
    
    def view_river(self) -> None:
        """Function to see river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def remove_fish(self, amount: int) -> None:
        """Fish die."""
        fish2: list[Fish] = []
        for x in range(len(self.fish)):
            if x >= amount:
                fish2.append(self.fish[x])
        self.fish = fish2
        return None

    def check_ages(self):
        """Tell how old things are."""
        fish2: list[Fish] = []
        bear2: list[Bear] = []
        for x in range(len(self.bears)): 
            if self.bears[x].age <= 5:  
                bear2.append(self.bears[x])
        for x in range(len(self.fish)):
            if self.fish[x].age <= 3: 
                fish2.append(self.fish[x])
        self.bears = bear2
        self.fish = fish2
        return None

    def bears_eating(self):
        """Bears gotta eat."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None
    
    def check_hunger(self):
        """Bears can starve."""
        bear2: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0: 
                bear2.append(bear)
        self.bears = bear2
        return None

    def repopulate_fish(self):
        """Fish get born."""
        smolfish: int = 0
        smolfish2: int = 0
        count: int = 0
        for fish in self.fish:
            smolfish = len(self.fish) // 2
            smolfish2 = smolfish * 2
            while count < smolfish2:
                Fish()
                self.fish.append(Fish())
                count += 1
        return None
    
    def repopulate_bears(self):
        """Bears get born."""
        cubs: int = 0
        count: int = 0
        for bears in self.bears:
            cubs = len(self.bears) // 2
            while count < cubs:
                Bear()
                self.bears.append(Bear())
                count += 1
        return None
    
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self): 
        """I'm honestly not sure what this does."""
        count = 0
        while count < 7: 
            self.one_river_day()
            count += 1
