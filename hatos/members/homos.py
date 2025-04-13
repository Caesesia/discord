import os
import random
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
HOMOS = int(os.getenv("HOMOS"))
LOGOS = int(os.getenv("LOGOS"))



async def homos(message):
    liste = [
            "https://tenor.com/view/dyslexia-dyslexic-omori-kel-kel-omori-gif-26554958",
            "Ramsès... :broken_heart:",
            ":heart:",
            "tg",
            "pleure",
            "https://tenor.com/view/this-man-wriorinde-gif-9100771755843288188"
            ]
    choix = random.choice(liste)

    if message.author.id == HOMOS and random.random() < 0.1:
        await message.reply(choix)
