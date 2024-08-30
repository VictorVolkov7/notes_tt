from fastapi import FastAPI
from app.notes.router import router as router_notes
from app.users.router import router as router_users


app = FastAPI()

app.include_router(router_notes)
app.include_router(router_users)
