from pydantic import BaseModel, EmailStr, Field


class VerificationEmailSchema(BaseModel):
    email: EmailStr = Field(example="user@imaqliq.ru")
    order_id: int
