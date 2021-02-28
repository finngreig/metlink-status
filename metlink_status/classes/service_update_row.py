from .service_update_type import *
from colorama import Fore
from datetime import datetime
from ..parser import parse_informed_entity
from ..gtfs_rt import Cause, Effect


class ServiceUpdateRow:
    def __init__(self, update_type, title, description, link, valid_from, affected_services):
        self.update_type = update_type
        self.title = title
        self.description = description
        self.link = link
        self.valid_from = valid_from
        self.affected_services = affected_services

    def is_service_affected(self, service):
        if service.upper() in self.affected_services:
            return True
        else:
            return False

    def colorize(self, text):
        if self.update_type == ServiceUpdateType.MAJOR:
            color = Fore.RED
        elif self.update_type == ServiceUpdateType.DELAYS_ALERTS or \
                self.update_type == ServiceUpdateType.CLOSURES_DIVERSIONS:
            color = Fore.YELLOW
        elif self.update_type == ServiceUpdateType.SERVICE_CHANGES or \
                self.update_type == ServiceUpdateType.BUS_REPLACEMENT:
            color = Fore.CYAN
        else:
            return text

        return color + text + Fore.RESET

    def __str__(self):
        string = f'{self.colorize(self.update_type.value)}\n{self.colorize(self.title)}\n'

        if self.description:
            string += f'{self.description}\n'
        if self.valid_from:
            string += f'{self.valid_from}\n'
        if self.link:
            string += f'{self.link}\n'

        return string


class GTFSRTServiceUpdateItem:

    def __init__(self, alert_json):
        alert = alert_json["alert"]

        self.start_time = str(datetime.fromtimestamp(alert["active_period"][0]["start"]))
        self.end_time = str(datetime.fromtimestamp(alert["active_period"][0]["end"]))
        self.cause = Cause[alert["cause"]]
        self.description = alert["description_text"]["translation"][0]["text"]
        self.effect = Effect[alert["effect"]]
        self.header = alert["header_text"]["translation"][0]["text"]

        self.stop_ids = []
        self.route_ids = []
        for entity in alert["informed_entity"]:
            if "stop_id" in entity:
                self.stop_ids.append(entity["stop_id"])
            elif "route_id" in entity:
                self.route_ids.append(parse_informed_entity(entity))

        self.severity_level = alert["severity_level"]
        self.url = alert["url"]["translation"][0]["text"]

        self.id = alert_json["id"]
        self.timestamp = datetime.strptime(alert_json["timestamp"], "%Y-%m-%dT%H:%M:%S%z")

    def is_service_affected(self, service):
        if service.upper() in [str(rid) for rid in self.route_ids]:
            return True
        else:
            return False

    def __str__(self):
        text = ""

        if self.severity_level == "SEVERE":
            text += Fore.RED
        elif self.severity_level == "WARNING":
            text += Fore.YELLOW
        elif self.severity_level == "INFO":
            text += Fore.CYAN

        text += (f"From {self.start_time} until {self.end_time}\n"
                 f"Cause: {self.cause}\n"
                 f"Effect: {self.effect}\n"
                 f"Header: {self.header}\n"
                 f"Description: {self.description}\n"
                 f"Severity: {self.severity_level}\n")

        if len(self.stop_ids) > 0:
            text += f"Stops: {', '.join(self.stop_ids)}\n"
        if len(self.route_ids) > 0:
            text += f"Routes: {', '.join([str(rid) for rid in self.route_ids])}\n"

        if self.url:
            text += f"Link to more information: {self.url}\n"

        text += Fore.RESET

        return text
