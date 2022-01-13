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





def get_prefix(client, message): ##first we define get_prefix
    with open('./json/prefixes.json', 'r') as f: ##we open and read the prefixes.json, assuming it's in the same file
        prefixes = json.load(f) #load the json as prefixes
    return prefixes[str(message.guild.id)] #recieve the prefix for the guild id given
bot = commands.Bot(description='Speed', help_command=None,command_prefix=commands.when_mentioned_or(get_prefix))
#buttons = ButtonsClient(bot)

@bot.command(pass_context=True)
@has_permissions(administrator=True) #ensure that only administrators can use this command
async def changeprefix(ctx, prefix): #command: bl!changeprefix ...
    with open('./json/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('./json/prefixes.json', 'w') as f: #writes the new prefix into the .json
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefix changed to: {prefix}') #confirms the prefix it's been changed to
#next step completely optional: changes bot nickname to also have prefix in the nickname

@bot.event
async def on_guild_join(guild): #when the bot joins the guild
    with open('./json/prefixes.json', 'r') as f: #read the prefix.json file
        prefixes = json.load(f) #load the json file

    prefixes[str(guild.id)] = '?'#default prefix

    with open('./json/prefixes.json', 'w') as f: #write in the prefix.json "message.guild.id": "bl!"
        json.dump(prefixes, f, indent=4) #the indent is to make everything look a bit neater

@bot.event
async def on_guild_remove(guild): #when the bot is removed from the guild
    with open('./json/prefixes.json', 'r') as f: #read the file
        prefixes = json.load(f)

    prefixes.pop(str(guild.id)) #find the guild.id that bot was removed from

    with open('./json/prefixes.json', 'w') as f: #deletes the guild.id as well as its prefix
        json.dump(prefixes, f, indent=4)

@bot.command()
async def invite(ctx):
  await ctx.send("https://discord.com/oauth2/authorize?client_id=860098847311921162&scope=bot&permissions=8589934591")

@bot.command()
async def prefix(ctx):
  with open('./json/prefixes.json', 'r') as f: #read the prefix.json file
        prefixes = json.load(f) #load the json file

  prefixes[str(ctx.guild.id)] = prefix
  await ctx.send(f"{prefix}")


#@bot.command()
#async def tcreate(ctx):
  #embed=discord.Embed(title="Ticket", color=0x554e4e)
  #embed.add_field(name="Katt a reakcióra, hogy megnyiss egy ticketet!", value="ㅤ", inline=False)
  #await ctx.send(embed=embed)
  #await buttons.send(
	  #content = "ㅤ", 
	  #channel = ctx.channel.id,
	  #components = [
		  #ActionRow([
		  	#Button(
				  #label="Hello", 
				  #style=ButtonType().Primary, 
				  #custom_id="ticket1"       
			  #)
		  #])
	  #]
  #)
  
#@buttons.click
#async def ticket1(ctx):
	#guild = ctx.guild
	#channel = await guild.create_text_channel()
	#wait ctx.reply("Hello!", flags = MessageFlags().EPHEMERAL)




    





@bot.command(name="birb",aliases=["bird"])
async def birb(ctx):
	embed = discord.Embed(color=0x00ffee,
	                      timestamp=ctx.message.created_at,
	                      title="birb")
	embed.set_image(
	    url=
	    "https://api.cool-img-api.ml/birb"
	)
	await ctx.send(embed=embed)

@bot.command()
async def dog(ctx):
	embed = discord.Embed(color=0x00ffee,
	                      timestamp=ctx.message.created_at,
	                      title="dog")
	embed.set_image(
	    url=
	    "https://api.cool-img-api.ml/dogs"
	)
	await ctx.send(embed=embed)

@bot.command()
async def hitler(ctx):
	embed = discord.Embed(color=0x00ffee,
	                      timestamp=ctx.message.created_at,
	                      title="hitler")
	embed.set_image(
	    url=
	    f"https://api.cool-img-api.ml/hitler?image={ctx.author.avatar_url}"
	)
	await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def meme(ctx):
    embed = discord.Embed(title="meme", description="test")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

@bot.command()
async def achievement(ctx,message):
	embed = discord.Embed(color=0x00ffee,
	                      timestamp=ctx.message.created_at,
	                      title="achievement")
	embed.set_image(
	    url=
	    f"https://api.cool-img-api.ml/achievement?text={message}"
	)
	await ctx.send(embed=embed)  

@bot.command()
async def testapi(ctx):
  async with aiohttp.ClientSession() as cs:
    async with cs.get('https://no-api-key.com/api/v1/animals/cat') as r:
      r=await r.json()
      await ctx.send(f"**{r['fact']}**\n\n||{r['fact']}||")

@bot.command()
async def cat(ctx):
  async with aiohttp.ClientSession() as cs:
    async with cs.get('https://no-api-key.com/api/v1/animals/cat') as r:
      r=await r.json()
      x=discord.Embed(color=0x00ffee, timestamp=ctx.message.created_at, title=r["fact"])
      x.set_image(url=r['image'])
      await ctx.send(embed=x)

@bot.command()
async def texttobin(ctx, message):
  async with aiohttp.ClientSession() as cs:
    async with cs.get(f'https://no-api-key.com/api/v1/binary?text={message}') as r:
      r=await r.json()
      await ctx.send(f"**{r['binary']}**")
      

@bot.command()
async def gay(ctx, member: discord.Member=None):
  if member is None:
	  x = discord.Embed(color=0x00ffee,
	                        timestamp=ctx.message.created_at,
	                        title="gay")
	  x.set_image(
	      url=
	      f"https://api.cool-img-api.ml/gay?image={ctx.author.avatar_url}"
	  )
	  await ctx.send(embed=x)
  elif member != None:
    y = discord.Embed(color=0x00ffee,
    timestamp=ctx.message.created_at,
    title="gay")
    y.set_image(
      url=
      f"https://api.cool-img-api.ml/gay?image={member.avatar_url}"
    )
    await ctx.send(embed=y)

@bot.command()
async def suggest(ctx, *,message):
  embed=discord.Embed(title="Suggestion", description=f"{message}", color=0x00ffee)
  embed.set_author(name=ctx.author.name, icon_url=f"{ctx.author.avatar_url}")
  await ctx.message.delete()
  msg=await ctx.send(embed=embed)
  await msg.add_reaction("✅")
  await msg.add_reaction("❌")

@bot.command()
async def serverinfo(ctx):
  name = str(ctx.guild.name)
  description = str(ctx.guild.description)
  owner = str(ctx.guild.owner)
  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)
  icon = str(ctx.guild.icon_url)
  embed = discord.Embed(
    title=name + " Server Information",
    description=description, color=0x00ffee
  )
  embed.set_thumbnail(url=icon)
  embed.add_field(name="Owner", value=owner, inline=True)
  embed.add_field(name="Server ID", value=id, inline=True)
  embed.add_field(name="Region", value=region, inline=True)
  embed.add_field(name="Member Count", value=memberCount, inline=True)
  await ctx.send(embed=embed)

