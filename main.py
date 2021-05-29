#!/usr/bin/env python3

import discord
from discord.ext import commands

BOT_PREFIX = 'hc!'

bot= commands.Bot(discord.ext.commands.when_mentioned_or('hc!'),
    intents=discord.Intents.all())
bot.load_extension('info')
bot.load_extension('moderation')
bot.load_extension('ticket.ticket')
bot.load_extension('reaction')

@bot.event
async def on_ready() -> None:
    print("The bot is now online")
    # Setting 'Watching status
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name='for @HoneyComb'))
    print("----------------------------------------------")

if __name__ == '__main__':

    with open('token.txt', 'r') as f:
        token:str = f.readline().strip()

    bot.run(token)
