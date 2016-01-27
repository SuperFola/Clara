__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

from .buildings import Building


class Street:
    def __init__(self, name: str="", size: float=1.0):
        self.name = name
        self.size = size
        self.buildings = []
        self.connections = []

    def add(self, building: Building) -> object:
        """Add a building in the street"""
        self.buildings.append(building)
        return self

    def can_join(self, a_street: object) -> bool:
        """Return True or False whether it's possible to join a specific street from this one, or not"""
        if a_street in self.connections:
            return True
        return False

    def connect_to(self, a_street: object) -> object:
        """Add a new connection to this street"""
        self.connections.append(a_street)
        if self not in a_street.connections:
            a_street.connect_to(self)
        return self

    def __repr__(self):
        return self.__str__

    def __str__(self):
        return self.name + " Street's"