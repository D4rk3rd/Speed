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
import qrcode

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def qr(self,ctx,arg):
      img=qrcode.make(f'{arg}')
      img.save('qrcode.png')
      channel=ctx.channel
      file = discord.File("qrcode.png", filename="qrcode.png")
      await channel.send("QR Kód", file=file)

    @commands.command(name="pp",aliases=["penis","erikfasz"])
    async def pp(self, ctx):
      pp=['8D','8=D','8==D','8===D','8====D','8=====D','8======D','8=======D','8========D', '8=========D','8==========D','8===========D','8============D']
      embed = discord.Embed(title='PP',description="{}".format(random.choice(pp)), color=0x00ffee)
      await ctx.send(embed=embed)

    @commands.command(name="8ball",aliases=["eightball","nyolclabda"])
    async def eightball(self, ctx):
      eightball = [
        ":8ball: | Bizonyos.",
        ":8ball: | Ez határozottan így van.",
        ":8ball: | Kétségtelen.",
        ":8ball: | Igen határozottan",
        ":8ball: | Bízhatsz benne.",
        ":8ball: | Ahogy látom, igen.",
        ":8ball: | A legvalószínűbb.",
        ":8ball: | Igen.",
        ":8ball: | Jelek szerint igen.",
        ":8ball: | Válasz homályos, próbálkozzon újra.",
        ":8ball: | Kérjen újra később.",
        ":8ball: | Jobb, ha most nem mondom el.",
        ":8ball: | Most nem lehet megjósolni.",
        ":8ball: | Koncentráljon és kérdezzen újra.",
        ":8ball: | Ne számítson rá.",
        ":8ball: | A válaszom nem.",
        ":8ball: | Forrásaim nemet mondanak.",
        ":8ball: | Nagyon kétséges.",]
      await ctx.send("{}".format(random.choice(eightball)))

      @commands.command()
      async def wiki(self, ctx, *, arg=None):
        try:
            if arg == None:
                await ctx.send("Please, specify what do you want me to search")
            elif arg:
                start = arg.replace(" ", "")
                end = wikipedia.summary(start)
                await ctx.send(end)
        except:
            try:
                start = arg.replace(" ", "")
                end = wikipedia.summary(start, sentences=15)
                await ctx.send(end)
            except:
                await ctx.send("I can't send info because I got an unknown reference")

        @commands.command(name="reverse",aliases=["rev"])
        async def reverse(self, ctx, *, arg): 
          await ctx.message.delete() 
          await ctx.send(arg[::-1])   


def setup(bot):
    bot.add_cog(fun(bot))        