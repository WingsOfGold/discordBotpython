import discord
from discord.ext import commands

def getChannel(channels, name):
    for channel in channels:
        if (channel.name == name):
            return channel
    return False

def channelCreate(type, guild, name, _overwrites=None, _category=None, _position=0, _topic=None, _slowmode_delay=None, _nsfw=False, _reason=None):
    if (type == "txt"):
        channel = await guild.create_text_channel(name, overwrites=_overwrites, category=_category, position=_position, topic=_topic, slowmode_delay=_slowmode_delay, nsfw=_nsfw, reason=_reason)
    elif (type == "vc"):
        channel = await guild.create_voice_channel(name, overwrites=_overwrites, category=_category, position=_position, topic=_topic, slowmode_delay=_slowmode_delay, nsfw=_nsfw, reason=_reason)
    else:
        channel = await guild.create_category(name, overwrites=_overwrites, category=_category, position=_position, topic=_topic, slowmode_delay=_slowmode_delay, nsfw=_nsfw, reason=_reason)
    return Channel or False
