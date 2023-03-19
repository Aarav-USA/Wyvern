#!/usr/bin/env python3

import discord
from discord.ext import commands

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

bot_prefixes = config['DEFAULT']['DefaultPrefixes'].split()
if config['DEFAULT'].getboolean('AllowMentionPrefix'):
    bot = commands.Bot(discord.ext.commands.when_mentioned_or(*bot_prefixes),
        intents=discord.Intents.all(), case_insensitive=True)
else:
    bot = commands.Bot(bot_prefixes,
        intents=discord.Intents.all(), case_insensitive=True)

# Mypy doesn't understand an implicit setattr.
setattr(bot, 'config', config)

bot.load_extension('info')
bot.load_extension('moderation')
bot.load_extension('ticket.ticket')
bot.load_extension('reaction')
bot.load_extension('suicide_prevention.suicide_prevention')
bot.load_extension('fun')
bot.load_extension('welcome')

@bot.event
async def on_ready() -> None:
    print("The bot is now online")
    # Setting 'Watching status
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name='for @Wyvern'))
    print("----------------------------------------------")

if __name__ == '__main__':
    bot_token = config['auth']['BotToken']
    if bot_token == 'REDACTED':
        print('Please add your bot token to the auth section in config.ini')
    else:
        bot.run(bot_token)
