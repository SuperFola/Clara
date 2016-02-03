__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

from . import constants


class Node:
    def __init__(self, name: str="", priority: float=0.0):
        self.childs = []
        self.name = name
        self.priority = priority

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

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name


class Sequence(Node):
    def __init__(self, name: str="", priority: float=0.0):
        super().__init__(name, priority)
        self.current = 0

    def play(self):
        """Read the sequence in its order and start each action of each node"""
        final_status = constants.RUNNING
        while True:
            status = self.next()
            if status["status"] == constants.SUCCESS:
                final_status = constants.SUCCESS
                break
        return final_status

    def next(self):
        status = self.childs[self.current].play()
        self.current += 1
        if status["status"] == constants.SUCCESS and self.current < len(self.childs) - 1:
            return {
                "status": constants.RUNNING,
                "from": self.name
            }
        elif status["status"] == constants.SUCCESS and self.current == len(self.childs) - 1:
            return {
                "status": constants.SUCCESS,
                "from": self.name
            }


class Leaf(Node):
    def __init__(self, name: str="", priority: float=0.0):
        super().__init__(name, priority)

    def play(self):
        """Start the action of this leaf"""
        return {
            "from": str(self)
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

    def play(self):
        """Launch the action of the childs nodes, after having ordered them by priority if there is one"""
        max_priority = 0.0
        for node in self.tree.childs:
            if node.priority > max_priority:
                max_priority = node.priority
        if max_priority:
            order = sorted(child.priority for child in self.tree.childs)
            already_played = []
            for priority in order:
                for node in self.tree.childs:
                    if node.priority == priority and node not in already_played:
                        node.play()
                        already_played.append(node)
        else:
            for node in self.tree.childs:
                node.play()