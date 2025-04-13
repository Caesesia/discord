from discord.ext import commands

# ----------------------------------------------------------------------
# REGROUPE LES COMMANDES DISPONIBLES AUX MEMBRES
# ----------------------------------------------------------------------

class Client(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    async def stats(self, ctx):
        await ctx.send(f"")



# ----------------------------------------------------------------------
# AJOUTE LES COMMANDES POUR UTILISATION
# ----------------------------------------------------------------------

async def setup(bot):
    await bot.add_cog(Client(bot))
