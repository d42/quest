from openai import OpenAI
from quest.core.config import settings


class LLM:
    clinet: OpenAI

    def __init__(self) -> None:
        self.client = OpenAI(
            api_key=settings.HEURIST_API,  # for API key visit = https://dev-api-form.heurist.ai/
            base_url=settings.HEURIST_URL,
        )

    def do_init(self) -> str:
        completion = self.client.chat.completions.create(
            model=settings.TEXT_MODEL,
            messages=[
                {
                    "role": "narrator",
                    "content": "You're the narrator, create a story, which explains difficult crypto terminology, in a way that a five year old can understand, make the plot ironic",
                },
                {
                    "role": "user",
                    "content": "You're a beginner in the crypto industry and also a gamer, you know nothing about the cryptocurrency world, and want to learn terminology",
                },
            ],
        )
        return completion.choices[0].message.content

    def do_input(self, text_input: str) -> str:
        completion = self.client.chat.completions.create(
            model=settings.TEXT_MODEL,
            messages=[
                {
                    "role": "narrator",
                    "content": "You're the narrator, create a story, which explains difficult crypto terminology, in a way that a five year old can understand, make the plot ironic",
                },
                {
                    "role": "user",
                    "content": text_input,
                },
            ],
        )

        return completion.choices[0].message.content
