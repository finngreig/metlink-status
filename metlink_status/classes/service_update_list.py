from ..parser import get_opendata_api_key
import requests
from .service_update_row import GTFSRTServiceUpdateItem


class ServiceUpdateList:
    def __init__(self, rows):
        self.rows = rows

    def get_rows(self, user_service=None):
        if user_service:
            return [service for service in self.rows if service.is_service_affected(user_service)]
        else:
            return self.rows

    def is_empty(self):
        return len(self.rows) == 0


class GTFSRTServiceUpdateList:
    def __init__(self):
        self.api_key = get_opendata_api_key()
        self.items = []

    def get_service_alerts(self):
        response = requests.get("https://api.opendata.metlink.org.nz/v1/gtfs-rt/servicealerts",
                                headers={
                                    'x-api-key': self.api_key
                                }).json()

        self.items = [GTFSRTServiceUpdateItem(alert_json) for alert_json in response["entity"]]

    def get_items(self, user_service=None):
        if user_service:
            return [str(service) for service in self.items if service.is_service_affected(user_service)]
        else:
            return self.items
