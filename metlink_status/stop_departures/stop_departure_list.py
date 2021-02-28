import requests
from .stop_departure import StopDeparture


class StopDepartureList:

    def __init__(self, stop):
        self.stop = stop
        self.closed = False
        self.departures = []

    def get_departures(self):
        response = requests.get(f"https://backend.metlink.org.nz/api/v1/stopdepartures/{self.stop}").json()

        self.closed = response["closed"]
        self.departures = [StopDeparture(departure) for departure in response["departures"]]

    def get_items(self, user_service=None):
        if user_service:
            return [departure for departure in self.departures if departure.service_id.upper() == user_service.upper()]
        else:
            return self.departures
