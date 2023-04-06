from discord.ext import commands
import asyncio


class ServerStat(commands.Cog):
    async def __init__(self, bot):
        self.bot = bot
        self.server_stats = {
            "members": {
                "title": "Total Members",
                "count": lambda server: len(server.members)
            },
            "bots": {
                "title": "Total Bots",
                "count": lambda server: len([m for m in server.members if m.bot])
            },
            "members_only": {
                "title": "Members Only",
                "count": lambda server: len([m for m in server.members if not m.bot])
            },
            "bots_only": {
                "title": "Bots Only",
                "count": lambda server: len([m for m in server.members if m.bot])
            },
            "banned_members": {
                "title": "Banned Members",
                "count": lambda server: len(await server.bans())
            },
            "pending_members": {
                "title": "Pending Members",
                "count": lambda server: len(await server.invites())
            }
        }
        self.roles = {
            "all_roles": {
                "title": "All Roles",
                "members": lambda server: server.members
            }
        }
        self.category = None

    async def create_voice_channels(self, server, category, name):
        channels = []
        for _, stat in self.server_stats.items():
            channel_name = f"{name} - {stat['title']}"
            channel = await server.create_voice_channel(channel_name, category=category)
            channels.append(channel)
        return channels

    async def update_voice_channels(self, server, channels, stats):
        for channel, stat in zip(channels, stats):
            count = stat['count'](server)
            await channel.edit(name=f"{stat['title']}: {count}")

    @commands.command()
    async def serverstats(self, ctx, *, setup="default"):
        setup = setup.lower()
        stats = self.server_stats.get(setup, None)
        roles = self.roles.get(setup, None)

        if not stats and not roles:
            await ctx.send(f"Invalid setup '{setup}'")
            return

        if not self.category:
            self.category = await ctx.guild.create_category(name="Server Stats")
            await self.category.set_permissions(ctx.guild.default_role, view_channel=True)

        channels_name = f"Stats: {stats['title']}" if stats else f"Roles: {roles['title']}"
        channels = [channel for channel in self.category.voice_channels if channel.name.startswith(channels_name)]

        if not channels:
            channels = await self.create_voice_channels(ctx.guild, self.category, channels_name)

        if stats:
            await self.update_voice_channels(ctx.guild, channels, [stats])
        elif roles:
            members = roles['members'](ctx.guild)
            for role in ctx.guild.roles:
                if role.name not in self.roles:
                    self.roles[role.name] = {
                        "title": role.name,
                        "members": lambda server: [m for m in members if role in m.roles]
                    }
            role_stats = [{"title": role.name, "count": lambda server: len(role['members'](server))} for role in self.roles.values()]
            await self.update_voice_channels(ctx.guild, channels, role_stats)

    async def setup(bot):
        bot.add_cog(ServerStat(bot))

    asyncio.run(setup())
    asyncio.run(__init__())
