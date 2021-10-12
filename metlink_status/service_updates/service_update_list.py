from ..parser import get_opendata_api_key
import requests
from .service_update_row import GTFSRTServiceUpdateItem


class GTFSRTServiceUpdateList:
    """
    Class that handles and stores getting a list of service alerts from the GTFS-RT service
    """
    def __init__(self):
        """
        Constructor - gets the latest API key and initialises the list that stores alerts
        """
        self.api_key = get_opendata_api_key()
        self.items = []

    def get_service_alerts(self):
        """Function to get all alerts from Metlink's GTFS-RT REST server
        """
        response = requests.get("https://api.opendata.metlink.org.nz/v1/gtfs-rt/servicealerts",
                                headers={
                                    'x-api-key': self.api_key,
                                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ('
                                                  'KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 '
                                                  'Edg/88.0.705.81',
                                    'origin': 'https://www.metlink.org.nz',
                                    'referer': 'https://www.metlink.org.nz/alerts/train/today'
                                }).json()

        self.items = [GTFSRTServiceUpdateItem(alert_json) for alert_json in response["entity"]]

    def get_items(self, user_service=None):
        """Getter for the service alerts list. If a user service is provided it will return a list with relevant alerts
        only.

        Args:
            user_service (str): The route ID of the relevant user service

        Returns:
            list[GTFSRTServiceUpdateItem] | list[str]: The relevant service alerts
        """
        if user_service:
            return [str(service) for service in self.items if service.is_service_affected(user_service)]
        else:
            return self.items
