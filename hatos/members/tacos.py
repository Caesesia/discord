import os
import random
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
TACOS = int(os.getenv("TACOS"))
LOGOS = int(os.getenv("LOGOS"))



async def tacos(message):

    liste = [
            "https://tenor.com/view/nerd-emoji-meme-this-you-gif-25696106",
            "https://tenor.com/view/me-playing-bowser-jr-nintendo-switch-2-final-fantasy-gif-5144056626380487676",
            "ulululuuu",
            "Zack détruit Cloud",
            "https://tenor.com/view/average-dark-soul-fan-vs-average-dark-soul-ii-enjoyer-gif-26366961",
            "pler",
            '"Peak character writing" :',
            "https://tenor.com/view/honey-final-fantasy-gif-dancing-twirl-video-game-gif-16574338"
            ]
    choix = random.choice(liste)

    if message.author.id == TACOS and random.random() < 0.2:
        if choix == liste[6] or choix == liste[7]:
            await message.reply(liste[6])
            await message.channel.send(liste[7])
        else:
            await message.reply(choix)
