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

    # if args.bus:
    #     service_updates = parse('bus')
    #     print_list(service_updates, args.bus)
    # elif args.train:
    #     service_updates = parse('train')
    #     print_list(service_updates, args.train)
    # else:
    #     service_updates = parse()
    #     print_list(service_updates)

    update_list = GTFSRTServiceUpdateList()
    update_list.get_service_alerts()
    print_list(update_list)
