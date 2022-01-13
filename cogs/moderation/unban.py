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


class unban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):

        #Check if user has manage messages perm
        return ctx.author.guild_permissions.ban_members
    
    @commands.command()
    async def pardon(ctx, *, member):
      banned_users = await ctx.guild.bans()
      member_name, member_discriminator = member.split('#')

      for ban_entry in banned_users:
          user = ban_entry.banned_users

          if (user.name, user.discriminator) == (member_name, member_discriminator):
              await ctx.guild.unban(user)
  


def setup(bot):
    bot.add_cog(unban(bot))