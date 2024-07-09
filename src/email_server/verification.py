from fastapi import BackgroundTasks

from .email import Email
from .schemas import CredentialsEmailSchema


async def send_credentials_in_background(
    background_tasks: BackgroundTasks, email_schema: CredentialsEmailSchema
):
    mail = Email([email_schema.email])
    background_tasks.add_task(
        mail.send_credentials, "user name", "login", "password"
    )  # TODO Брать из базы данных логин и пароль по user_id