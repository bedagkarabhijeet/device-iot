

class DeviceSensorMappingDataAccess:
    def __init__(self, cursor):
        self.__cursor = cursor

    def insert(self, device_id, sensor_ids):
        """
        Insert device and sensor mapping
        :param device_id: Id of device
        :param sensor_ids: Ids of sensors
        """
        args = ','.join(self.__cursor.mogrify("(%s,%s)", i).decode('utf-8')
                        for i in {(device_id, s) for s in sensor_ids})
        self.__cursor.execute("INSERT INTO device_sensor_mapping VALUES " + args)
