from typing import Dict
from quest.core.types import GameData


from pathlib import Path

path = Path(__file__).parent


def get_models() -> Dict[str, GameData]:
    with open(path / "blockchain.json") as f:
        blockchain = GameData.model_validate_json(f.read())

    with open(path / "eth.json") as f:
        eth = GameData.model_validate_json(f.read())

    with open(path / "smartcontracts.json") as f:
        smartcontracts = GameData.model_validate_json(f.read())

    models = {
        "blockchain": blockchain,
        "eth": eth,
        "smartcontracts": smartcontracts,
    }
    return models


get_models()
