import sys
import discord
import math
import os
import random

from discord.ext import commands

default_prefix = ['!']
client = commands.Bot(command_prefix = default_prefix)


@client.event
async def on_ready():
    print("Bot is of operation")
    await client.get_channel(795796608461176845).send("Bot is online!")

@client.event
async def on_member_join(member):
    print(f'(member) has joined the current server')
    await client.get_channel(795796608461176845).send(f'(member) has joined the server I guess')

@client.event
async def on_member_leave(member):
    print(f'(member) has left the current server')
    await client.get_channel(795796608461176845).send(f'(member) left the server, oh well')

@client.command()
async def ping(ctx):
    await ctx.send(f'ping is {round(client.latency * 1000)}ms loser')


@client.command(pass_context = True)
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if channel == None:
        await ctx.send("Must be in voice channel to use command")
        return
    if voice and voice.is_connected():
        await voice.move_to(channel)
        await client.get_channel(795796608461176845).send("I joined the channel!")
    else:
        voice = await channel.connect()
        await client.get_channel(795796608461176845).send("I joined the channel!")

@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    await client.get_channel(795796608461176845).send("I left the channel, see ya'll next time")

client.run('TOKEN HERE')
