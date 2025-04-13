import os
import random
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
TACOS = int(os.getenv("TACOS"))
print(TACOS)
LOGOS = int(os.getenv("LOGOS"))
print(LOGOS)


async def tacos(message):

    liste = [
            "ulululuuu",
            "Zack détruit Cloud",
            "tg",
            "pler",
            '"Peak character writing" :',
            "https://tenor.com/view/honey-final-fantasy-gif-dancing-twirl-video-game-gif-16574338"
            ]
    choix = random.choice(liste)

    if message.author.id == TACOS and random.random() < 0.1:
        if choix == liste[4] or choix == liste[5]:
            await message.reply(liste[4])
            await message.channel.send(liste[5])
        else:
            await message.reply(choix)
