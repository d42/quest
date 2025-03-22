import pytest
from quest.llm.llm import LLM


@pytest.fixture
def llm() -> LLM:
    return LLM()
