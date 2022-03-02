# fortunes.py
import random
from discord.ext import commands
from discord.utils import get

class Fortunes(commands.Cog):
    """
    The fortune commands that are the core of this bot.
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='fortune', invoke_without_command=True)
    async def fortune(self, ctx):
        await ctx.send(":x: Use `fortune a` for normal fortunes or `fortune b` for the funny ones.")

    @fortune.command(aliases=['A', 'a'])
    async def fortuneA(self, ctx):
        fortuneA = [
            'A beautiful, smart, and loving person will be coming into your life.',
            'A dubious friend may be an enemy in camouflage.',
            'A faithful friend is a strong defense. ',
            'Believe in yourself and others will too.',
            'Believe it can be done. (My thoughts making this bot)',
            'Get your mind set – confidence will lead you on.',
            'You will stay socially distanced next time you go out.',
        ]
        response = random.choice(fortuneA)
        await ctx.send(response)

    @fortune.command(aliases=['B', 'b'])
    async def fortuneB(self, ctx):
        fortuneB = [
            'Ignore previous fortune',
            'eNJoY yOuRSelF whILE YoU CAn',
            'run',
            'To avoid criticism, do nothing, say nothing, be nothing.',
            'Any day above ground is a good day',
            'You are the crispy noodle in the vegetairan salad of life',
            'To truly find yourself you should play hide and seek alone',
            'Actions speak louder than talks',
            'You will read this and say "Geez! I could come up with better fortunes than that!"',
            'You laugh now, wait until you get home',
            'Catch on fire with enthusiasm and people will come for miles to watch you burn',
            'Enjoy your own company, if you dont who will?',
            'this fortune is never gonna give you up, never gonna let you down',
            'Work on improving your exercise routine',
            'Your cat is plotting to kill you',
            'you are going to get some new clothes.',
            'An alien of some sort will be appearing to you shortly!',
            'When in anger, sing the alphabet',
            'You will stay socially distanced next time you go out.',
        ]
        response = random.choice(fortuneB)
        await ctx.send(response)

def setup(bot):
    bot.add_cog(Fortunes(bot))
