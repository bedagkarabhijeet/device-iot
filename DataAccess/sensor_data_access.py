

class SensorDataAccess:
    def __init__(self, cursor):
        self.__cursor = cursor

    def insert(self, sensor_model):
        """
        Insert new sensors in the system
        :param sensor_model: Sensor data
        """
        sql_query = "INSERT INTO sensor (sensor_hardware_id, sensor_name, sensor_type) " \
                    "VALUES (%s, %s, %s) RETURNING sensor_id, sensor_hardware_id"

        self.__cursor.execute(sql_query, (str(sensor_model.hardware_id), sensor_model.name, sensor_model.type.value))

        output = self.__cursor.fetchone()

        if output and output.get("sensor_hardware_id"):
            return output
        else:
            raise Exception("Failed while inserting record")

    def select(self, hardware_id):
        """
        Fetch sensor data based on hardware_id
        :param hardware_id:
        :return: Sensor data
        """
        sql_query = f"SELECT sensor_id, sensor_hardware_id, sensor_name, sensor_type " \
                    f"FROM sensor WHERE is_deleted=False AND sensor_hardware_id='{str(hardware_id)}'"

        self.__cursor.execute(sql_query)

        return self.__cursor.fetchone()

    def select_all(self):
        """
        Fetch all sensors in the system
        :return: ll sensors
        """
        sql_query = "SELECT sensor_hardware_id, sensor_name, sensor_type FROM sensor WHERE is_deleted=False"

        self.__cursor.execute(sql_query)

        return self.__cursor.fetchall()
