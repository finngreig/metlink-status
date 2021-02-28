from datetime import datetime


def parse_delay(delay):
    number_str_array = [c for c in delay if c.isdigit()]
    number = int(''.join(number_str_array))

    if delay[0] == "-":
        return -number
    else:
        return number


class StopDeparture:

    def __init__(self, json_obj):
        if json_obj["arrival"]["expected"] != "":
            self.time = json_obj["arrival"]["expected"]
        elif json_obj["arrival"]["aimed"] != "":
            self.time = json_obj["arrival"]["aimed"]
        elif json_obj["departure"]["expected"]:
            self.time = json_obj["departure"]["expected"]
        else:
            self.time = json_obj["departure"]["aimed"]
        self.time = datetime.strptime(self.time, "%Y-%m-%dT%H:%M:%S%z")

        self.delay = parse_delay(json_obj["delay"])
        self.destination = json_obj["destination"]["name"]
        self.destination_stop_id = json_obj["destination"]["stop_id"]
        self.name = json_obj["name"][:-2]
        self.origin = json_obj["origin"]["name"]
        self.origin_stop_id = json_obj["origin"]["stop_id"]
        self.service_id = json_obj["service_id"]
        self.status = json_obj["status"]    # can be empty
        self.vehicle_id = json_obj["vehicle_id"]    # can be empty
        self.wheelchair_accessible = json_obj["wheelchair_accessible"]

    def __str__(self):
        text = (f"Time: {self.time}\n"
                f"Difference: {self.delay}s\n"
                f"Destination: {self.destination} - {self.destination_stop_id}\n"
                # f"Name: {self.name}\n"
                f"Origin: {self.origin} - {self.origin_stop_id}\n"
                f"Service: {self.service_id}\n"
                f"Wheelchair Accessible: {'Yes' if self.wheelchair_accessible else 'No'}\n")

        if self.status != "":
            text += f"Status: {self.status}\n"
        if self.vehicle_id != "":
            text += f"Vehicle ID: {self.vehicle_id}\n"

        return text
