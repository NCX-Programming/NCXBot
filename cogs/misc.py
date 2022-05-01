# misc.py
import random
import discord
from discord.ext import commands
import time
from discord.utils import get

class Misc(commands.Cog):
    """
    Misc. commands that don't fit into another category and aren't worth creating a category for.
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='dice', help='Simulates rolling dice.')
    async def roll(self, ctx, number_of_dice: int, number_of_sides: int):
        if number_of_dice > 500:
            await ctx.send(":x: You cannot roll more than 500 dice.")
        elif number_of_sides > 500:
            await ctx.send(":x: You cannot roll a die with more than 500 sides.")
        else:
            dice = [
                str(random.choice(range(1, number_of_sides + 1)))
                for _ in range(number_of_dice)
                ]
            await ctx.send(', '.join(dice))

    @commands.command(name='say', help='Make the bot speak.')
    async def say(self, ctx, *, message):
        await ctx.send(message)

    @commands.command(name='melt', help='Melts a user')
    async def melt(self, ctx, target: discord.Member):
        await ctx.send(f":fire: {target} has been melted!")

    @commands.command(name='ping', help='Gets the ping from the bot.')
    async def ping(self, ctx):
        before = time.monotonic()
        message = await ctx.send(":ping_pong: Pinging...")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f":ping_pong: Ping:  `{int(ping)}ms`")

async def setup(bot):
    await bot.add_cog(Misc(bot))
