import enum
from pydantic import BaseModel, UUID4


class SensorTypes(enum.Enum):
    Temperature = "Temperature"
    Pressure = "Pressure"


class ReadSensor(BaseModel):
    sensor_type: str
    sensor_name: SensorTypes
    sensor_hardware_id: UUID4


class SensorAddEventModel(BaseModel):
    value: int
    timestamp: int


class SensorGetEventModel(BaseModel):
    sensor_value: int
    sensor_hardware_id: UUID4
    time_stamp: int
