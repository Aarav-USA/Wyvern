import discord
from discord.ext import commands

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# change to base 16
color = int(config['INFO'].get('ThemeColor'), 16)
botname = config['INFO'].get('BotName')
icon = config['INFO'].get('BotIcon')

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if self.bot.user.mentioned_in(message):
            embed = discord.Embed(
                title="Prefixes Not Supported",
                description=f"`@{botname}` is enabled in this server as a backup command. Type `/` to use a slash command.",
                color=color
            )
            embed.set_footer(text=f"Bot Ping: {self.bot.latency*1000:.0f}ms")
            embed.set_author(name=f"{botname}", icon_url=f"{icon}")
            await message.reply(embed=embed, mention_author=False)

async def setup(bot):
    await bot.add_cog(help(bot))

