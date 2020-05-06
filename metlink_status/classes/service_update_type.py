from enum import Enum


class ServiceUpdateType(Enum):
    MAJOR = 'Major'
    OTHER = 'Info'
    DELAYS_ALERTS = 'Delays & Alerts'
    SERVICE_CHANGES = 'Service Changes'
    CLOSURES_DIVERSIONS = 'Closures & Diversions'
    BUS_REPLACEMENT = 'Buses Replace Trains'
    UNKNOWN = 'Unknown Type'
