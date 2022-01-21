

from fastapi import FastAPI
import os
from mangum import Mangum

from Controllers.device_controller import device_route
from Controllers.sensor_controller import sensor_route


app = FastAPI(title="DeviceIOT", openapi_prefix=f"/{os.environ.get('STAGE')}" if os.environ.get('STAGE') else "")

app.include_router(device_route, prefix="/devices",  tags=["devices"])
app.include_router(sensor_route, prefix="/sensors", tags=["sensors"])

handler = Mangum(app)
