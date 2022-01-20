

from enum import Enum


class DeviceExceptionTypes(Enum):
    DEVICE_ALREADY_REGISTERED = "Device '{0}' has already been registered"
    DEVICE_NOT_PRESENT = "Device '{0}' not present in the system; Please rechecked specified id"


class DeviceException(Exception):
    def __init__(self, error_type):
        self.error_type = error_type
