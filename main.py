#!/usr/local/bmgraves-python/discord/bin/python
import discord
import asyncio
from libsupport import chatty

client = discord.Client()
token = "MzQ4MjEyNDI5ODU2OTY0NjEw.DHjpng.j6SN31kiCFTRkAG7eDExhGo94Ww"

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    butt_count = 0
    # First we make sure the bot isn't seeing its own messages, this prevents infinite loops.
    sane_response = client.user.id != message.author.id
    msg = message.content
    
    if sane_response and ("your face" in msg.lower()):
        await client.send_message(message.channel, chatty.face_joke(message))
    elif sane_response and ("butt" in msg.lower()):
        butt_count +=1
        await client.send_message(message.channel, chatty.butt_joke(message, butt_count))
    elif sane_response and (msg.startswith("?test")):
        await client.send_message(message.channel, chatty.test_joke(message))
    elif sane_response and (msg.startswith("?help")):
        await client.send_message(message.channel, chatty.get_help())
    elif sane_response and (msg.startswith("?admintest")):
        await client.send_message(message.channel, chatty.get_help())




# This is where the Actual login happens?
client.run(token)
