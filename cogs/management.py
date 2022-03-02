# management.py
import random
import discord
from discord.ext import commands
from discord.utils import get

class Management(commands.Cog):
    """
    Nobody will ever see this little message... shh...
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
        activity = discord.Game(name=status_string, type=3)
        await self.bot.change_presence(activity=activity)
        await ctx.send(":white_check_mark: Set status to: `" + status_string + "`")

    @commands.command(name="about")
    async def about(self, ctx):
        embed=discord.Embed(title="NCX Offical Bot", color=0x000000)
        embed.set_author(name="About")
        embed.add_field(name=":computer: Host:", value="Raspberry Pi 3B", inline=True)
        embed.add_field(name="Creator:", value="NinjaCheetah", inline=True)
        embed.add_field(name=":snake: Python version:", value="3.9.10", inline=True)
        embed.add_field(name="Bot version:", value="v0.2", inline=True)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def servers(self, ctx):
        await ctx.send("I'm in `" + str(len(self.bot.guilds)) + "` server(s).")

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send(":electric_plug: Shutting down...")
        await ctx.bot.logout()

def setup(bot):
    bot.add_cog(Management(bot))
