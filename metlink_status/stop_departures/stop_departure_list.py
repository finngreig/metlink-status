import requests
from ..parser import get_opendata_api_key
from .stop_departure_row import StopDeparture


class StopDepartureList:
    """
    Class that handles and stores getting a list of stop departures from Metlink's API
    """

    def __init__(self, stop):
        """Constructor

        Args:
            stop (str): The stop ID to get departures for
        """
        self.api_key = get_opendata_api_key()
        self.stop = stop
        self.closed = False
        self.departures = []

    def get_departures(self):
        """Function to get stop departures from Metlink's API, and unpack them into a list
        """
        response = requests.get(f"https://api.opendata.metlink.org.nz/v1/stop-predictions?stop_id={self.stop}",
                                headers={
                                    "x-api-key": self.api_key
                                }).json()

        self.closed = response["closed"]
        self.departures = [StopDeparture(departure) for departure in response["departures"]]

    def get_items(self, user_service=None):
        """Getter for the stop departures list. If a user service is provided it will return a list with relevant
        departures

        Args:
            user_service (str): The route ID of the relevant user service

        Returns:
            list[StopDeparture]: The relevant stop departures
        """
        if user_service:
            return [departure for departure in self.departures if departure.service_id.upper() == user_service.upper()]
        else:
            return self.departures
