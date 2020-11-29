import discord
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
    for c in g.channels:
        n = c.name
        if (n.find(name)):
            await client.get_channel(782480148011679844).send(f"'{c.name}' and '{name}'")
            return c
    return False

async def updateSvsStats(g):
    await client.get_channel(782480148011679844).send("REached updateSVsStats")
    await getChannel(g, svsTotalName).edit(name=svsTotalName + str(len(g.members)))

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="u snitching"))
    await client.get_channel(782480148011679844).send("I'm ready!")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong? Ah! Ping: {round(client.latency *1000)}ms")

# Server Stats Code:
@client.command()
async def svsCtgOn(ctx):
    svsCategoryI = getChannel(ctx.guild, svsCategoryName)
    if (svsCategoryI):
        await ctx.send("It's already on!")
    else:
        every1 = get(ctx.guild.roles, name="@everyone")
        overwrites = {
            every1: discord.PermissionOverwrite(connect=False)
        }
        svsCategory = await ctx.guild.create_category(svsCategoryName, position=svsCtgPos)
        await svsCategory.edit(position=svsCtgPos)
        await ctx.guild.create_voice_channel(svsTotalName, category=svsCategory, overwrites=overwrites)
        await ctx.guild.create_voice_channel(svsMembersName, category=svsCategory, overwrites=overwrites)
        await ctx.guild.create_voice_channel(svsBotsName, category=svsCategor, overwrites=overwritesy)
        await ctx.send("Category has been initiated!")

@client.command()
async def svsCtgOff(ctx):
    svsCategory = getChannel(ctx.guild, svsCategoryName)
    if (not svsCategory):
        await ctx.send("It's not on!")
        return True
    for channel in svsCategory.channels:
        await channel.delete()
    await svsCategory.delete()
    await ctx.send("Category has been obliterated!")

@client.event
async def on_guild_channel_create(c):
    if (c.name == svsTotalName):
        updateSvsStats(c.guild)

#@client.event
#async def on_member_join(member):
    #updateSvsStats(member.guild)

#@client.event
#async def on_member_remove(member):
    #updateSvsStats(member.guild)

# Welcome Category Code:
@client.command()
async def wlcCtgOn(ctx):
    wlcCategoryI = getChannel(ctx.guild, wlcCategoryName)
    svsCategoryI = getChannel(ctx.guild, svsCategoryName)
    if (wlcCategoryI):
        await ctx.send("It's already on!")
    else:
        num = wlcCtgPos - 1
        if (svsCategoryI):
            num += 1
        wlcCategory = await ctx.guild.create_category(wlcCategoryName, position=svsCtgPos)
        await wlcCategory.edit(position=num)
        await ctx.guild.create_text_channel(wlcRulesName, category=wlcCategory)
        await ctx.guild.create_text_channel(wlcAnouncementsName, category=wlcCategory)
        await ctx.send("Category has been initiated!")

@client.command()
async def wlcCtgOff(ctx):
    wlcCategoryI = getChannel(ctx.guild, wlcCategoryName)
    if (not wlcCategoryI):
        await ctx.send("It's not on!")
        return True
    for channel in wlcCategoryI.channels:
        await channel.delete()
    await wlcCategoryI.delete()
    await ctx.send("Category has been obliterated!")

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
