from .service_update_type import *
from colorama import Fore
from datetime import datetime


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
        self.cause = alert["cause"]
        self.description = alert["description_text"]["translation"][0]["text"]
        self.effect = alert["effect"]
        self.header = alert["header_text"]["translation"][0]["text"]

        self.route_ids = []
        for entity in alert["informed_entity"]:
            if "stop_id" in entity:
                self.route_ids.append(entity["stop_id"])
            elif "route_id" in entity:
                if entity["route_type"] == 2:
                    self.route_ids.append(entity["route_id"])
                else:
                    self.route_ids.append(str(int(entity["route_id"]) // 10))

        self.severity_level = alert["severity_level"]
        self.url = alert["url"]["translation"][0]["text"]

        self.id = alert_json["id"]
        self.timestamp = datetime.strptime(alert_json["timestamp"], "%Y-%m-%dT%H:%M:%S%z")

    def __str__(self):
        text = f"From {self.start_time} until {self.end_time}\nCause: {self.cause}\nEffect: {self.effect}\nHeader: {self.header}\nDescription: {self.description}\nRoutes: {', '.join(self.route_ids)}\nSeverity: {self.severity_level}\n"

        if self.url:
            text += f"Link to more information: {self.url}\n"

        return text
