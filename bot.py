import sys
import discord
import math
import os
import random
import youtube_dl
import asyncio

from discord.ext import commands
from youtube_dl import YoutubeDL

default_prefix = ['/']
client = commands.Bot(command_prefix = default_prefix)
queue = {}

@client.event
async def on_ready():
    print("Bot is of operation")
    await client.get_channel(795796608461176845).send("Bot is online!")

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    print(f'(member) has joined the current server')
    await channel.send(f'(member.mention) has joined the server I guess')

@client.event
async def on_member_leave(member):
    print(f'(member) has left the current server')
    await client.get_channel(795796608461176845).send(f'(member) left the server, oh well')


@client.command()
async def ping(ctx):
    await ctx.send(f'ping is {round(client.latency * 1000)}ms loser')

@client.command(pass_context = True)
async def join(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.message.author.voice.channel
        await ctx.send("I connected to the channel!")
    else:
        await ctx.send("Connect to a channel first dumbfuck")
        return
        global voice
        try:
            voice = await channel.connect()
        except:
            TimeoutError


    await channel.connect()
@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    await client.get_channel(795796608461176845).send("I left the channel, see ya'll next time")

@client.command()
async def echo(ctx, *args):
    output = ''
    if ctx.author.id == 342880029165748226:
        for word in args:
            output += str(word)
            output += ' '
            await ctx.message.delete()
            await ctx.send(output)

    else:
        await ctx.send("You are not allowed to use this command dumbass")

@client.command()
async def queue(ctx, url):
    global queue
    queue.append(url)
    await ctx.send('Added to the queue!')

@client.command()
async def play(ctx, url : str):
    await ctx.message.delete()
    songSearch = os.path.isfile("music.mp3")
    if not ctx.message.author.voice:
        await ctx.send('Join a voice channel first loser')
        return
    try:
        if songSearch:
            os.remove("music.mp3")
    except PermissionError:
        await ctx.send("A song is currently playing")
        return

    channel = ctx.message.author.voice.channel
    await channel.connect()
    await ctx.send("I joined, imma play something")
    player = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "music.mp3")
    player.play(discord.FFmpegPCMAudio("music.mp3"))
    await ctx.send('Now Playing: {}'.format(url))

@client.command()
async def pause(ctx):
    player = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if player.is_playing():
        player.pause()
    else:
        await ctx.send('No audio is playing rn idiot')

@client.command()
async def start(ctx):
    player = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if player.is_paused():
        player.resume()
    else:
        await ctx.send('The audio is already playing stupid')

@client.command()
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()
    await ctx.send('I stopped playing audio, imma go chill now')

 @client.command()
async def on_message(message):
    global messages
    messages += 1

    id = client.get_guild(794039596941180969)
    channels = ["commands"]
    valid_users = ["JOHN#0006,Irwin Kun#2918"]
    bad_words = ["slots", "clipped", "fuck"]

    for word in bad_words:
        if message.content.count(word) > 0:
            print("A bad word was said")
            await message.channel.purge(limit=1)

    if message.content == "-help":
        embed = discord.Embed(title="Help on BOT", description="Some useful commands")
        embed.add_field(name="!hello", value="Greets the user")
        embed.add_field(name="!users", value="Prints number of users")
        await message.channel.send(content=None, embed=embed)

    if str(message.channel) in channels and str(message.author) in valid_users:
        if message.content.find("!hello") != -1:
            await message.channel.send("Hi")
        elif message.content == "!users":
            await message.channel.send(f"""# of Members: {id.member_count}""")


client.loop.create_task(update_stats())
client.run('TOKEN HERE')
