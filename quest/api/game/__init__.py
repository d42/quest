from typing import List
from fastapi import APIRouter
from pydantic import BaseModel
from quest.llm.llm import LLM


router = APIRouter()


class GameRequest(BaseModel):
    text: str
    context: List[str]


class ImageRequest(BaseModel):
    image_id: str


class GameResponse(BaseModel):
    text: str


@router.post("/{game_id}/do")
def do_action(request: GameRequest, game_id: str) -> GameResponse:
    ll = LLM()
    asd = ll.do_input(request.text, context=request.context, game_id=game_id)
    return GameResponse(text=asd)


@router.get("/image")
def do_image(request: ImageRequest) -> str:
    ll = LLM()
    asd = ll.do_input(request.text)
    return GameResponse(text=asd)
