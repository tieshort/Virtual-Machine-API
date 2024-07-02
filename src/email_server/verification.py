from fastapi import BackgroundTasks

from .email import Email
from .schemas import VerificationEmailSchema


async def send_verification_in_background(background_tasks: BackgroundTasks, email_schema: VerificationEmailSchema):
    mail = Email([email_schema.email])
    background_tasks.add_task(mail.send_verification_code, "varif url", "user name")  # TODO Генерировать url для верификации, брать из базы данных имя пользователя