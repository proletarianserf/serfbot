#This is a python based bot to do RPG things in discord
import discord
from serfbot_commands import on_command
from serfbot_roller import rolldice
#Load discord token from file:
token = open("token.dat","r").read()
#specify which starting charecter should be used for bot commands
botkey = "~"
client = discord.Client()

#Event Listener
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
#Message Handler
@client.event
async def on_message(message):
    #Import message into a list:
    current_message = "a string"
    #Do nothing if message is from self
    if message.author == client.user:
        return
    #For now we will leave the rolling function as is, but we will add another check to look for other bot commands
    if message.content.startswith(botkey):
        #await message.channel.send(f"bot command detected")
        await on_command(message, botkey)
        return
    if message.content.startswith('/roll'):
        await rolldice(message)
        return



#Run the bot
client.run(token)
