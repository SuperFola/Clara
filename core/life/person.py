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
        self.scheduled_events = []

    def add_event(self, event: object) -> object:
        """Add an event to the event list of this person"""
        self.scheduled_events.append(event)
        return self

    def evolve(self, clock: object) -> object:
        """Allow this person to evolve (example : birthday, special project planed ...)"""
        print("\t\t\t {} is evolving".format(self))
        for event in self.scheduled_events:
            if event.time == clock.time:
                event.act(self)
        return self

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name