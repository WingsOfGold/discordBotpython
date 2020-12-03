import discord
from discord.ext import commands
#import exports.test as ex

client = commands.Bot(command_prefix='*', intents=intents)
botToken = "Nzc2NDAxMTQ3OTc1NTY1MzEz.X60V6g.yN4Y4wmj4RR2yGaXsbhSWUlUv7g"
@client.event
async def on_ready():
    await client.get_channel(782480148011679844).send("I'm ready!")
    #await client.get_channel(782480148011679844).send(ex.re)

client.run(botToken)
