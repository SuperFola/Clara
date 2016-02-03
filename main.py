__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

import sys
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


def main(*args):
    street1 = "Baxbaxwalanuksiwe"
    street2 = "Ardakaniz"
    street3 = "Qames"
    print(core.constants.NAME + " is starting ...")

    the_time = core.life.time.Time()

    a_person = core.life.person.Person("Patrick", "Doe", 0)
    a_person.get_behavior_tree()\
        .add_child(
            core.life.behavior_tree.Sequence("sequence", 0.5)
        ).get_child_by_name("sequence")\
        .add_child(
            core.life.behavior_tree.Leaf("eat")
        ).add_child(
            core.life.behavior_tree.Leaf("sleep")
        ).add_child(
            core.life.behavior_tree.Leaf("wake up")
        ).add_child(
            core.life.behavior_tree.Leaf("go to work")
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
        .add(core.town.buildings.House("A house"))
    city.get_street_by_name(street1)\
        .get_buildind_by_name("A house")\
        .add_settler(a_person)

    print_city_streets_and_connections(city)

    while True:
        print("Evolving - Time is {}".format(the_time))
        the_time.next()
        city.evolve()
        time.sleep(0.5)


if __name__ == '__main__':
    main(*sys.argv[1:] if sys.argv[1:] else [])