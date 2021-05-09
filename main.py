#!/usr/bin/env python3

import discord
from discord.ext import commands

BOT_PREFIX: str = 'hc!'

bot: commands.Bot = commands.Bot(BOT_PREFIX, intents=discord.Intents.all())
bot.load_extension('ticket.ticket')
bot.load_extension('reaction')

@bot.event
async def on_ready() -> None:
    print("The bot is now online")
    print("----------------------------------------------")

if __name__ == '__main__':

    with open('token.txt', 'r') as f:
        token:str = f.readline().strip()

    bot.run(token)
