import discord
from discord.ext import commands

class AutoMod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bad_words = ['bad', 'words', 'list']
        self.max_repeated_text = 3
        self.max_discord_invites = 1
        self.max_external_links = 1
        self.max_caps = 5
        self.max_emoji = 5
        self.max_spoilers = 3
        self.max_mentions = 5
        self.ignore_roles = [1234567890, 0987654321] # ignore roles
        self.ignore_channels = [1234567890, 0987654321] # ignore channels
        self.action = 'warn_delete' # 'disable', 'warn', 'delete', 'warn_delete'
        self.warn_message = 'Please refrain from using inappropriate language or spamming.'
        self.delete_message = 'Your message has been deleted due to inappropriate content or spamming.'
        self.ban_message = 'You have been banned for violating our community guidelines.'
        self.kick_message = 'You have been kicked for violating our community guidelines.'
        self.mute_message = 'You have been muted for violating our community guidelines.'

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.guild is None:
            return
        if message.channel.id in self.ignore_channels:
            return
        if any(role.id in self.ignore_roles for role in message.author.roles):
            return

        if any(word.lower() in message.content.lower() for word in self.bad_words):
            await self.handle_action(message)
            return

        # repeated text
        if self.check_repeated_text(message):
            await self.handle_action(message)
            return

        # discord invites
        if self.check_discord_invites(message):
            await self.handle_action(message)
            return

        # external links
        if self.check_external_links(message):
            await self.handle_action(message)
            return

        # excessive caps
        if self.check_excessive_caps(message):
            await self.handle_action(message)
            return

        # excessive emoji
        if self.check_excessive_emoji(message):
            await self.handle_action(message)
            return

        # excessive spoilers
        if self.check_excessive_spoilers(message):
            await self.handle_action(message)
            return

        # excessive mentions
        if self.check_excessive_mentions(message):
            await self.handle_action(message)
            return

    def check_repeated_text(self, message):
        words = message.content.split()
        for word in words:
            if len(word) > 3 and word * self.max_repeated_text in message.content:
                return True
        return False

    def check_discord_invites(self, message):
        count = message.content.count('discord.gg/')
        if count > self.max_discord_invites:
            return True
        return False

    def check_external_links(self, message):
        count = message.content.count('http')
        if count > self.max_external_links:
            return True
        return False

    def check_excessive_caps(self, message):
        count = sum(1 for c in message.content if c.isupper())
        if count > self.max_caps:
            return True
        return False

    def check_excessive_emoji(self, message):
        count = sum(1 for c in message.content if c in emoji.UNICODE_EMOJI)
        if count > self.max_emoji:
            return True
return False

    def check_excessive_spoilers(self, message):
        count = message.content.count('||')
        if count > self.max_spoilers:
            return True
        return False

    def check_excessive_mentions(self, message):
        count = len(message.mentions)
        if count > self.max_mentions:
            return True
        return False

    async def handle_action(self, message):
        if self.action == 'disable':
            return
        if self.action == 'warn':
            await message.channel.send(self.warn_message)
        if self.action == 'delete':
            await message.delete()
            await message.channel.send(self.delete_message)
        if self.action == 'warn_delete':
            await message.channel.send(self.warn_message)
            await message.delete()
            await message.channel.send(self.delete_message)
        if self.action == 'ban':
            await message.author.send(self.ban_message)
            await message.guild.ban(message.author, reason='AutoMod')
        if self.action == 'kick':
            await message.author.send(self.kick_message)
            await message.guild.kick(message.author, reason='AutoMod')
        if self.action == 'mute':
            role = discord.utils.get(message.guild.roles, name='Muted')
            if role is None:
                role = await message.guild.create_role(name='Muted')
                for channel in message.guild.channels:
                    await channel.set_permissions(role, send_messages=False)
            await message.author.send(self.mute_message)
            await message.author.add_roles(role, reason='AutoMod')

    @commands.command()
    async def automod(self, ctx, action=None):
        if action is None:
            await ctx.send(f'Current action: {self.action}')
        elif action in ['disable', 'warn', 'delete', 'warn_delete', 'ban', 'kick', 'mute']:
            self.action = action
            await ctx.send(f'Action set
to: {self.action}')
        else:
            await ctx.send('Invalid action.')

    @commands.command()
    async def set_max_repeated_text(self, ctx, value: int):
        self.max_repeated_text = value
        await ctx.send(f'Max repeated text set to: {self.max_repeated_text}')

def setup(bot):
    bot.add_cog(AutoMod(bot))
