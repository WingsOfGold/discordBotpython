import discord
import random
from discord.ext import commands

serverName = "Diamond"

svsCtgPos = 0
svsCategoryName = serverName + "'s Stats"
svsTotalName = "All Members: "
svsMembersName = "Members: "
svsBotsName = "Bots: "

wlcCtgPos = 1
wlcCategoryName = "____________welcome____________"
wlcRulesName = "Rules"
wlcAnouncementsName = "Anouncements"

botToken = "Nzc2NDAxMTQ3OTc1NTY1MzEz.X60V6g.yN4Y4wmj4RR2yGaXsbhSWUlUv7g"
client = commands.Bot(command_prefix = '*')

def getChannel(g, name):
    for channel in g.channels:
        if (channel.name == name):
            return channel
    return False

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="u snitching"))
    await client.get_channel(776501520471949337).send("I'm ready!")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong? Ah ping: {round(client.latency *1000)}ms")

@client.command()
async def start(ctx):
    await ctx.guild.create_category("TEST", position=0)

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
