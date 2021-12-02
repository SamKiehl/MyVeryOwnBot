import discord
import os

client = discord.Client()

@client.event
async def on_ready(): # Happens when the bot goes online
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user: # Keeps the bot from responding to its own messages.
    return
  
  # Additional Bot behaviors can be added below!

  if message.content.startswith('ping!'):
    await message.channel.send('pong!')
  
  if message.content.startswith('!reverse '):
    await message.channel.send((message.content)[9 : len(message.content)][::-1])

client.run(os.getenv('TOKEN'))
