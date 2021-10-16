import io
import sys

from metlink_status.cli import print_list
from metlink_status.helpers import APIHelper
from metlink_status.service_updates import GTFSRTServiceUpdateList
from metlink_status.stop_departures import StopDepartureList


def call(bus=None, train=None, stop=None):
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    api_helper = APIHelper()

    update_list = GTFSRTServiceUpdateList(api_helper)
    update_list.get_service_alerts()

    if bus:
        print_list(update_list, bus)
    elif train:
        print_list(update_list, train)
    else:
        print_list(update_list)

    if stop:
        departure_list = StopDepartureList(api_helper, stop)
        departure_list.get_departures()

        if bus and train:
            print_list(departure_list, bus)
            print_list(departure_list, train)
        elif bus:
            print_list(departure_list, bus)
        elif train:
            print_list(departure_list, train)
        else:
            print_list(departure_list)

    output = new_stdout.getvalue()
    sys.stdout = old_stdout

    return output
