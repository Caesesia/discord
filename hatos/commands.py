from discord.ext import commands


# ----------------------------------------------------------------------
# REGROUPE LES METHODES LIEES A L'ADMINISTRATION DU SERVEUR
# ----------------------------------------------------------------------

class Server(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help = "Affiche le nom de l'utilisateur et le serveur où la commande a été effectuée")
    async def info(self, ctx):
        await ctx.send(f"Salam aleykoum **{ctx.author}** ! Tu te trouves actuellement sur le serveur **{ctx.guild}**. Utilise **.aled** pour obtenir la liste des commandes disponibles !")





# ----------------------------------------------------------------------
# REGROUPE LES COMMANDES DISPONIBLES AUX MEMBRES
# ----------------------------------------------------------------------

class Client(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    async def stats(self, ctx):
        await ctx.send(f"")





# ----------------------------------------------------------------------
# REGROUPE LES COMMANDES LIEES AU FONCTIONNEMENT DU BOT 
# ----------------------------------------------------------------------

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help = "Affiche la liste des commandes disponibles")
    async def aled(self, ctx):
        cmd_list = []
        
        for command in self.bot.commands:
            name = command.name
            desc = command.help
            cmd_list.append(f"**.{name}** → {desc}")

        rep = "".join(f"{cmd}\n" for cmd in cmd_list)

        await ctx.send(f"blud a besoin d'aide pour voir les commandes disponibles :mock:\n\n{rep}")





# ----------------------------------------------------------------------
# AJOUTE LES COMMANDES POUR UTILISATION
# ----------------------------------------------------------------------

async def setup(bot):
    await bot.add_cog(Server(bot))
    await bot.add_cog(Help(bot))
