

from fastapi import FastAPI
import uvicorn


from Controllers.device_controller import device_route
from Controllers.sensor_controller import sensor_route


app = FastAPI()
app.include_router(device_route, tags=["devices"])
app.include_router(sensor_route, tags=["sensors"])

uvicorn.run(app, host="localhost", port=8000)
