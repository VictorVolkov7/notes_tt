from sqlalchemy import String, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.config.db import Base


class User(Base):
    """Модель пользователя."""

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    surname: Mapped[str] = mapped_column(String(30), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)

    notes: Mapped[list["Student"]] = relationship("Note", back_populates="author")

    is_user: Mapped[bool] = mapped_column(
        default=True, server_default=text("true"), nullable=False
    )
    is_super_admin: Mapped[bool] = mapped_column(
        default=False, server_default=text("false"), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(
        default=True, server_default=text("true"), nullable=False
    )

    def __str__(self) -> str:
        """Метод для строкового представления."""
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"first_name={self.name!r},"
            f"last_name={self.surname!r})"
        )

    def __repr__(self) -> str:
        """Метод для строкового представления (отладка)."""
        return str(self)
