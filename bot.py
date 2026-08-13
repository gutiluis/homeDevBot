import os

import discord
from discord import app_commands
from dotenv import load_dotenv

from agent import agent

load_dotenv()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")


class MyClient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)

        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()


client = MyClient()


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.tree.command(
    name="ask",
    description="Ask my local AI agent a question.",
)
async def ask(interaction: discord.Interaction, prompt: str):
    await interaction.response.defer()

    try:
        result = agent.grab_final_result(prompt)
        await interaction.followup.send(result)

    except Exception as exc:
        print(f"Agent error: {exc}")
        await interaction.followup.send("Sorry, I couldn't process that request.")


client.run(TOKEN)
