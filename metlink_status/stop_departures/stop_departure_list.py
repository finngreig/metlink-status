import requests
from ..parser import get_opendata_api_key
from .stop_departure import StopDeparture


class StopDepartureList:

    def __init__(self, stop):
        self.api_key = get_opendata_api_key()
        self.stop = stop
        self.closed = False
        self.departures = []

    def get_departures(self):
        response = requests.get(f"https://api.opendata.metlink.org.nz/v1/stop-predictions?stop_id={self.stop}",
                                headers={
                                    "x-api-key": self.api_key
                                }).json()

        self.closed = response["closed"]
        self.departures = [StopDeparture(departure) for departure in response["departures"]]

    def get_items(self, user_service=None):
        if user_service:
            return [departure for departure in self.departures if departure.service_id.upper() == user_service.upper()]
        else:
            return self.departures
