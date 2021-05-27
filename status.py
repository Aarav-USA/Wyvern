import discord
from discord.ext import commands
@client.event
async def on_ready():
await client.change_presence(status=discord.Status.idle, activity=discord. Game('for @HoneyComb'))
print('Bot is ready.')
