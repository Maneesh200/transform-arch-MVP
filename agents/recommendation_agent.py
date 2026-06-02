import json

from agents.base_agent import BaseAgent
from llm.gemini_client import GeminiClient


class RecommendationAgent(BaseAgent):

    def execute(self, context):

        architecture = context.architecture_detection

        domain_analysis = context.domain_analysis

        dependency_analysis = context.dependency_analysis

        domain_count = len(
            domain_analysis.get("domains", [])
        )

        coupling_score = dependency_analysis.get(
            "coupling_score",
            0
        )

        metrics = {

            "domain_count": domain_count,

            "node_count":
                dependency_analysis.get(
                    "node_count",
                    0
                ),

            "edge_count":
                dependency_analysis.get(
                    "edge_count",
                    0
                ),

            "coupling_score":
                coupling_score
        }

        prompt = f"""
You are an expert software architect.

Analyze the following application.

Architecture:
{architecture}

Metrics:
{metrics}

Domain Analysis:
{domain_analysis}

Provide concise architecture recommendations.

Rules:

1. reasoning must contain short bullet points.
2. Each reasoning item must be under 15 words.
3. Do not write paragraphs.
4. Return ONLY valid JSON.

Return ONLY valid JSON.

Format:

{{
  "recommended_target_architecture": "",
  "migration_complexity": "",
  "confidence": 0,
  "recommended_services": [],
  "reasoning": []
}}
"""

        client = GeminiClient()

        response = client.invoke(
            prompt
        )

        try:

            cleaned = (
                response
                .replace("```json", "")
                .replace("```", "")
                .strip()
            )

            context.recommendations = (
                json.loads(cleaned)
            )

        except Exception:

            context.recommendations = {

                "error":
                    "Unable to parse Gemini response",

                "raw_response":
                    response
            }

        return context