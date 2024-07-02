from pydantic import BaseModel, Field, field_validator
from typing import Optional

class UserCreate(BaseModel):
    name: str = Field(..., example="John Doe")
    password: str = Field(..., example="password123")
    email: str = Field(..., example="john.doe@example.com")
    phone: str = Field(..., example="+1234567890")

    @field_validator('name', 'password', 'email', 'phone')
    def not_empty(cls, value):
        if not value or not value.strip():
            raise ValueError('Field cannot be empty or blank')
        return value

class ImageCreate(BaseModel):
    name: str = Field(..., example="Image1")
    operating_system: str = Field(..., example="Linux")
    memory: str = Field(..., example="4096")
    disk: str = Field(..., example="200")

    @field_validator('name', 'operating_system', 'memory', 'disk')
    def not_empty(cls, value):
        if not value or not value.strip():
            raise ValueError('Field cannot be empty or blank')
        return value

class CustomImageCreate(ImageCreate):
    load_file: str = Field(..., example="C:\Lib\help")
    user_id: str = Field(..., example="100785")
    pass

class UserOrderCreate(BaseModel):
    name: str = Field(..., example="Order1")
    image_id: Optional[int] = Field(None, example=1)
    custom_image_id: Optional[int] = Field(None, example=1)
    configuration: dict = Field(..., example={"config": "value1"})
    network: dict = Field(..., example={"network": "value1"})
    access: dict = Field(..., example={"access": "value1"})
    cloud_ini: dict = Field(..., example={"cloud": "value1"})
    user_id: int = Field(..., example=1)

    # @field_validator('name', 'configuration','network', 'access', 'cloud_ini',)
    # def not_empty(cls, value):
    #     if not value or not value.strip():
    #         raise ValueError('Field cannot be empty or blank')
    #     return value

