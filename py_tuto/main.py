# This example requires the 'message_content' intent.


from dotenv import load_dotenv
import os
import random
import discord


load_dotenv()
token = os.getenv("TOKEN")


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

    elif message.author.id == 757771138678915142:
        await message.reply(choix)



@client.event
async def on_message_delete(message):
    if message.author == client.user:
        return

    await message.channel.send(f'/!\\ {message.author} n\'assume pas d\'avoir dit "{message.content}"')


client.run(token)
