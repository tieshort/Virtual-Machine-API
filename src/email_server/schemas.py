from pydantic import BaseModel, EmailStr


class VerificationEmailSchema(BaseModel):
    email: EmailStr
    order_id: int
