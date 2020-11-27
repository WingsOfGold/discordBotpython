import discord
import random
from discord.ext import commands

serverName = "Diamond"
svrsCategoryName = serverName + "s Stats"
svrsTotalName = "All Members: "
svrsMembersName = "Members: "
svrsBotsName = "Bots: "

wlcCategoryName = "____________welcome____________"
wlcChannelName = "Welcome"
wlcRulesName = "Rules"
wlcAnouncementsName = "Anouncements"

botToken = "Nzc2NDAxMTQ3OTc1NTY1MzEz.X60V6g.yN4Y4wmj4RR2yGaXsbhSWUlUv7g"
client = commands.Bot(command_prefix = '*')

def getChannel(channels, name):
    for channel in channels:
        if (channel.name == name):
            return channel
    return False

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="u snitching"))

@client.command(aliases=['wlcCategoryOn'])
async def wlcCategoryOn(ctx):
    ctx.send("TEST")
"""
@client.command(aliases=['wlcCategoryOff'])
async def wlcCategoryOff(ctx)
    wlcCategory = getChannel(ctx.guild.channels, wlcCategoryName)
    if (wlcCategory):
        for channel in wlcCategory.channels:
            channel.delete()
        wlcCategory.delete()
        ctx.send("Success mon amie")
    else:
        ctx.send("It's already off!")
"""
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong? Ah ping: {round(client.latency *1000)}ms aa")

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
