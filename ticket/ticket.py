import time
from typing import Any, Optional, Union

import discord
from discord.ext import commands

DEFAULT_CATEGORY = 'courier'

class TicketManager(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        # Channel the bot is set up in
        self.setup_channel: Optional[discord.TextChannel] = None
        self.__category: Optional[discord.CategoryChannel] = None
        # User currently in setup process
        self.__setup_user: Optional[Union[discord.User, discord.Member]] = None
        self.__setup_guild: Optional[discord.Guild] = None

    @commands.command(help='Set the ticket category')
    async def category(self, ctx:commands.Context, name: str) -> None:
        if ctx.guild is None:
            await ctx.send('This command can only be used from a guild!')
            return
        await self.set_category(ctx.guild, name, no_clobber=False)

    @commands.command(help='Cancel setup', aliases=['c'])
    async def cancel(self, ctx: commands.Context) -> None:
        if self.__setup_user is not None:
            self.__setup_user = None
            await ctx.send('Canceled.')
        else:
            await ctx.send('No setup is in progress.')

    async def set_category(self, guild: discord.Guild, name: str,
            no_clobber:bool = True) -> None:
        """Sets the category for ticket channels."""
        if no_clobber:
            for category in guild.categories:
                if category.name == name:
                    assert self.setup_channel is not None
                    await self.setup_channel.send(
                        'Could not set up category - ' \
                        f'Category {category} already exists. ' \
                        'Please remove the category or set ' \
                        'the category by hand with `category`'
                    )
                    return
        try:
            self.__category = await guild.create_category(name,
                reason="Created by Courier")
        except discord.Forbidden:
            assert self.setup_channel is not None
            await self.setup_channel.send(
                'Could not set up category - Missing channel permissions.')
            raise

    async def __setup(self) -> None:
        """Performs the setup procedure for the discord server."""
        if self.__category is None:
            assert self.__setup_guild is not None
            await self.set_category(self.__setup_guild, DEFAULT_CATEGORY)

    @commands.command(help='Set setup channel', aliases=['s'])
    async def setup(self, ctx: commands.Context) -> None:
        if self.__setup_user is not None:
            await ctx.send('A setup is already in progress.')
        else:
            self.__setup_user = ctx.author
            self.__setup_guild = ctx.guild
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
            await self.__setup()
            self.__setup_user = None
            self.__setup_guild = None
            await msg.channel.send('Setup complete.')

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context,
            error: commands.CommandError) -> None:
        await ctx.send(str(error))
        

def setup(bot: commands.Bot) -> None:
    print('Loading ticket manager extension...')
    bot.add_cog(TicketManager(bot))
