import discord
from discord.ext import commands

class AutoMod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bad_words = ["bad_word1", "bad_word2", "bad_word3"]
        self.ignore_roles = [1234567890, 0987654321]  # role ids
        self.ignore_channels = [1234567890, 0987654321]  # channel ids
        self.warn_threshold = 3
        self.warn_message = "Please refrain from spamming the chat or you will be muted."

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        # nono words
        for word in self.bad_words:
            if word in message.content.lower():
                if any(role.id in self.ignore_roles for role in message.author.roles):
                    return
                await message.delete()
                await message.channel.send(f"{message.author.mention}, please refrain from using that language.")

        # repeated text
        if len(set(message.content)) <= 2:
            if any(role.id in self.ignore_roles for role in message.author.roles):
                return
            await message.delete()
            await message.channel.send(f"{message.author.mention}, please refrain from spamming the chat.")

        # discord invites & external links
        if "discord.gg/" in message.content or "http" in message.content:
            if any(role.id in self.ignore_roles for role in message.author.roles):
                return
            await message.delete()
            await message.channel.send(f"{message.author.mention}, please refrain from sending external links or server invites.")

        # excessive caps
        caps_ratio = sum(1 for c in message.content if c.isupper()) / len(message.content)
        if caps_ratio > 0.7:
            if any(role.id in self.ignore_roles for role in message.author.roles):
                return
            await message.delete()
            await message.channel.send(f"{message.author.mention}, please refrain from typing in all caps.")

        # excessive emoji
        if sum(1 for c in message.content if c in discord.emojis.EMOJI_UNICODE.values()) > 5:
            if any(role.id in self.ignore_roles for role in message.author.roles):
                return
            await message.delete()
            await message.channel.send(f"{message.author.mention}, please refrain from using too many emojis.")

        # excessive spoilers
        if sum(1 for c in message.content if c == "||") > 3:
            if any(role.id in self.ignore_roles for role in message.author.roles):
                return
            await message.delete()
            await message.channel.send(f"{message.author.mention}, please refrain from using too many spoilers.")

        # excessive mentions
        if len(message.mentions) >= 5:
            if any(role.id in self.ignore_roles for role in message.author.roles):
                return
            await message.delete()
            await message.channel.send(f"{message.author.mention}, please refrain from mentioning too many users in one message.")

        # zalgo text
        if any(0x0300 <= ord(c) <= 0x036F for c in message.content):
            if any(role.id in self.ignore_roles for role in message.author.roles):
                return
            await message.delete()
            await message.channel.send(f"{message.author.mention}, please refrain from using zalgo text.")

        # spam
        # continue this later if message.author.id not in
