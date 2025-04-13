import os
import random
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
MYNTHOS= int(os.getenv("MYNTHOS"))
LOGOS = int(os.getenv("LOGOS"))



async def mynthos(message):

    liste = [
            ]
    choix = random.choice(liste)

    if message.author.id == MYNTHOS and random.random() < 0.1:
        if choix == liste[4] or choix == liste[5]:
            await message.reply(liste[4])
            await message.channel.send(liste[5])
        else:
            await message.reply(choix)
