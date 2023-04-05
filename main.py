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
    # 'auditlog',
    # 'automod',
    # 'bankofdiscord',
    # 'boostreward',
    # 'bulletin',
    # 'captcha',
    # 'courier',
    # 'crosspost',
    # 'customcmd',
    # 'discorddefender',
    # 'embed',
    # 'emoji',
    # 'form',
    # 'fun',
    # 'giveaway',
    # 'help',
    # 'information',
    # 'invitemonitor',
    # 'joinleave',
    # 'kingofword',
    # 'level',
    # 'moderation',
    # 'music',
    # 'profile',
    # 'reactionrole',
    # 'roomie',
    # 'serverstat',
    # 'utility',
    # 'vault',
    # 'voicemail',
    ]

name = bot.user.name + ":"
async def load_all_cogs():
    for extension in cogs:
        try:
            await bot.load_extension("cogs." + extension)
            print(f'{name} Loaded {extension} cog.')
        except Exception as e:
            print(f'{name} Error loading {extension} cog: {str(e)}')

@bot.event
async def on_ready() -> None:
    print(f"{name} has successfully connected to ")
    # Setting 'Watching' status
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name=f'for @{name}'))
    print("-" * 47)

async def main():
    try:
        await bot.start(config['auth']['BotToken'])
    except KeyboardInterrupt:
        print(f"{name} Keyboard interrupt, disconnecting...")
    except Exception as e:
        print(f"{name} Error while running: '{e}'")
    finally:
        async with bot:
            await bot.logout()

asyncio.run(main())