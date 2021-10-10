from requests import get as get_page
from bs4 import BeautifulSoup
import json


def get_homepage():
    """Performs an HTTP GET to Metlink's homepage

    Returns:
        str: The homepage as an HTML string
    """
    response = get_page('https://www.metlink.org.nz/')
    return response.text


def get_opendata_api_key():
    """Gets Metlink's homepage and scrapes the API key out of a JSON object which is in a body attribute

    Returns:
        str: The API key needed to make requests to the opendata server
    """
    soup = BeautifulSoup(get_homepage(), 'html.parser')
    body = soup.find('body')
    app_settings = json.loads(body['data-app-settings'])

    return app_settings['api']['apiGatewayKey']
