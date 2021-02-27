from ..classes.trains import Trains
from ..classes.other import Ferries, CableCar


def bus(informed_entity):
    route_id = informed_entity["route_id"]

    # handle night buses
    if len(route_id) == 4 and route_id[:3] == "991":
        return "N" + route_id[-1]
    elif len(route_id) == 4 and route_id[:2] == "99":
        return "N" + route_id[2:]

    else:
        express_route = route_id[-1] == "1"

        route_id = route_id[:-1]
        if express_route:
            route_id += "e"

        return route_id


def train(informed_entity):
    return Trains.from_route_id(informed_entity["route_id"])


def ferry(informed_entity):
    return Ferries.from_route_id(informed_entity["route_id"])


def cable_car(informed_entity):
    return CableCar.from_route_id(informed_entity["route_id"])


# found in Metlink's app.js bundle:
#
# MODE_IDS: {
#     bus: [3],
#     train: [0, 1, 2],
#     school: [6, 712],
#     "cable-car": [5],
#     ferry: [4],
#     other: [4, 5]
# }
def parse_informed_entity(informed_entity):
    if "route_id" in informed_entity:
        if informed_entity["route_type"] in (0, 1, 2):
            return train(informed_entity)
        elif informed_entity["route_type"] == 4:
            return ferry(informed_entity)
        elif informed_entity["route_type"] == 5:
            return cable_car(informed_entity)
        elif informed_entity["route_type"] in (3, 6, 712):
            return bus(informed_entity)
