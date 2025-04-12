async def pun(message):

    msg = message.content.lower().strip().replace(" ", "")

    if "allo" in msg or "allô" in msg:
        await message.reply('selem?')

    elif msg == "quoi" or msg == "quoi?":
        await message.reply("FEUR")


