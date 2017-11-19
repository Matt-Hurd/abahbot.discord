import discord
import asyncio
import secrets

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author.id == 171328042763812864:
        await client.add_reaction(message, '🇸')
        await client.add_reaction(message, '🇱')
        await client.add_reaction(message, '🇺')
        await client.add_reaction(message, '🇹')

if __name__ == '__main__':
    client.run(secrets.CLIENT_TOKEN)
