# software.py
import discord
from discord.ext import commands
from discord.utils import get

class Software(commands.Cog):
    """
    HALP!
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='core', help='Shows this message', invoke_without_command=True)
    async def core(self, ctx, *message):
        embed=discord.Embed(title="NCX-Core", color=0x000000)
        embed.set_author(name="Software")
        embed.set_thumbnail(url="https://cdn.ncxprogramming.com/file/icon/ncxcore.png")
        embed.add_field(name="Info", value="NCX-Core is the main project I work on. It can be used to install and run my other programs.", inline=False)
        embed.add_field(name="Latest Version", value="Version numbers from the bot are coming soon!", inline=False)
        embed.add_field(name="Latest Release", value="https://github.com/NinjaCheetah/NCX-Installer/releases/latest", inline=False)
        embed.set_footer(text="Copyright NinjaCheetah 2021")
        await ctx.send(embed=embed)

    @commands.group(name='software', help='Shows this message', invoke_without_command=True)
    async def software(self, ctx, *message):
        embed=discord.Embed(title="Software Commands", color=0x000000)
        embed.set_author(name="Software")
        embed.add_field(name="cscollection", value="Command to get information about CSharpCollection", inline=False)
        embed.add_field(name="core", value="Command to get information about NCX-Core", inline=False)
        embed.add_field(name="xware", value="Command to get information about XWare", inline=False)
        embed.set_footer(text="Copyright NinjaCheetah 2021")
        await ctx.send(embed=embed)

    @software.command(aliases=['cscollection', 'CSCollection'])
    async def software_cscol(self, ctx):
        embed=discord.Embed(title="CSharpCollection", color=0x000000)
        embed.set_author(name="Software")
        embed.set_thumbnail(url="https://cdn.ncxprogramming.com/file/icon/csharpcollection.png")
        embed.add_field(name="Info", value="CSharpCollection is a collection of small programs I've written in CSharp to experiment with it.", inline=False)
        embed.add_field(name="Latest Version", value="Version numbers from the bot are coming soon!", inline=False)
        embed.add_field(name="Latest Release", value="https://github.com/NinjaCheetah/CSharp-Collection/releases/latest", inline=False)
        embed.set_footer(text="Copyright NinjaCheetah 2021")
        await ctx.send(embed=embed)

    @software.command(aliases=['core', 'Core'])
    async def software_core(self, ctx):
        embed=discord.Embed(title="NCX-Core", color=0x000000)
        embed.set_author(name="Software")
        embed.set_thumbnail(url="https://cdn.ncxprogramming.com/file/icon/ncxcore.png")
        embed.add_field(name="Info", value="NCX-Core is the main project I work on. It can be used to install and run my other programs.", inline=False)
        embed.add_field(name="Latest Version", value="Version numbers from the bot are coming soon!", inline=False)
        embed.add_field(name="Latest Release", value="https://github.com/NinjaCheetah/NCX-Installer/releases/latest", inline=False)
        embed.set_footer(text="Copyright NinjaCheetah 2021")
        await ctx.send(embed=embed)

    @software.command(aliases=['xware', 'XWare'])
    async def software_xware(self, ctx):
        embed=discord.Embed(title="XWare", color=0x000000)
        embed.set_author(name="Software")
        embed.set_thumbnail(url="https://cdn.ncxprogramming.com/file/icon/xware.png")
        embed.add_field(name="Info", value="XWare is a set of add-on programs for NCX-Core. They are usually very small.", inline=False)
        embed.add_field(name="Latest Version", value="Version numbers from the bot are coming soon!", inline=False)
        embed.add_field(name="Latest Release", value="https://github.com/NinjaCheetah/NCX-XWare/releases/latest", inline=False)
        embed.set_footer(text="Copyright NinjaCheetah 2021")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Software(bot))
