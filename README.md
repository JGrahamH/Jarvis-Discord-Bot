# Jarvis-Discord-Bot
A discord bot created in python using discord.py. A list of commands provide features such as Youtube, images, and responses.

## Requirements
- discord.py
- python-dotenv - seperated bot token from code to reduce likelihood of token being posted and bot mis-used.
- random
- aiohttp
- youtube_dl - for music playback in channel
- kadal - used for searching using the anilist API v2

## Getting Started
1. Clone this repo.
2. Create a copy of `.env.example` named `.env`
3. Got to the Discord Developer Portal and create an application.
4. Go to "Bot" tab and click "Add a bot".
5. Copy the token for the bot and paste in `.env` file.
6. Run `jarvis_bot.py`

### Issues
If you have an error due to missing SSL certificates, refer to [this.](https://github.com/Rapptz/discord.py/issues/4159)

## Commands
Prefix "!" is required before command.

| Command | Description |
| --- | --- |
| help | Shows this message. |
| clear | Clears chat messages. |
| 404 | Random bot message. |
| bot | Bot message. |
| coin | Fetches coin price from Coingecko. |
| coinchart | Fetches coin price from Coingecko for the current day and post a graph as a .png. |
| fleb | Fleb. |
| anime | Searches Anilist for an Anime. |
| manga | Searches Anilist for a Manga. |
| ping | Pong and latency.|
| sudoku | Seppuku. |
| join | Bot joins voice channel. |
| leave | Bot leaves voice channel. |
| play | Bot plays the youtube video in the voice channel. |
| pause | Bot plays pauses the youtube video in the voice channel. |
| resume | Bot resumes pauses the youtube video in the voice channel. |
| stop | Bot stops pauses the youtube video in the voice channel. |
