__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

from ..life.person import Person
from ..objects.product import Product, QuantifiedProduct


class Building:
    def __init__(self, name: str="", *interests_involved):
        self.name = name
        self.interests_involved = interests_involved

    def can_interest(self, person: Person) -> float:
        """Return a percentage of possibility to interest someone"""
        score = 0
        for interest in person.interests:
            if interest in self.interests_involved:
                score += 1
        return score / len(self.interests_involved)


class House(Building):
    def __init__(self, name: str="", *interests_involved):
        super().__init__(name, *interests_involved)
        self.peoples_living_in = []

    def has_habitant(self, habitant: Person) -> bool:
        """Return True or False whether an habitant is in the house or not"""
        if habitant in self.peoples_living_in:
            return True
        return False

    def has_habitant_name(self, habitant_name: str) -> bool:
        """Return True or False whether an habitant with the name given is in the house or not"""
        for habitant in self.peoples_living_in:
            if habitant.name == habitant_name:
                return True
        return False

    def get_habitant_by_name(self, habitant_name: str) -> Person:
        """Return a Person object, which matches the name given"""
        if self.has_habitant_name(habitant_name):
            for habitant in self.peoples_living_in:
                if habitant.name == habitant_name:
                    return habitant
        else:
            raise ValueError("'{}' does not match any habitant".format(habitant_name))

    def add_settler(self, habitant: Person) -> object:
        """Add a person in a house (he/she is not in the house, but living in)"""
        self.peoples_living_in.append(habitant)
        return self

    def remove_settler(self, habitant_name: str) -> object:
        """Remove someone from the house (he/she can be outside the house, he/she will just have to found
           a new house)"""
        for i in range(len(self.peoples_living_in)):
            if self.peoples_living_in[i].name == habitant_name:
                self.peoples_living_in.pop(i)
        return self


class CommercialBuilding(Building):
    def __init__(self, name: str="", chief: Person=Person(), *interests_involved):
        super().__init__(name, *interests_involved)
        self.capital = 0
        self.available_goods = {}
        self.chief = chief

    def is_in_deficit(self) -> bool:
        """Check if the CommercialBuilding is in deficit and return True or False"""
        if self.capital < 0:
            return True
        return False

    def has_product_name(self, product_name: str) -> bool:
        """Check if the CommercialBuilding has product_name in his available_goods"""
        if product_name in self.available_goods.keys():
            return True
        return False

    def buy(self, product: Product, quantity: int) -> object:
        """Buy a product whom quantity is given, and deduce the calculated price from the capital"""
        self.capital -= product.price * quantity
        if product.name not in self.available_goods.keys():
            self.available_goods[product.name] = QuantifiedProduct().construct_from_product(product, quantity)
        else:
            self.available_goods[product.name].quantity += quantity
        return self


class Shop(CommercialBuilding):
    def __init__(self, name: str="", *interests_involved):
        super().__init__(name, *interests_involved)


class Enterprise(CommercialBuilding):
    def __init__(self, name: str="", *interests_involved):
        super().__init__(name, *interests_involved)