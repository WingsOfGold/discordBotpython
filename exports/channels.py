import discord
from discord.utils import get

serverName = "Diamond"

svsCtgPos = 0
svsCategoryName = serverName + "'s Stats"
svsTotalName = "All Members:"
svsMembersName = "Members:"
svsBotsName = "Bots:"

wlcCtgPos = 1
wlcCategoryName = "____________welcome____________"
wlcRulesName = "Rules"
wlcAnouncementsName = "Anouncements"
client = False

def setClient(bot):
    global client
    client = bot

def getChannel(g, name):
    for c in g.channels:
        if (c.name.find(name) > -1):
            return c
    return False

async def updateSvsStats(g):
    allMem = 0
    mem = 0
    bot = 0
    for member in g.members:
        allMem += 1
        if (member.bot):
            bot += 1
        else:
            mem += 1
    await getChannel(g, svsBotsName).edit(name=svsBotsName + " " + str(bot))
    await getChannel(g, svsMembersName).edit(name=svsMembersName + " " + str(mem))
    await getChannel(g, svsTotalName).edit(name=svsTotalName + " " + str(allMem))

@client.command()
async def tartar(ctx):
    await ctx.send("I'm here I'm here stop tartaring")
"""
@client.event
async def on_guild_channel_create(c):
    if (c.name.find(svsTotalName) > -1):
        await updateSvsStats(c.guild)

@client.event
async def on_guild_channel_update(cOld, cNew):
    if (c.name.find(svsTotalName) > -1):
        await updateSvsStats(c.guild)

@client.event
async def on_guild_channel_delete(c):
    if (c.name.find(svsTotalName) > -1):
        await updateSvsStats(c.guild)

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
        svsCategory = await ctx.guild.create_category(svsCategoryName, position=svsCtgPos, overwrites=overwrites)
        await svsCategory.edit(position=svsCtgPos)
        await ctx.guild.create_voice_channel(svsTotalName, category=svsCategory)
        await ctx.guild.create_voice_channel(svsMembersName, category=svsCategory)
        await ctx.guild.create_voice_channel(svsBotsName, category=svsCategory)
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

# Welcome Stats Code:
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
        every1 = get(ctx.guild.roles, name="@everyone")
        overwrites = {
            every1: discord.PermissionOverwrite(
                manage_roles = False,
                manage_nicknames = False,
                manage_emojis = False,
                manage_permissions = False,
                manage_webhooks = False,
                read_messages=True, 
                send_messages=False,
                send_tts_messages = False,
                external_emojis = False,
                mention_everyone = False,
                read_message_history = True,
                attach_files = False,
                embed_links = False,
                manage_messages = False,
                manage_channels = False,
                add_reactions = True,
                create_instant_invite = True,
            )
        }
        wlcCategory = await ctx.guild.create_category(wlcCategoryName, position=svsCtgPos, overwrites=overwrites)
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
    await ctx.send("Category has been obliterated!")"""
