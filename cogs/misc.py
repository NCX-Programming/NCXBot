# NCXBot "misc.py"
# Copyright (C) 2022  NinjaCheetah

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
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
