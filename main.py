import discord
from discord import app_commands

TOKEN='MTExMDE1OTQwODEwNjg0MDE4Nw.Ghisox.6WDidCFeXhNvpyZe7Yo7sBN7LY0uIWaygN9uvI'
intents=discord.Intents.default()
intents.message_content=True
client =discord.Client(intents=intents)
tree=app_commands.CommandTree(client)


@tree.command
