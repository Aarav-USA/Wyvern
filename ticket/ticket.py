from typing import Optional
import re

import discord
from discord.ext import commands

SOURCE_LINK: str = 'https://github.com/XxMidasTouchxX/HoneyComb.git'
SUPPORT_SERVER: str = 'https://discord.gg/Q2CTzHyk'

# Returns the first channel if one is found in content, or None.
def extract_channel(content: str) -> Optional[str]:
    regex: str = '<#[0-9]{18}>'
    matched = re.findall(regex, content)
    if matched:
        return str(matched[0])
    return None 

class TicketEmbed(discord.Embed):

    def __init__(self, *args: int, **kargs: str) -> None:
        super().__init__(*args, **kargs)
        # gold
        self.colour = 0xFFD700
        

class TicketManager(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        # Channel the bot is set up in
        self.setup_channel: Optional[discord.Channel]
        # User currently in setup process
        self.__setup_user: Optional[discord.User] = None

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
        await self.setup_channel.send('Am I spamming?')

    @commands.command(help='Set setup channel', aliases=['s'])
    async def setup(self, ctx: commands.Context) -> None:
        if self.__setup_user is not None:
            await ctx.send('A setup is already in progress.')
        else:
            self.__setup_user = ctx.author
            await ctx.send('Which channel would you like me to set up in?')

    @commands.command(help='Link source code')
    async def source(self, ctx: commands.Context) -> None:
        embed = TicketEmbed(
            title='Check out my source code!',
            url=SOURCE_LINK
        )
        await ctx.send(embed=embed)

    @commands.command(help='Link support server', aliases=['su'])
    async def support(self, ctx: commands.Context):
        await ctx.send(SUPPORT_SERVER)

    @commands.Cog.listener()
    async def on_message(self, msg: discord.Message) -> None:
        if msg.author == self.__setup_user:
            channel_id = extract_channel(msg.content)
            if channel_id is not None:
               channel = self.bot.get_channel(channel_id)
                self.setup_channel = channel
                await msg.channel.send(f'Setting up in {channel_id}...')
                await self.__send_setup_message()
                self.__setup_user = None
                await msg.channel.send('Setup complete.')

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context,
            error: commands.CommandError) -> None:
        await ctx.send(str(error))
        

def setup(bot):
    print('Loading ticket manager extension...')
    bot.add_cog(TicketManager(bot))
