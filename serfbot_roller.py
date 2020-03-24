#This is the handler for rolling dice
from random import randrange


#Dice Rolling Function, rolls XdY and returns the username and results from each roll
#Input example /roll 2d20
async def rolldice(message):
        #If the user has a nick set for a server use that for their name, otherwise use Dicord User ID
        if message.author.nick != None:
            roller = message.author.nick
        else:
            roller = message.author
        try:
            dice = message.content.split('d')[0]
            dice = dice.split(' ')[1]
            sides = message.content.split('d')[1]
        except Exception as e:
            print(e)
            await message.channel.send(f"{roller},you provided an invalid roll format. Example: 1d20")
            return
        #We need to limit the number of dice and sides to prevent message limits/abuse
        if int(dice) > 25:
            await message.channel.send(f"{roller}, I don't have {dice} dice. I'm not some sort of mechanical dice camel")
            return
        if int(sides) > 100:
            await message.channel.send(f"{roller}, NO, that is far too many sides. Please do try to be reasonable")
            return
        if int(sides) < 1:
            await message.channel.send(f"{roller}, you must specify at least one side")
            return
        if int (dice) < 1:
            await message.channel.send(f"{roller}, you must roll at least 1 die")
            return


        #We need to add 1 to the number of sides because randrange is indexed strangely
        sides_indexed = int(sides)
        sides_indexed += 1
        #Now we need to roll the number of dice and store the results in an array
        rollcount = 0
        rollout = []
        while rollcount < int(dice):
            roll = randrange(1, sides_indexed)
            rollout.append(roll)
            rollcount += 1

        await message.channel.send(f"{roller} rolled {dice}d{sides}: {rollout}")


if __name__== "__main__":
        main()
