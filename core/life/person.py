__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

from .time import Condition
from . import behavior_tree


class Person:
    seed = 0

    def __init__(self, name: str="", surname: str="", age: int=0):
        self.name = name
        self.surname = surname
        self.age = age
        self.interests = []
        self.scheduled_events = []
        self.events_stack = {}
        self.behavior_tree = behavior_tree.BehaviorTree()

    def handle_event(self, event: Condition) -> tuple:
        """Add an event to the events stack of this person"""
        self.events_stack[Person.seed] = event
        Person.seed += 1
        return self, Person.seed - 1

    def get_behavior_tree(self) -> behavior_tree.BehaviorTree:
        """Return the behavior tree of this Person ; in order to modify it for example"""
        return self.behavior_tree

    def add_scheduled_event(self, event: object) -> object:
        """Add an event to the event list of this person"""
        self.scheduled_events.append(event)
        return self

    def evolve(self, clock: object) -> object:
        """Allow this person to evolve (example : birthday, special project planed ...)"""
        print("\t\t\t {} is evolving".format(self))

        self.events_stack["time"] = Condition("time", clock.time, 0.0)
        events_launched = []

        for event in self.scheduled_events:
            ret = event.check(list(self.events_stack.values()))
            if ret:
                events_launched.append(event)
                print("\t\t\t\t {} started '{}'".format(self, event))

        print("\t\t\t\t {} played {} from his behavior tree".format(self, self.behavior_tree.play()))

        return self

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "{} {}".format(self.name, self.surname)