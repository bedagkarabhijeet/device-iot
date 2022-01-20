

class DeviceSensorMappingDataAccess:
    def __init__(self, cursor):
        self.__cursor = cursor

    def insert(self, device_id, sensor_ids):
        args = ','.join(self.__cursor.mogrify("(%s,%s)", i).decode('utf-8')
                        for i in {(device_id, s) for s in sensor_ids})
        self.__cursor.execute("INSERT INTO device_sensor_mapping VALUES " + args)

    def select(self):
        return