from agentic.common import Agent, AgentRunner

MODEL = "ollama/qwen3.5:4b"

agent = Agent(
    name="Local Test Agent",
    welcome="I am a local development assistant.",
    instructions="You are a helpful local development assistant.",
    model=MODEL,
)

if __name__ == "__main__":
    AgentRunner(agent).repl_loop()
