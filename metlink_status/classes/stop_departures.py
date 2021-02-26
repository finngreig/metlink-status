import requests
from .stop_departure import StopDeparture


class StopDepartures:

    def __init__(self, stop_id):
        self.stop_id = stop_id
        self.departures = []

    def get_departures(self):
        response = requests\
            .get(f"https://backend.metlink.org.nz/api/v1/stopdepartures/{self.stop_id}")\
            .json()

        self.departures = [StopDeparture(stop_dep) for stop_dep in response["departures"]]
