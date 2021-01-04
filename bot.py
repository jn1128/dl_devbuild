import sys
import discord
import math
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

default_prefix = ['!']
client = commands.Bot(command_prefix = default_prefix)


@client.event
async def on_ready(ctx):
    print("Bot is of operation")
    await client.get_channel(793847966162485288).send("Bot is online!")

@client.event
async def on_member_join(member):
    print(f'(member) has joined the current server')

@client.event
async def on_member_leave(member):
    print(f'(member) has left the current server')

@client.command()
async def ping(ctx):
    if {round(client.latency * 1000)} > 20: {
    await ctx.send(f'ping is {round(client.latency * 1000)}ms, you got cheap walmart connection?')
    else:
    await ctx.send(f'ping is {round(client.latency * 1000)}ms')

@client.command(pass_context = True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    voice_client = ctx.member.voice

    if voice_client is None:
        return await ctx.send('Must be in voice channel to use command')
    else:
    await client.join_voice_channel(channel)

@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

client.run('TOKEN HERE')
