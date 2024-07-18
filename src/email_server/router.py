from fastapi import APIRouter, BackgroundTasks
from fastapi.responses import JSONResponse

from .schemas import CredentialsEmailSchema
from .verification import send_credentials_in_background

email_router = APIRouter(prefix="/email")


@email_router.post("/send-credentials")
async def send_credentials(
    background_tasks: BackgroundTasks, email_schema: CredentialsEmailSchema
) -> JSONResponse:
    await send_credentials_in_background(background_tasks, email_schema)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})
