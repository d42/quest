from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from quest import prompt
from quest.api import game
from quest.llm.llm import LLM
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="quest/templates")

api_router = APIRouter()


@api_router.get("/", response_class=HTMLResponse)
def index():
    with open("quest/templates/index.html") as f:
        return f.read()


@api_router.get("/topics", response_class=HTMLResponse)
def topics():
    with open("quest/templates/topics.html") as f:
        return f.read()


@api_router.get("/game/{game_id}", response_class=HTMLResponse)
def play(game_id: str, request: Request):
    models = prompt.get_models()
    model = models[game_id]

    if not model.intro_text:
        llm = LLM()
        intro_text = llm.do_input(
            "create an introduction to the game", context=[], game_id=game_id
        )
    else:
        intro_text = model.intro_text

    return templates.TemplateResponse(
        request=request,
        name="gameplay.html",
        context={
            "game_id": game_id,
            "intro_text": intro_text,
        },
    )
    with open("quest/templates/topics.html") as f:
        return f.read()


api_router.include_router(game.router, prefix="/api/game")
