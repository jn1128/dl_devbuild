import sys
import discord
import math
import os

from discord.ext import commands
from dotenv import load_dotenv

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("Bot is of operation")

@client.event
async def on_member_join(member):
    print(f'(member) has joined the current server')

@client.event
async def on_member_leave(member):
    print(f'(member) has left the current server')

@client.event
async def ping(ctx):
    await ctx.send(f'ping is {round(client.latency * 1000)}ms')

client.run('TOKEN HERE')
