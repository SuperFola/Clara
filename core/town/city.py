__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

from .buildings import Building
from .street import Street


class City:
    def __init__(self, name: str="", size: float=1.0):
        self.name = name
        self.size = size
        self.streets = []

    def has(self, building_type: Building) -> bool:
        """Return True of False whether a building (which type is building_type) is in the city or not"""
        for street in self.streets:
            for building in street.buildings:
                if isinstance(building, building_type):
                    return True
        return False

    def has_on_street(self, street_name: str, building_type: Building) -> bool:
        """Return True of False whether a building (which type is building_type) is in the city or not"""
        for street in self.streets:
            if street.name == street_name:
                for building in street.buildings:
                    if isinstance(building, building_type):
                        return True
        return False

    def has_street_name(self, street_name: str) -> bool:
        """Return True or False whether a street is in the city or not"""
        for street in self.streets:
            if street.name == street_name:
                return True
        return False

    def get_street_by_name(self, street_name: str) -> Street:
        """Search for a specific street name in the name, and return it if it exists"""
        if self.has_street_name(street_name):
            for street in self.streets:
                if street.name == street_name:
                    return street
        raise ValueError("'{}' does not exist in this city".format(street_name))

    def add_street(self, street: Street) -> object:
        """Add a street to the city"""
        self.streets.append(street)
        return self

    def add_building_on(self, street_name: Street, building: Building) -> object:
        """Add a building to the city, in a specific street"""
        for i in range(len(self.streets)):
            if self.streets[i].name == street_name:
                self.streets[i].append(building)
        return self

    def __repr__(self):
        return self.__str__

    def __str__(self):
        return self.name