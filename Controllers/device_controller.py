import uuid

from fastapi import APIRouter, HTTPException

from DataAccess.uow_manager import UOWManager

from Exceptions.device_exception import DeviceException, DeviceExceptionTypes
from Models.Requests.device import CreateDevice, UpdateDeviceName
from Models.Responses.device import CreateDevice as DeviceResponse, GetDevice
from Models.Requests.sensor import CreateSensorRequest, SensorTypes

from BusinessLogic.device_bl import DeviceBL


from initializer import logger

device_route = APIRouter()


@device_route.post("/")
def device(device_model: CreateDevice):
    """
    Create new Device in the system
    """

    try:
        device_bl = DeviceBL(UOWManager, logger)
        device_data = device_bl.add(device_model,
                                    [
                                        CreateSensorRequest.parse_obj(
                                            {
                                                "name": "tempormeter",
                                                "hardware_id": str(uuid.uuid4()),
                                                "type": SensorTypes.Temperature.value
                                            }),
                                        CreateSensorRequest.parse_obj(
                                            {
                                                "name": "pressorometer",
                                                "hardware_id": str(uuid.uuid4()),
                                                "type": SensorTypes.Pressure.value
                                            })
                                    ])
        logger.info(f"Device {device_model.hardware_id} added successfully")
        return DeviceResponse.parse_obj(device_data)
    except DeviceException as de:
        logger.error(f"Failed in adding new device {de}")
        if de.error_type == DeviceExceptionTypes.DEVICE_ALREADY_REGISTERED:
            raise HTTPException(status_code=409, detail=de.error_type.value.format(device_model.hardware_id))
    except Exception as e:
        logger.error(f"Failed in adding new device {e}")
        raise HTTPException(status_code=500, detail="Some error occurred in the system; "
                                                    "This has been recorded and our team is working on it")


@device_route.patch("/{device_hardware_id}")
def device(device_hardware_id, device_model: UpdateDeviceName):
    """
    Updates device name
    """

    try:
        device_bl = DeviceBL(UOWManager, logger)
        device_model.hardware_id = device_hardware_id
        device_bl.update_device(device_model)
        logger.info(f"Device {device_hardware_id} updated successfully")
        return device_model
    except DeviceException as de:
        logger.error(f"Failed in adding new device {de}")
        if de.error_type == DeviceExceptionTypes.DEVICE_NOT_PRESENT:
            raise HTTPException(status_code=409, detail=de.error_type.value.format(device_model.hardware_id))
    except Exception as e:
        logger.error(f"Failed in updating new device {e}")
        raise HTTPException(status_code=500, detail="Some error occurred in the system; "
                                                    "This has been recorded and our team is working on it")


@device_route.get("/")
def device():
    """
    Gets all devices in the system
    """

    try:
        device_bl = DeviceBL(UOWManager, logger)
        all_device_data = device_bl.read_all()
        logger.info(f"Devices fetched successfully")
        return [GetDevice.parse_obj(device_data) for device_data in all_device_data]
    except Exception as e:
        logger.error(f"Failed in getting devices {e}")
        raise HTTPException(status_code=500, detail="Some error occurred in the system; "
                                                    "This has been recorded and our team is working on it")

