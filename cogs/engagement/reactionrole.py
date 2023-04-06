import discord
from discord.ext import commands

class ReactionRoles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.reaction_message_id = 1234567890 
        self.reaction_channel_id = 1234567890
        self.reaction_to_role = {
            "🎮": 1234567890,
            "🎵": 1234567890,
            "📺": 1234567890
        }

    @commands.Cog.listener()
    async def on_ready(self):
        self.reaction_channel = self.bot.get_channel(self.reaction_channel_id)
        self.reaction_message = await self.reaction_channel.fetch_message(self.reaction_message_id)
        for emoji in self.reaction_to_role.keys():
            await self.reaction_message.add_reaction(emoji)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == self.reaction_message_id and payload.channel_id == self.reaction_channel_id:
            guild = self.bot.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            role_id = self.reaction_to_role.get(str(payload.emoji))
            if role_id is not None:
                role = guild.get_role(role_id)
                await member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id == self.reaction_message_id and payload.channel_id == self.reaction_channel_id:
            guild = self.bot.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            role_id = self.reaction_to_role.get(str(payload.emoji))
            if role_id is not None:
                role = guild.get_role(role_id)
                await member.remove_roles(role)

def setup(bot):
    bot.add_cog(ReactionRoles(bot))
