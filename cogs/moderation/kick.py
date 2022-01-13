import asyncio
from discord.ext.commands import *
import functools
import itertools
import json
import math
import random
import time
#from discord_buttons_plugin import *
import os
from keep_alive import keep_alive
import discord
import youtube_dl
from async_timeout import timeout
from discord.ext import commands
import aiohttp
import requests
import wikipedia


class kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):

        #Check if user has manage messages perm
        return ctx.author.guild_permissions.kick_members

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
      await member.kick(reason=reason)
      await ctx.send(f'kicked {member.mention}')

    @commands.command()
    async def membertest(self, ctx):
      await ctx.send(f'{ctx.author.name}#{ctx.author.discriminator}')

  


def setup(bot):
    bot.add_cog(kick(bot))
