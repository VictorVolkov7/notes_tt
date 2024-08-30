from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import joinedload

from app.config.settings import get_db_url
from app.notes.models import Note

engine = create_async_engine(get_db_url())
Session = async_sessionmaker(engine, expire_on_commit=False)


class NoteService:
    """Класс с класс-методами для роутеров заметок."""

    model = Note

    @classmethod
    async def get_all_notes(cls, user_id) -> list:
        """
        Создание сессии и получение списка заметок.

        :param user_id: ID пользователя.
        :return: Список заметок текущего пользователя.
        """
        async with Session() as session:
            try:
                query = (
                    select(cls.model)
                    .filter_by(author_id=user_id)
                    .options(joinedload(cls.model.author))
                )
                result = await session.execute(query)
                notes_info = result.scalars().all()

                notes_data = []
                for note in notes_info:
                    note_data = note.to_dict()
                    note_data["author"] = note.author.email
                    notes_data.append(note_data)

                return notes_data
            except Exception as e:
                raise HTTPException(
                    status_code=500, detail="Ошибка при получении заметок"
                ) from e

    @classmethod
    async def add_note(cls, user_id, **values) -> Note:
        """
        Создание сессии и создание заметок.

        :param user_id: ID текущего пользователя.
        :param values: Данные из post запроса.
        :return: Объект созданной заметки.
        """
        async with Session() as session:
            async with session.begin():
                try:
                    new_note = cls.model(**values, author_id=user_id)
                    session.add(new_note)
                    return new_note
                except IntegrityError:
                    raise HTTPException(
                        status_code=400,
                        detail="Ошибка целостности данных: передан несуществующий ID автора",
                    )
                except Exception as e:
                    raise HTTPException(
                        status_code=500,
                        detail="Ошибка при добавлении заметки: " + str(e),
                    )

    # @classmethod
    # async def get_note(cls, note_id: int):
    #     """
    #     Создание сессии и получение заметки по её id.
    #
    #     :param note_id: ID заметки.
    #     :return: Объект заметки или None.
    #     """
    #     async with Session() as session:
    #         try:
    #             query = select(cls.model).filter_by(id=note_id)
    #             result = await session.execute(query)
    #             return result.scalar_one_or_none()
    #         except Exception as e:
    #             raise HTTPException(status_code=500, detail="Ошибка при получении заметок") from e
