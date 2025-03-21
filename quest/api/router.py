from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from quest.api import game1


api_router = APIRouter()


@api_router.get("/", response_class=HTMLResponse)
def index():
    with open("quest/static/index.html") as f:
        return f.read()


api_router.include_router(game1.router, prefix="/api/game1")
