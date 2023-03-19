from __future__ import annotations

import discord
import json
from typing import Optional
from discord.ext import commands

JSON_FILE = 'reactions.json'

class ReactRole(commands.Cog):

    def __init__(self, bot: commands.Bot, json_file: str) -> None:
        self.bot = bot
        self.json_file = json_file

    # Saves a react role to the JSON file; does not catch exceptions.
    async def __save_role_record(self, emoji: str, role: discord.Role,
            msg: discord.Message) -> None:
        role_record = {
            'role_name' : role.name,
            'role_id' : role.id,
            'emoji' : emoji,
            'message_id' : msg.id
        }

        with open(self.json_file, 'r') as file_handle:
            react_roles = json.load(file_handle)
        react_roles.append(role_record)

        with open(self.json_file, 'w') as file_handle:
            json.dump(react_roles, file_handle, indent=4)
            
    # Get the reaction role id corresponding to the given emoji, or None.
    async def __role_id_from_record(self, emoji: str,
            message_id: int) -> Optional[int]:
        with open(self.json_file, 'r') as file_handle:
            react_roles: list[dict[str, str]] = json.load(file_handle)

        for role_record in react_roles:
            if role_record['emoji'] == emoji \
                    and role_record['message_id'] == message_id:
                return int(role_record['role_id'])
        return None

    @commands.command()
    async def reactrole(self, ctx: commands.Context, emoji: str,
            role: discord.Role, *, message: str) -> None:
        emb = discord.Embed(description=message)
        msg = await ctx.channel.send(embed=emb)
        await msg.add_reaction(emoji)
        await self.__save_role_record(emoji, role, msg)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self,
            payload: discord.RawReactionActionEvent) -> None:
        emoji, message_id = payload.emoji.name, payload.message_id
        # Mypy thinks these types are optional
        if emoji is None or payload.guild_id is None:
            return
        role_id = await self.__role_id_from_record(emoji, message_id)
        if role_id is None:
            return

        guild = self.bot.get_guild(payload.guild_id)
        if guild is None:
            print('Failed to get guild.')
            return

        role = discord.utils.get(guild.roles,
            id=role_id)
        if role is None:
            print('Failed to get role.')
            return

        member = guild.get_member(payload.user_id)
        if member is None:
            print('Failed to get member.')
            return

        await member.add_roles(role)

def setup(bot: commands.Bot) -> None:
    print('Loading reactrole extension...')
    bot.add_cog(ReactRole(bot, JSON_FILE))
