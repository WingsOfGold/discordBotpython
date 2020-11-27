import discord
#import exports as ex
import random
from discord.ext import commands

wlcCategoryName = "____________welcome____________"
wlcTextChannelName = "Welcome :wave:"

botToken = "Nzc2NDAxMTQ3OTc1NTY1MzEz.X60V6g.yN4Y4wmj4RR2yGaXsbhSWUlUv7g"
client = commands.Bot(command_prefix = '*')

def getChannel(channels, name):
    for channel in channels:
        if (channel.name == name):
            return channel
    return False

async def channelCreate(type, guild, name, _overwrites=None, _category=None, _position=0, _topic=None, _slowmode_delay=None, _nsfw=False, _reason=None):
    if (type == "txt"):
        channel = await guild.create_text_channel(name, overwrites=_overwrites, category=_category, position=_position, topic=_topic, slowmode_delay=_slowmode_delay, nsfw=_nsfw, reason=_reason)
    elif (type == "vc"):
        channel = await guild.create_voice_channel(name, overwrites=_overwrites, category=_category, position=_position, topic=_topic, slowmode_delay=_slowmode_delay, nsfw=_nsfw, reason=_reason)
    else:
        channel = await guild.create_category(name, overwrites=_overwrites, category=_category, position=_position, topic=_topic, slowmode_delay=_slowmode_delay, nsfw=_nsfw, reason=_reason)
    return True

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="u snitching"))
    print("Bot is ready!")
                    
@client.command()
async def wlcOn(ctx):
    wlcCategory = True#getChannel(ctx.guild.channels, wlcCategoryName)
    if (wlcCategory):
        await ctx.reply("It's already On!")
    else:
        #channelCreate("txt", ctx.guild, wlcTextChannelName, _category=wlcCategory, _position=2)
        await ctx.reply("Success amigo")

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
