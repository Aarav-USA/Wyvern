#!/usr/bin/env python3

import discord
from discord.ext import commands

import configparser
import asyncio

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

cogs = [
    # 'afk',
    # 'altraider',
    # 'auditlog',
    # 'automod',
    # 'nitroperk',
    # 'bulletin',
    # 'captcha',
    # 'channels',
    # 'courier',
    # 'customcmd',
    # 'embed',
    # 'emoji',
    # 'entertainment',
    # 'form',
    # 'fun',
    # 'giveaway',
    # 'help',
    # 'information',
    # 'invitetrack',
    # 'level',
    # 'moneygame',
    # 'music',
    # 'platformalert',
    # 'profile',
    # 'reaction',
    # 'reactionrole',
    # 'serverlayout',
    'serverstat',
    # 'tempchannel',
    # 'utility',
    # 'voicemail',
    # 'welcomegoodbye',
    # 'wordrace'
    ]

name = 'Wyvern: '
async def load_all_cogs():
    for extension in cogs:
        try:
            await bot.load_extension("cogs." + extension)
            print(name + f'Loaded {extension} cog.')
        except Exception as e:
            print(name + f'Error loading {extension} cog: {str(e)}')

@bot.event
async def on_ready() -> None:
    print("The bot is now online")
    # Setting 'Watching' status
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name='for @Wyvern'))
    print("-" * 47)

async def main():
    try:
        await bot.start(config['auth']['BotToken'])
    except KeyboardInterrupt:
        print(name + "Keyboard interrupt, closing application.")
    except Exception as e:
        print(name + f"Error while running: '{e}'")
    finally:
        async with bot:
            await bot.logout()

asyncio.run(main())