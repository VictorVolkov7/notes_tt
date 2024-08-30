from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class SNoteGet(BaseModel):
    """Модель, описывающая тело запроса получения заметок"""

    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str = Field(..., description="Название заметки")
    description: str = Field(..., max_length=500, description="Тело заметки")
    author: Optional[str] = Field(..., description="ID автора заметки")


class SNoteAdd(BaseModel):
    """Модель, описывающая тело запроса создания заметок"""

    model_config = ConfigDict(from_attributes=True)

    title: str = Field(..., description="Название заметки")
    description: str = Field(..., max_length=500, description="Тело заметки")
