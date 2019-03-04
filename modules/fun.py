import discord
from discord.ext import commands
from random import randint
import asyncio

class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config

    @commands.command()
    async def roll(self, ctx, value: int):
        result=randint(1,value)
        msg=await ctx.send(f'Et le résultat est...')
        await asyncio.sleep(2)
        await msg.edit(content=f'Et le réultat est **`{result}`** !')

def setup(bot):
    bot.add_cog(Fun(bot))
