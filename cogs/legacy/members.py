import discord
from discord.ext import commands

class Members(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('this worked')


def setup(bot):
    bot.add_cog(Members(bot))