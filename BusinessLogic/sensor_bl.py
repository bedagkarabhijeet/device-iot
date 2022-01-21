from Exceptions.sensor_exception import SensorException, SensorExceptionTypes


class SensorBL:
    def __init__(self, uow_manager_cls, logger):
        self.uow_manager = uow_manager_cls
        self._logger = logger

    def add(self, sensor_models):
        """
        Adds Add new sensor model
        :param sensor_models: Model containing sensor data
       """
        with self.uow_manager() as uow:
            for sensor_model in sensor_models:
                sensor_access = uow.get_sensor_data_access()
                sensor_access.insert(sensor_model)

    def get_events(self, hardware_id, start_time, end_time):
        """
        Used to fetch events corresponding to specified sensor hardware id and withing specified timestamp
        :param hardware_id: Hardware id of the sensor
        :param start_time: Start time in epoch time format
        :param end_time: End time in epoch time format
        :return: Event data
        """
        with self.uow_manager() as uow:
            sensor_access = uow.get_sensor_data_access()
            sensor_data = sensor_access.select(hardware_id)
            if not sensor_data:
                raise SensorException(SensorExceptionTypes.SENSOR_NOT_PRESENT)

            sensor_event_access = uow.get_sensor_event_data_access()
            return sensor_event_access.get_events(hardware_id, start_time, end_time)

    def delete(self):
        raise Exception("To be Implemented")

    def update(self):
        raise Exception("To be Implemented")

    def sensed(self, sensor_hardware_id, sensor_event_model):
        """
        Used to record events happened on given sensor
        :param sensor_hardware_id: Hardware Id of the sensor
        :param sensor_event_model: Model containing sensor valued and tiem of the event in EPOCH format
        """
        with self.uow_manager() as uow:
            sensor_access = uow.get_sensor_data_access()
            sensor_data = sensor_access.select(sensor_hardware_id)
            if not sensor_data:
                raise SensorException(SensorExceptionTypes.SENSOR_NOT_PRESENT)

            sensor_event_access = uow.get_sensor_event_data_access()
            sensor_event_access.insert(sensor_data["sensor_id"],
                                       sensor_event_model.value,
                                       sensor_event_model.timestamp)

    def get_all(self):
        """
        Gets all the sensor
        :return: All the sensors
        """
        with self.uow_manager() as uow:
            sensor_access = uow.get_sensor_data_access()
            return sensor_access.select_all()
