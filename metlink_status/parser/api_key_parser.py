from requests import get as get_page
from bs4 import BeautifulSoup
import json


def get_homepage():
    response = get_page('https://www.metlink.org.nz/')
    return response.text


def get_opendata_api_key():
    soup = BeautifulSoup(get_homepage(), 'html.parser')
    body = soup.find('body')
    app_settings = json.loads(body['data-app-settings'])

    return app_settings['api']['apiGatewayKey']
