__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

from . import constants
from . import time


class Node:
    def __init__(self, name: str="", priority: float=0.0):
        self.childs = []
        self.name = name
        self.priority = priority
        self.stopped_there = False
        self.cpt = 0

    def get_child_by_name(self, name: str) -> object:
        """Search for a node named 'name' in the childs and return it"""
        for node in self.childs:
            if node.name == name:
                return node
        raise ValueError("No child is named '{}' in the node '{}'".format(name, self))

    def add_child(self, child: object) -> object:
        """Add a child to the node"""
        self.childs.append(child)
        return self

    def remove_child_where_name_is(self, name: str) -> object:
        """Remove a child of the node where his name is 'name'"""
        to_pop = -1
        for i in range(len(self.childs)):
            if self.childs[i].name == name:
                to_pop = i
        if to_pop != -1:
            self.childs.pop(to_pop)
        return self

    def play(self, states: list) -> dict:
        """Launch the action of the childs nodes, after having ordered them by priority if there is one"""
        max_priority = 0.0
        for node in self.childs:
            if node.priority > max_priority:
                max_priority = node.priority

        if max_priority:
            order = sorted(self.childs, key=lambda x: x.priority)[::-1]

            tmp = order.pop(self.cpt)
            action = tmp.play(states)
        else:
            action = self.childs[self.cpt].play(states)

        self.cpt += 1
        if self.cpt == len(self.childs):
            self.cpt = 0

        return action

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name


class Sequence(Node):
    def __init__(self, name: str="", priority: float=0.0):
        super().__init__(name, priority)
        self.current = 0

    def play(self, states: list) -> dict:
        """Read the sequence in its order and start each action of each node"""
        return self.next(states)

    def next(self, states: list) -> dict:
        """Iter on the list of childs and launch them in a specifical order"""
        if self.current < len(self.childs):
            status = self.childs[self.current].play(states)
            self.current += 1
        else:
            status = self.childs[0].play(states)
            self.current = 1

        if status["status"] == constants.SUCCESS and self.current < len(self.childs):
            return {
                "status": constants.RUNNING,
                "from": status["from"]
            }
        elif status["status"] == constants.SUCCESS and self.current == len(self.childs):
            return {
                "status": constants.SUCCESS,
                "from": status["from"]
            }
        elif status["status"] == constants.FAILURE:
            self.current = 0
            return {
                "status": constants.FAILURE,
                "from": status["from"]
            }
        elif status["status"] == constants.RUNNING:
            return {
                "status": constants.RUNNING,
                "from": status["from"]
            }


class Leaf(Node):
    def __init__(self, name: str, priority: float=0.0, cond: time.Condition=time.Condition("", "", 0.0)):
        super().__init__(name, priority)
        self.cond = cond

    def check(self, current: list) -> bool:
        """Check if the trigger should be launched or not"""
        total = self.priority
        if self.cond.key != "" and self.cond.value != "":
            for state in current:
                if state.key == self.cond.key and state.value == self.cond.value:
                    total += self.cond.importance
                if total >= 1.0:
                    break
            return total > 1.0
        # we do not have any condition, it is working every time
        return True

    def play(self, states: list):
        """Start the action of this leaf"""
        return {
            "from": str(self),
            "status": constants.SUCCESS if self.check(states) else constants.FAILURE
        }

    def get_child_by_name(self, name: str):
        raise PermissionError("A leaf can not have a child !")

    def add_child(self, child: Node):
        raise PermissionError("A leaf can not have a child !")

    def remove_child_where_name_is(self, name: str):
        raise PermissionError("A leaf can not have a child !")


class BehaviorTree:
    def __init__(self):
        self.tree = Node("main")

    def add_child(self, child: Node) -> object:
        """Add a child to the main node"""
        self.tree.add_child(child)
        return self

    def get_child_by_name(self, name: str) -> Node:
        """Get a child node by his name and return it"""
        return self.tree.get_child_by_name(name)

    def remove_child_where_name_is(self, name: str) -> object:
        """Remove a child by his name"""
        self.tree.remove_child_where_name_is(name)
        return self

    def play(self, states: list) -> dict:
        """Launch the action of the childs nodes, after having ordered them by priority if there is one"""
        return self.tree.play(states)