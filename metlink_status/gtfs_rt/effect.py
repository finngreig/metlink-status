from enum import Enum


class Effect(Enum):
    NO_SERVICE = "No Service"
    REDUCED_SERVICE = "Reduced Service"
    SIGNIFICANT_DELAYS = "Significant Delays"
    DETOUR = "Detour"
    ADDITIONAL_SERVICE = "Additional Service"
    MODIFIED_SERVICE = "Modified Service"
    OTHER_EFFECT = "Other"
    UNKNOWN_EFFECT = "Unknown"
    STOP_MOVED = "Stop Moved"
    NO_EFFECT = "None"
    ACCESSIBILITY_ISSUE = "Accessibility Issue"

    def __str__(self):
        return self.value
