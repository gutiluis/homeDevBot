> [!WARNING]
> CURRENTLY UNDER DEVELOPMENT

# homeDevBot

A personal, local-development Discord AI bot that connects a **Discord User Install** application to a local AI agent powered by **Supercog Agentic** and **Ollama**.

## Description

`homeDevBot` is a Python-based Discord application designed for personal development and experimentation with local AI agents.

The bot exposes an `/ask` slash command in Discord. When a user submits a prompt, the request is passed from Discord to the local Supercog Agentic framework, which uses Ollama to interact with a locally running language model. The generated response is then returned to Discord.

The project is designed to keep the AI workload local rather than relying on a hosted LLM API.


### Request Flow

1. The user installs `homeDevBot` as a **Discord User Install** application.
2. The user invokes `/ask` in Discord.
3. `bot.py` receives the interaction.
4. The prompt is passed to the Agentic agent defined in `agent.py`.
5. Supercog Agentic orchestrates the agent interaction.
6. Ollama provides access to the locally running language model.
7. The generated result is returned to Discord.

---

## Features

* **Discord User Install** — The application is installed to a user's Discord account rather than requiring installation as a guild bot.
* **Slash Command Interface** — Interact with the agent through the `/ask` Discord application command.
* **Local AI** — Uses Ollama to run the language model locally.
* **Agent Framework** — Uses Supercog Agentic for agent orchestration.
* **Python-Based** — Built with Python and `discord.py`.
* **Environment Configuration** — Sensitive configuration is loaded from `.env`.
* **Error Handling** — Agent errors are caught and reported without exposing internal exceptions to Discord users.
* **Testable Agent Layer** — Agent functionality is separated from the Discord interface, allowing the agent to be tested independently.
* **Reproducible Environment** — Python version and project dependencies are documented in `.python-version` and `requirements.txt`.

---

## How it works


### 1. Clone the Repository

```bash
git clone https://github.com/gutiluis/homeDevBot.git
cd homeDevBot
```

### 2. Create the Python Environment

The project uses Python 3.11 because the current Supercog Agentic framework requires Python 3.11 or newer and less than Python 3.13.

If using `pyenv`:

```bash
pyenv install 3.11.9
pyenv virtualenv 3.11.9 homeDevBot
pyenv local homeDevBot
```

Verify:

```bash
python --version
```

Expected:

```text
Python 3.11.9
```

### 3. Install Dependencies

Install the project dependencies:

```bash
pip install -r requirements.txt
```

This installs the Discord integration, environment configuration, and Supercog Agentic framework.

### 4. Configure Environment Variables

Create a local `.env` file from the provided example:

```bash
cp .env.example .env
```

Open `.env` and add your Discord bot token:

```text
DISCORD_BOT_TOKEN=your_discord_bot_token
```

**Do not commit `.env` to GitHub.**

The repository's `.gitignore` excludes the file.

### 5. Configure Ollama

Install and start Ollama, then make sure the local model you want to use is available.

Verify that Ollama is running before starting the Discord application.

The specific model configuration is defined by the Agentic setup in `agent.py`.

### 6. Configure the Discord Application

Create a Discord application in the Discord Developer Portal.

Under **Installation**:

* Enable **User Install**
* Configure the application command scope
* Generate the installation link
* Open the installation link
* Authorize the application for your Discord account

`homeDevBot` is designed as a **User Install** application and does not need to be installed as a traditional guild bot in your personal `homeBot` server.

### 7. Test the Agent

Before starting Discord, verify that the Agentic integration works:

```bash
python -c "from agent import agent; print(agent.grab_final_result('What is 2 + 2?'))"
```

The agent should return a response.

### 8. Start the Discord Bot

Run:

```bash
python bot.py
```

You should see:

```text
Logged in as YourBotName
```

Keep this process running while using the bot.

### 9. Use the Bot in Discord

Open Discord and use the application in a location where your User Install is available.

Enter:

```text
/ask
```

Then provide your prompt.

For example:

```text
/ask What is 2 + 2?
```

The request is sent to the local Agentic/Ollama stack and the response is returned to Discord.

### Stopping the Bot

The Discord application runs as a local Python process. When you're finished using it, stop it with:

```text
Ctrl+C
```

Because `homeDevBot` is a local-development project, the bot only needs to be running when you want to use or test it.


---

## Tech Stack

- Python 3.11.9
- discord.py
- Supercog Agentic
- Ollama
- python-dotenv
- Git / GitHub


`bot.py` handles the Discord application interface, while `agent.py` contains the agent logic. This separation allows the AI component to be tested independently from Discord.

---

## Contributing

If you are interested in reporting/fixing issues and contributing directly to the code base, please see [CONTRIBUTING.md](https://github.com/gutiluis/.github/blob/main/CONTRIBUTING.md) for more information on what we're looking for and how to get started.

---

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](https://github.com/gutiluis/.github/blob/main/CODE_OF_CONDUCT.md).

---

## Security Policy

The Discord bot token is stored in a local `.env` file and is intentionally excluded from version control.

The repository includes `.env.example` as a template for the required environment variable without exposing credentials.

```text
DISCORD_BOT_TOKEN=your_discord_bot_token_here
```

Never commit the real `.env` file or expose your Discord bot token publicly.


If you discover a security vulnerability, please review our [Security Policy](https://github.com/gutiluis/.github/blob/main/SECURITY.md) for reporting guidelines.

---

## Support

If you run into any issues or have questions, please check our [SUPPORT.md](https://github.com/gutiluis/.github/blob/main/SUPPORT.md) file for guidance, or reach out through one of our community channels below.

---

## Community

Info on reporting bugs, getting help, finding third-party tools and sample apps, and more can be found on our **Community** channels:
* **Discord:** [Community channel](https://discord.gg/5xdAFuadP)
* **Slack Workspace:** [technobool.slack.com](https://technobool.slack.com)
* **GitHub Discussions:** [Open a discussion](https://github.com/gutiluis/homeDevBot/discussions)

---

## License

[MIT LICENSE](LICENSE)
