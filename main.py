#!/usr/bin/env python3

import discord
from discord.ext import commands

import configparser
import asyncio

config = configparser.ConfigParser()
config.read('config.ini')

bot_prefixes = config['DEFAULT']['DefaultPrefixes'].split()
intents = discord.Intents.all()

if config['DEFAULT'].getboolean('SlashCommands'):
    if config['DEFAULT'].getboolean('AllowMentionPrefix'):
        bot = commands.Bot(command_prefix=commands.when_mentioned,
            intents=intents)
    else:
        bot = commands.Bot(intents=intents)
else:
    if config['DEFAULT'].getboolean('AllowMentionPrefix'):
        bot = commands.Bot(discord.ext.commands.when_mentioned_or(*bot_prefixes),
        intents=discord.Intents.all(), case_insensitive=True)
    else:
        bot = commands.Bot(bot_prefixes,
            intents=intents, case_insensitive=True)

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
    print(name + "Successfully connected to Discord.\n" + "-" * 47)

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
