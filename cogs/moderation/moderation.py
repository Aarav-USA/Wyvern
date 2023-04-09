import discord
from discord import app_commands
from discord.ext import commands

from datetime import timedelta
import re

import configparser

config = configparser.ConfigParser()
config.read('config.ini')
color = int(config['INFO'].get('ThemeColor'), 16)
botname = config['INFO'].get('BotName')
icon = config['INFO'].get('BotIcon')

def embed(title, description, color):
    embed = discord.Embed(
    title=title,
    description=description,
    color=color
    )
    embed.set_author(name=f"{botname}", icon_url=f"{icon}")

class moderation(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    
    # ban a member
    @commands.has_permissions(ban_members=True)
    @commands.has_permissions(administrator=True)
    @app_commands.command(name='ban', description='Ban a member')
    async def ban_member(ctx, slash: discord.Interaction, member: discord.Member, *, reason: str = 'Moderators have decided to ban you from this guild'):
        try:
            await member.ban(reason=reason)
            await slash.response.send_message(f'{member.mention} has been banned from the guild for "{reason}"')
        except:
            await slash.response.send_message(f'{botname} does not have permission to ban {member.mention} from the guild.')

    # kick a member
    @commands.has_permissions(kick_members=True)
    @commands.has_permissions(administrator=True)
    @app_commands.command(name='kick', description='Kick a member')
    async def kick_member(ctx, slash: discord.Interaction, member: discord.Member, *, reason: str = 'Moderators have decided to kick you from this guild'):
        try:
            await member.kick(reason=reason)
            await slash.response.send_message(f'{member.mention} has been kicked from the guild for "{reason}"')
        except:
            await slash.response.send_message(f'{botname} does not have permission to kick {member.mention} from the guild.')
    
    # mute a member
    @commands.has_permissions(moderate_members=True)
    @commands.has_permissions(administrator=True)
    @app_commands.command(name='mute', description='Mute a member')
    async def mute_member(ctx, slash: discord.Interaction, member: discord.Member, *, time: str = '1d', reason: str = 'Moderators have decided to mute you in this guild'):
        if 'd' in time or 'D' in time:
            try:
                time = int(re.sub(r"[^0-9]", "", time))
                delta = timedelta(days=time)
            except ValueError:
                await slash.response.send_message(f'You need to specify the timelimit as ex: 5m, 5h, or 5d')
                return
        
        elif 'h' in time or 'H' in time:
            try:
                time = int(re.sub(r"[^0-9]", "", time))
                delta = timedelta(hours=time)
            except ValueError:
                await slash.response.send_message(f'You need to specify the timelimit as ex: 5m, 5h, or 5d')
                return
        
        elif 'm' in time or 'M' in time:
            try:
                time = int(re.sub(r"[^0-9]", "", time))
                delta = timedelta(minutes=time)
            except ValueError:
                await slash.response.send_message(f'You need to specify the timelimit as ex: 5m, 5h, or 5d')
                return
        
        elif time.isdigit():
            if time <= 59:
                time = int(time)
                delta = timedelta(minutes=time)
            elif time >= 60:
                time = int(time)
                delta = timedelta(hours=time)
        
        if delta > timedelta(days = 28):
            delta = timedelta(days = 28)
            mute_response = " A mute cannot be longer than 28 days, the mute was still set to the maximnum."
        else:
            mute_response = ""

        try:
            await member.timeout(delta, reason=reason)
            await slash.response.send_message(f'{member.mention} has been muted in the server for "{reason}, until {delta}".{mute_response}')  
        except:
            await slash.response.send_message(f'{botname} does not have permissions to mute {member.mention}.')

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(moderation(bot))
