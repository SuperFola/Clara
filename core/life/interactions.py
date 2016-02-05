__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""


class Interaction:
    def __init__(self, name: str="", priority: float=0.0, *interests_involved):
        self.name = name
        self.priority = priority
        self.interests_involved = interests_involved


class HumanInteraction(Interaction):
    def __init__(self, name: str, priority: float, with_persons: tuple, *interests_involved):
        super().__init__(name, priority, *interests_involved)
        self.with_persons = with_persons

    def get_participants(self) -> tuple:
        """Return the list of participants in this interaction"""
        return self.with_persons


class HumanObjectInteraction(Interaction):
    def __init__(self, name: str, priority: float, with_objects: tuple, *interests_involved):
        super().__init__(name, priority, *interests_involved)
        self.with_objects = with_objects