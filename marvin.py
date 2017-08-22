import discord
import asyncio, random
import loadconf
from libsupport import chatty
import os.path

__version__ = ".10a"

client = discord.Client()
dev_mode = True
# Stim is a regulating variable. The lower it is, the more often Marvin will add to the chatdd
#stim = 0
#boredom is a replacement for stimulation, Designed to simplify the logic behind random chats.
boredom = 0
jokes = {'butt':0, 'face':0}
current_msg = ""
last_msg = ""

@client.event
async def on_ready():
    print('Marvin: %s' % __version__)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    #global stim
    global boredom
    global jokes
    global current_msg
    sane_response = client.user.id != message.author.id
    msg = message.content
    if sane_response:
        current_msg = msg
        boredom -= 2
#        await client.send_message(message.channel, "Dev Mode: %s" % current_msg)
    if sane_response and ("your face" in msg.lower()):
        jokes['face'] +=1
        await client.send_message(message.channel, chatty.face_joke(message, jokes['face']))
        boredom -= random.randint(5,30)
        #stim += 1
    elif sane_response and ("butt" in msg.lower()):
        jokes['butt'] +=1
        await client.send_message(message.channel, chatty.butt_joke(message, jokes['butt']))
        boredom -= random.randint(5,20)
        #stim += 1
    elif sane_response and (client.user.mentioned_in(message)):
        await client.send_message(message.channel, chatty.mention(message, boredom))
        boredom -= random.randint(8,50)


async def random_chat(channel_in):
    #global stim
    global boredom
    global current_msg
    global last_msg

    await client.wait_until_ready()
    while not client.is_closed:
        channel = client.get_channel(channel_in)
        #await client.send_message(channel, "dev message: Stimulation: %d " % stim)

        # This is here to cause more interaction with slow chat rooms. if the last message hasn't changed since the last cycle, it ups
        # Marvins boredom.
        #await client.send_message(channel, "Dev Mode: %s" % current_msg)
        #await client.send_message(channel, "Dev Mode: %s" % last_msg)
        if current_msg == last_msg:
            boredom += random.randint(12,20)
            #await client.send_message(channel, "Dev Mode: the cycle must be broken")

        # this updates the last message to the current message, resetting the cycle.
        last_msg = current_msg   


        # this determines a basic floor that will leave the bot functional even in high chat environments
        floor = 10
        if boredom < floor:
            boredom = floor

        if (chatty.chat_logic(boredom)):
            await client.send_message(channel, chatty.initiate())
            boredom -= random.randint(5,40)

        #dev check
        #await client.send_message(channel, "Dev Mode: boredom: %d" % boredom)
        boredom += random.randint(10,30)
        await asyncio.sleep(random.randint(650,1540))

        # this was an old path for the chat logic, I've turned bordom into a positive rising integer that increases percentile
        #if (chatty.chat_logic(60) and (stim == 0)):
        #    await client.send_message(channel, chatty.initiate())
        #    stim += 2
        #elif (chatty.chat_logic(30) and (stim == 1 )):
        #    await client.send_message(channel, chatty.initiate())
        #    stim += 2
        #elif (chatty.chat_logic(20) and (stim == 2 )):
        #    await client.send_message(channel, chatty.initiate())
        #    stim += 2
        #elif (chatty.chat_logic(10) and (stim >= 3 )):
        #    await client.send_message(channel, chatty.initiate())
        #    stim += 2
            
        #if (stim > 0):
        #    stim -= 1
        #await asyncio.sleep(random.randint(40,80))
        





print('------------')
# End Setup
# This is where the Actual login happens?
if (dev_mode):
    client.loop.create_task(random_chat(loadconf.__dev_channel__))
    client.run(loadconf.__dev_token__)
else:
    client.loop.create_task(random_chat(loadconf.__channel__))
    client.run(loadconf.__token__)
    
