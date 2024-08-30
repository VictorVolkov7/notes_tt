from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone

from pydantic import EmailStr

from app.config.settings import get_auth_data

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    """Функция для создания хэша пароля."""

    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Функция для верификации пароля."""

    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    """
    Функция для создания jwt access токена.

    :param data: Словарь с данными.
    """

    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=7)
    to_encode.update({"exp": expire})
    auth_data = get_auth_data()
    encode_jwt = jwt.encode(
        to_encode, auth_data["secret_key"], algorithm=auth_data["algorithm"]
    )
    return encode_jwt


async def authenticate_user(email: EmailStr, password: str):
    """
    Функция для аутентификации пользователя.

    :param email: Электронная почта.
    :param password: Пароль.
    :return: Объект пользователя или None.
    """

    from app.users.service import UserService

    user = await UserService.find_or_none(email=email)
    if (
        not user
        or verify_password(plain_password=password, hashed_password=user.password)
        is False
    ):
        return None
    return user
