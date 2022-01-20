from fastapi import APIRouter, HTTPException

from DataAccess.uow_manager import UOWManager
from Exceptions.sensor_exception import SensorException, SensorExceptionTypes
from Models.Requests.sensor import SensorAddEventModel, SensorGetEventModel
from initializer import logger
from BusinessLogic.sensor_bl import SensorBL

sensor_route = APIRouter()


@sensor_route.get("/sensors")
def events():
    """
    Post method to create new devices
    :return: DeviceResponse instance containing response data
    """

    try:
        sensor_bl = SensorBL(UOWManager, logger)
        return sensor_bl.get_all()
    except Exception:
        raise HTTPException(status_code=500, detail="Some error occurred in the system; "
                                                    "This has been recorded and our team is working on it")


@sensor_route.get("/sensors/{hardware_id}/events")
def events(hardware_id, start_time: int = 0, end_time: int = 0):
    """
    Post method to create new devices
    :return: DeviceResponse instance containing response data
    """

    try:
        sensor_bl = SensorBL(UOWManager, logger)
        all_sensor_data = sensor_bl.get_events(hardware_id, start_time, end_time)
        return [SensorGetEventModel.parse_obj(sensor_data) for sensor_data in all_sensor_data]
    except SensorException as de:
        if de.error_type == SensorExceptionTypes.SENSOR_NOT_PRESENT:
            raise HTTPException(status_code=404, detail=de.error_type.value.format(hardware_id))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Some error occurred in the system; "
                                                    "This has been recorded and our team is working on it")


@sensor_route.post("/sensors/{sensor_hardware_id}/events")
def events(sensor_hardware_id, sensor_event_model: SensorAddEventModel):
    """
    Post method to create new devices
    :return: DeviceResponse instance containing response data
    """

    try:
        sensor_bl = SensorBL(UOWManager, logger)
        sensor_bl.sensed(sensor_hardware_id, sensor_event_model)
    except SensorException as de:
        if de.error_type == SensorExceptionTypes.SENSOR_NOT_PRESENT:
            raise HTTPException(status_code=404, detail=de.error_type.value.format(sensor_hardware_id))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Some error occurred in the system; "
                                                    "This has been recorded and our team is working on it")
