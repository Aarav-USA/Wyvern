import discord
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(help='ban a user')
    async def ban(self, ctx: commands.Context, user: discord.User) -> None:
        await ctx.send('Not Implemented')
        raise NotImplementedError()

    @commands.command(help='kick a user')
    async def kick(self, ctx: commands.Context, user: discord.User) -> None:
        await ctx.send('Not Implemented')
        raise NotImplementedError()

    @commands.command(help='mute a user')
    async def mute(self, ctx: commands.Context, user: discord.User) -> None:
        await ctx.send('Not Implemented')
        raise NotImplementedError()

def setup(bot: commands.Bot) -> None:
    print('Loading moderation extension...')
    bot.add_cog(Moderation(bot))
