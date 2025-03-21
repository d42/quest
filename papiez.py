import uuid
import httpx
from openai import OpenAI
from quest.core.config import settings


def generate_job_id():
    return "sdk_image_" + str(uuid.uuid4())


def main():
    client = OpenAI(
        api_key=settings.HEURIST_API,  # for API key visit = https://dev-api-form.heurist.ai/
        base_url=settings.HEURIST_URL,
    )

    completion = client.chat.completions.create(
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
    print(completion.choices[0].message.content)
    # model = "ArthemyComics"
    #
    # url = "http://sequencer.heurist.xyz/submit_job"
    #
    # payload = {
    #     "job_id": generate_job_id(),
    #     "model_input": {
    #         "SD": {
    #             "prompt": "A beautiful landscape with mountains and a river",
    #             "neg_prompt": "Avoid any signs of human presence",
    #             "num_iterations": 20,
    #             "width": 1024,
    #             "height": 512,
    #             "guidance_scale": 7.5,
    #             "seed": -1,
    #         }
    #     },
    #     "model_id": model,
    #     "deadline": 60,
    #     "priority": 1,
    # }
    # headers = {
    #     "Authorization": f"Bearer {settings.HEURIST_API}",
    #     "Content-Type": "application/json",
    # }
    #
    # response = httpx.request("POST", url, json=payload, headers=headers)
    # print(response.text)
    #


if __name__ == "__main__":
    main()
