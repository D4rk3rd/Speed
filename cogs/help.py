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

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx,* ,command=None):
      if command is None:
        embed=discord.Embed(title="Segítség", color=0x00ffee)
        embed.set_author(name="Speed", icon_url=f"https://cdn.discordapp.com/avatars/860098847311921162/660589feb3baa461708cff28e7f3ddfc.webp?size=1024")
        embed.add_field(name="Szórakozás", value="?help fun", inline=True)
        embed.add_field(name="Moderáció", value="?help moderation", inline=True)
        embed.add_field(name="Zene", value="?help music", inline=True)
        embed.add_field(name="Infó", value="?help info", inline=True)
        embed.add_field(name="Rang", value="?help rank", inline=True)
        embed.add_field(name="Support", value="?help support", inline=True)
        await ctx.send(embed=embed)
        return
      elif command == "fun":
        embed=discord.Embed(title="Segítség: Szórakozás", description="8ball, meme, hitler, pp, gay, achievement, dog, birb, reverse", color=0x00ffee)
        embed.set_author(name="Speed", icon_url=f"https://cdn.discordapp.com/avatars/860098847311921162/660589feb3baa461708cff28e7f3ddfc.webp?size=1024")
        embed.add_field(name="8ball", value="?8ball/nyolclabda/eightball (szöveg)", inline=True)
        embed.add_field(name="meme", value="?meme (ping)", inline=False)
        embed.add_field(name="hitler", value="?hitler (ping)", inline=False)
        embed.add_field(name="pp", value="?pp (ping)", inline=False)
        embed.add_field(name="gay", value="?gay (ping)", inline=False)
        embed.add_field(name="achievement", value="?achievement [szöveg]", inline=False)
        embed.add_field(name="dog", value="?dog", inline=False)
        embed.add_field(name="birb", value="?birb", inline=False)
        embed.add_field(name="reverse", value="?rev/reverse [szöveg]", inline=False)
        embed.set_footer(text="Használati Szintaxis: [kötelező] (opcionális)")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(help(bot))