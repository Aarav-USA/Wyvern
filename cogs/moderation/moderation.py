import discord
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice

class moderation(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    # bans a user with a reason
    @commands.has_permissions(ban_members=True)
    @app_commands.command(name="ban", description="Ban a member from your guild")
    @app_commands.describe(
        member = "Member to ban",
        reason = "Reason for ban",
        # duration = "Amount of time to ban member",
        # preserve = "Preserve member messages",
        # appeal = "Appeal the ban",
    )

    # @app_commands.choices(preserve = [
    #     Choice(name = "True", value = True),
    #     Choice(name = "False", value = False)
    # ])
    # @app_commands.choices(appeal = [
    #     Choice(name = "True", value = True),
    #     Choice(name = "False", value = False)
    # ])
    async def ban(self, ctx: commands.Context, member: discord.Member, *,
            reason: str = f"The moderators have decided to ban you from this guild.") -> None:
        if member is None or member == ctx.author:
            await ctx.send('You cannot ban yourself!')
            return
        message = f'You have been banned from {ctx.guild.name} Reason: {reason}'
        await member.send(message)
        await ctx.guild.ban(member, reason=reason)
        await ctx.send(f'{member} is banned!')

#     # kicks a user with a reason
#     @commands.command()
#     @commands.has_any_role('Administrators','Moderators,','Mods','Admins','Admin','Mod')
#     async def kick(self, ctx: commands.Context, user: discord.User, *,
#             reason: str) -> None:
#         if user is None or user == ctx.message.author:
#             await ctx.channel.send('You cannot kick yourself!')
#             return
#         if reason is None:
#             reason = 'We have decided to kick you out of our server!'
#         if ctx.guild is None:
#             await ctx.send('You can only use this command in a server.')
#             return
#         message = f'You have been kicked from {ctx.guild.name} Reason: {reason}'
#         await user.send(message)
#         await ctx.guild.kick(user, reason=reason)
#         await ctx.channel.send(f'{user} has been kicked!')

#     @commands.command(help='Mutes a user')
#     async def mute(self, ctx: commands.Context, user: discord.User) -> None:
#         await ctx.send('Not Implemented')
#         raise NotImplementedError()

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(moderation(bot))
