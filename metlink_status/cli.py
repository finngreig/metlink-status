from argparse import ArgumentParser
# from .parser import parse
from colorama import init as colorama_init
from .classes import GTFSRTServiceUpdateList


def print_list(update_list, service=None):
    for row in update_list.get_items(service):
        print(row)


def main():
    colorama_init()
    
    argument_parser = ArgumentParser(description='Prints Metlink service updates')
    argument_parser.add_argument('-b', '--bus', type=str, help="Specifies a bus route")
    argument_parser.add_argument('-t', '--train', type=str, help="Specifies a train line")
    args = argument_parser.parse_args()

    update_list = GTFSRTServiceUpdateList()
    update_list.get_service_alerts()

    if args.bus:
        print_list(update_list, args.bus)
    elif args.train:
        print_list(update_list, args.train)
    else:
        print_list(update_list)

