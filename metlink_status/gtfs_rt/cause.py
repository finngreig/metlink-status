from enum import Enum


class Cause(Enum):
    UNKNOWN_CAUSE = "Unknown"
    OTHER_CAUSE = "Other"
    TECHNICAL_PROBLEM = "Technical Problem"
    STRIKE = "Strike"
    DEMONSTRATION = "Demonstration"
    ACCIDENT = "Accident"
    HOLIDAY = "Holiday"
    WEATHER = "Weather"
    MAINTENANCE = "Maintenance"
    CONSTRUCTION = "Construction"
    POLICE_ACTIVITY = "Police Activity"
    MEDICAL_EMERGENCY = "Medical Emergency"

    def __str__(self):
        return self.value
