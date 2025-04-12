from discord.ext import commands
from dotenv import load_dotenv

import os
import random
import discord

from snitch import snitch
from puns import pun
from homos import homos
from nerd import nerd
from commands import ok

load_dotenv()
TOKEN = os.getenv("TOKEN")
HOMOS = int(os.getenv("HOMOS"))
LOGOS = int(os.getenv("LOGOS"))
PATHOS = int(os.getenv("PATHOS"))
TACOS = int(os.getenv("TACOS"))
POPOS = int(os.getenv("POPOS"))
MYNTHOS = int(os.getenv("MYNTHOS"))


intents = discord.Intents.default()
intents.message_content = True

# client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix = "hatos ", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} au rapport.')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    trig = False
 
    await bot.process_commands(message)

    if message.content.startswith(bot.command_prefix):
        trig = True
    elif await pun(message):
        trig = True
    elif await nerd(message):
        trig = True

    if not trig:
        await homos(message)
     
@bot.event
async def on_message_delete(message):
    if message.author == bot.user:
        return

    await snitch(message)


@bot.command()
async def test(ctx):
    await ok(ctx)


bot.run(TOKEN)
