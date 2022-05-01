# help.py
import discord
from discord.ext import commands
from discord.utils import get

class Help(commands.Cog):
    """
    HALP!
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='help', help='Shows this message', invoke_without_command=True)
    async def help(self, ctx, *message):
        embed=discord.Embed(title="Categories", color=0x000000)
        embed.set_author(name="Help")
        embed.add_field(name="Software", value="Commands related to NCX software", inline=False)
        embed.add_field(name="Weblinks", value="Commands for easily sending links", inline=False)
        embed.add_field(name="Fortunes", value="Commands to get your fortune told.", inline=False)
        embed.add_field(name="Misc", value="Commands that didn't fit into another category", inline=False)
        embed.set_footer(text="Use .help [category] to view the commands in that category")
        await ctx.send(embed=embed)

    @commands.group(name="one", invoke_without_command=True)
    async def one_group(self, ctx):
        await ctx.send("No subcommand was found!")

    @help.command(aliases=['Weblinks', 'weblinks'])
    async def help_weblinks(self, ctx):
        embed=discord.Embed(title="Weblink Commands", description="Commands to easily send links to websites.", color=0x000000)
        embed.set_author(name="Help")
        embed.add_field(name="tias", value="Try It and See :tm:", inline=False)
        embed.add_field(name="shut", value="*shut*", inline=False)
        embed.add_field(name="roll", value="it's just a rickroll", inline=False)
        embed.set_footer(text="Copyright NinjaCheetah 2021")
        await ctx.send(embed=embed)

    @help.command(aliases=['Misc', 'misc'])
    async def help_misc(self, ctx):
        embed=discord.Embed(title="Misc. Commands", description="Misc commands that didn't fit into any other category", color=0x000000)
        embed.set_author(name="Help")
        embed.add_field(name="dice", value="Roll some dice! Usage: `..dice [# of dice] [# of sides]`", inline=False)
        embed.add_field(name="say", value="Make the bot speak!", inline=False)
        embed.add_field(name="melt", value="Melt somebody! Usage: `..melt [user]`", inline=False)
        embed.add_field(name="ping", value="Gets the ping for the bot.", inline=False)
        embed.set_footer(text="Copyright NinjaCheetah 2021")
        await ctx.send(embed=embed)

    @help.command(aliases=['Software', 'software'])
    async def help_software(self, ctx):
        embed=discord.Embed(title="Software Commands", description="Commands for info about my software.", color=0x000000)
        embed.set_author(name="Help")
        embed.add_field(name="software", value="Shows all software related commands.", inline=False)
        embed.add_field(name="core", value="Gives the link to the latest NCX-Core release page.", inline=False)
        embed.set_footer(text="Copyright NinjaCheetah 2021")
        await ctx.send(embed=embed)

    @help.command(aliases=['Fortunes', 'fortunes'])
    async def help_fortunes(self, ctx):
        embed=discord.Embed(title="Fortune Commands", description="Commands to get your fortune told.", color=0x000000)
        embed.set_author(name="Help")
        embed.add_field(name="fortune a", value="The more normal fortunes.", inline=False)
        embed.add_field(name="fortune b", value="The weird, stupid, and occasionally creepy fortunes. (The good ones)", inline=False)
        embed.set_footer(text="Copyright NinjaCheetah 2021")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))
