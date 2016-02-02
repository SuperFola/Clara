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

    def get_buildind_by_name(self, name: str) -> Building:
        """Search for a building named 'name' and return it if it is in this street"""
        if self.has_building_name(name):
            for building in self.buildings:
                if building.name == name:
                    return building
        raise ValueError("Building named '{}' can't be located in this street".format(name))

    def has_building_name(self, name: str):
        """Search for a building named 'name' in this street and return True or False whether it had been found or not"""
        for building in self.buildings:
            if building.name == name:
                return True
        return False

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

    def evolve(self, clock: object) -> object:
        """
           Allow all the buildings and the persons inside to evolve. All the update() methods of these elements
           will be launched one time.
        """
        for building in self.buildings:
            building.evolve(clock)
        self._update(clock)
        return self

    def _update(self, clock: object):
        """This will update every street"""
        pass

    def __repr__(self):
        return self.__str__

    def __str__(self):
        return self.name + " Street's"