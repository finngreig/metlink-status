from enum import Enum


class ServiceUpdateType(Enum):
    """
    Convenience enum for service update/alert types
    """

    MAJOR = 'Major'
    OTHER = 'Info'
    DELAYS_ALERTS = 'Delays & Alerts'
    SERVICE_CHANGES = 'Service Changes'
    CLOSURES_DIVERSIONS = 'Closures & Diversions'
    BUS_REPLACEMENT = 'Buses Replace Trains'
    UNKNOWN = 'Unknown Type'
