from discord.ext import commands

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

        await ctx.send(f"blud ne connaît pas les commandes <a:mock:1360922838244135083>\n\n{rep}")



# ----------------------------------------------------------------------
# AJOUTE LES COMMANDES POUR UTILISATION
# ----------------------------------------------------------------------

async def setup(bot):
    await bot.add_cog(Help(bot))
