from enum import Enum


class Trains(Enum):
    """
    Convenience enum for train routes
    """

    KPL = "KPL"
    MEL = "MEL"
    WRL = "WRL"
    HVL = "HVL"
    JVL = "JVL"

    @staticmethod
    def from_route_id(rid):
        """Turns a route ID string into a Trains enum

        Args:
            rid (str): The route ID

        Returns:
            enum: The Trains enum value for that particular route
        """

        if rid == "2":
            return Trains.KPL
        elif rid == "3":
            return Trains.MEL
        elif rid == "4":
            return Trains.WRL
        elif rid == "5":
            return Trains.HVL
        elif rid == "6":
            return Trains.JVL
        else:
            print("Got unknown route ID " + rid, type(rid))
            raise NotImplementedError

    def __str__(self):
        """String representation function

        Returns:
            str: The value
        """
        return self.value
