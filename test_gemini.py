from llm.gemini_client import GeminiClient

client = GeminiClient()

response = client.invoke(
    "Say Hello World"
)

print(response)