from fastapi import APIRouter, HTTPException

from Models.Requests.login import LoginRequest
from BusinessLogic.login_bl import LoginBL
from initializer import logger, configuration

login_route = APIRouter()


@login_route.post('/')
def login(request_data: LoginRequest):
    login_bl = LoginBL(logger, configuration)

    if login_bl.verify_password(username=request_data.username, password=request_data.password):
        return {
            'token': login_bl.generate_token(request_data.username)
        }
    else:
        raise HTTPException(status_code=404, detail="User not found")
