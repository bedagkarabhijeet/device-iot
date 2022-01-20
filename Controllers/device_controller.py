import uuid

from fastapi import APIRouter, HTTPException

from DataAccess.uow_manager import UOWManager

from Exceptions.device_exception import DeviceException, DeviceExceptionTypes
from Models.Requests.device import CreateDevice, UpdateDeviceName
from Models.Responses.device import CreateDevice as DeviceResponse, GetDevice
from Models.Requests.sensor import ReadSensor as SensorRequest, SensorTypes

from BusinessLogic.device_bl import DeviceBL


from initializer import logger

device_route = APIRouter()


@device_route.post("/devices")
def device(device_model: CreateDevice):
    """
    Post method to create new devices
    :return: DeviceResponse instance containing response data
    """

    try:
        device_bl = DeviceBL(UOWManager, logger)
        device_data = device_bl.add(device_model,
                                    [
                                        SensorRequest.parse_obj(
                                            {
                                                "name": "tempormeter",
                                                "hardware_id": str(uuid.uuid4()),
                                                "type": SensorTypes.Temperature
                                            }),
                                        SensorRequest.parse_obj(
                                            {
                                                "name": "pressorometer",
                                                "hardware_id": str(uuid.uuid4()),
                                                "type": SensorTypes.Pressure
                                            })
                                    ])

        return DeviceResponse.parse_obj(device_data)
    except DeviceException as de:
        if de.error_type == DeviceExceptionTypes.DEVICE_ALREADY_REGISTERED:
            raise HTTPException(status_code=409, detail=de.error_type.value.format(device_model.hardware_id))
    except Exception:
        raise HTTPException(status_code=500, detail="Some error occurred in the system; "
                                                    "This has been recorded and our team is working on it")


@device_route.patch("/devices/{hardware_id}")
def device(hardware_id, device_model: UpdateDeviceName):
    """
    Post method to create new devices
    :return: DeviceResponse instance containing response data
    """

    try:
        device_bl = DeviceBL(UOWManager, logger)
        device_model.hardware_id = hardware_id
        device_bl.update_device_attributes(device_model)
        return device_model
    except DeviceException as de:
        if de.error_type == DeviceExceptionTypes.DEVICE_NOT_PRESENT:
            raise HTTPException(status_code=409, detail=de.error_type.value.format(device_model.hardware_id))
    except Exception:
        raise HTTPException(status_code=500, detail="Some error occurred in the system; "
                                                    "This has been recorded and our team is working on it")


@device_route.get("/devices")
def device():
    """
    Post method to create new devices
    :return: DeviceResponse instance containing response data
    """

    try:
        device_bl = DeviceBL(UOWManager, logger)
        all_device_data = device_bl.get_all()
        return [GetDevice.parse_obj(device_data) for device_data in all_device_data]
    except Exception:
        raise HTTPException(status_code=500, detail="Some error occurred in the system; "
                                                    "This has been recorded and our team is working on it")

