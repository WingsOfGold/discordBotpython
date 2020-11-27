def getChannel(channels, name=None):
    for channel in channels:
        if (channel.name == name):
            return channel
    return False

def channelCreate():
    return False
