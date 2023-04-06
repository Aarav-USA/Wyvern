#!/usr/bin/env python3

import discord
from discord.ext import commands

import configparser
import asyncio

config = configparser.ConfigParser()
config.read('config.ini')

if config['DEFAULT'].getboolean('AllowMentionPrefix'):
    command_prefix = command_prefix=commands.when_mentioned

else:
    command_prefix = None

bot = commands.Bot(command_prefix=command_prefix,
    intents=discord.Intents.all(),
    case_insensitive=True)

# mypy doesnt understand an implicit setattr
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

name = config['INFO'].getboolean('BotName') + ":"
async def load_all_cogs():
    for extension in cogs:
        try:
            await bot.load_extension("cogs." + extension)
            print(f'{name} Loaded {extension} cog.')
        except Exception as error:
            print(f'{name} Error loading {extension} cog: {error}')

@bot.event
async def on_ready() -> None:
    # Setting 'Watching' status
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name='for @Wyvern'))
    print(f"{name} Successfully connected to Discord.\n" + "-" * 37)

async def main():
    try:
        await bot.start(config['AUTH']['BotToken'])
    except KeyboardInterrupt:
        print(f"{name} Keyboard interrupted, disconnecting.")
    except Exception as error:
        print(f"{name} Error while running: '{error}'")
    finally:
        async with bot:
            await bot.logout()

if config['AUTH'].get('BotToken') == "REDACTED":
    raise Exception(f"{name} Configure your token in 'config.ini', try again.")
else:
    asyncio.run(main())
