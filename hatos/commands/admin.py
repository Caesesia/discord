from discord.ext import commands

# ----------------------------------------------------------------------
# REGROUPE LES METHODES LIEES A L'ADMINISTRATION DU SERVEUR
# ----------------------------------------------------------------------

class Admin(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help = "Affiche le nom de l'utilisateur et le serveur où la commande a été effectuée")
    async def info(self, ctx):
        await ctx.send(f"Salam aleykoum **{ctx.author}** ! Tu te trouves actuellement sur le serveur **{ctx.guild}**. Utilise **.aled** pour obtenir la liste des commandes disponibles !")



# ----------------------------------------------------------------------
# AJOUTE LES COMMANDES POUR UTILISATION
# ----------------------------------------------------------------------

async def setup(bot):
    await bot.add_cog(Admin(bot))
