import discord
async def on_command(message, botkey):
    #Convert the command to lower case
    command = message.content
    command = command.lower()
    #Strip out botkey from the command
    #
    if 'you roll dice' in command:
        with open('./res/images/passbutter.gif', 'rb') as fp:
            await message.channel.send(file=discord.File(fp, 'ipassbutter.gif'))








#Stop this from being run at import
if __name__== "__main__":
    main()
