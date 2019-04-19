import discord
from discord.ext import commands
import json

with open('./config.json', 'r') as cjson:
    config = json.load(cjson)

PREFIX = config["prefix"]
MODS = config["l-mods"]
ARCH = config["l-arch"]
ERRS = config["l-errs"]
MSGS = config["l-msgs"]

bot = commands.Bot(command_prefix=PREFIX)

class Logs(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config
    
    @Cog.listener()
    async def on_message_delete(self, message):
        e = discord.embed

def setup(bot):
bot.add_cog(General(bot))
