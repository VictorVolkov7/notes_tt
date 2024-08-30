from fastapi.openapi.models import Response
from pydantic import BaseModel, EmailStr, Field, ConfigDict


class SUserRegister(BaseModel):
    """Модель, описывающая тело запроса регистрации пользователя."""

    model_config = ConfigDict(from_attributes=True)

    email: EmailStr = Field(..., description="Электронная почта")
    password: str = Field(
        ..., min_length=12, max_length=50, description="Пароль, от 12 до 50 знаков"
    )
    name: str = Field(..., description="Имя")
    surname: str = Field(..., description="Фамилия")


class SUserAuth(BaseModel):
    """Модель, описывающая тело запроса авторизации пользователя."""

    model_config = ConfigDict(from_attributes=True)

    email: EmailStr = Field(..., description="Электронная почта")
    password: str = Field(
        ..., min_length=12, max_length=50, description="Пароль, от 12 до 50 знаков"
    )
