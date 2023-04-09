#!/usr/bin/env python3

import discord
from discord.ext import commands

import configparser
import asyncio

config = configparser.ConfigParser()
config.read('config.ini')

# prefix required for bot to initialize
command_prefix = commands.when_mentioned

if config['AUTH'].get('AppId') == "REDACTED":
    raise Exception("Configure your application ID in 'config.ini', try again.")
else:
    app_id = config['INFO'].get('AppId')
    bot = commands.Bot(command_prefix=command_prefix,
        intents=discord.Intents.all(), 
        application_id=app_id)

# mypy doesn't understand an implicit setattr
setattr(bot, 'config', config)

cogs = [
    'utility.help',
    'moderation.moderation',
]

botname = config['INFO'].get('BotName')
async def load_all_cogs():
    for extension in cogs:
        try:
            await bot.load_extension("cogs." + extension)
            print(f'{botname}: Loaded {extension} cog.')
        except Exception as error:
            print(f'{botname}: Error loading {extension} cog: {error}')
    await bot.tree.sync()
    print(f"{botname}: Successfully synced slash commands.")

@bot.event
async def on_ready() -> None:
    # set watching status
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name=f'for @{botname}'))
    print(f"{botname}: Successfully connected to Discord.\n" + "-" * 37)
    await load_all_cogs()

async def main():
    if config['AUTH'].get('BotToken') == "REDACTED":
        raise Exception("Configure your token in 'config.ini', try again.")
    else:
        try:
            await bot.start(config['AUTH']['BotToken'])
        except KeyboardInterrupt:
            print(f"{botname}: Keyboard interrupted, disconnecting.")
        except Exception as error:
            print(f"{botname}: Error while running: '{error}'")
        finally:
            async with bot:
                await bot.logout()

asyncio.run(main())