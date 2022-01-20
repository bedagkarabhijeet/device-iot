
from typing import List

from pydantic import BaseModel
from pydantic.json import UUID


class CreateDevice(BaseModel):
    device_hardware_id: UUID
    sensor_hardware_ids: List[UUID]


class GetDevice(BaseModel):
    device_hardware_id: UUID
    device_name: str
