class StopDeparture:

    def __init__(self, json_dict):
        if json_dict["arrival"]["expected"] is not "":
            self.arrival = json_dict["arrival"]["expected"]
        else:
            self.arrival = json_dict["arrival"]["aimed"]

        self.origin_id = json_dict["origin"]["stop_id"]
        self.origin = json_dict["origin"]["name"]

        self.destination_id = json_dict["destination"]["stop_id"]
        self.destination = json_dict["destination"]["name"]

        self.service_id = json_dict["service_id"]
        self.status = json_dict["status"]
        self.accessible = json_dict["wheelchair_accessible"]

        # TODO: parse delay field
