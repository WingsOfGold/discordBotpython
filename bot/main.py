import discord
from discord.ext import commands

botToken = "Nzc2NDAxMTQ3OTc1NTY1MzEz.X60V6g.yN4Y4wmj4RR2yGaXsbhSWUlUv7g"

client = commands.Bot(command_prefix = '*')

@client.event
async def on_ready():
    print("Bot is ready!")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency *1000)}ms")


client.run(botToken)
