import discord, asyncio
import os
from keepAlive import keep_alive
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='-')

valid_Users = ["WhoDiis#5662, elicitly#5544, DemonKing0000#1200"]

@client.event
async def on_ready():
  print("Bot is on")

@client.event
async def on_message(message):

  if message.author == client.user:
    return

  if message.content.startswith('-ping'):
    await message.channel.send("pong")

  if message.content.startswith('-add'):
    text = message.content.strip("-add")
    x = text.split()
    add = int(x[0]) + int(x[1])
    await message.channel.send("It's {a}".format(a = add))

  if message.content.startswith('-mod'):
    text = message.content.strip("-mod")
    x = text.split()
    mod = int(x[0]) % int(x[1])
    await message.channel.send("It's {m}".format(m = mod))

  if message.content.startswith('-sub'):
    text = message.content.strip("-sub")
    x = text.split()
    sub = int(x[0]) - int(x[1])
    await message.channel.send("It's {s}".format(s = sub))

  if message.content.startswith('-floorDiv'):
    text = message.content.strip("-floorDiv")
    x = text.split()
    ans = int(x[0]) // int(x[1])
    await message.channel.send("It's {a}".format(a = ans))

  if message.content.startswith('-div'):
    text = message.content.strip("-div")
    x = text.split()
    div = int(x[0]) / int(x[1])
    await message.channel.send("It {d}".format(d = div))

  if message.content.startswith('-multi'):
    text = message.content.strip("-multi")
    x = text.split()
    multi = int(x[0]) * int(x[1])
    await message.channel.send("It {m}".format(m = multi))

  
  if message.content.startswith('-Commands'):
    Commands = "-add, -sub, -multi, -div, -ping, -mod(modulus), -floorDiv"
    await message.channel.send(Commands)

  #clear all messsages in channel only for user "WhoDiis"
  if message.content.startswith('-cAll') & (message.author.name == "WhoDiis"):
    await message.channel.purge()

  if message.content.startswith('-clear'):
    text = message.content.strip("-clear")
    await message.channel.purge(limit=int(text))

  if message.content.startswith('-me'):
    guild = client.get_guild(820037042703564801)
    channel = guild.get_channel(820037042703564803)
    await channel.send(f"Hello { message.author.mention}")

@client.event
async def on_member_join(member):
  guild = client.get_guild(820037042703564801)
  channel = guild.get_channel(820037042703564803)
  await channel.send(f"{member.mention} has joined the server.")
  await member.send("Welcome")

keep_alive()
client.run(os.environ['TOKEN'])
