import discord
from discord.ext import commands
import sys
import json

try:
    with open('./config.json', 'r') as cjson:
        config = json.load(cjson)

    MASTER = config("owner_id")
except:
    pass

class Master(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config

    def is_owner(self, ctx):
        if ctx.author.id == MASTER:
            return True
        else:
            return False
    
    @commands.check(is_owner)
    @commands.command(pass_context=True)
    async def say(self, ctx, channel: discord.TextChannel, *, text):
        await ctx.message.delete()
        await channel.send(text)

    @say.error
    async def say_handler(self, ctx, err):
        if isinstance(err, commands.CheckFailure):
            await ctx.send('Désolé. Seul mon propriétaire peut utiliser cette commande !')
        else:
            raise err

    @commands.check(is_owner)
    @commands.command()
    async def shutdown(self, ctx):
        await ctx.send('Arrêt en cours.')
        sys.exit()

def setup(bot):
    bot.add_cog(Master(bot))
