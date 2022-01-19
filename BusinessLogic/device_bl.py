

class DeviceBL:
    def __init__(self, uow_manager_cls, logger):
        self.uow_manager = uow_manager_cls
        self._logger = logger

    def add(self, device_model):
        with self.uow_manager() as uow:
            device_access = uow.get_event_detection_data_access()
            return device_access.insert(device_model)

    def delete(self):
        pass

    def update(self):
        pass
