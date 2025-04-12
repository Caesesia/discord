async def nerd(message):

    if "https://" in message.content and "elsword" in message.content or "https://" in message.content and "nerd" in message.content:
        await message.reply("Nerd :nerd:")
        return True
