

from fastapi import FastAPI
import uvicorn


from initializer import configuration

from Controllers.device import device_route


app = FastAPI()
app.include_router(device_route, tags=["device"])

uvicorn.run(app, port=configuration["port"])
