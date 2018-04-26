import discord
import asyncio
import random
import pickle
import os

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
 
	@client.event
	async def on_message(message):
		if message.content.upper().startswith('N!NIKO'):
			await client.send_message(message.channel, 'Yeah?')
		elif message.content.upper().startswith('N!PICK'):
			flip = random.choice(['Of course I would pick Crimped', 'Of course I would pick Indomie', 'Of course I would pick Myth', 'Of course I would pick Tuan', 'Of course I would pick fckboi', 'Of course I would pick Tuna', 'Of couse I would pick Scoot', 'Of course I would pick Creepy', 'Of course I would pick myself'])
			await client.send_message(message.channel, flip)
		elif message.content.startswith('n!skip'):
			await client.send_message(message.channel, 'Why skip ;-;')
		elif message.content.startswith('!pancake'):
			await client.send_message(message.channel,  ':3')
		elif message.content.startswith('!wakeup'):
			await client.send_message(message.channel, 'No Im going back to sleep')	
		elif message.content.startswith('!meow'):
			await client.send_message(message.channel, 'Meow :3')
		elif message.content.startswith('n!help'):
			await client.send_message(message.channel, '**COMMANDS** n!niko, n!pick, n!skip, !pancake, !wakeup, !meow, n!help, n!hi')
		elif message.content.upper().startswith('N!HI'):
			userID = message.author.id
			await client.send_message(message.channel, "Hi, <@%s>" % (userID))
		elif message.content.upper().startswith('N!QUOTE'):
			b = random.randint(0,51)

			a = open("quotes.txt", "r")
			for  x, line in enumerate(a):
				if x == b:
					await client.send_message(message.channel, line)
			a.close()

		
client.run('BOT_TOKEN')

