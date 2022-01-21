from fastapi import APIRouter, HTTPException, Depends

from DataAccess.uow_manager import UOWManager
from Exceptions.sensor_exception import SensorException, SensorExceptionTypes
from Models.Requests.sensor import SensorAddEventModel, SensorGetEventModel
from Utilities.Security.security import validate_token
from initializer import logger
from BusinessLogic.sensor_bl import SensorBL

sensor_route = APIRouter()


@sensor_route.get("/", dependencies=[Depends(validate_token)])
def sensors():
    """
    Get all sensors
    """

    try:
        sensor_bl = SensorBL(UOWManager, logger)
        logger.info(f"Sensor fetched successfully")
        return sensor_bl.get_all()
    except Exception as e:
        logger.error(f"Failed in updating new device {e}")
        raise HTTPException(status_code=500, detail="Some error occurred in the system; "
                                                    "This has been recorded and our team is working on it")


@sensor_route.get("/{sensor_hardware_id}/events", dependencies=[Depends(validate_token)])
def events(sensor_hardware_id, start_time: int = 0, end_time: int = 0):
    """
    Gets all events from sensor
    """

    try:
        sensor_bl = SensorBL(UOWManager, logger)
        all_sensor_data = sensor_bl.get_events(sensor_hardware_id, start_time, end_time)
        logger.info(f"Sensor events fetched successfully")
        return [SensorGetEventModel.parse_obj(sensor_data) for sensor_data in all_sensor_data]
    except SensorException as de:
        logger.error(f"Failed in updating new device {de}")
        if de.error_type == SensorExceptionTypes.SENSOR_NOT_PRESENT:
            raise HTTPException(status_code=404, detail=de.error_type.value.format(sensor_hardware_id))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Some error occurred in the system; "
                                                    "This has been recorded and our team is working on it")


@sensor_route.post("/{sensor_hardware_id}/events", dependencies=[Depends(validate_token)])
def events(sensor_hardware_id, sensor_event_model: SensorAddEventModel):
    """
    Add new event to sensor
    """

    try:
        sensor_bl = SensorBL(UOWManager, logger)
        sensor_bl.sensed(sensor_hardware_id, sensor_event_model)
        logger.info(f"Event posted successfully for {sensor_hardware_id}")
    except SensorException as de:
        logger.error(f"Failed in updating new device {de}")
        if de.error_type == SensorExceptionTypes.SENSOR_NOT_PRESENT:
            raise HTTPException(status_code=404, detail=de.error_type.value.format(sensor_hardware_id))
    except Exception as e:
        logger.error(f"Failed in updating new device {e}")
        raise HTTPException(status_code=500, detail="Some error occurred in the system; "
                                                    "This has been recorded and our team is working on it")
