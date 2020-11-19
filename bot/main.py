import discord
import random
from discord.ext import commands


gmMsg = ["Good morning :smile:", "Oh hello! Break a leg :joy:", "Good morning sleephead :upside_down:", "YO! I bought you a cow so you can drink milk!! Although it's a binary cow :cow2:, here's your binary milk :milk:"];
gmMsgNum = 0;

botToken = "Nzc2NDAxMTQ3OTc1NTY1MzEz.X60V6g.yN4Y4wmj4RR2yGaXsbhSWUlUv7g"

client = commands.Bot()

@client.event
async def on_ready():
    print("Bot is ready!")

@client.command(aliases=['hi', 'hello', 'Hi', 'Hello', 'Good morning', 'Gm', 'gm', 'Yo', 'yo'])
async def _doyouknow(ctx):
    byeMsg = ["See you again daddy :smiling_face_with_3_hearts:", 
              "Bell rings, ringning bells, senta's telling you! SAY YOUR PRAYERS! Bye:raised_back_of_hand:",
              "See you homie :woozy_face:",
              "Till another time :upside_down:",
              "Pew it up, Die aside, Pie it down, then next time, maybe PewDiePie shall tell you bye :joy:"]
    await ctx.send(f'{random.choice(byeMsg)}')

@client.command(aliases=['bye', 'cya', 'cu', 'See you later', 'Till we meet', 'Till our path cross'])
async def _doyouknow(ctx):
    gmMsg = ["Good morning :smile:", "Oh hello! Break a leg :joy:",
             "Good morning sleephead :upside_down:",
             "YO! I bought you a cow so you can drink milk!! Although it's a binary cow :cow2:, here's your binary milk :milk:"]
    await ctx.send(f'{random.choice(gmMsg)}')

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency *1000)}ms")

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

client.run(botToken)
