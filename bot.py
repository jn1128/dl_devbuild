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
    if voice and voice.is_connected():
        await voice.move_to(channel)
        await client.get_channel(795796608461176845).send("I joined the channel!")
    elif voice and voice.is_connected() == False:
        await client.get_channel(795796608461176845).send("Join a channel first!")

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

client.run('TOKEN HERE')
