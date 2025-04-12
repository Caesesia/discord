# This example requires the 'message_content' intent.


from dotenv import load_dotenv

import os
import random
import discord

from snitch import snitch


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

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower().strip().replace(" ", "")

    liste = ["ouais", "c'est", "greg"]
    choix = random.choice(liste)

    if "allo" in msg or "allô" in msg:
        await message.reply('selem?')

    elif msg == "quoi" or msg == "quoi?":
        await message.reply("FEUR")

    elif "https://" in message.content and "elsword" in message.content or "https://" in message.content and "nerd" in message.content:
        await message.reply("Nerd :nerd:")

    elif message.author.id == LOGOS:
        await message.reply(choix)

@client.event
async def on_message_delete(message):
    if message.author == client.user:
        return

    await snitch(message)


client.run(TOKEN)
