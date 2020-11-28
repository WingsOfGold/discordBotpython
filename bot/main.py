import discord
import random
from discord.ext import commands

botToken = "Nzc2NDAxMTQ3OTc1NTY1MzEz.X60V6g.yN4Y4wmj4RR2yGaXsbhSWUlUv7g"
client = commands.Bot(command_prefix = '*')

@client.event
async def on_ready():
    await client.get_channel(776501520471949337).send("I'm ready!")

@client.command()
async def start(ctx):
    a = await ctx.guild.create_category("TEST", position=0)
    a.position = 0

client.run(botToken)
