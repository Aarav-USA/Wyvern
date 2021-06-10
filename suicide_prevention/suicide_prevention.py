import discord
from discord.ext import commands

import json

class SuicidePrevention(commands.Cog):
    
        def __init__(self, bot: commands.Bot) -> None:
            self.bot = bot
            
        @commands.Cog.listener()
        async def on_message(self, msg: discord.Message) -> None:
            with open('suicide.json', 'r') as f:
                blacklist = json.load(f)
            for phrase in blacklist:
                if phrase in msg.content:
                    await msg.channel.send('Nu uh, that is not allowed.')
                    if isinstance(msg.author, discord.Member):
                        await msg.author.kick()


def setup(bot: commands.Bot) -> None:
    print('Loading suicide prevention extension...')
    bot.add_cog(SuicidePrevention(bot))