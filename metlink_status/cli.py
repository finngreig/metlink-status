from argparse import ArgumentParser
from colorama import init as colorama_init
from .helpers import APIHelper
from .service_alerts import GTFSRTServiceUpdateList
from .stop_departures import StopDepartureList


def print_list(update_list, service=None):
    """Helper function which ensures a list of updates/alerts are scoped to a specific service if needed, and then
    prints them

    Args:
        update_list (GTFSRTServiceUpdateList|StopDepartureList): The update list
        service (str): The user service to scope to
    """
    for row in update_list.get_items(service):
        print(row)


def main():
    """Main function that parses CLI arguments and creates lists and prints them
    """
    colorama_init()
    
    argument_parser = ArgumentParser(description='Prints Metlink service updates')
    argument_parser.add_argument('-b', '--bus', type=str, help="Specifies a bus route")
    argument_parser.add_argument('-t', '--train', type=str, help="Specifies a train line")
    argument_parser.add_argument('-s', '--stop', type=str, help="Specifies a stop or station")
    args = argument_parser.parse_args()

    api_helper = APIHelper()

    update_list = GTFSRTServiceUpdateList(api_helper)
    update_list.get_service_alerts()

    if args.bus:
        print_list(update_list, args.bus)
    elif args.train:
        print_list(update_list, args.train)
    else:
        print_list(update_list)

    if args.stop:
        departure_list = StopDepartureList(api_helper, args.stop)
        departure_list.get_departures()

        if args.bus and args.train:
            print_list(departure_list, args.bus)
            print_list(departure_list, args.train)
        elif args.bus:
            print_list(departure_list, args.bus)
        elif args.train:
            print_list(departure_list, args.train)
        else:
            print_list(departure_list)
