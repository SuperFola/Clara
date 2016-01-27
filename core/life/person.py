__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""


class Person:
    def __init__(self, name: str="", surname: str="", age: int=0):
        self.name = name
        self.surname = surname
        self.age = age
        self.interests = []