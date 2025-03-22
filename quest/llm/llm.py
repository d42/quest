import json
from logging import getLogger
from typing import List
from openai import OpenAI
from quest import prompt
from quest.core.config import settings
from quest.core import types


logger = getLogger(__name__)


class LLM:
    client: OpenAI

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

    def select_image_for_act(
        self,
        game: types.Games,
        context: str,
        text_input: str,
    ) -> str:
        if game == types.Games.game_test:
            enum = ["ethereum.png", "bitcoin.png", "doge.png"]
        else:
            raise NotImplemented(game)

        tool = {
            "type": "function",
            "function": {
                "name": "select_best_image",
                "description": "select best image for the current context",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "image": {
                            "type": "string",
                            "description": "one of the image names",
                            "enum": enum,
                        },
                    },
                    "required": ["image"],
                },
            },
        }

        response = self.client.chat.completions.create(
            model=settings.TEXT_MODEL,
            temperature=0.01,
            messages=[
                {
                    "role": "system",
                    "content": " Given the context, try to select a best fitting image",
                },
                {
                    "role": "user",
                    "content": context,
                },
            ],
            tools=[tool],
            tool_choice="required",
        )
        try:
            arguments = response.choices[0].message.tool_calls[0].function.arguments
            return json.loads(arguments)["image"]
        except Exception as e:
            logger.exception("context: %s", context, exc_info=e)
            return ""

    def do_input(self, text_input: str, context: List[str], game_id: str) -> str:
        models = prompt.get_models()
        model = models[game_id]
        system_context = model.system_prompt

        if context:
            system_context += "your history of messages is as follows" + "\n".join(
                context
            )
        completion = self.client.chat.completions.create(
            model=settings.TEXT_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": system_context,
                },
                {
                    "role": "user",
                    "content": text_input,
                },
            ],
        )

        return completion.choices[0].message.content
