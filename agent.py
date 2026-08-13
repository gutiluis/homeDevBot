from agentic.common import Agent

MODEL = "ollama/qwen3.5:4b"

agent = Agent(
    name="Home Development Agent",
    welcome="I am your local development assistant.",
    instructions="You are a helpful local development assistant.",
    model=MODEL,
)
