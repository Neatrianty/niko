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
		if message.content.startswith('n!niko'):
			await client.send_message(message.channel, 'Yeah?')
		elif message.content.startswith('n!pick'):
			flip = random.choice(['Of course I would pick Crimped', 'Of course I would pick Indomie', 'Of course I would pick Myth', 'Of course I would pick Tuan', 'Of course I would pick Tuna', 'Of couse I would pick Scoot', 'Of course I would pick Creepy', 'Of course I would pick myself'])
			await client.send_message(message.channel, flip)
		elif message.content.startswith('n!skip'):
			await client.send_message(message.channel, 'Why skip ;-;')
		elif message.content.startswith('!pancake'):
			await client.send_message(message.channel, ':3')

client.run('NDE3NjU4NDAzNTg2OTY1NTA0.DXZtNA.Lg2MqT406fNDX2B_kIMQuIoT99A')
 
