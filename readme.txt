The purpose of this project is to provide a basic framework for running a discord bot that rolls dice and
helps you manage your RPG played over discord. 

To run this bot you must have python3 installed and a discord bot account created.
The bot relies on discord.py which is published under the MIT license.

Setup instructions:
The following instructions are for Linux. I may add scripts and instructions for windows at some point
For now if you want to run on Windows you'll have to reverse engineer the linux scripts

First step is to setup a bot account with discord. You can use the guide at the following link:
	https://discordpy.readthedocs.io/en/latest/discord.html
Once you have your bot account created save your bot token in a safe place, this is your bot's login credentials.
	DO NOT SHARE YOUR BOT TOKEN WITH ANYONE
	DO NOT RUN THIS BOT AS ROOT OR ADMINISTRATOR, THAT WOULD BE VERY UNWISE
Next, clone the git repo or unzip to the folder within which you want the bot to reside
Ensure you have python3 package installed and updated to the latest version
From within the cloned folder run ./configure
	When prompted provide the script your bot token from the second step
You should now have a python virtual environment with all of the bot's dependencies in the current folder.

To start the bot
	./start
To stop the bot
	./stop
The bot's pid will be stored in serfbot.pid

export.sh is provided as a utility to export just the files required for others to setup the bot on their system.
It will export the files listed in manifest.txt. You may add or remove files from that list as you require.





