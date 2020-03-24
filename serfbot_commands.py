async def on_command(message):
#    sender = message.author
    await message.channel.send(message.content)

if __name__== "__main__":
    main()
