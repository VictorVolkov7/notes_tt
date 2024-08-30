from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.config.settings import get_db_url
from app.users.auth import get_password_hash
from app.users.models import User

engine = create_async_engine(get_db_url())
Session = async_sessionmaker(engine, expire_on_commit=False)


class UserService:
    """Класс с класс-методами для роутеров пользователя."""

    model = User

    @classmethod
    async def user_register(cls, **values) -> User:
        """
        Регистрация пользователя.

        :param values: Данные из post запроса.
        :return: Объект пользователя.
        """
        password = values.pop("password")
        if password:
            hashed_password = get_password_hash(password)
            values["password"] = hashed_password

        async with Session() as session:
            async with session.begin():
                new_user = User(**values)
                session.add(new_user)
                return new_user

    @classmethod
    async def find_or_none(cls, **filter_by) -> object | None:
        """
        Поиск пользователя по заданным фильтрам.

        :param filter_by: Фильтр с почтой пользователя.
        :return: Объект пользователя или None.
        """

        async with Session() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_or_none_by_id(cls, user_id: int) -> object | None:
        """
        Поиск пользователя по-заданному id.

        :param user_id: ID пользователя.
        :return: Объект пользователя или None.
        """

        async with Session() as session:
            query = select(cls.model).filter_by(id=user_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()
