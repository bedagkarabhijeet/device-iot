

from enum import Enum


class SensorExceptionTypes(Enum):
    SENSOR_NOT_PRESENT = "Device '{0}' not present in the system; Please rechecked specified id"


class SensorException(Exception):
    def __init__(self, error_type):
        self.error_type = error_type
