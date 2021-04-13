from typing import Tuple, Dict

import discord
from discord.ext import commands
SOURCE_LINK: str = 'https://github.com/XxMidasTouchxX/HoneyComb.git'
SUPPORT_SERVER: str = 'https://discord.gg/Q2CTzHyk'

class TicketEmbed(discord.Embed):

    def __init__(self, *args: int, **kargs: str) -> None:
        super().__init__(*args, **kargs)
        # gold
        self.colour = 0xFFD700
        

class TicketManager(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(help = 'Link source code', aliases = ['s'])
    async def source(self, ctx: commands.Context) -> None:
        embed = TicketEmbed(
            title = 'Check out my source code!',
            url = SOURCE_LINK
        )
        await ctx.send(embed=embed)

    @commands.command(help = 'Link support server', aliases = ['su'])
    async def support(self, ctx: commands.Context):
        await ctx.send(SUPPORT_SERVER)

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context,
            error: commands.CommandError) -> None:
        await ctx.send(str(error))
        

def setup(bot):
    print('Loading ticket manager extension...')
    bot.add_cog(TicketManager(bot))
