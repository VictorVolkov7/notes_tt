from datetime import datetime, timezone

from fastapi import Request, HTTPException, status, Depends
from jose import jwt, JWTError

from app.config.settings import get_auth_data
from app.users.service import UserService


def get_token(request: Request) -> str:
    """
    Функция для получения access токена их куки.

    :param request: HTTP-запрос
    :return: access токен.
    """

    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Токен не найден."
        )
    return token


async def get_current_user(token: str = Depends(get_token)) -> object:
    """
    Функция для проверки токена и поиска текущего пользователя.

    :param token: Access токен.
    :return: Объект пользователя.
    """

    try:
        auth_data = get_auth_data()
        payload = jwt.decode(
            token, auth_data["secret_key"], algorithms=[auth_data["algorithm"]]
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Токен не валидный."
        )

    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Не найден ID пользователя"
        )

    user = await UserService.find_or_none_by_id(int(user_id))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Пользователь не найден."
        )

    return user
