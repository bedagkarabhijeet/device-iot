

class SensorEventDataAccess:
    def __init__(self, cursor):
        self.__cursor = cursor

    def insert(self, sensor_id, value, timestamp):
        sql_query = "INSERT INTO sensor_events (sensor_id, sensor_value, time_stamp) " \
                    "VALUES (%s, %s, %s) RETURNING sensor_id"

        self.__cursor.execute(sql_query, (sensor_id, value, timestamp))

        output = self.__cursor.fetchone()

        if output and output.get("sensor_id"):
            return output
        else:
            raise Exception("Failed while inserting record")

    def get_events(self, hardware_id, start_time=0, end_time=0):

        params = [str(hardware_id)]
        sql_query = "SELECT S.sensor_hardware_id, SE.time_stamp, SE.sensor_value " \
                    "FROM sensor S inner join sensor_events SE ON S.sensor_id = SE.sensor_id " \
                    "WHERE S.sensor_hardware_id = (%s) "

        if start_time:
            sql_query += " AND SE.time_stamp >= (%s) "
            params.append(start_time)
        if end_time:
            sql_query += " AND SE.time_stamp <= (%s) "
            params.append(end_time)

        self.__cursor.execute(sql_query, tuple(params))

        return self.__cursor.fetchall()