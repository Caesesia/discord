import os
import random
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
POPOS = int(os.getenv("POPOS"))
LOGOS = int(os.getenv("LOGOS"))



async def popos(message):

    liste = [
            "ulululuuu",
            "https://tenor.com/view/dying-dies-dies-from-cringe-dying-from-cringe-dies-to-cringe-gif-7438506245051526559",
            "https://tenor.com/view/star-wars-cringe-dies-from-cringe-meme-star-wars-meme-gif-22116997",
            "https://tenor.com/view/dies-dying-cringe-cringe-die-dies-from-cringe-gif-2120415937878153850",
            ]
    choix = random.choice(liste)

    if message.author.id == POPOS and random.random() < 0.1:
        await message.reply(choix)
