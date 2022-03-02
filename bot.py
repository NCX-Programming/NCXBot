# bot.py
import discord
from discord.ext import commands
import json
from discord.utils import get

with open('config.json', 'r') as f:
    config = json.load(f)

TOKEN = config["TOKEN"]
# GUILD = config["GUILD"]

class Bot(commands.Bot):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    async def process_commands(self, message: discord.Message):
        ctx = await self.get_context(message)
        await self.invoke(ctx)

bot = Bot(command_prefix='x!', activity=discord.Game(name="Programming | x!help", type=3))
bot.remove_command('help')

startup_extensions = ["cogs.fortunes", "cogs.help", "cogs.management", "cogs.misc", "cogs.software", "cogs.weblinks"]

bot.load_extension('jishaku')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(":x: You are missing a required argument!")
    if isinstance(error, commands.CommandNotFound):
        print("Command not found.")
    if isinstance(error, commands.ExtensionError):
        await ctx.send(":x: That extension could not be found!")
    if isinstance(error, commands.ExtensionNotLoaded):
        await ctx.send(":x: There was an error while loading that extension.")
    if isinstance(error, commands.ExtensionFailed):
        await ctx.send(":x: There was an error while loading that extension.")
    if isinstance(error, commands.ExtensionNotFound):
        await ctx.send(":x: That extension could not be found!")

@bot.command(name='load', help='Loads an extension.')
@commands.is_owner()
async def load(ctx, extension):
    try:
        bot.load_extension(f'cogs.{extension}')
        await ctx.send(":white_check_mark: Loaded `cogs."+extension+"`")
    except Exception as e:
        exc = '{}: {}'.format(type(e).__name__, e)
        await ctx.send(":warning: Failed to load extension `{}`\n```\n{}\n```".format(extension, exc))

@bot.command(name='unload', help='Unloads an extension.')
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(":white_check_mark: Unloaded `cogs."+extension+"`")

@bot.command(name='reload', help='Reloads an extension.')
@commands.is_owner()
async def reload(ctx, extension):
    try:
        bot.reload_extension(f'cogs.{extension}')
        await ctx.send(":repeat: Reloaded `cogs."+extension+"`")
    except Exception as e:
        exc = '{}: {}'.format(type(e).__name__, e)
        await ctx.send(":warning: Failed to reload extension `{}`\n```\n{}\n```".format(extension, exc))

@bot.command(name='reloadall', help='Reloads all extensions.')
@commands.is_owner()
async def reloadall(ctx):
    for extension in startup_extensions:
        try:
            bot.reload_extension(extension)
            await ctx.send(":repeat: Reloaded `"+extension+"`")
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            await ctx.send(":warning: Failed to reload extension `{}`\n```\n{}\n```".format(extension, exc))

@bot.event
async def on_ready():
    print("Bot is ready!")

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
    bot.run(TOKEN)