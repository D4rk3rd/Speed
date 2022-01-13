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
import hypixel

HYKEY = "AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA"
BASE = 10_000
GROWTH = 2_500
REVERSE_PQ_PREFIX = -(BASE - 0.5 * GROWTH) / GROWTH
REVERSE_CONST = REVERSE_PQ_PREFIX
GROWTH_DIVIDES_2 = 2 / GROWTH


class hystats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hytest(self,ctx,arg):
      async with aiohttp.ClientSession() as cs:
        async with cs.get(f'https://api.mojang.com/users/profiles/minecraft/{arg}') as r:
          r=await r.json()
          uuid=r["id"]
          x=discord.Embed(color=0x00ffee, timestamp=ctx.message.created_at, title=r["id"])
          #x.set_image(url=r['image'])
          await ctx.send(embed=x)
          async with cs.get(f'https://api.hypixel.net/player?key=dd0fd7fe-d3e5-4e0b-8c0c-f1fc8f844b36&uuid={uuid}') as y:
            y=await y.json()
            x.add_field(name=y["success"], value=uuid, inline=False)
            x.add_field(name=y["player"]["displayname"], value="test", inline=False)
            x.set_image(url=y['image'])
            await ctx.send(embed=x)

    

  

def setup(bot):
    bot.add_cog(hystats(bot))