from typing import List

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.notes.schemas import SNoteGet, SNoteAdd
from app.notes.service import NoteService
from app.notes.utils import check_spelling
from app.users.dependecies import get_current_user
from app.users.models import User

router = APIRouter(prefix="/notes", tags=["Заметки"])


@router.get("/", response_model=List[SNoteGet], summary="Получить все заметки.")
async def get_all_notes(user_data: User = Depends(get_current_user)) -> List[SNoteGet]:
    return await NoteService.get_all_notes(user_id=user_data.id)


@router.post("/add/", summary="Создать заметку.")
async def note_create(
    note: SNoteAdd, user_data: User = Depends(get_current_user)
) -> JSONResponse:
    spelling_errors = await check_spelling(note.description)
    if spelling_errors:
        return JSONResponse(
            content={
                "message": "Заметка содержит орфографические ошибки",
                "errors": [error["word"] for error in spelling_errors],
            },
            status_code=400,
        )

    result = await NoteService.add_note(**note.model_dump(), user_id=user_data.id)
    return JSONResponse(
        content={"message": "Заметка успешно добавлена!", "note": result.to_dict()},
        status_code=201,
    )


# @router.get("/{id}/", response_model=SNote, summary="Получение заметки по id")
# async def get_note_by_id(note_id: int) -> SNote | None:
#     note = await NoteService.get_note(note_id)
#     if note is None:
#         raise HTTPException(status_code=404, detail="Заметка не найдена")
#     return note
