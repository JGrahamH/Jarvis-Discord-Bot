import discord
from discord.ext import commands
from discord.utils import get
import random
import aiohttp
import json
import youtube_dl
import os
import kadal
from kadal import MediaNotFound

client = commands.Bot(command_prefix='!')
TOKEN = 'YOUR TOKEN'

AL_ICON = 'https://avatars2.githubusercontent.com/u/18018524?s=280&v=4'

# Shows bot is Online
@client.event
async def on_ready():
    print('Bot is Online')
    print('Version 05')
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
    """Random bot message."""
    bot_message_response = 'I am a robot, beep boop.',
    'beep',
    'frequency overload',
    '10101010101010'
    response = random.choice(bot_message_response)
    await ctx.channel.send(response)

# ping, pong, latency
@client.command()
async def ping(ctx):
    """Pong and latency."""
    await ctx.send(f'pong! {round(client.latency * 1000)}ms')

# clears 5 chat messages, unless specified
@client.command()
async def clear(ctx, amount=5):
    """Clears chat messages."""
    await ctx.channel.purge(limit=amount)

# simple message
@client.command()
async def bot(ctx):
    """Bot message."""
    bot_status = "```Hello, I am Jarvis.```"
    await ctx.send(bot_status)

# cypto commands

# bitcoin
@client.command()
async def btc(ctx):
    """Fetches BTC price from Coingecko."""
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=USD'  # noqa
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        responseStr = str(response)
        await session.close()
        await ctx   .channel.send("Bitcoin price is: $" + responseStr[19:27])

# litecoin
@client.command()
async def ltc(ctx):
    """Fetches LTC price from Coingecko."""
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd'  # noqa
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        responseStr = str(response)
        await session.close()
        await ctx.channel.send("Litecoin price is: $" + responseStr[19:25])

# ethereum
@client.command()
async def eth(ctx):
    """Fetches ETH price from Coingecko."""
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd'  # noqa
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        responseStr = str(response)
        await session.close()
        await ctx.channel.send("Ethereum price is: $" + responseStr[20:26])

# sudoku/ seppuku
@client.command()
async def sudoku(ctx):
    """Seppuku"""
    file = discord.File("image/sudoku.jpg", filename="sudoku.jpg")
    await ctx.channel.send(file=file)

# Neko Love API
# list image types from neko api
@client.command()
async def imglist(ctx):
    """List of image search terms."""
    terms = "```neko``````kitsune``````hug``````pat``````waifu``````cry``````kiss``````slap``````smug``````punch```"  # noqa
    await ctx.send(terms)

# Embed - gets random cat girl image from neko love
@client.command()
async def neko(ctx):
    """Fetches neko image."""
    endpoint = 'neko'
    url = ('https://neko-love.xyz/api/v1/' + endpoint)
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        responseimg = response['url']
        await session.close()
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
    """Fetches NSFW image."""
    endpoint = 'nekolewd'
    url = ('https://neko-love.xyz/api/v1/' + endpoint)
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        responseimg = response['url']
        await session.close()
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
    """Fetches kitsune image."""
    endpoint = 'kitsune'
    url = ('https://neko-love.xyz/api/v1/' + endpoint)
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        responseimg = response['url']
        await session.close()
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
    """Fetches image based on tag."""
    endpoint = endpoint_val
    url = ('https://neko-love.xyz/api/v1/' + endpoint)
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        responseimg = response['url']
        await session.close()
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
    """Bot joins voice channel."""
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
    """Bot leaves voice channel."""
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
    """Bot plays the youtube video in the voice channel."""
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
    """Bot plays pauses the youtube video in the voice channel."""
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
    """Bot resumes pauses the youtube video in the voice channel."""
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
    """Bot stops pauses the youtube video in the voice channel."""
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print('Music Stopped')
        voice.stop()
        await ctx.send('Music is Stopped.')
    else:
        print('No music playing - Stopped')
        await ctx.sent('No music playing - Stopped')

