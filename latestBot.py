# ! ! !
# ESSA points no working
# ! ! !

import re
import os
import sys
import Cython
import ctypes
from ctypes import cdll, CDLL

import random
import datetime
import asyncio
import json
from difflib import SequenceMatcher


import nextcord as discord 

from nextcord import ActivityType, guild
from nextcord import user
from nextcord import member
from nextcord import Message
from nextcord import channel

from nextcord.ext import commands, tasks
from nextcord.ext.commands import has_permissions

from nextcord.utils import get


# mydll = cdll.LoadLibrary('c:\\Users\\jaroz\\documents\\fap box\\~Python\\~DIscord-Trader\\clear.dll')


with open('c:\\Users\\jaroz\\Documents\\fap box\\~Python\\~DIscord-Trader\\settings.json', 'r') as d:

    settings = json.loads(d.read())
    
    powerUser = settings['powerUser']

    pref = settings['prefix']

    d.close()





class fg:
    black = "\u001b[30m"
    red = "\u001b[31m"
    green = "\u001b[32m"
    yellow = "\u001b[33m"
    blue = "\u001b[34m"
    magenta = "\u001b[35m"
    cyan = "\u001b[36m"
    white = "\u001b[37m"

    def rgb(r, g, b):
        return f"\u001b[38;2;{r};{g};{b}m"

class bg:
    black = "\u001b[40m"
    red = "\u001b[41m"
    green = "\u001b[42m"
    yellow = "\u001b[43m"
    blue = "\u001b[44m"
    magenta = "\u001b[45m"
    cyan = "\u001b[46m"
    white = "\u001b[47m"

    def rgb(r, g, b): 
        return f"\u001b[48;2;{r};{g};{b}m"


def consoleStatus(status : str):

    # mydll.clearScreen()
    os.system("cls")
    print('\n'*5)
    print(f'{fg.white}Status: ')
    print(f'{fg.white}Prefix: {fg.cyan}{pref}{fg.white}')



client = commands.Bot(command_prefix=pref)

locTime = datetime.datetime.now()

usersStatsPath = 'c:\\Users\\jaroz\\Documents\\fap box\\~Python\\~DIscord-Trader\\usersStats.json'

serversNames = []
serversIDs = []

# for guild in client.guilds:

#     serversList.append(guild)

def add(a : int, b : int):
    return a + b;
    

def subtrack(a : int, b : int):
    return a - b;


def percetage(a : int, b : int):
    return a % b;


def multiply(a : int, b : int):
    return a * b;


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio();



def Log(logg : str):

    with open('logs.txt', 'a', 'utf8') as logfile:
        logfile.write(f"{locTime}\n{logg}\n \n")





@tasks.Loop(seconds=60)
async def loop():

    with open(usersStatsPath, 'r') as j:

        usersStats = json.loads(j.read())

        for member in discord.guilds.members(limit=None):


            if not f'user.{member.id}' in usersStats:
                    usersStats[f'user.{member.id}'] = {}
                    usersStats[f'user.{member.id}']['essa'] = 0
                    usersStats[f'user.{member.id}']['warns']

        j.close()

    with open(usersStatsPath, 'w') as j:

        j.write(json.dumps(usersStats), indent=4)
        j.close()








@client.event
async def on_ready():

    # serversList.append(discord.client.guilds)
    for guild in client.guilds:

        serversNames.append(guild.name)
        serversIDs.append(guild.id)


    await client.change_presence(activity=discord.Game(name=settings['activity']))

    consoleStatus(f'{fg.green}Online')
    
    await client.get_channel(settings['joinLeaveChannel']).send(f"Hello")



@client.event
async def on_command_error(ctx, error : Exception):


    embed=discord.Embed(title=error, description=f'{error}', color=0x00fbff)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_footer(text=datetime.datetime.now())

    await ctx.send(embed=embed)


    print(f"""
            \n
            \n
            exception: {fg.RED}
            {error}
            {fg.white}
            \n
            \n
            """)






@client.event
async def on_member_join(member : discord.member):

    await client.get_channel(settings['joinLeaveChannel']).send(f"Hello <@{member.id}>")

    Log(f'@<{member}> przybył na serwer')


@client.event
async def on_member_remove(ctx, member : discord.member):

    await client.get_channell(settings['joinLeaveChannel']).send(f"{member} spierdolił z serwera")


@client.event
async def on_message_delete(ctx, message : discord.message):

    if message.author.id != 921832817854398505:
        Log(f"{message.author} usunoł wiadomość: \n \n '{message.content}'\n")



