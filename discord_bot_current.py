import discord
from discord.ext import commands
from discord.utils import get
import random
import aiohttp
import json
import youtube_dl
import os

client = commands.Bot(command_prefix='!')
TOKEN = 'YOUR TOKEN'

# Shows bot is Online
@client.event
async def on_ready():
    print('Bot is Online')
    print('Logged on as {0.user}!'.format(client))
    print('------------')

# error
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        print('Command Error.')
        await ctx.send('Invalid Command Used.')

# someone leaves server
@client.event
async def on_member_join(member):
    print(f"{member} has joined the server.")
    channel = discord.utils.get(member.guild.channels, name="general")
    mName = member.mention
    await channel.send(f"{mName} has joined the server.")

# someone joins server
@client.event
async def on_member_leave(member):
    print(f"{member} has left the server.")
    channel = discord.utils.get(member.guild.channels, name="general")
    mName = member.mention
    await channel.send(f"{mName} has left the server.")

# shows messages in console
@client.event
async def on_message(message):
    print('Message from {0.author}: {0.content}'.format(message))

    if message.author == client.user:
        return

    await client.process_commands(message)

# sends a random message from selection, uses alias for command name
@client.command(aliases=['404'])
async def _404(ctx):
    bot_message_response = 'I am a robot, beep boop.',
    'beep',
    'frequency overload',
    '10101010101010'
    response = random.choice(bot_message_response)
    await ctx.channel.send(response)

# ping, pong, latency
@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency * 1000)}ms')

# clears 5 chat messages, unless specified
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

# simple message
@client.command()
async def bot(ctx):
    bot_status = 'I am Jarvis, ready to help'
    await ctx.channel.send(bot_status)

# cypto commands

# bitcoin
@client.command()
async def btc(ctx):
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=USD'  # noqa
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        responseStr = str(response)
        await ctx   .channel.send("Bitcoin price is: $" + responseStr[19:27])

# litecoin
@client.command()
async def ltc(ctx):
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd'  # noqa
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        responseStr = str(response)
        await ctx.channel.send("Litecoin price is: $" + responseStr[19:25])

# ethereum
@client.command()
async def eth(ctx):
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd'  # noqa
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        responseStr = str(response)
        await ctx.channel.send("Ethereum price is: $" + responseStr[20:26])

# sudoku/ seppuku
@client.command()
async def sudoku(ctx):
    file = discord.File("image/sudoku.jpg", filename="sudoku.jpg")
    await ctx.channel.send(file=file)

# Neko Love API
# list image types from neko api
@client.command()
async def imglist(ctx):
    await ctx.channel.send('neko',
                           'kitsune',
                           'hug',
                           'pat',
                           'waifu',
                           'cry',
                           'kiss',
                           'slap',
                           'smug',
                           'punch')

# Embed - gets random cat girl image from neko love
@client.command()
async def neko(ctx):
    endpoint = 'neko'
    url = ('https://neko-love.xyz/api/v1/' + endpoint)
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        responseimg = response['url']

    embed = discord.Embed(title="Click for Source",
                          colour=discord.Colour(0x3ec490),
                          url=responseimg)
    embed.set_author(name="Jarvis",
                     url="",
                     icon_url="https://cdn.discordapp.com/attachments/727523746059124759/728043489824211034/FH5pIK55ki.png")  # noqa
    embed.set_image(url=responseimg)
    await ctx.channel.send(embed=embed)

# Embed - gets random NSFW image from neko love
@client.command()
async def hentai(ctx):
    endpoint = 'nekolewd'
    url = ('https://neko-love.xyz/api/v1/' + endpoint)
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        responseimg = response['url']

    embed = discord.Embed(title="Click for Source",
                          colour=discord.Colour(0x3ec490),
                          url=responseimg)
    embed.set_author(name="Jarvis",
                     url="",
                     icon_url="https://cdn.discordapp.com/attachments/727523746059124759/728043489824211034/FH5pIK55ki.png")  # noqa
    embed.set_image(url=responseimg)
    await ctx.channel.send(embed=embed)

# Embed - gets random kitsune image from neko love
@client.command()
async def kitsune(ctx):
    endpoint = 'kitsune'
    url = ('https://neko-love.xyz/api/v1/' + endpoint)
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        responseimg = response['url']

    embed = discord.Embed(title="Click for Source",
                          colour=discord.Colour(0x3ec490),
                          url=responseimg)
    embed.set_author(name="Jarvis",
                     url="",
                     icon_url="https://cdn.discordapp.com/attachments/727523746059124759/728043489824211034/FH5pIK55ki.png")  # noqa
    embed.set_image(url=responseimg)
    await ctx.channel.send(embed=embed)


# Embed - gets random kitsune image from neko love
@client.command()
async def img(ctx, endpoint_val):
    endpoint = endpoint_val
    url = ('https://neko-love.xyz/api/v1/' + endpoint)
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        responseimg = response['url']

    embed = discord.Embed(title="Click for Source",
                          colour=discord.Colour(0x3ec490),
                          url=responseimg)
    embed.set_author(name="Jarvis", url="",
                     icon_url="https://cdn.discordapp.com/attachments/727523746059124759/728043489824211034/FH5pIK55ki.png")  # noqa
    embed.set_image(url=responseimg)
    await ctx.channel.send(embed=embed)

# youtube playback
# make bot join channel
@client.command(aliases=['j'])
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
        print(f'Bot has joined - {channel}')
    else:
        voice = await channel.connect()

    await ctx.send(f'Bot has joined - {channel}')

# make bot leave channel
@client.command(aliases=['l'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"Bot has left - {channel}")
        await ctx.send(f'Bot has left - {channel}')
    else:
        print("Bot was told to leave voice channel, but was not in one")
        await ctx.send("Not currently in a voice channel")

# plays video from youtube
@client.command(aliases=['p'])
async def play(ctx, url):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
        print(f'Bot has joined - {channel}')
    else:
        voice = await channel.connect()
        await ctx.send(content=f"```Bot has joined - {channel}```")

    searchURL = str(url)
    print(searchURL)
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            print("Removed old song file")
    except PermissionError:
        print("Song file tried to be deleted, but it's being played")
        await ctx.send("ERROR: Music playing")
        return

    await ctx.send(content="```Getting everything ready now```")

    voice = get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio now")
        ydl.download([searchURL])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"),
               after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.1

    nname = name.rsplit("-", 2)
    print("Playing")

    embed = discord.Embed(title=f"Playing: {nname[0]}",
                          colour=discord.Colour(0x3ec490),
                          url='',
                          description=(searchURL))

    embed.set_author(name="Jarvis", url="",
                     icon_url="https://cdn.discordapp.com/attachments/727523746059124759/728043489824211034/FH5pIK55ki.png")  # noqa

    await ctx.channel.send(embed=embed)

# pauses youtube video
@client.command(aliases=['ps'])
async def pause(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print('Music Paused')
        voice.pause()
        await ctx.send('Music is paused.')
    else:
        print('Music is not playing - Failed Pause')
        await ctx.sent('Music is not playing - Failed Pause')

# resume youtube video
@client.command(aliases=['rs'])
async def resume(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_paused():
        print('Resumed Music')
        voice.resume()
        await ctx.send('Music is resumed.')
    else:
        print('Music is not paused - Failed Pause')
        await ctx.sent('Music is not paused - Failed Pause')


# resume youtube video
@client.command(aliases=['st'])
async def stop(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print('Music Stopped')
        voice.stop()
        await ctx.send('Music is Stopped.')
    else:
        print('No music playing - Stopped')
        await ctx.sent('No music playing - Stopped')

client.run(TOKEN)
