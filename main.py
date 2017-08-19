#!/usr/local/bmgraves-python/discord/bin/python
import discord
import asyncio
#from libsupport import sanity

client = discord.Client()
token = "MzQ4MjEyNDI5ODU2OTY0NjEw.DHjpng.j6SN31kiCFTRkAG7eDExhGo94Ww"

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

async def input_check(message, client):
    if message.content.startswith("?help"):
        response = """Help? don't talk to me about help. I can't help you...nobody can... here are your options
?help - #Displays this help message
"""
        return client.send_message(message.channel, response)
        
def get_response(text):
    if "?help" in text:
        response = """Help? Help? I can't help you, no one can...Here's your bloody help:
- test1
        """
        return response

@client.event
async def on_message(message):
    sane_response = client.user.id != message.author.id
    msg = message.content
    
    # First we make sure the bot isn't seeing its own messages, this prevents infinite loops.
    if sane_response and ("your face" in msg.lower()):
        await client.send_message(message.channel, "Really " + str(message.author.name) + " a 'your face' joke? fucking moron")
    elif sane_response and ("butt" in msg.lower()):
        await client.send_message(message.channel, "Jesus" + str(message.author.name) + " why are you always talking about butts?")
    elif sane_response and (msg.startswith("?help")):
        await client.send_message(message.channel, get_response(msg))




# This is where the Actual login happens?
client.run(token)
