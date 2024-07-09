from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

authorization_key = "bearer_key"

security = HTTPBearer()

def check_auth_header(authorization: Annotated[HTTPAuthorizationCredentials, Depends(security)]) -> None:
    if authorization.credentials != authorization_key:
        raise HTTPException(status_code=401, detail="Unauthorized")
