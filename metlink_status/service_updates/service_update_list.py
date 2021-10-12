from .service_update_row import GTFSRTServiceUpdateItem


class GTFSRTServiceUpdateList:
    """
    Class that handles and stores getting a list of service alerts from the GTFS-RT service
    """
    def __init__(self, api_helper):
        """
        Constructor - gets the latest API key and initialises the list that stores alerts
        """
        self.items = []
        self.api_helper = api_helper

    def get_service_alerts(self):
        """Function to get all alerts from Metlink's GTFS-RT REST server
        """
        response = self.api_helper.do_json_request("https://api.opendata.metlink.org.nz/v1/gtfs-rt/servicealerts")

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
