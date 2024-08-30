from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Класс настроек проекта 'Notes TT'."""

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    SECRET_KEY: str
    ALGORITHM: str

    class Config:
        env_file = ".env"


settings = Settings()


def get_db_url():
    """Метод для генерации урла базы данных."""
    return (
        f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@"
        f"{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
    )


def get_auth_data():
    """
    Функция для создания словаря с секретным
    ключом и алгоритмом шифрования.
    """
    return {"secret_key": settings.SECRET_KEY, "algorithm": settings.ALGORITHM}
