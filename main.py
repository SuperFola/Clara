__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

import time
import core


def print_city_streets_and_connections(city: core.town.city.City):
    print("In the city {} :".format(city))
    for street in city.streets:
        print("\t{} is connected".format(street), end=' ')
        if not len(street.connections):
            print("to no other streets")
            continue
        elif len(street.connections) == 1:
            print("to", end=' ')
        else:
            print("to the streets", end=' ')
        for i in range(len(street.connections)):
            print("{}".format(street.connections[i]), end='')
            if i < len(street.connections) - 1:
                print(",", end=' ')
            else:
                print(".")


def main():
    street1 = "Baxbaxwalanuksiwe"
    street2 = "Ardakaniz"
    street3 = "Qames"
    print(core.constants.NAME + " is starting ...")

    the_time = core.life.time.Time()

    a_person = core.life.person.Person("John", "Doe", 0)
    a_person.get_behavior_tree()\
        .callbacks.update({
            "go to work": core.life.callbacks.test_callback
        })
    a_person.get_behavior_tree()\
        .add_child(
            core.life.behavior_tree.Sequence("sequence", 0.4)
        ).get_child_by_name(
            "sequence"
        ).add_child(
            core.life.behavior_tree.Leaf("eat")
        ).add_child(
            core.life.behavior_tree.Leaf("sleep")
        ).add_child(
            core.life.behavior_tree.Leaf("wake up")
        ).add_child(
            core.life.behavior_tree.Leaf("go to work")
        )
    a_person.get_behavior_tree()\
        .add_child(
            core.life.behavior_tree.Node("node", 1.0)
        ).get_child_by_name(
            "node"
        ).add_child(
            core.life.behavior_tree.Leaf("first work with high priority", 0.8)
        ).add_child(
            core.life.behavior_tree.Leaf("second work with low priority", 0.1)
        ).add_child(
            core.life.behavior_tree.Leaf("third work with normal priority", 0.5)
        )
    a_person.add_scheduled_event(
        core.life.time.Event(
            "going to see the boss",
            core.life.time.TriggerEvent(
                at=0,
                cond=[
                    core.life.time.Condition("time", 3, 0.5),
                    core.life.time.Condition("end_time", 5, 0.5)
                ]
            ),
            core.life.time.Action(
                name="moving and going to see the boss -action"
            )
        )
    )

    city = core.town.city.City("SmallVille")
    city.add_clock(the_time)\
        .add_street(
            core.town.street.Street(street1)
        ).add_street(
            core.town.street.Street(street2)
        ).add_street(
            core.town.street.Street(street3)
        )
    city.get_street_by_name(street1)\
        .connect_to(city.get_street_by_name(street2))\
        .connect_to(city.get_street_by_name(street3))
    city.get_street_by_name(street1)\
        .add(core.town.buildings.House(
            "A house",
            city.get_street_by_name(street1)
        ))
    city.get_street_by_name(street1)\
        .get_buildind_by_name("A house")\
        .add_settler(a_person)

    print_city_streets_and_connections(city)
    print("\n" + "- " * 10 + "\n")

    while True:
        print("Evolving - Time is {}".format(the_time))
        city.evolve()
        the_time.next()
        time.sleep(0.5)
        print("- " * 10)


if __name__ == '__main__':
    main()