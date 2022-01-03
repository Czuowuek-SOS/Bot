# GPL 3.0
# Jareoz
# Beta

import random
import re
import time
import datetime
import sys
import os
import pickle
import ctypes
from data import join_channel

import discord
from discord import user
from discord import member
from discord import Message
from discord.message import Author
from discord import channel
from discord.ext import commands
from discord.ext.commands import has_permissions

token = 'sex'
client = commands.Bot(command_prefix='.')

kernel32 = ctypes.WinDLL('kernel32')

class Colors:

    white  = '\033[0m'  # white (normal)
    red  = '\033[31m' # red
    green  = '\033[32m' # green
    orange  = '\033[33m' # orange
    blue  = '\033[34m' # blue
    purple  = '\033[35m' # purple



def Log(logg : str):

    binLog = pickle.dumps(logg)

    with open('Logs.txt', 'wb') as w:
        w.write(binLog)
        w.close()



@client.event
async def on_ready():
    print(Colors.green+'Online')
    kernel32.SetConsoleTitleW('Trader Bot')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.channel.send('ogólnie nie możesz wykonać tej operacji bo coś z permisjami jest nie tak ale nie wiem co, mam nadzieję żę pomogłem')
    else:
        await ctx.channel.send('coś jebło ale nie wiem co')

# sets commands

@client.command()
async def set_join_chanel (ctx, channel : discord.channel):
    ctx.channel.send(f'Ustawiono kanał przywirań na {channel} \n wymagane ponowne uruchomienie bota')

    with open(os.getcwd + '/.DIscord-Trader/data/join-channel.py', 'w') as w:
        w.write(f'joinChannel = {channel}')
        w.close()



# admin commands

@client.command()
@has_permissions(kick_members=True)
async def wyjeb(ctx, member : discord.Member, *, reason=None):
    await ctx.guild.kick(member)
    await ctx.channel.send(f"wyjebano {member.mention} za {reason}")

    Log(f'{Message.author.id} wyrzucił {member} za {reason} \n')



@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await ctx.guild.ban(member)
    await ctx.channel.send(f'{Message.author} zbanował {member} za {reason}')



# user commands

@client.command()
async def random_choice(ctx, choice1 : str, choice2 : str):
    choice = random.choice(choice1, choice2)
    await ctx.channel.send(choice)

@client.command()
async def ranndom_Int(ctx, min, max):
    await ctx.channel.send(str(random.randint(int(min), int(max))))

@client.command()
async def twoja(ctx):
    await ctx.channel.send('stara')

@client.command()
async def zelson(ctx):
    await ctx.channel.send('E')
    await time.sleep(1)
    await ctx.channel.send('XD')
    await time.sleep(1)
    await ctx.channel.send('Kto pytal')

@client.command()
async def send(ctx, mes):
    await ctx.channel.delete()
    await ctx.channel.send(f'{mes}')

@client.command()
async def end(ctx):
    await ctx.channel.send('wyłonczanie bota...')
    print(Colors.red+'Offline')
    sys.exit()

client.run(token)
