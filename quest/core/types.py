from enum import Enum

from pydantic import BaseModel


class Games(int, Enum):
    game1 = 1
    game2 = 2
    game3 = 3
    game_test = 9001


class GameData(BaseModel):
    intro_text: str | None = None
    system_prompt: str
