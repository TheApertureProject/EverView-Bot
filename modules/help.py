import discord
from discord.ext import commands
import datetime
import json

with open('./config.json', 'r') as cjson:
    config = json.load(cjson)

VERSION = config["version"]
PREFIX = config["prefix"]

bot = commands.Bot(command_prefix=PREFIX)

class Help(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config
    
    def is_owner(self, ctx):
        if ctx.author.id == 458586186328571913:
            return True
        else :
            return False

    @commands.command()
    async def info(self, ctx):
        a = """Entièrement programmé par Poulpy#9355
[Page Discord Bot List de la version publique](https://discordbots.org/bot/467332623677521940)
Hébergé gratuitement sur [Heroku](https://www.heroku.com/)
En fonctionnement sous  [discord.py v1.0.0a](https://discordpy.readthedocs.io/en/latest/api.html)
[Lien d'invite de la version publique](https://discordapp.com/oauth2/authorize?client_id=467332623677521940&scope=bot&permissions=2146958591)
[Serveur de support de la version publique](https://discord.gg/PTT9UpZ)
[🆕 Sho! Music Network](https://www.youtube.com/channel/UCYuh-fE3VqvmdSmZYtioH4Q)"""
        e = discord.Embed(description="Everview Bot", title='En savoir plus', color=0xF4A2FF)
        e.set_thumbnail(url="https://cdn.discordapp.com/attachments/568845812767916042/568845905650909208/JPEG_20190407_001724.png")
        e.add_field(name='Information', value=a)
        e.set_footer(text=VERSION)
        e.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=e)


    @commands.group(invoke_without_command=True, aliases=['hlp', 'commandlist', 'commands'])
    async def help(self, ctx):
        e = discord.Embed(description="Catégories de documentation", title='➡️Aide Interactive', color=0x33CC33)
        e.add_field(name='`info`', value='Commandes d\'informations relatives au bot.')
        e.add_field(name='`utilities`', value='Commandes utilitaires.')
        e.add_field(name='`moderator`', value='Commandes de modération.')
        e.add_field(name='`fun`', value='Commandes de jeu & divertissement.')
        e.set_footer(text=f'Entrez {PREFIX}help <categorie> pour afficher une liste de commandes spécifiques.')
        await ctx.send(embed=e)

    @help.command(name="info")
    async def help_info(self, ctx):
        e = discord.Embed(description="Commandes de base", title='➡️Liste de commandes', color=0x00FFC0)
        e.add_field(name=f'<{prefiximg}>`info`', value='Plus d\'infos sur le bot.')
        e.add_field(name=f'<{prefiximg}>`ping`', value='Retourne "Pong!".')
        e.add_field(name=f'<{prefiximg}>`help`', value='Retourne le message d\'aide général.')
        await ctx.send(embed=e)

    @help.command(name='all')
    async def help_all(self, ctx):
        c = discord.Embed(description='Toutes les commandes', title='➡️Liste de commandes', color=0x003366)
        c.set_thumbnail(url="https://cdn.discordapp.com/emojis/471044511804686348.gif?v=1")
        c.add_field(name="`help`, `info`, `ping`, `kick <membre/id>`,`ban <membre/id> <raison>`, `clear <quantité de messages>`, `pp <utilisateur>`, `roll <entier>`", value='Liste complète de toutes les commandes')
        c.add_field(name="`info`, `utilities`, `moderator`, `fun`", value='Catégories d\'aide')
        await ctx.send(embed=c)

    @help.command(name='utilities')
    async def help_utilities(self, ctx):
        c = discord.Embed(description='Utilities', title='➡️Liste de commandes', color=0x003366)
        c.add_field(name=f'<{prefiximg}>`translate <text>`', value='Traduction d\'une colonne de texte de n\'importe quel langue vers l\'anglais.')
        c.add_field(name=f'<{prefiximg}>`pp <user>`', value='Obtention de la photo de profil de l\'utilisateur spécifié.')
        c.add_field(name=f'<{prefiximg}>`qr <url>`', value='Obtention d\'un code QR correspondant à l\'adresse URL entrée.')
        c.add_field(name=f'<{prefiximg}>`emote <emoji>`', value='Obtention du lien de téléchargement d\'un emoji.')
        c.add_field(name=f'<{prefiximg}>`wiki <request>`', value='Recherche WikiPédia.')
        await ctx.send(embed=c)

    @help.command(name="moderator")
    async def help_moderator(self, ctx):
        a = discord.Embed(description="Commandes de modération", title='➡️Liste de commandes', color=0xffff00) 
        a.add_field(name=f'<{prefiximg}>`kick <membre/id>`', value='Exclusion du membre spécifié du serveur.')
        a.add_field(name=f'<{prefiximg}>`ban <membre/id> <raison>`', value='Exclusion permanente (ban) du membre spécifié du serveur.')
        a.add_field(name=f'<{prefiximg}>`clear <amount of messages>`', value='Suppression d\'un nombre spécifié de messages dans le serveur. Attention, aucune limitation du nombre de messages à supprimer.')
        await ctx.send(embed=a)

    @help.command(name="fun")
    async def help_fun(self, ctx):
        d = discord.Embed(description='Divertissement', title='➡️Liste de commandes', color=0xFFA2DD)
        d.add_field(name='`roll <entier>`', value="Simulation d'un lancé de dé au nombre de faces spécifié.")
        await ctx.send(embed=d)

    @commands.check(is_owner)
    @help.command(name="master")
    async def help_master(self, ctx):
        b = discord.Embed(description='Commandes de maintenance', title='➡️Liste de commandes', color=0xFF0000)
        b.set_thumbnail(url="https://cdn.discordapp.com/attachments/476653267036930049/498859365046943745/1538964466545.png")
        b.add_field(name=f'<{prefiximg}>`say <salon> <texte>`', value='Envoi d\'un texte au travers du bot, dans le salon spécifié.')
        b.add_field(name=f'<{prefiximg}>`shutdown`', value='Arrêt complet du bot. Un relancement complet du programme sera nécessaire.')
        await ctx.send(embed=b)
    
    @commands.command(aliases=['utilities', 'moderator', 'all', 'master'])
    async def fun(self, ctx):
        await ctx.send("Entrée inconnue. Si vous essayez d'accéder à une catégorie d'aide spécifique, n'oubliez pas le `help` dans la commande (`k!help <catégorie>`).")

def setup(bot):
    bot.add_cog(Help(bot))
