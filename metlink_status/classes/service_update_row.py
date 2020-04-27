from .service_update_type import *
from colorama import Fore


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
