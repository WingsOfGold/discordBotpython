import discord
import random
from discord.ext import commands

botToken = "Nzc2NDAxMTQ3OTc1NTY1MzEz.X60V6g.yN4Y4wmj4RR2yGaXsbhSWUlUv7g"
client = commands.Bot(command_prefix = '*')
welcomeCategory = false
welcomeText = false

@client.event
async def on_ready():
    print("Bot is ready!")

@client.command()
async def wlc(ctx):
    global welcomeCategory, welcomeText
    welcomeCategory = await ctx.guild.create_category('Testing')
    welcomeText = await ctx.guild.create_text_channel('Welcome', category=welcomeCategory)

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong? Ah ping: {round(client.latency *1000)}ms")

@client.event
async def on_member_join(member):
    if (welcomeText):
        welcomeText.send(f'{member} has came!')

@client.event
async def on_member_remove(member):
    if (welcomeText):
        welcomeText.send (f'{member} has left!')

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
                 'Very doubtful.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command(aliases=['bye', 'cya', 'cu', 'See you later', 'Till we meet', 'Till our path cross'])
async def _doyouknow(ctx):
    gmMsg = ["Good morning :smile:", "Oh hello! Break a leg :joy:",
             "Good morning sleephead :upside_down:",
             "YO! I bought you a cow so you can drink milk!! Although it's a binary cow :cow2:, here's your binary milk :milk:"]
    await ctx.send(f'{random.choice(gmMsg)}')

client.run(botToken)
