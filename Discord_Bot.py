'''
This is the source code for the 'titled bot' (aka The Counter) made by 01001010 01010011#8677
'''

import discord
import json
import datetime

client = discord.Client()
activity = discord.Game(name="Jude is watching...")
log = {}

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.online, activity=activity)

@client.event
async def on_message(message):
    #Ignores bot messages and focuses on client messages
    if message.author == client.user:
        return

    #Echo message if it starts with "$"
    if message.content.startswith('$'):
        await message.channel.send(message.content.replace('$',' ', 1))
    #Exeption handler for the counter
    else:
        try:
            #Casts int into string and returns it as a formateed string
            await message.channel.send(str("{:,}".format(int(message.content.replace(',', '')) + 1)))
        except:
            #Does nothing if exeption occured
            pass
    #Prints messages in console >:]
    print(message.author, ": ", message.content)
    if str(message.author) in log:
        log[str(message.author)].append({str(datetime.datetime.now()): str(message.content)})
    else:
        log[str(message.author)] = []
    with open('Log.json', 'w') as logoutput:
        json.dump(log, logoutput)

with open('config.json','r') as cf:
    config = json.load(cf)

#Logs into discord with token
client.run(config['token'])
