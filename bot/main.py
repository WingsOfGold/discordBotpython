import discord
import random
from discord.ext import commands

botToken = "Nzc2NDAxMTQ3OTc1NTY1MzEz.X60V6g.yN4Y4wmj4RR2yGaXsbhSWUlUv7g"

client = commands.Bot(command_prefix = '*')

@client.command()
async def wlc(ctx):
    await ctx.send("test")
    channel = await guild.create_text_channel('Welcome :wave:')

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_member_join(member):
    print(f'{member} has came!')

@client.event
async def on_member_remove(member):
    print(f'{member} has left!')

@client.command(aliases=['bye', 'cya', 'cu', 'See you later', 'Till we meet', 'Till our path cross'])
async def _doyouknow(ctx):
    gmMsg = ["Good morning :smile:", "Oh hello! Break a leg :joy:",
             "Good morning sleephead :upside_down:",
             "YO! I bought you a cow so you can drink milk!! Although it's a binary cow :cow2:, here's your binary milk :milk:"]
    await ctx.send(f'{random.choice(gmMsg)}')

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong? Ah ping: {round(client.latency *1000)}ms")

client.run(botToken)
