__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

from .time import Condition


class Person:
    def __init__(self, name: str="", surname: str="", age: int=0):
        self.name = name
        self.surname = surname
        self.age = age
        self.interests = []
        self.scheduled_events = []
        self.state = {}

    def add_event(self, event: object) -> object:
        """Add an event to the event list of this person"""
        self.scheduled_events.append(event)
        return self

    def evolve(self, clock: object) -> object:
        """Allow this person to evolve (example : birthday, special project planed ...)"""
        print("\t\t\t {} is evolving".format(self))
        self.state["time"] = Condition("time", clock.time, 0.0)
        for event in self.scheduled_events:
            ret = event.check(list(self.state.values()))
            if ret:
                print("{} started {}".format(self, event))
        return self

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name