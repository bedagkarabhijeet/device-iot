
from DataAccess.device_data_access import DeviceDataAccess
from DataAccess.sensor_data_access import SensorDataAccess
from DataAccess.device_sensor_mapping_data_access import DeviceSensorMappingDataAccess
from DataAccess.sensor_event_data_access import SensorEventDataAccess


class UOW:
    """
    Unit of work pattern it is a gateway to fetch data access classes for providers layer
    """
    def __init__(self, cursor):
        self.__cursor = cursor

    def get_device_data_access(self):
        return DeviceDataAccess(self.__cursor)

    def get_sensor_data_access(self):
        return SensorDataAccess(self.__cursor)

    def get_device_sensor_mapping_data_access(self):
        return DeviceSensorMappingDataAccess(self.__cursor)

    def get_sensor_event_data_access(self):
        return SensorEventDataAccess(self.__cursor)
