

from pydantic import BaseModel


class Device(BaseModel):
    name: str
    type: str
