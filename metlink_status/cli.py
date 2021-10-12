from argparse import ArgumentParser
from colorama import init as colorama_init
from .helpers import APIHelper
from .service_updates import GTFSRTServiceUpdateList
from .stop_departures import StopDepartureList
from rich.console import Console
from rich.table import Table

console = Console()


def print_list(update_list, service=None):
    """Helper function which ensures a list of updates/alerts are scoped to a specific service if needed, and then
    prints them

    Args:
        update_list (GTFSRTServiceUpdateList|StopDepartureList): The update list
        service (str): The user service to scope to
    """
    table = Table(show_header=True)

    if isinstance(update_list, GTFSRTServiceUpdateList):
        table.add_column("From", width=10)
        table.add_column("Until", width=10)
        table.add_column("Cause")
        table.add_column("Effect")
        table.add_column("Summary")
        table.add_column("Description")
        table.add_column("Severity")
        table.add_column("Stops")
        table.add_column("Routes")
        # table.add_column("Link", width=50)

        for row in update_list.get_items(service):
            table.add_row(row.start_time, row.end_time, row.cause.value, row.effect.value, row.header, row.description,
                          row.severity_level, ', '.join(row.stop_ids), ', '.join([str(rid) for rid in row.route_ids]))
            # row.url)
    elif isinstance(update_list, StopDepartureList):
        table.add_column("Time")
        table.add_column("Delay")
        table.add_column("Destination")
        table.add_column("Origin")
        table.add_column("Service")
        table.add_column("Wheelchair Accessible")
        table.add_column("Status")
        table.add_column("Vehicle ID")

        for row in update_list.get_items(service):
            table.add_row(row.time.strftime("%m/%d/%Y, %H:%M:%S"), str(row.delay),
                          f"{row.destination} - {row.destination_stop_id}",
                          f"{row.origin} - {row.origin_stop_id}", str(row.service_id),
                          f"{'Yes' if row.wheelchair_accessible else 'No'}", row.status, str(row.vehicle_id))

    console.print(table)


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