# plays video from youtube
@client.command(aliases=['f'])
async def fleb(ctx, user):
    """Fleb"""
    user = user
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
        print(f'{user} is a fleb.')
    else:
        voice = await channel.connect()
        await ctx.send(content=f"```{user} is a fleb.```")

    voice = get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("data/fleb.mp3"),
               after=lambda e: print("Fleb played"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.1
    print("Fleb command")

# searches for anime on anilist
@client.command(name="anime")
async def al_anime(ctx, query):
    """Searches Anilist for an Anime."""
    k = kadal.Client()
    async with ctx.typing():
        try:
            result = await k.search_anime(query, popularity=True)
        except MediaNotFound:
            return await ctx.send(":exclamation: Anime was not found!")
        except Exception as e:
            return await ctx.send(f":exclamation: An unknown error occurred:\n{e}")  # noqa
    if len(result.description) > 1024:
        result.description = result.description[:1024 - (len(result.site_url) + 7)] + f"[...]({result.site_url})"  # noqa
    em = discord.Embed(title=result.title['english'] or result.title['romaji'], colour=0x02a9ff)  # noqa
    em.description = ", ".join(result.genres)
    em.url = result.site_url
    em.add_field(name="Japanese Title", value=result.title['native'], inline=True)  # noqa
    em.add_field(name="Type", value=str(result.format.name).replace("_", " ").capitalize(), inline=True)  # noqa
    em.add_field(name="Episodes", value=result.episodes or "?", inline=True)
    em.add_field(name="Score", value=str(result.average_score / 10) + " / 10" if result.average_score else "?",  # noqa
                 inline=False)
    em.add_field(name="Status", value=str(result.status.name).replace("_", " ").capitalize(), inline=True)  # noqa
    (year, month, day) = result.start_date.values()
    aired = f"{day}/{month}/{year}"
    (year, month, day) = result.end_date.values() if result.end_date['day'] else ('?', '?', '?')  # noqa
    aired += f" - {day}/{month}/{year}"
    em.add_field(name="Aired", value=aired, inline=True)
    em.add_field(name="Synopsis", value=result.description, inline=False)
    em.add_field(name="Link", value=result.site_url, inline=False)
    em.set_author(name='Anilist', icon_url=AL_ICON)
    em.set_thumbnail(url=result.cover_image)
    await ctx.send(embed=em)


# searches for manga on anilist
@client.command(name="manga")
async def al_manga(ctx, query):
    """Searches Anilist for a Manga."""
    k = kadal.Client()
    async with ctx.typing():
        try:
            result = await k.search_manga(query, popularity=True)
        except MediaNotFound:
            return await ctx.send(":exclamation: Manga was not found!")
        except Exception as e:
            return await ctx.send(f":exclamation: An unknown error occurred:\n{e}")  # noqa
    if len(result.description) > 1024:
        result.description = result.description[:1024 - (len(result.site_url) + 7)] + f"[...]({result.site_url})"  # noqa
    em = discord.Embed(title=result.title['english'] or result.title['romaji'], colour=0xFF9933)  # noqa
    em.description = ", ".join(result.genres)
    em.url = result.site_url
    em.add_field(name="Japanese Title", value=result.title['native'], inline=True)  # noqa
    em.add_field(name="Type", value=str(result.format.name).replace("_", " ").capitalize(), inline=True)  # noqa
    em.add_field(name="Chapters", value=result.chapters or "?", inline=True)
    em.add_field(name="Volumes", value=result.volumes or "?", inline=True)
    em.add_field(name="Score", value=str(result.average_score / 10) + " / 10" if result.average_score else "?",  # noqa
                 inline=False)
    em.add_field(name="Status", value=str(result.status.name).replace("_", " ").capitalize(), inline=True)  # noqa
    (year, month, day) = result.start_date.values()
    published = f"{day}/{month}/{year}"
    (year, month, day) = result.end_date.values() if result.end_date['day'] else ('?', '?', '?')  # noqa
    published += f" - {day}/{month}/{year}"
    em.add_field(name="Published", value=published, inline=True)
    em.add_field(name="Synopsis", value=result.description, inline=False)
    em.add_field(name="Link", value=result.site_url, inline=False)
    em.set_author(name='Anilist', icon_url=AL_ICON)
    em.set_thumbnail(url=result.cover_image)
    await ctx.send(embed=em)


client.run(TOKEN)