@bot.command()
async def userinfo(ctx, *, user: discord.User = None): # b'\xfc'
    embed=discord.Embed(title="Info", color=0x00ffee)
    embed.add_field(name="Ping:", value="undefined", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def test(ctx):
    await ctx.send()

@bot.command()
async def ping(ctx):
  calc = bot.latency * 1000
  pong = round(calc)
  await ctx.message.delete()

  x = discord.Embed(title='*Pong*', description=f'{pong} ms', color=0xff0000) #red

  y = discord.Embed(title='*Pong*', description=f'{pong} ms', color=0xffff00) #yellow

  z = discord.Embed(title='*Pong*', description=f'{pong} ms', color=0x008000) #green

  if pong > 160: 
    msg = await ctx.send(embed=x)
  elif 80 <= pong <= 160:
    msg = await ctx.send(embed=y)
  elif pong < 80:
    msg = await ctx.send(embed=z)

@bot.command()
async def userinfotest(ctx, *, user: discord.User = None): # b'\xfc'
    if user is None:
      user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(color=0x00ffee, description=user.mention)
    embed.set_author(name=str(user), icon_url=user.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    embed.add_field(name="Join position", value=str(members.index(user)+1))
    embed.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    embed.add_field(name="Guild permissions", value=perm_string, inline=False)
    embed.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=embed)


@bot.command()
async def botavatar(ctx):
  await ctx.send("<" + str(ctx.bot.user.avatar_url) + ">")

@bot.event
async def ch_pr():
 await bot.wait_until_ready()
 print('=====================')
 print('Logged in as')
 print(bot.user.name)
 print('=====================')
 print('Connected Servers:')
 for server in bot.guilds:
  print(server.name)
 print('=====================')
 statuses = ["Kell segítség? || ?help",f"Már {len(bot.guilds)} Szerveren!"]

 while not bot.is_closed():

   status = random.choice(statuses)

   await bot.change_presence(status=discord.Status.do_not_disturb,activity=discord.Game(name=status))

   await asyncio.sleep(3)



bot.loop.create_task(ch_pr())
async def on_ready():
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))
    status = ["Már " + "5" + " Szerveren!", '?help']
    await bot.change_presence(status=discord.Status.do_not_disturb,activity=discord.Game(next(status)))

with open('./json/warns.json', encoding='utf-8') as f:
  try:
    report = json.load(f)
  except ValueError:
    report = {}
    report['users'] = []
keep_alive()
bot.load_extension("cogs.music")
bot.load_extension("cogs.fun")
bot.load_extension("cogs.info")
bot.load_extension("cogs.moderationpy")
bot.load_extension("cogs.help")
bot.load_extension("cogs.hystats")
bot.load_extension("cogs.moderation.purge")
bot.load_extension("cogs.moderation.kick")
bot.load_extension("cogs.moderation.unban")
bot.run(os.environ['TOKEN'])