@client.event
async def on_message(message : discord.message):


    
    if similar('Jebac Jara', message.content) > 0.5:
        await message.channel.send('Nie jara, ciebie jebać')
    

    if similar('Trader', message.content) > 0.7 and message.author.id != 921832817854398505:
        await message.channel.send('Trader to bug')


    if similar('mati', message.content) > 0.7 and message.author.id:
        await message.channel.send("https://media.discordapp.net/attachments/791411982380695592/927649861321519104/Screenshots_2022-01-01-23-31-08.png")


    if similar('zelson', message.content) > 0.7 and message.author.id != 921832817854398505:
        await message.channel.send('E')
        await asyncio.sleep(1)
        await message.channel.send('XD')
        await asyncio.sleep(1)
        await message.channel.send('Kto pytał')

    await client.process_commands(message)



@has_permissions(ban_members=True)
@client.command()
async def ban(ctx, member : discord.member, reason=None):
    await member.ban()

    if reason is None:
        reason = 'No provided'

    Log(f"user {member.id} has banned from {ctx.author.id} ")

    embed=discord.Embed(title="Banned", description="user", color=0x00fbff)
    embed.add_field(name="reason", value=f"{reason}", inline=False)
    embed.set_thumbnail(url=member.avatar_url)

    await ctx.send(embed=embed)

@has_permissions(kick_members=True)
@client.command()
async def kick(ctx, member : discord.Member, reason=None):
    await member.kick()

    if reason is None:
        reason = 'No provided'

    Log(f"user {member.id} has kicked from {ctx.author.id} ")

    embed=discord.Embed(title="Kicked", description="user", color=0x00fbff)
    embed.add_field(name="reason", value=f"{reason}", inline=False)
    await ctx.send(embed=embed)


@has_permissions(mute_members=True)
@client.command()
async def mute(ctx, member : discord.Member, reason=None):

    muteRole = discord.utils.get(ctx.message.guild.roles, id=settings['muteRole'])

    if reason is None:
        reason = 'No provided'

    await client.add_roles(member, muteRole)





@client.command()
async def log(ctx, loggg : str):
    
    if len(loggg) > 69:
        await ctx.channel.send()

    try:
        Log(loggg)
        
        embed = discord.Embed(title="Udana akcja", description="Log pomyślnie wprowadzony do dziennika", color=0x00fbff)
        await ctx.channel.send(embed)
    except:
        embed = discord.Embed(title="błąd", description="Maksymalna długość zmiennej string loggg to 69 znaków", color=0x00fbff)
        await ctx.channel.send(embed)


@client.command()
async def end(ctx):

    if ctx.author.id == powerUser:

        consoleStatus(f'{fg.red}Offline')
        await ctx.channel.send("baj")

        sys.exit(0)

    else:

        await ctx.channel.send('Missing permisions !')



@client.command()
async def rename(ctx, name : str):

    if ctx.author.id == powerUser:

        await client.user.edit(username=name)

    else:

        ctx.channel.send('Missing permisions !')


@client.command()
async def retag(ctx):

    botTag = client.get_user(921832817854398505).discriminator

    await client.user.edit(username=botTag)
    await client.user.edit(username='Trader')


@client.command()
async def restatus(ctx, typeActicity : discord.activity, status : str):

    if ctx.author.id == powerUser:

        await client.change_presence(activity=ActivityType(name=status))

    else:

        await ctx.channel.send('Missing permisions !')


@client.command()
async def prefix(ctx):

    await ctx.channel.send(f"My prefix is {pref}")


@client.command()
async def av(ctx, *, member : discord.Member = None):

    if member is None:

        member == ctx.author



    avatar = member.avatar

    await ctx.channel.send(avatar)


@client.command()
async def serversL(ctx):

    for i in serversNames:

        await ctx.send(i)


@client.command()
async def source(ctx):

    src = open('c:\\Users\\jaroz\\Documents\\fap box\\~Python\\~DIscord-Trader\\bot.py', 'r').read()

    await ctx.channel.send(f"```py\n{src}\n```")



@client.command()
async def plus(ctx, member : discord.Member, amount : int):

    j = open('c:\\Users\\jaroz\\Documents\\fap box\\~Python\\~DIscord-Trader\\essaPoints.json', 'a')

    essa = json.loads(j.read())

    


    for member in ctx.guild.members(limit=None):


        if not member.id in essa:
            essa.append({f'{member.id}': 0})

        if essa[f"{ctx.author.id}"] < amount and ctx.author.id != powerUser:

            embed=discord.Embed(title=f'error - {datetime.datetime.now()}', description='Twoja essa jest za mała', color=0x00fbff)
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

        else:

            fromUser = int(essa[f'"{ctx.author.id}"'])
            toUser = int(essa[f'"{member.id}"'])

            fromUser -= amount
            toUser += amount

            








    j.close()


@client.command()
async def send(ctx, msg : str):
    
    await ctx.message.delete()
    await ctx.channel.send(f"{msg}")

    Log(f"\n <@{ctx.author.id}> używając {settings['prefix']} wyslal wiadomość {msg}")


