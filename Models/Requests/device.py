

from pydantic import BaseModel, UUID4
from pydantic.class_validators import Optional


class CreateDevice(BaseModel):
    name: str
    type: str
    hardware_id: UUID4


class UpdateDeviceName(BaseModel):
    name: str
    hardware_id: Optional[UUID4]
