import discord
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

#bans a user with a reason
@commands.command()
@commands.has_any_role('Administrators','Moderators,','Mods','Admins','Admin','Mod')
async def ban(self, ctx: commands.Context, user: discord.User, reason: str) -> None:
    if member is None or member == ctx.message.author:
        await ctx.channel.send('You cannot ban yourself')
        return
    if reason is None:
        reason = 'We have decided you ban you out of our server!'
    message = f'You have been banned from {ctx.guild.name} for {reason}'
    await member.send(message)
    # await ctx.guild.ban(member, reason=reason)
    await ctx.channel.send(f'{member} is banned!')

    @commands.command(help='Kicks a user')
    async def kick(self, ctx: commands.Context, user: discord.User) -> None:
        await ctx.send('Not Implemented')
        raise NotImplementedError()

    @commands.command(help='Mutes a user')
    async def mute(self, ctx: commands.Context, user: discord.User) -> None:
        await ctx.send('Not Implemented')
        raise NotImplementedError()

def setup(bot: commands.Bot) -> None:
    print('Loading moderation extension...')
    bot.add_cog(Moderation(bot))
