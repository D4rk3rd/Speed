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

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def avatar(self, ctx, member: discord.Member):
      await ctx.send("<" + "> " + str(member.avatar_url))

    @commands.command()
    async def weather(self, ctx, message=None):
	    embed = discord.Embed(color=0x00ffee,
	                          timestamp=ctx.message.created_at,
	                          title=f"weather in {message}")
	    embed.set_image(
	        url=
	        f"https://api.cool-img-api.ml/weather-card?location={message}"
	    )
	    await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(info(bot))