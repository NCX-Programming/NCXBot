# moderation.py
import os
import random
from dotenv import load_dotenv
import discord
from discord.ext import commands
import io
import re
import math
import time
from discord.utils import get
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions

class Moderation(commands.Cog):
    """
    Nobody will ever see this little message... shh...
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def mute(self, message, member : discord.Member, reason=None):
        if message.guild == 714479281312366592:
            if message.author == member:
                await message.channel.send(":x: You can't mute yourself!")
            role = discord.utils.get(member.guild.roles, name="Muted")
            owner = discord.utils.get(member.guild.roles, name="Top Fish")
            if member.top_role == owner:
                await message.channel.send("seriously? SERIOUSLY?! **SERIOUSLY?!?!** I'm sorry if you disagree with this server's owner and are too petty to just talk to him about it, but did you really think some salty backstab was going to improve things? *have fun not being mod anymore!* <@455681686823239681>")
            if message.author != member:
                if member.top_role >= message.author.top_role:
                    await message.channel.send("Did you just try to mute another staff member? The moderation bot is not the key to ending your petty arguments.")
                if member.top_role < message.author.top_role:
                    await member.add_roles(role, reason=reason)
                    await message.channel.send(f":mute: {member} has been muted.")

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, message, member : discord.Member, reason=None):
        if message.guild == 714479281312366592:
            role = discord.utils.get(member.guild.roles, name="Muted")
            await member.remove_roles(role, reason=reason)
            await message.channel.send(f":loud_sound: {member} has been unmuted.")

    @commands.command(pass_context=True, aliases=['nolinks', 'no-links', 'no-link'])
    @commands.has_permissions(manage_roles=True)
    async def nolink(self, message, member : discord.Member, reason=None):
        if message.guild == 714479281312366592:
            if message.author == member:
                await message.channel.send(":x: You can't disable links for yourself!")
            role = discord.utils.get(member.guild.roles, name="no-links")
            if message.author != member:
                if member.top_role >= message.author.top_role:
                    await message.channel.send("Did you just try to disabled links for another staff member? If there's really an issue you need to ask an admin or NinjaCheetah.")
                if member.top_role < message.author.top_role:
                    await member.add_roles(role, reason=reason)
                    await message.channel.send(f":link: {member} can no longer embed links.")

    @commands.command(pass_context=True, aliases=['links'])
    @commands.has_permissions(manage_roles=True)
    async def link(self, message, member : discord.Member, reason=None):
        if message.guild == 714479281312366592:
            role = discord.utils.get(member.guild.roles, name="no-links")
            await member.remove_roles(role, reason=reason)
            await message.channel.send(f":link: {member} can now embed links.")

    @commands.command(pass_context=True, aliases=['noimages', 'no-images', 'no-image'])
    @commands.has_permissions(manage_roles=True)
    async def noimage(self, message, member : discord.Member, reason=None):
        if message.guild == 714479281312366592:
            if message.author == member:
                await message.channel.send(":x: You can't disable images for yourself!")
            role = discord.utils.get(member.guild.roles, name="no-photos")
            if message.author != member:
                if member.top_role >= message.author.top_role:
                    await message.channel.send("Did you just try to disabled images for another staff member? If there's really an issue you need to ask an admin or NinjaCheetah.")
                if member.top_role < message.author.top_role:
                    await member.add_roles(role, reason=reason)
                    await message.channel.send(f":frame_photo: {member} can no longer send images.")

    @commands.command(pass_context=True, aliases=['images'])
    @commands.has_permissions(manage_roles=True)
    async def image(self, message, member : discord.Member, reason=None):
        if message.guild == 714479281312366592:
            role = discord.utils.get(member.guild.roles, name="no-photos")
            await member.remove_roles(role, reason=reason)
            await message.channel.send(f":frame_photo: {member} can now send images.")

    @commands.command(pass_context=True, aliases=['noreacts', 'no-react', 'no-reacts'])
    @commands.has_permissions(manage_roles=True)
    async def noreact(self, message, member : discord.Member, reason=None):
        if message.guild == 714479281312366592:
            if message.author == member:
                await message.channel.send(":x: You can't disable images for yourself!")
            role = discord.utils.get(member.guild.roles, name="no-react")
            if message.author != member:
                if member.top_role >= message.author.top_role:
                    await message.channel.send("Did you just try to stop a staff member from reacting to messages? If there's really an issue you need to ask an admin or NinjaCheetah.")
                if member.top_role < message.author.top_role:
                    await member.add_roles(role, reason=reason)
                    await message.channel.send(f":slight_frown: {member} can no longer react to messages.")

    @commands.command(pass_context=True, aliases=['reacts'])
    @commands.has_permissions(manage_roles=True)
    async def react(self, message, member : discord.Member, reason=None):
        if message.guild == 714479281312366592:
            role = discord.utils.get(member.guild.roles, name="no-react")
            await member.remove_roles(role, reason=reason)
            await message.channel.send(f":slight_smile: {member} can now react to messages.")

def setup(bot):
    bot.add_cog(Moderation(bot))
