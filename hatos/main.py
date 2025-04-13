from discord.ext import commands
from dotenv import load_dotenv

import os
import discord

from commands.admin import Admin
from commands.user import User
from commands.help import Help

from members.homos import homos
#from members.pathos import pathos
from members.tacos import tacos
#from members.popos import popos
#from members.mynthos import mynthos

from functions.nerd import nerd
from functions.puns import puns
from functions.snitch import snitch

load_dotenv()
TOKEN = os.getenv("TOKEN")
HOMOS = int(os.getenv("HOMOS"))
LOGOS = int(os.getenv("LOGOS"))
PATHOS = int(os.getenv("PATHOS"))
TACOS = int(os.getenv("TACOS"))
POPOS = int(os.getenv("POPOS"))
MYNTHOS = int(os.getenv("MYNTHOS"))

#ID = {HOMOS: homos, LOGOS: logos, PATHOS: pathos, TACOS: tacos, POPOS: popos, MYNTHOS: mynthos}
ID = {HOMOS: homos, TACOS: tacos, LOGOS: tacos}

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = ".", intents = intents, help_command = None)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} au rapport.')
    await bot.load_extension("commands.admin")
    await bot.load_extension("commands.user")
    await bot.load_extension("commands.help")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)

    if message.content.startswith(bot.command_prefix):
        return

    trig = False
    
    if await puns(message):
        trig = True
    elif await nerd(message):
        trig = True

    if not trig:
        cible = ID.get(message.author.id)
        if cible:
            await cible(message)
     
@bot.event
async def on_message_delete(message):
    if message.author == bot.user:
        return

    await snitch(message)



bot.run(TOKEN)
