import discord
from discord.ext import commands

from exports import test

client = commands.Bot(command_prefix='*')#, intents=intents)
botToken = "Nzc2NDAxMTQ3OTc1NTY1MzEz.X60V6g.yN4Y4wmj4RR2yGaXsbhSWUlUv7g"

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong? Ah! Ping: {round(client.latency *1000)}ms")

@client.event
async def on_ready():
    await client.get_channel(782480148011679844).send("I'm ready!")
    await client.get_channel(782480148011679844).send(test.re())

client.run(botToken)
