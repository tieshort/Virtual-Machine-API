from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, MessageType

from .config import email_config
from .schemas import VerificationEmailSchema


async def send_verification_in_background(background_tasks: BackgroundTasks, email_schema: VerificationEmailSchema):
    html = """<p>Hi this test mail, thanks for using Fastapi-mail</p> """
    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=[email_schema.email],
        body=html,
        subtype=MessageType.html)

    fm = FastMail(email_config)
    background_tasks.add_task(fm.send_message, message)