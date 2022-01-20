import uuid

from fastapi import APIRouter, HTTPException

from DataAccess.uow_manager import UOWManager

from DataAccess.device_data_access import DeviceDataAccess
from Models.Requests.device import Device as DeviceRequest
from Models.Responses.device import Device as DeviceResponse
from Models.Requests.sensor import Sensor as SensorRequest, SensorTypes

from BusinessLogic.device_bl import DeviceBL
from BusinessLogic.sensor_bl import SensorBL

from initializer import logger

device_route = APIRouter()


@device_route.post("/device")
def device(device_model: DeviceRequest):
    """
    Post method to create new devices
    :return: DeviceResponse instance containing response data
    """
    device_bl = DeviceBL(UOWManager, logger)
    device_data = device_bl.add(device_model,
                                [
                                    SensorRequest.parse_obj(
                                        {
                                            "name": "tempormeter",
                                            "id": str(uuid.uuid4()),
                                            "type": SensorTypes.Temperature
                                        }),
                                    SensorRequest.parse_obj(
                                        {
                                            "name": "pressorometer",
                                            "id": str(uuid.uuid4()),
                                            "type": SensorTypes.Pressure
                                        })
                                ])

    return DeviceResponse.parse_obj(device_data)
