from ..parser import get_opendata_api_key
import requests
from .service_update_row import GTFSRTServiceUpdateItem


class GTFSRTServiceUpdateList:
    def __init__(self):
        self.api_key = get_opendata_api_key()
        self.items = []

    def get_service_alerts(self):
        response = requests.get("https://api.opendata.metlink.org.nz/v1/gtfs-rt/servicealerts",
                                headers={
                                    'x-api-key': self.api_key,
                                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
                                    'origin': 'https://www.metlink.org.nz',
                                    'referer': 'https://www.metlink.org.nz/alerts/train/today'
                                }).json()

        self.items = [GTFSRTServiceUpdateItem(alert_json) for alert_json in response["entity"]]

    def get_items(self, user_service=None):
        if user_service:
            return [str(service) for service in self.items if service.is_service_affected(user_service)]
        else:
            return self.items
