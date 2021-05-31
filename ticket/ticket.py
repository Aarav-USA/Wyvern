import time
from typing import Any, Optional, Union

import discord
from discord.ext import commands

class TicketManager(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        # Channel the bot is set up in
        self.setup_channel: Optional[discord.TextChannel] = None
        # User currently in setup process
        self.__setup_user: Optional[Union[discord.User, discord.Member]] = None

    @commands.command(help='Cancel setup', aliases=['c'])
    async def cancel(self, ctx: commands.Context) -> None:
        if self.__setup_user is not None:
            self.__setup_user = None
            await ctx.send('Canceled.')
        else:
            await ctx.send('No setup is in progress.')

    async def __send_setup_message(self) -> None:
        if self.setup_channel is None:
            return
        await self.setup_channel.send('Ticket bot setup.')

    @commands.command(help='Set setup channel', aliases=['s'])
    async def setup(self, ctx: commands.Context) -> None:
        if self.__setup_user is not None:
            await ctx.send('A setup is already in progress.')
        else:
            self.__setup_user = ctx.author
            await ctx.send('Which channel would you like me to set up in?')

    @commands.Cog.listener()
    async def on_message(self, msg: discord.Message) -> None:
        if msg.author == self.__setup_user:
            if len(msg.channel_mentions) > 0:
                channel = msg.channel_mentions[0]
            else:
                return

            if not isinstance(channel, discord.TextChannel):
                await msg.channel.send('That isn\'t a text channel!')
                return
            self.setup_channel = channel
            await msg.channel.send(f'Setting up in {channel}...')
            await self.__send_setup_message()
            self.__setup_user = None
            await msg.channel.send('Setup complete.')

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context,
            error: commands.CommandError) -> None:
        await ctx.send(str(error))
        

def setup(bot: commands.Bot) -> None:
    print('Loading ticket manager extension...')
    bot.add_cog(TicketManager(bot))
