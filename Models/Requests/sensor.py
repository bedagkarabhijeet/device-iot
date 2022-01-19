import enum
from pydantic import BaseModel, UUID4


class SensorTypes(enum.Enum):
    Temperature = "Temperature"
    Pressure = "Pressure"


class Sensor(BaseModel):
    name: str
    type: SensorTypes
    id: UUID4
