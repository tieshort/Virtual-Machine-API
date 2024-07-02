from fastapi import APIRouter, BackgroundTasks
from fastapi.responses import JSONResponse

from .schemas import VerificationEmailSchema
from .verification import send_verification_in_background

api_router = APIRouter(prefix="/email")

@api_router.post("/send-verification")
async def send_verification(
    background_tasks: BackgroundTasks, email_schema: VerificationEmailSchema
) -> JSONResponse:
    await send_verification_in_background(background_tasks, email_schema)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})
