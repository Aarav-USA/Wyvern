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
    # Setting 'Watching' status
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name='for @Wyvern'))
    print(name + "Successfully connected to Discord.\n" + "-" * 37)

async def main():
    try:
        await bot.start(config['AUTH']['BotToken'])
    except KeyboardInterrupt:
        print(name + "Keyboard interrupt, closing application.")
    except Exception as e:
        print(name + f"Error while running: '{e}'")
    finally:
        async with bot:
            await bot.logout()

if config['AUTH'].get('BotToken') == "REDACTED":
    raise Exception(name + "Configure your bot token in 'config.ini', and try again.")
else:
    asyncio.run(main())
