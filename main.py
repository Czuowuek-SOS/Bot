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
import platform

from nextcord import guild
from data import join_channel
from data import Token

systemInfo = platform.uname()

try:
    import nextcord as discord
except ImportError:
    if systemInfo.system == 'Windows':
        os.startfile(f'{os.getcwd()}/pkg-install.ps1')
        import nextcord as discord
    elif systemInfo.system == 'Linux' or systemInfo.system == 'MacOS':
        os.system('python3 -m pip install -U discord.py')
        import nextcord as discord

from discord import user
from discord import member
from discord import Message
from discord import channel
from discord.ext import commands
from discord.ext.commands import has_permissions

token = Token.token
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

    with open('Logs.txt', 'ab', 'utf8') as w:
        w.write(binLog)
        w.close()



@client.event
async def on_ready():
    print(Colors.green+'Online')
    kernel32.SetConsoleTitleW('Trader Bot')

    Log(f'Wlonczono bota - {datetime.datetime.now()}')

@client.event
async def on_member_join(member):
    await guild.system_channel.send(f'<@{member.id}> wbił na serwer')

    Log(f'@{member.id} wszedl na serwer - {datetime.datetime.now()}')



# @client.event
# async def on_guild_join():
#     async guild.join_channel.send('')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.channel.send('ogólnie nie możesz wykonać tej operacji bo coś z permisjami jest nie tak ale nie wiem co, mam nadzieję żę pomogłem')
    else:
        await ctx.channel.send(f'''```py\n{error}\n```''')

# sets commands

@client.command()
async def set_join_channel (ctx, channel : discord.channel):
    ctx.channel.send(f'Ustawiono kanał przywitań na {channel} \n wymagane ponowne uruchomienie bota')

    with open(os.getcwd + '/.DIscord-Trader/data/join-channel.py', 'w') as w:
        w.write(f'joinChannel = {channel}')
        w.close()



# admin commands

@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await ctx.guild.kick(member)
    await ctx.channel.send(f"@{ctx.author.id} wyjebał {member.mention} za {reason}")

    Log(f'@{ctx.author.id} wyrzucil {member} za {reason} - {datetime.datetime.now()}\n')



@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await ctx.guild.ban(member)
    await ctx.channel.send(f'@{ctx.author.id} zbanował {member} za {reason}')


@client.command()
async def end(ctx):
    await ctx.channel.send('wyłonczanie bota...')
    print(Colors.red+'Offline')
    sys.exit(0)

# user commands

@client.command()
async def random_choice(ctx, choice1 : str, choice2 : str):
    choice = random.choice([choice1, choice2])
    await ctx.channel.send(choice)

@client.command()
async def ranndom_Int(ctx, min : int, max : int):
    if max > 2137:
        await ctx.channel.send('maksymalna wartość INT dla zmiannej max to 2137')
    elif max < 0:
        await ctx.channel.send('Zmienna max nie akceptuje wartości ujemnych')
    await ctx.channel.send(str(random.randint(min, max)))

@client.command()
async def twoja(ctx):
    await ctx.channel.send('stara')

@client.command()
async def zelson(ctx):
    await ctx.channel.send('E')
    time.sleep(1)
    await ctx.channel.send('XD')
    time.sleep(1)
    await ctx.channel.send('Kto pytal')

@client.command()
async def send(ctx, mes):
    await ctx.channel.purge(limit=1)
    await ctx.channel.send(f'{mes}')

@client.command()
async def sex(ctx, member : discord.member):
    await ctx.channel.send(f'@{ctx.author.id} zaczoł ostro zapinać w dupe {member}')
    time.sleep(5)
    await ctx.channel.send(f'@{ctx.author.id} spuscił sie {member} prosto do dupy')

@client.command()
async def mati(ctx):
    ctx.channel.send('''
Samo bawienie się w politykow
Już jest posrane
I trzeba mieć źle w głowie
Żeby kurwą w jakieś politykowanie się bawic
Biorąc pod uwage
Że średnia wieku tej spolecznosci to 14 lat 
''')

@client.command()
async def aszer(ctx):
    for i in range(69):
        await ctx.channel.send(f'<@{ctx.author.id}> rel')

@client.command()
async def atack(ctx, integer : int, mamber : discord.member):
    if integer > 69:
        await ctx.channel.send('nie')
        
    await ctx.channel.purge(limit=1)
    for i in range(integer):
        ctx.channel.send(f'<@{member.id}>')

client.run(token)
