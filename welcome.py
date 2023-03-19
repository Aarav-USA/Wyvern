import discord
from discord.ext import commands

class WelcomeGoodbye(commands.Cog):

    def __init__(self, wyvern):
        self.wyvern = wyvern

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # Set up welcome message and role to give
        welcome_channel = self.wyvern.get_channel(123456789012345678)
        welcome_message = f"Welcome to the server, {member.display_name}! Please read the rules and enjoy your stay."
        role_to_give = member.guild.get_role(123456789012345678)

        try:
            await welcome_channel.send(welcome_message)
            await member.add_roles(role_to_give)
        except discord.Forbidden:
            error_message = f"Wyvern does not have permission to send messages or give roles in {welcome_channel.mention}."
            await self.wyvern.owner.send(error_message)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        # Set up goodbye message
        goodbye_channel = self.wyvern.get_channel(123456789012345678)
        goodbye_message = f"{member.name} has left the server. Goodbye!"

        try:
            await goodbye_channel.send(goodbye_message)
        except discord.Forbidden:
            error_message = f"Wyvern does not have permission to send messages in {goodbye_channel.mention}."
            await self.wyvern.owner.send(error_message)

    @commands.command()
    async def wyvernwelcome(self, ctx):
        welcome_channel = ctx.channel
        welcome_message = f"Welcome to the server, {ctx.author.display_name}! Please read the rules and enjoy your stay."
        role_to_give = ctx.guild.get_role(123456789012345678)

        try:
            await welcome_channel.send(welcome_message)
            await ctx.author.add_roles(role_to_give)
        except discord.Forbidden:
            error_message = "Wyvern does not have permission to send messages or give roles in this channel."
            await ctx.author.send(error_message)

def setup(wyvern):
    wyvern.add_cog(WelcomeGoodbye(wyvern))
