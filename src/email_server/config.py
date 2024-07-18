from fastapi_mail import ConnectionConfig
from jinja2 import Environment, PackageLoader, select_autoescape
from pydantic import EmailStr
from pydantic_settings import BaseSettings


class EmailEnvVars(BaseSettings):
    EMAIL_USERNAME: str
    EMAIL_PASSWORD: str
    EMAIL_FROM: EmailStr
    EMAIL_PORT: int
    EMAIL_SERVER: str
    EMAIL_FROM_NAME: str
    EMAIL_STARTTLS: bool
    EMAIL_SSL_TLS: bool
    USE_CREDENTIALS: bool
    VALIDATE_CERTS: bool

    class Config:
        env_file = "email.env"


__env_vars = EmailEnvVars()  # type: ignore

email_config = ConnectionConfig(
    MAIL_USERNAME=__env_vars.EMAIL_USERNAME,
    MAIL_PASSWORD=__env_vars.EMAIL_PASSWORD,
    MAIL_FROM=__env_vars.EMAIL_FROM,
    MAIL_PORT=__env_vars.EMAIL_PORT,
    MAIL_SERVER=__env_vars.EMAIL_SERVER,
    MAIL_STARTTLS=__env_vars.EMAIL_STARTTLS,
    MAIL_SSL_TLS=__env_vars.EMAIL_SSL_TLS,
    USE_CREDENTIALS=__env_vars.USE_CREDENTIALS,
    VALIDATE_CERTS=__env_vars.VALIDATE_CERTS,
)

jinja2_env = Environment(
    loader=PackageLoader("email_server", "templates"),
    autoescape=select_autoescape(["html", "xml"]),
    enable_async=True,
)
