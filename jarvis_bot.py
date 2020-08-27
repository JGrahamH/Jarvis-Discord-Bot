import discord
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
import random
import aiohttp
import youtube_dl
import os
import kadal
from kadal import MediaNotFound
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt


today = dt.datetime.now().date()

client = commands.Bot(command_prefix='!')

load_dotenv()
TOKEN = os.getenv('TOKEN')

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
# coin
@client.command()
async def coin(ctx, id):
    """Fetches Coin price from Coingecko."""
    id = id
    url = ("https://api.coingecko.com/api/v3/simple/price?ids="
           + id
           + "&vs_currencies=USD")

    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        df = pd.read_json(response, orient='columns')
        price = (df.iat[0, 0])
        responseStr = str(price)
        await ctx.channel.send("Price is: $ " + responseStr)

# coin graph
@client.command()
async def coinchart(ctx, id):
    """Fetches Coin price from Coingecko showing - Open, Close, Low, High."""
    id = id
    url = "https://api.coingecko.com/api/v3/coins/"
    + id
    + "/ohlc?vs_currency=usd&days=1"

    async with aiohttp.ClientSession() as session:  # AsyncHTTPrequest
        raw_response = await session.get(url)
        response = await raw_response.text()
        df = pd.read_json(response, orient='columns')

        mapping = {df.columns[0]: 'Timestamp',
                   df.columns[1]: 'Open',
                   df.columns[2]: 'High',
                   df.columns[3]: 'Low',
                   df.columns[4]: 'Close'}
        df = df.rename(columns=mapping)
        df = df.drop('Timestamp', 1)
        df['Open'].plot()
        df['High'].plot()
        df['Low'].plot()
        df['Close'].plot()
        plt.legend()
        ax = df.plot(lw=2, colormap='jet',
                     marker='.',
                     markersize=10,
                     title=id)
        ax.set_xlabel("Time")
        ax.set_ylabel("Price - $USD")
        plt.savefig("./image/coinGraph.png")

        file = discord.File("image/coinGraph.png",
                            filename="coinGraph.png")
    await ctx.channel.send(f"{id} 3-Day Chart (USD)")
    await ctx.channel.send(file=file)

# sudoku - seppuku
@client.command()
async def sudoku(ctx):
    """Seppuku"""
    file = discord.File("image/sudoku.jpg", filename="sudoku.jpg")
    await ctx.channel.send(file=file)

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
                     icon_url="https://cdn.discordapp.com"
                     "/avatars/727522439046889623/"
                     "a00dbb8459c13e69663a1c52a338a15b.png")

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
async def fleb(ctx):
    """Fleb"""
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
        print('Fleb command used.')
    else:
        voice = await channel.connect()

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
            return await ctx.send(
                f":exclamation: An unknown error occurred:\n{e}")

    if len(result.description) > 1024:
        result.description = result.description[:1024 - (len(result.site_url) + 7)] + f"[...]({result.site_url})"  # noqa

    em = discord.Embed(title=result.title['english'] or result.title['romaji'],
                       colour=0x02a9ff)
    em.description = ", ".join(result.genres)
    em.url = result.site_url
    em.add_field(name="Japanese Title", value=result.title['native'],
                 inline=True)
    em.add_field(name="Type",
                 value=str(result.format.name).replace("_", " ").capitalize(),
                 inline=True)
    em.add_field(name="Episodes", value=result.episodes or "?", inline=True)
    em.add_field(name="Score",
                 value=str(result.average_score / 10)
                 + " / 10" if result.average_score else "?", inline=False)
    em.add_field(name="Status",
                 value=str(result.status.name).replace("_", " ").capitalize(),
                 inline=True)
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
            return await ctx.send(
                f":exclamation: An unknown error occurred:\n{e}")
    if len(result.description) > 1024:
        result.description = result.description[:1024 - (len(result.site_url) + 7)] + f"[...]({result.site_url})"  # noqa
    em = discord.Embed(title=result.title['english'] or result.title['romaji'],
                       colour=0xFF9933)
    em.description = ", ".join(result.genres)
    em.url = result.site_url
    em.add_field(name="Japanese Title", value=result.title['native'],
                 inline=True)
    em.add_field(name="Type",
                 value=str(result.format.name).replace("_", " ").capitalize(),
                 inline=True)
    em.add_field(name="Chapters", value=result.chapters or "?", inline=True)
    em.add_field(name="Volumes", value=result.volumes or "?", inline=True)
    em.add_field(name="Score",
                 value=str(result.average_score / 10) + " / 10" if result.average_score else "?",  # noqa
                 inline=False)
    em.add_field(name="Status",
                 value=str(result.status.name).replace("_", " ").capitalize(),
                 inline=True)  # noqa
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
