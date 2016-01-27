__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

import sys
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
    if args:
        city_name, *streets = args
    else:
        city_name, *streets = "SmallVille", "Baxbaxwalanuksiwe", "Ardakaniz", "Qames"
    print(core.constants.NAME + " is starting ...")
    city = core.town.city.City(city_name)
    baxbax_street = core.town.street.Street(streets[0])
    arda_street = core.town.street.Street(streets[1])
    qames_street = core.town.street.Street(streets[2])
    city.add_street(baxbax_street).add_street(arda_street).add_street(qames_street)
    city.get_street_by_name(streets[0]).connect_to(city.get_street_by_name(streets[1])).connect_to(city.get_street_by_name(streets[2]))

    print_city_streets_and_connections(city)


if __name__ == '__main__':
    main(*sys.argv[1:] if sys.argv[1:] else [])