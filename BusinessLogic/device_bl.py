from Exceptions.device_exception import DeviceException, DeviceExceptionTypes


class DeviceBL:
    def __init__(self, uow_manager_cls, logger):
        self.uow_manager = uow_manager_cls
        self._logger = logger

    def add(self, device_model, sensor_models):
        with self.uow_manager() as uow:
            device_data = self.__insert_device_data(device_model, uow)
            sensor_ids = []
            sensor_hardware_ids = []
            sensor_data_access = uow.get_sensor_data_access()
            for sensor_model in sensor_models:
                sensor_data = sensor_data_access.insert(sensor_model)
                sensor_ids.append(sensor_data["sensor_id"])
                sensor_hardware_ids.append(sensor_data["sensor_hardware_id"])

            uow.get_device_sensor_mapping_data_access().insert(device_data["device_id"], sensor_ids)

            return {"device_hardware_id": device_data["device_hardware_id"], "sensor_hardware_ids": sensor_hardware_ids}

    def __insert_device_data(self, device_model, uow):
        device_access = uow.get_device_data_access()
        try:
            return device_access.insert(device_model)
        except Exception as e:
            if type(e).__name__ == "UniqueViolation":
                raise DeviceException(DeviceExceptionTypes.DEVICE_ALREADY_REGISTERED)
            raise

    def delete(self):
        pass

    def update_device_attributes(self, update_device_model):
        with self.uow_manager() as uow:
            device_access = uow.get_device_data_access()
            device_data = device_access.update(update_device_model)

            if device_data:
                return device_data

            raise DeviceException(DeviceExceptionTypes.DEVICE_NOT_PRESENT)

    def get_all(self):
        with self.uow_manager() as uow:
            device_access = uow.get_device_data_access()
            all_devices = device_access.select_all()
            return all_devices

