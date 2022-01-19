

from fastapi import APIRouter, HTTPException

from DataAccess.device_data_access import DeviceDataAccess
from Models.Requests.device import Device as DeviceRequest
from Models.Responses.device import Device as DeviceResponse

from BusinessLogic.device import DeviceBL

from initializer import logger

device_route = APIRouter()


@device_route.post("/device")
def device(device_model: DeviceRequest):
    """
    Post method to create new devices
    :return: DeviceResponse instance containing response data
    """
    device_bl = DeviceBL(DeviceDataAccess, logger)
    """
    Future scope strategy ex. hashing could be retrieved by using user 
    subscription or other techniques based on business needs 
    """
    device_id = device_bl.add(device_model)

    return ""
    return DeviceResponse.parse_obj({"name": device_model.name, "device_id": device_id})
