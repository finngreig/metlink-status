from enum import Enum


class Ferries(Enum):
    WHF = "WHF"

    @staticmethod
    def from_route_id(rid):
        if rid == "8":
            return Ferries.WHF
        else:
            raise NotImplementedError

    def __str__(self):
        return self.value


class CableCar(Enum):
    CCL = "CCL"

    @staticmethod
    def from_route_id(rid):
        if rid == "9":
            return CableCar.CCL
        else:
            raise NotImplementedError

    def __str__(self):
        return self.value
