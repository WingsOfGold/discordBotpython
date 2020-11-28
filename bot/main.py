import discord
import random
from discord.ext import commands

serverName = "Diamond"

svsCtgPosition = 0
svsCategoryName = serverName + "'s Stats"
svsTotalName = "All Members: "
svsMembersName = "Members: "
svsBotsName = "Bots: "

wlcCtgPosition = 1
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

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong? Ah ping: {round(client.latency *1000)}ms aa")

@client.command()
async def svsCtgOn(ctx):
    svsCategoryI = getChannel(ctx.guild, svsCategoryName)
    if (svsCategoryI):
        await ctx.send("It's already on!")
    else:
        svsCategory = await ctx.guild.create_category(svsCategoryName, position=svsCtgPosition)
        await ctx.guild.create_voice_channel(svsTotalName, category=svsCategory)
        await ctx.guild.create_voice_channel(svsMembersName, category=svsCategory)
        await ctx.guild.create_voice_channel(svsBotsName, category=svsCategory)
        await ctx.send("Category initiated!")
    
@client.command()
async def wlcCtgOn(ctx):
    wlcCategoryI = getChannel(ctx.guild, wlcCategoryName)
    svsCategory = getChannel(ctx.guild, svsCategoryName)
    if (wlcCategoryI):
        await ctx.send("It's already on!")
        return True
    else:
        num = wlcCtgPosition - 1
        if (svrsCategory):
            num = wlcCtgPosition
        wlcCategory = await ctx.guild.create_category(wlcCategoryName, position=num)
        await ctx.create_text_channel(wlcRulesName, category=wlcCategory)
        await ctx.create_text_channel(wlcAnouncementsName, category=wlcCategory)
        await ctx.send("Category initiated!")

#@client.command()
#async def wlcCtgOff(ctx):
#    wlcCategoryI = getChannel(ctx.guild, wlcCategoryName)
#    if (not wlcCategoryI):
#        await ctx.send("It's not on!")
#        return True
#    for channel in wlcCategoryI.channels:
#        channel.delete()
#    wlcCategoryI.delete()
#    await ctx.send("Category obliterated!")

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
