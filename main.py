#!/usr/local/bmgraves-python/discord/bin/python
import discord
import asyncio

client = discord.Client()
token = "MzQ4MjEyNDI5ODU2OTY0NjEw.DHjpng.j6SN31kiCFTRkAG7eDExhGo94Ww"

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

#@client.event
#async def on_message(message):
#    if message.content.startswith('!test'):
#        counter = 0
#        tmp = await client.send_message(message.channel, 'Calculating messages...')
#        async for log in client.logs_from(message.channel, limit=100):
#            if log.author == message.author:
#                counter += 1
#        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
#    elif message.content.startswith('!sleep'):
#        await asyncio.sleep(5)
#        await client.send_message(message.channel, 'Done sleeping')
@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        await client.send_message(message.channel, str(message.author.name))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')





# This is where the Actual login happens?
client.run(token)
