

class DeviceDataAccess:
    def __init__(self, cursor):
        self.__cursor = cursor

    def insert(self, device_model):
        sql_query = "INSERT INTO device (device_hardware_id, device_name) VALUES (%s, %s) " \
                    "RETURNING device_id, device_hardware_id"

        self.__cursor.execute(sql_query, (str(device_model.hardware_id), device_model.name))

        return self.__cursor.fetchone()

    def update(self, device_model):
        sql_query = "UPDATE device SET device_name=(%s) WHERE device_hardware_id = (%s) AND is_deleted=False " \
                    "RETURNING device_id"
        self.__cursor.execute(sql_query, (device_model.name, str(device_model.hardware_id)))

        return self.__cursor.fetchone()

    def select_all(self):
        sql_query = "SELECT device_hardware_id, device_name FROM device WHERE is_deleted=False "
        self.__cursor.execute(sql_query)
        return self.__cursor.fetchall()
