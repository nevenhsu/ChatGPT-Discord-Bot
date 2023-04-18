import os

from dotenv import load_dotenv
import discord

from src.discordBot import DiscordClient, Sender
from src.logger import logger
from src.chatgpt import ChatGPT
from src.models import OpenAIModel
from src.memory import Memory
from src.server import keep_alive

load_dotenv()

models = OpenAIModel(api_key=os.getenv("OPENAI_API"), model_engine=os.getenv("OPENAI_MODEL_ENGINE"))
memory = Memory(system_message=os.getenv("SYSTEM_MESSAGE"))
chatgpt = ChatGPT(models, memory)


def run():
    client = DiscordClient()
    sender = Sender()

    @client.tree.command(name="chat", description="Have a chat with ChatGPT")
    async def chat(interaction: discord.Interaction, *, message: str):
        id = interaction.channel.id
        if interaction.user == client.user:
            return

        try:
            await interaction.response.defer()
            receive = chatgpt.get_response(id, message)
            await sender.send_message(interaction, message, receive)
        except Exception as e:
            logger.error(f"Error chat: {e}")
            await interaction.followup.send(f"> **Error: {e}**")

    @client.tree.command(name="reset", description="Reset to MidJourney Prompt Generator")
    async def reset(interaction: discord.Interaction):
        id = interaction.channel.id
        name = interaction.channel.name
        logger.info(f"resetting memory from {name}")
        try:
            chatgpt.clean_history(id, "mj")
            await interaction.response.defer(ephemeral=True)
            await interaction.followup.send(
                f"> Reset ChatGPT to MidJourney Prompt Generator < - <@{name}>"
            )
        except Exception as e:
            logger.error(f"Error resetting memory: {e}")
            await interaction.followup.send(
                "> **Error: Something went wrong, please try again later!**"
            )

    @client.tree.command(name="story", description="Reset to Short Story Generator")
    async def story(interaction: discord.Interaction):
        id = interaction.channel.id
        name = interaction.channel.name
        logger.info(f"resetting memory from {name}")
        try:
            chatgpt.clean_history(id, "story")
            await interaction.response.defer(ephemeral=True)
            await interaction.followup.send(
                f'> Reset ChatGPT to Short Story Generator < - <@{name}>\nType keywords: "Monster, woods, camping, horror story" , "flowers, field, best friend, sunset", etc.'
            )
        except Exception as e:
            logger.error(f"Error resetting memory: {e}")
            await interaction.followup.send(
                "> **Error: Something went wrong, please try again later!**"
            )

    @client.tree.command(name="default", description="Reset to normal ChatGPT")
    async def default(interaction: discord.Interaction):
        id = interaction.channel.id
        name = interaction.channel.name
        logger.info(f"resetting memory from {name}")
        try:
            chatgpt.clean_history(id, "default")
            await interaction.response.defer(ephemeral=True)
            await interaction.followup.send(
                f"> Reset ChatGPT to default mode < - <@{name}>"
            )
        except Exception as e:
            logger.error(f"Error resetting memory: {e}")
            await interaction.followup.send(
                "> **Error: Something went wrong, please try again later!**"
            )

    client.run(os.getenv("DISCORD_TOKEN"))


if __name__ == "__main__":
    keep_alive()
    run()
