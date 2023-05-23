import discord
from discord import app_commands

TOKEN='MTExMDE1OTQwODEwNjg0MDE4Nw.GcF6Xe.E3V6464aFLoZ4zK3AUT9bcPACpecFUAugKcy6g'
intents=discord.Intents.default()
intents.message_content=True
client =discord.Client(intents=intents)
tree=app_commands.CommandTree(client)


@tree.command
