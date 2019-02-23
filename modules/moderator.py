import discord
from discord.ext import commands

class Moderator:
    
    conf = {}
	
    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config

    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, member: discord.Member, reason: str = None):
        if reason==None:
            await member.ban()
            await ctx.send(f'Le membre {member} a été banni avec succès !')
        else:
            await member.ban(reason=reason)
            await ctx.send(f'Le membre {member} a lamentablement été banni pour la raison suivante : {reason} !')

    @commands.guild_only()    
    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx, *, member: discord.Member):
        await member.kick()
        await ctx.send(f'Le membre {member} a été expulsé avec succès !')

    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def clear(self, ctx, amount: int):
        await ctx.message.delete()
        deleted = await ctx.channel.purge(limit=amount)
        await ctx.send(f"`{len(deleted)}` Messages supprimés avec succès.", delete_after = 5)

def setup(bot):
    bot.add_cog(Moderator(bot))
