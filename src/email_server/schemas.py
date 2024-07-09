from pydantic import BaseModel, EmailStr, Field


class CredentialsEmailSchema(BaseModel):
    email: EmailStr = Field(example="user@imaqliq.ru")
    user_id: int
