import discord
import random
from discord.ext import commands

botToken = "Nzc2NDAxMTQ3OTc1NTY1MzEz.X60V6g.yN4Y4wmj4RR2yGaXsbhSWUlUv7g"
client = commands.Bot(command_prefix = '*')

async def channel(guild, channelName=None):
    return 213
@client.event
async def on_ready():
    print("Bot is ready!")

#@client.event
#async def on_member_join(member):
#    welcomeText.send(f'{member} has came!')

#@client.event
#async def on_member_remove(member):
#    welcomeText.send(f'{member} has left!')

#@client.command()
#async def svstatson(ctx):
#    aC = getChannel(ctx.guild, "")

#@client.command()
#async def svstatsoff(ctx):
#    ac = getChannel(ctx.guild, "
                    
@client.command()
async def wlcOn(ctx):
    await ctx.send(f"Phase 1 is Complete {channel(ctx.guild, "general"}")
    #for channel in ctx.guild.channels:
        #await ctx.send(f'{channel.name}')

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong? Ah ping: {round(client.latency *1000)}ms")

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes - definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, rey again.',
                 'Ask again later.',
                 'better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 "Don't count on it.",
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 '-_-',
                 'Very doubtful.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

client.run(botToken)
