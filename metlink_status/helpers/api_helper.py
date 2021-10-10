from requests import get as http_get
from bs4 import BeautifulSoup
import json


class APIHelper:
    """
    Helper class with convenience functions for the Metlink API
    """

    def __init__(self):
        """Constructor
        """
        self.api_key = ""
        self.get_opendata_api_key()

    def get_opendata_api_key(self):
        """Gets Metlink's homepage and scrapes the API key out of a JSON object which is in a body attribute

        Returns:
            str: The API key needed to make requests to the opendata server
        """
        response = http_get('https://www.metlink.org.nz/')

        soup = BeautifulSoup(response.text, 'html.parser')
        body = soup.find('body')
        app_settings = json.loads(body['data-app-settings'])

        self.api_key = app_settings['api']['apiGatewayKey']

    def do_json_request(self, url):
        """Performs an HTTP request with all necessary headers, and unpacks the JSON into a dict

        Args:
            url (str): The URL to GET

        Returns:
            dict: The JSON unpacked as a dict
        """
        return http_get(url,
                        headers={
                            'x-api-key': self.api_key,
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ('
                                          'KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 '
                                          'Edg/88.0.705.81',
                            'origin': 'https://www.metlink.org.nz',
                            'referer': 'https://www.metlink.org.nz/alerts/train/today'
                        }).json()
