import discord
from discord.ext import commands

botToken = "Nzc2NDAxMTQ3OTc1NTY1MzEz.X60V6g.yN4Y4wmj4RR2yGaXsbhSWUlUv7g"

client = commands.Bot(command_prefix = '*')

@client.event
async def on_ready():
    print("Bot is ready!")

async def on_message(message):
    if (message.content.lower() == "ping"):
        channel.send("pong")

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")


client.run(botToken)
