import discord
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    #bans a user with a reason
    @commands.command()
    @commands.has_any_role('Administrators','Moderators,','Mods','Admins','Admin','Mod')
    async def ban(self, ctx: commands.Context, user: discord.User, *,
            reason: str) -> None:
        if user is None or user == ctx.message.author:
            await ctx.channel.send('You cannot ban yourself!')
            return
        if reason is None:
            reason = 'We have decided you ban you out of our server!'
        if ctx.guild is None:
            await ctx.send('You can only use this command in a server.')
            return
        message = f'You have been banned from {ctx.guild.name} Reason: {reason}'
        await user.send(message)
        await ctx.guild.ban(user, reason=reason)
        await ctx.channel.send(f'{user} is banned!')

    #kicks a user with a reason
    @commands.command()
    @commands.has_any_role('Administrators','Moderators,','Mods','Admins','Admin','Mod')
    async def kick(self, ctx: commands.Context, user: discord.User, reason: str) -> None:
        if user is None or user == ctx.message.author:
            await ctx.channel.send('You cannot kick yourself!')
            return
        if reason is None:
            reason = 'We have decided to kick you out of our server!'
        if ctx.guild is None:
            await ctx.send('You can only use this command in a server.')
            return
        message = f'You have been kicked from {ctx.guild.name} Reason: {reason}'
        await user.send(message)
        await ctx.guild.kick(user, reason=reason)
        await ctx.channel.send(f'{user} has been kicked!')

    @commands.command(help='Mutes a user')
    async def mute(self, ctx: commands.Context, user: discord.User) -> None:
        await ctx.send('Not Implemented')
        raise NotImplementedError()

def setup(bot: commands.Bot) -> None:
    print('Loading moderation extension...')
    bot.add_cog(Moderation(bot))