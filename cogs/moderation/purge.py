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


class purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):

        #Check if user has manage messages perm
        return ctx.author.guild_permissions.manage_messages

    @commands.command(name='purge', aliases=['del','delete'])
    async def purge(self, ctx, limit:int, member: discord.Member=None):
        await ctx.message.delete()
        msg = []
        try:
            limit = int(limit)
        except:
            return await ctx.send("Please pass in an integer as limit")
        if not member:
            await ctx.channel.purge(limit=limit)
            return await ctx.send(f'{limit} üzenet törölve lett {ctx.message.author.mention} által', delete_after=3)
        async for m in ctx.channel.history():
            if len(msg) == limit:
                break
            if m.author == member:
                msg.append(m)
        await ctx.channel.delete_messages(msg)
        await ctx.send(f"Purged {limit} messages of {member.mention}", delete_after=3)

    @purge.error 
    async def purge_error(ctx, error): 
      if isinstance(error, commands.MissingPermissions): 
        await ctx.send("Ezt nem teheted!")
  


def setup(bot):
    bot.add_cog(purge(bot))