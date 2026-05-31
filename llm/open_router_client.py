import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


class OpenRouterClient:

    def __init__(self):

        self.client = OpenAI(

            base_url="https://openrouter.ai/api/v1",

            api_key=os.getenv(
                "OPENROUTER_API_KEY"
            )
        )

    def invoke(

        self,

        prompt,

        model="google/gemini-2.5-flash"

    ):

        response = self.client.chat.completions.create(

            model=model,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )

        return response.choices[0].message.content