from Exceptions.sensor_exception import SensorException, SensorExceptionTypes


class SensorBL:
    def __init__(self, uow_manager_cls, logger):
        self.uow_manager = uow_manager_cls
        self._logger = logger

    def add(self, sensor_models):
        with self.uow_manager() as uow:
            for sensor_model in sensor_models:
                sensor_access = uow.get_sensor_data_access()
                sensor_access.insert(sensor_model)

    def get_events(self, hardware_id, start_time, end_time):
        with self.uow_manager() as uow:
            sensor_access = uow.get_sensor_data_access()
            sensor_data = sensor_access.select(hardware_id)
            if not sensor_data:
                raise SensorException(SensorExceptionTypes.SENSOR_NOT_PRESENT)

            sensor_event_access = uow.get_sensor_event_data_access()
            return sensor_event_access.get_events(hardware_id, start_time, end_time)

    def delete(self):
        pass

    def update(self):
        pass

    def sensed(self, sensor_hardware_id, sensor_event_model):
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
        with self.uow_manager() as uow:
            sensor_access = uow.get_sensor_data_access()
            return sensor_access.select_all()


