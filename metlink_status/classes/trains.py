from enum import Enum


class Trains(Enum):
    KPL = "KPL"
    MEL = "MEL"
    WRL = "WRL"
    HVL = "HVL"
    JVL = "JVL"

    @staticmethod
    def from_route_id(rid):
        if rid == "2":
            return Trains.KPL
        elif rid == "3":
            return Trains.MEL
        elif rid == "4":
            return Trains.JVL
        elif rid == "5":
            return Trains.WRL
        elif rid == "6":
            return Trains.HVL
        else:
            print("Got unknown route ID " + rid, type(rid))
            raise NotImplementedError

    def __str__(self):
        return self.value
