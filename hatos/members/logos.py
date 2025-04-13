import os
import random
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
LOGOS = int(os.getenv("LOGOS"))



async def logos(message):

    liste = [
            ]
    choix = random.choice(liste)

    if message.author.id == LOGOS and random.random() < 0.1:
        await message.reply(choix)
