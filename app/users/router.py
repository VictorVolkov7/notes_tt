from fastapi import APIRouter, HTTPException, Response, Depends

from fastapi.responses import JSONResponse
from starlette import status

from app.users.auth import authenticate_user, create_access_token
from app.users.dependecies import get_current_user
from app.users.models import User
from app.users.schemas import SUserRegister, SUserAuth
from app.users.service import UserService

router = APIRouter(prefix="/users", tags=["Пользователи"])


@router.post("/register/", summary="Регистрация пользователя")
async def register_user(user_data: SUserRegister) -> JSONResponse:
    user = await UserService.find_or_none(email=user_data.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Пользователь уже существует"
        )

    await UserService.user_register(**user_data.model_dump())

    return JSONResponse(
        content={"message": "Регистрация прошла успешно!"},
        status_code=201,
    )


@router.post("/login/", summary="Аутентификация пользователя.")
async def auth_user(user_data: SUserAuth, response: Response) -> dict:
    check_user = await authenticate_user(
        email=user_data.email, password=user_data.password
    )
    if check_user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Неверная почта или пароль"
        )

    access_token = create_access_token({"sub": str(check_user.id)})
    response.set_cookie(key="access_token", value=access_token, httponly=True)
    return {"access_token": access_token}


@router.get("/me/")
async def get_me(user_data: User = Depends(get_current_user)):
    return user_data
