

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from pydantic import ValidationError

from datetime import datetime

from initializer import configuration

bearer_token = HTTPBearer(scheme_name='Authorization')


def validate_token(http_authorization_credentials=Depends(bearer_token)):
    """
    Decode JWT token to get username
    return username
    """
    try:
        payload = jwt.decode(http_authorization_credentials.credentials, configuration["SECRET_KEY"],
                             algorithms=configuration["SECURITY_ALGORITHM"])

        print(payload.get("exp"))
        print(datetime.now().timestamp())
        if payload.get('username') and payload.get("exp") <= datetime.now().timestamp():
            raise HTTPException(status_code=403, detail="Token expired")
        return payload.get('username')
    except(jwt.PyJWTError, ValidationError):
        raise HTTPException(
            status_code=403,
            detail=f"Could not validate credentials",
        )