@client.command()
async def similarity(ctx, a : str, b : str):

    await ctx.channel.send(f'{float(similarity(a, b))}%')


@client.command()
async def anal(ctx, member : discord.Member):
    await ctx.channel.send(f"*<@{ctx.author.id}> zaczol zapinać <@{member.id}> prosto w jego dupalce :hot_face:*")
    await asyncio.sleep(5)
    await ctx.channel.send(f"*<@{ctx.author.id}> spuscił się <@{member.id}> prosto w głąb jego mokrego odbytu :weary:*")


@client.command()
async def roll(ctx, min : int, max : int):
    if max > 6900 or max < -6900:
        max = 6900
    
    if min < -6900 or min > 6900:
        min = -6900

    await ctx.channel.send(random.randint(min, max))

@client.command()
async def choice(ctx, choice0 : str, choice1 : str, choice2=None, choice3=None, choice4=None):
    choices = []
    
    if choice0 != None:
        choices.append(choice0)
    
    if choice1 != None:
        choices.append(choice1)
    
    if choice2 != None:
        choices.append(choice2)

    if choice3 != None:
        choices.append(choice3)

    if choice4 != None:
        choices.append(choice4)



    await ctx.channel.send(random.choice(choices))


@client.command()
async def meme(ctx):

    memes = [

        'https://cdn.discordapp.com/attachments/753683283182747759/939476919739621407/FB_IMG_1643793609067.jpg', # 0
        'https://cdn.discordapp.com/attachments/753683283182747759/939476920108728330/FB_IMG_1643793642945.jpg', # 1
        'https://cdn.discordapp.com/attachments/753683283182747759/939476920360370206/FB_IMG_1643793770997.jpg', # 2
        'https://cdn.discordapp.com/attachments/753683283182747759/939478970410356766/Untitled18_20220204165110.png', # 3
        'x', # 4
        'x', # 5
        'x', # 6
        'x', # 7
        'x', # 8
        'x', # 9
        'x', # 10
        'x', # 11
        'x', # 12
        'x', # 13
        'x', # 14
        'x', # 15
        'x', # 16
        'x', # 17
        'x', # 18
        'x' # 19
    ]

    memeChoice = random.choice(memes)

    while memeChoice == 'x':

        memeChoice = random.choice(memes)


    await ctx.channel.send(random.choice(memes))
    # await client.say(ctx.message.channel, f"{random.choice(memes)}")


@client.command()
async def film(ctx):

    films = [

        'https://cdn.discordapp.com/attachments/296056831514509312/773404299609767946/video0-58.mp4',
        'https://cdn.discordapp.com/attachments/296056831514509312/773404299609767946/video0-58.mp4',
        'https://cdn.discordapp.com/attachments/773151424724729886/806854489742245888/video0_2.mp4',
        'https://cdn.discordapp.com/attachments/773151424724729886/808636325934792744/7b2c1bf81d9016431aa46ea9a5c3a130.mp4',
        'https://cdn.discordapp.com/attachments/796881224718221323/808303823974039602/redditsave.com-weird_flex_but_ok-edzlanht70e61.mp4',
        'https://cdn.discordapp.com/attachments/796881224718221323/808318518835413003/Teams.mp4',
        'https://cdn.discordapp.com/attachments/792792798377279509/808089281435926548/video0.mp4',
        'https://cdn.discordapp.com/attachments/621057340963160115/809166647108960257/video-1612904500.mp4',
        'https://cdn.discordapp.com/attachments/755771736561287209/809730636801376256/video0-67.mp4',
        'https://cdn.discordapp.com/attachments/755771736561287209/809731909801476116/video0_1_2.mp4',
        'https://cdn.discordapp.com/attachments/773151424724729886/809765492671774760/video-1613040259.mp4',
        'https://cdn.discordapp.com/attachments/773151424724729886/810244464396206090/Top_10_niebezpieczne_gangi-2.mp4',
        'https://cdn.discordapp.com/attachments/773151424724729886/811210304452165672/xD.mp4',
        'https://cdn.discordapp.com/attachments/773151424724729886/812319349166833664/video0_6.mp4',
        'https://cdn.discordapp.com/attachments/773151424724729886/812628207530278922/video0-15_1.mp4',
        'https://cdn.discordapp.com/attachments/773151424724729886/812825229746765844/2e0bb6c0-a98d-4f22-83c5-abba8a93000c.mp4',
        'https://cdn.discordapp.com/attachments/773151424724729886/814106087665172540/true.mp4',
        'https://cdn.discordapp.com/attachments/676232229189451787/816653608975204382/video0.mp4',
        'https://cdn.discordapp.com/attachments/676232229189451787/816725693017751634/video0a.mp4'
    ]

    await ctx.channel.send(random.choice(films))







client.run(settings["token"])
