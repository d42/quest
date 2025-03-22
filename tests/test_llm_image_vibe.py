from quest.core.types import Games
from quest.llm.llm import LLM


def test_llm_image_dummy_selection(llm: LLM):
    image = llm.select_image_for_act(
        Games.game_test,
        "what is bitcoin",
        "",
    )
    assert image == "bitcoin.png"

    image = llm.select_image_for_act(
        Games.game_test,
        "vitalik butterin visits you at night",
        "",
    )
    assert image == "ethereum.png"
