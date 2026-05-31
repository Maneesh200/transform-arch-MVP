import json

from agents.base_agent import BaseAgent
from llm.gemini_client import GeminiClient


class DomainDiscoveryAgent(BaseAgent):

    def execute(self, context):

        repo = context.repository_analysis

        class_names = []

        for group in [

            repo["controllers"],
            repo["services"],
            repo["repositories"],
            repo["entities"]

        ]:

            for item in group:

                class_names.append(
                    item["name"]
                )

        prompt = f"""
You are a software architect.

Group the following classes into business domains.

Classes:

{class_names}

Return ONLY valid JSON.

Format:

{{
  "domains": [
    {{
      "name": "DomainName",
      "classes": []
    }}
  ]
}}
"""

        client = GeminiClient()

        response = client.invoke(prompt)

        try:

            cleaned = response.replace(
                "```json",
                ""
            ).replace(
                "```",
                ""
            ).strip()

            context.domain_analysis = json.loads(
                cleaned
            )

        except Exception:

            context.domain_analysis = {

                "error": "Unable to parse Gemini response",

                "raw_response": response
            }

        return context