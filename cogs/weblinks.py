# NCXBot "weblinks.py"
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

async def setup(bot):
    await bot.add_cog(Weblinks(bot))