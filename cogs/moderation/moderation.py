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

class moderation(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    # ban a member
    @commands.has_permissions(ban_members=True)
    @commands.has_permissions(administrator=True)
    @app_commands.command(name='ban', description='Ban a member')
    async def ban_member(ctx, slash: discord.Interaction, member: discord.Member, *, 
                         reason: str = 'The moderators have decided to ban you from this server.'):
        try:
            embed = discord.Embed(
                title="Successfully Banned Member",
                description=f'{member.mention} has been banned from the server.',
                color=color
                )
            embed.add_field(name = "Reason: ", value = f'"{reason}"', inline=True)
            embed.set_author(name=f"{botname}", icon_url=f"{icon}")
            await member.ban(reason=reason)
            await slash.response.send_message(embed=embed)
        except:
            embed = discord.Embed(
            title="Failed Banning Member",
            description=f'{botname} does not have permission to ban {member.mention} from the server.',
            color=color
                )
            embed.set_author(name=f"{botname}", icon_url=f"{icon}")
            await slash.response.send_message(embed=embed, ephemeral=True)

    # unban a member
    # @commands.has_permissions(ban_members=True)
    # @commands.has_permissions(administrator=True)
    # @app_commands.command(name='unban', description='Unban a member')
    # async def unban_member(ctx, slash: discord.Interaction, member: discord.Member, *, 
    #                      reason: str = 'The moderators have decided to unban you from this server.'):
    #     try:
    #         await member.unban(reason=reason)
    #         await slash.response.send_message(f'{member.mention} has been unbanned from the server for "{reason}"')
    #     except:
    #         await slash.response.send_message(f'{botname} does not have permission to unban {member.mention} from the server.')

    # kick a member
    @commands.has_permissions(kick_members=True)
    @commands.has_permissions(administrator=True)
    @app_commands.command(name='kick', description='Kick a member')
    async def kick_member(ctx, slash: discord.Interaction, member: discord.Member, *, 
                          reason: str = 'The moderators have decided to kick you from this server.'):
        try:
            embed = discord.Embed(
                title="Successfully Kicked Member",
                description=f'{member.mention} has been kicked from the server.',
                color=color
                )
            embed.add_field(name = "Reason: ", value = f'"{reason}"', inline=True)
            embed.set_author(name=f"{botname}", icon_url=f"{icon}")          
            await member.kick(reason=reason)
            await slash.response.send_message(embed=embed, ephemeral=True)
        except:
            embed = discord.Embed(
            title="Failed Kicking Member",
            description=f'{botname} does not have permission to kick {member.mention} from the server.',
            color=color
                )
            embed.set_author(name=f"{botname}", icon_url=f"{icon}")
            await slash.response.send_message(embed=embed, ephemeral=True)

            await slash.response.send_message(f'{botname} does not have permissions to mute {member.mention}.')

    # mute a member
    @commands.has_permissions(moderate_members=True)
    @commands.has_permissions(administrator=True)
    @app_commands.command(name='mute', description='Mute a member')
    async def mute_member(ctx, slash: discord.Interaction, member: discord.Member, *, time: str = '', reason: str = 'The moderators have decided to mute you in the server.'):
        if time == '':
            try:
                mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
            except:
                mute_role = await ctx.guild.create_role(name="Muted")
                for channel in ctx.guild.channels:
                    await channel.set_permissions(mute_role, speak=False, send_messages=False)

            await member.add_roles(mute_role, reason=reason)
            embed = discord.Embed(
                title="Successfully Muted Member",
                description=f'{member.mention} has been muted in the server indefinitely.',
                color=color
            )
            embed.add_field(name = "Reason: ", value = f'"{reason}"', inline=True)
            embed.set_author(name=f"{botname}", icon_url=f"{icon}")
            await slash.response.send_message(embed=embed)
        else:    
            if 'd' in time or 'D' in time:
                try:
                    time = int(re.sub(r"[^0-9]", "", time))
                    delta = timedelta(days=time)
                    if time == 1:
                        mute_unit = "day"
                    else:
                        mute_unit = "days"
                except ValueError:
                    embed = discord.Embed(
                    title="Failed Muting Member",
                    description=f'You need to specify the timelimit as ex: 5m, 5h, or 5d',
                    color=color
                        )
                    embed.set_author(name=f"{botname}", icon_url=f"{icon}")
                    await slash.response.send_message(embed=embed, ephemeral=True)
                    return
            
            elif 'h' in time or 'H' in time:
                try:
                    time = int(re.sub(r"[^0-9]", "", time))
                    delta = timedelta(hours=time)
                    if time == 1:
                        mute_unit = "hour"
                    else:
                        mute_unit = "hours"
                except ValueError:
                    embed = discord.Embed(
                    title="Failed Muting Member",
                    description=f'You need to specify the timelimit as ex: 5m, 5h, or 5d',
                    color=color
                        )
                    embed.set_author(name=f"{botname}", icon_url=f"{icon}")
                    await slash.response.send_message(embed=embed, ephemeral=True)
                    return
            
            elif 'm' in time or 'M' in time:
                try:
                    time = int(re.sub(r"[^0-9]", "", time))
                    delta = timedelta(minutes=time)
                    if time == 1:
                        mute_unit = "minute"
                    else:
                        mute_unit = "minutes"
                except ValueError:
                    embed = discord.Embed(
                    title="Failed Muting Member",
                    description=f'You need to specify the timelimit as ex: 5m, 5h, or 5d',
                    color=color
                        )
                    embed.set_author(name=f"{botname}", icon_url=f"{icon}")
                    await slash.response.send_message(embed=embed, ephemeral=True)
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
                embed = discord.Embed(
                    title="Successfully Muted Member",
                    description=f'{member.mention} has been muted in the server.{mute_response}',
                    color=color
                    )
                embed.add_field(name = "Reason: ", value = f'"{reason}"', inline=True)
                embed.add_field(name = "Time: ", value = f"{time} {mute_unit}", inline=True)
                embed.set_author(name=f"{botname}", icon_url=f"{icon}")
                await slash.response.send_message(embed=embed)
            except:
                embed = discord.Embed(
                title="Failed Muting Member",
                description=f'{botname} does not have permission to mute {member.mention} in the server.',
                color=color
                    )
                embed.set_author(name=f"{botname}", icon_url=f"{icon}")
                await slash.response.send_message(embed=embed, ephemeral=True)

    # unmute a member
    @commands.has_permissions(ban_members=True)
    @commands.has_permissions(administrator=True)
    @app_commands.command(name='unmute', description='Unmute a member')
    async def unmute_member(ctx, slash: discord.Interaction, member: discord.Member, *, 
                         reason: str = 'The moderators have decided to unmute you in this server.'):
        try:
            await member.timeout(None, reason=reason)
            embed = discord.Embed(
                title="Successfully Unmuted Member",
                description=f'{member.mention} has been unmuted in the server.',
                color=color
                )
            embed.add_field(name = "Reason: ", value = f'"{reason}"', inline=True)
            embed.set_author(name=f"{botname}", icon_url=f"{icon}")
            await slash.response.send_message(embed=embed)
        except:
            embed = discord.Embed(
            title="Failed Unmuting Member",
            description=f'{botname} does not have permission to unmute {member.mention} in the server.',
            color=color
                )
            embed.set_author(name=f"{botname}", icon_url=f"{icon}")
            await slash.response.send_message(embed=embed, ephemeral=True)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(moderation(bot))