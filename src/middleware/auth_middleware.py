from fastapi import HTTPException
from fastapi.security import HTTPBearer
from typing import Annotated

authorization_key = "bearer_key"
    
def check_auth_header(authorization: Annotated[str, HTTPBearer]) -> dict:
    if authorization != authorization_key:
        raise HTTPException(
            status_code=401, 
            detail="Unauthorized"
        )