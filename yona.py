import discord
from discord.ext import commands
import asyncio
import os
import time
import math
import random


bot = commands.Bot("ÄÄÄ", self_bot=True)

client = discord.Client()

choicefile=open("cum.txt","r")
linelist=[]
for line in choicefile:
    linelist.append(line)
choice=random.choice(linelist)


@bot.event
async def on_message(message):
    if message.author == bot.user:
            return

    if (message.channel.id == put a channel id here):
        async with message.channel.typing():
            type_time = random.uniform(0.5, 10)
            await asyncio.sleep(type_time)
            await message.channel.send(random.choice(linelist))
            time.sleep(100)
            



bot.run("put token here", bot=False)


