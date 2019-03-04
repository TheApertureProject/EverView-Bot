import discord
from discord.ext import commands
import asyncio
import discord
import json
from datetime import datetime
from discord.ext.commands import Cog

with open('./config.json', 'r') as cjson:
    config = json.load(cjson)

PREFIX = config["prefix"]
SERVERID = config["mainserv_id"]
WELCHAN = config["welcome_channel"]

class Listeners(Cog):
	
    def __init__(self, bot):
        self.bot = bot
    
    @Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == SERVERID:
            e=discord.Embed(description='Bienvenue sur EverView !', color=0xdb90f4)
            e.set_thumbnail(url='https://cdn.discordapp.com/attachments/476653267036930049/528247247574401025/WindowKamuis.gif')
            e.set_image(url='https://cdn.discordapp.com/attachments/476653267036930049/528247286598467614/train-girl.jpg')
            await member.send(embed=e)
                            
    @Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f'⚠ Veuillez vérifier votre entrée et réessayer.')
        elif isinstance(error, commands.CommandNotFound):
            await ctx.message.add_reaction('❓')
            await asyncio.sleep(15)
            await ctx.message.remove_reaction(emoji='❓', member=ctx.guild.me)
        elif isinstance(error, commands.CheckFailure):
            await ctx.send('⚠ Vous ne disposez pas de permissions suffisantes à l\'utilisation de cette commande.')
        elif isinstance(error, commands.NotOwner):
            await ctx.send('⚠ Vous n\'êtes pas propriétaire du bot.')
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('⚠ Un argument requis est manquant.')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(' ⚠ Vous ne disposez pas de permissions suffisantes à l\'utilisation de cette commande.')
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send('⚠ Je ne dispose pas des permissions requises à l\'éxécution de cette commande.')
        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.send('⚠ Cette commande n\'est pas utilisable en conversation privée.')
        elif isinstance(error, commands.DisabledCommand):
            await ctx.send('⚠ Cette commande est actuellement désactivée pour cause de maintenance.')
        else:
            embedbasic = discord.Embed(color=discord.Color.red(), description='⚠ Une erreur est survenue lors de l\'éxecution de cette commande. Un rapport d\'erreur a été envoyé au serveur de maintenance EverView.')
            errorembed = discord.Embed(color=discord.Color.red(), title=f'Error caused by {ctx.author} ({ctx.author.id})', description=f'```py\n{error}\n```')
            errorembed.add_field(name='Serveur', value=f'**{ctx.guild.name}** ({ctx.guild.id})', inline=True)
            errorembed.add_field(name='Commande', value=f'**{ctx.command.name}**')
            channel = ctx.bot.get_channel(462876207097053195)
            await ctx.send(embed=embedbasic)
            await channel.send(embed=errorembed)

def setup(bot):
    bot.add_cog(Listeners(bot))
