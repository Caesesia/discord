import os
import random
from dotenv import load_dotenv

load_dotenv()
HOMOS = int(os.getenv("HOMOS"))
LOGOS = int(os.getenv("LOGOS"))



async def homos(message):

    liste = ["ulululuuu", "jeu tem...", ":heart:", "tg", "pleure", "https://tenor.com/view/this-man-wriorinde-gif-9100771755843288188"]
    choix = random.choice(liste)

    if message.author.id == LOGOS:
        await message.reply(choix)
