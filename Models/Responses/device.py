

from pydantic import BaseModel
from pydantic.json import UUID


class Device(BaseModel):
    name: str
    device_id: UUID
