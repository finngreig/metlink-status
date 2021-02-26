from requests import get as get_page
from bs4 import BeautifulSoup
# from ..classes import ServiceUpdateList
# from ..classes import ServiceUpdateRow
# from ..classes import ServiceUpdateType
# import re
import json

HOST = 'https://www.metlink.org.nz'


# def get_service_update_page():
#     response = get_page('https://www.metlink.org.nz/service-updates')
#     return response.text


def get_homepage():
    response = get_page('https://www.metlink.org.nz/')
    return response.text


# def parse_update(update):
#     raw_details = update.find(class_='serviceUpdateItemDetails')
#
#     description_and_link = raw_details.find('p')
#     title_and_type = raw_details.find('h5')
#
#     update_type = title_and_type.find('span').get('title')
#     if update_type == 'Major' or update_type == 'Major Important':
#         update_type = ServiceUpdateType.MAJOR
#     elif update_type == 'Other':
#         update_type = ServiceUpdateType.OTHER
#     elif update_type == 'Delays & Alerts':
#         update_type = ServiceUpdateType.DELAYS_ALERTS
#     elif update_type == 'Service Changes':
#         update_type = ServiceUpdateType.SERVICE_CHANGES
#     elif update_type == 'Road Closures & Diversions':
#         update_type = ServiceUpdateType.CLOSURES_DIVERSIONS
#     elif update_type == 'Buses Replace Trains':
#         update_type = ServiceUpdateType.BUS_REPLACEMENT
#     else:
#         update_type = ServiceUpdateType.UNKNOWN
#
#     title = title_and_type.get_text()
#
#     if description_and_link:
#         description = re.search(r'.+?(?=…)', description_and_link.get_text()).group()
#         link = HOST + description_and_link.find('a', href=True)['href']
#     else:
#         description = ''
#         link = ''
#
#     if raw_details.find('small'):
#         valid_from = re.sub(r'\s+', ' ', raw_details.find('small').get_text())
#     else:
#         valid_from = ''
#
#     affected_services = []
#     raw_affected_services = update.select('div.col-xs-12.col-sm-5.col-md-3')
#
#     if len(raw_affected_services) == 1:
#         for service in raw_affected_services[0].find_all('span', class_='routeNumber', recursive=True):
#             affected_services.append(service.get_text().upper())
#
#     return ServiceUpdateRow(update_type, title, description, link, valid_from, affected_services)
#
#
# def parse(service_type=None):
#     soup = BeautifulSoup(get_service_update_page(), 'lxml')
#     rows = []
#
#     if service_type == 'bus':
#         category = soup.find(id='ServiceUpdates-Bus')
#         updates = category.find_all(class_='serviceUpdateItem', recursive=True)
#     elif service_type == 'train':
#         category = soup.find(id='ServiceUpdates-Train')
#         updates = category.find_all(class_='serviceUpdateItem', recursive=True)
#     else:
#         updates = soup.find_all(class_='serviceUpdateItem', recursive=True)
#
#     for update in updates:
#         rows.append(parse_update(update))
#
#     return ServiceUpdateList(rows)


def get_opendata_api_key():
    soup = BeautifulSoup(get_homepage(), 'lxml')
    body = soup.find('body')
    app_settings = json.loads(body['data-app-settings'])

    return app_settings['api']['apiGatewayKey']
