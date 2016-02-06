__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

from .buildings import Building
from ..life import person
from ..life import time


class Street:
    def __init__(self, name: str="", size: float=1.0):
        self.name = name
        self.size = size
        self.buildings = []
        self.connections = []
        self.persons_in = []

    def add_a_person(self, a_person: person.Person) -> object:
        """Add a person in the street"""
        self.persons_in.append(a_person)
        return self

    def remove_a_person_from_name(self, name: str) -> object:
        """Search a person by his/her name and remove it from the street"""
        to_pop = -1
        for i in range(len(self.persons_in)):
            if self.persons_in[i].name == name:
                to_pop = i
                break
        if to_pop != -1:
            self.persons_in.pop(to_pop)
            return self
        raise ValueError("Person named '{}' can't be located in this street. Try to look directly in the buildings".format(name))

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
        print("\t {} is evolving".format(self))
        for building in self.buildings:
            building.evolve(clock)
        for person in self.persons_in:
            person.handle_event(time.Condition("persons", [_ for _ in self.persons_in if _ != person], 0.1))
            person.evolve(clock)
        self._update(clock)
        return self

    def _update(self, clock: object):
        """This will update every street"""
        pass

    def __repr__(self):
        return self.__str__

    def __str__(self):
        return self.name + " Street's"