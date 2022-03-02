# weblinks.py
from discord.ext import commands
from discord.utils import get

class Weblinks(commands.Cog):
    """
    Commands to quickly post links to sites, specifically meme sites.
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='tias', help='try it and see.')
    async def tias(self, ctx):
        await ctx.send('https://tryitands.ee')

    @commands.command(name='shut', help='shut')
    async def shut(self, ctx):
        await ctx.send('https://shutplea.se/')

    @commands.command(name='roll', help='alt dice command (experimental)')
    async def roll2(self, ctx):
        await ctx.send('(Rick) Rolling!')
        await ctx.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

def setup(bot):
    bot.add_cog(Weblinks(bot))