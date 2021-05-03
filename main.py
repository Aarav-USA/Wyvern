#!/usr/bin/env python3

from discord.ext import commands

BOT_PREFIX: str = 'hc!'

bot: commands.Bot = commands.Bot(BOT_PREFIX)
bot.load_extension('ticket/ticket')

if __name__ == '__main__':

    with open('token.txt', 'r') as f:
        token:str = f.readline().strip()

    bot.run(token)
