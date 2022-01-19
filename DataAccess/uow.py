
from DataAccess.device_data_access import DeviceDataAccess


class UOW:
    """
    Unit of work pattern it is a gateway to fetch data access classes for providers layer
    """
    def __init__(self, cursor):
        self.__cursor = cursor

    def device_access_data_access(self):
        return DeviceDataAccess(self.__cursor)
