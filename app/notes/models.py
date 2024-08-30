from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.config.db import Base
from app.users.models import User


class Note(Base):
    """Модель заметки."""

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)

    author: Mapped["User"] = relationship("User", back_populates="notes")

    def __str__(self) -> str:
        """Метод для строкового представления."""
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"title={self.title!r},"
            f"author={self.author!r})"
        )

    def __repr__(self) -> str:
        """Метод для строкового представления (отладка)."""
        return str(self)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "author_id": self.author_id,
        }
