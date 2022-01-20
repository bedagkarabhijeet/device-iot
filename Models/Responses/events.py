

from pydantic import BaseModel
from pydantic.json import UUID


class SensorEvents(BaseModel):
    sensor_hardware_id: UUID
    time_stamp: int
    sensor_value: int
