

class SensorBL:
    def __init__(self, uow_manager_cls, logger):
        self.uow_manager = uow_manager_cls
        self._logger = logger

    def add(self, device_id, sensor_models):
        with self.uow_manager() as uow:
            for sensor_model in sensor_models:
                sensor_access = uow.get_sensor_data_access()
                sensor_access.insert(sensor_model)

    def delete(self):
        pass

    def update(self):
        pass
