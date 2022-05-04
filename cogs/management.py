# NCXBot "management.py"
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
from discord.utils import get

class Management(commands.Cog):
    """
    Basic bot management, stuff like the status.
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='status', invoke_without_command=True)
    @commands.is_owner()
    async def status(self, ctx):
        await ctx.send(":x: Use `x!status set <message>` to set status message, or if you are indecisive then use `x!status random`.")

    @status.command(aliases=['Set', 'set'])
    @commands.is_owner()
    async def presence_set(self, ctx, *, message):
        activity = discord.Game(name=message, type=3)
        await self.bot.change_presence(activity=activity)
        await ctx.send(":white_check_mark: Set status message to: `" + message + "`")

    @status.command(aliases=['Classic', 'classic', '-c'])
    @commands.is_owner()
    async def status_random_classic(self, ctx):
        status_list = [
            'Programming | x!help',
            'Hi! | x!help',
            ':thonk: | x!help',
            'Talking to EvilCookie | x!help',
            'I know what you did! | x!help',
            'Bruh | x!help',
            ':( | x!help',
            'ERROR: No witty status | x!help',
            'NinjaCheetah is the best | x!help',
        ]
        response = random.choice(status_list)
        activity = discord.Game(name=response, type=3)
        await self.bot.change_presence(activity=activity)
        await ctx.send(":white_check_mark: Set status to: `" + response + "`")

    @status.command(aliases=['Random', 'random', '-r'])
    @commands.is_owner()
    async def status_random(self, ctx):
        with open("words.txt", "r") as f:
            status_word_list = f.readlines()
        num_words = random.randrange(3,6)
        status_string = ""
        for i in range(num_words):
            status_string += str(random.choice(status_word_list)).strip()+" "
        status_string = status_string[:len(status_string)-1]
        activity = discord.Game(name=status_string, type=3)
        await self.bot.change_presence(activity=activity)
        await ctx.send(":white_check_mark: Set status to: `" + status_string + "`")

    @commands.command(pass_context=True)
    async def servers(self, ctx):
        await ctx.send("I'm in `" + str(len(self.bot.guilds)) + "` server(s).")

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send(":electric_plug: Shutting down...")
        await ctx.bot.logout()

async def setup(bot):
    await bot.add_cog(Management(bot))
