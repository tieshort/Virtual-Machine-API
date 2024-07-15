from fastapi_mail import FastMail, MessageSchema, MessageType
from jinja2 import Template
from pydantic import EmailStr

from .config import email_config, jinja2_env
from .templates.enum import HtmlTemplate


class Email:
    def __init__(self, emails: list[EmailStr]):
        self.emails = emails

    @staticmethod
    def get_template(template: HtmlTemplate) -> Template:
        return jinja2_env.get_template(f"{template.value}.html")

    async def send_mail(self, subject: str, message_body: str) -> None:
        message = MessageSchema(
            subject=subject,
            recipients=self.emails,
            body=message_body,
            subtype=MessageType.html,
        )

        fm = FastMail(email_config)
        await fm.send_message(message)

    async def send_credentials(self, user_name: str, login: str, password: str) -> None:
        subject = "Ваши учетные данные"
        template = self.get_template(HtmlTemplate.Credentials)
        body = await template.render_async(
            subject=subject, first_name=user_name, login=login, password=password
        )
        await self.send_mail(subject, body)