#!/usr/bin/python3

# Leveling bot, by Asger and Josiah.

# These import the discord stuff into our program so we can use it.
import discord
from discord.ext import commands

# This makes a new bot with the prefix hc! and stores it in
# a variable called bot.
bot = commands.Bot('hc!')

# Command to kick yourself.
@bot.command()
async def kickme(ctx):
    await ctx.author.kick()

# Under here we will put our commands, we don't have any yet.


# This opens the token.txt file and reads the token out of it.
with open('ticket/token.txt', 'r') as token_file:
    token = token_file.readline().strip()

# This starts the bot up.
bot.run(token)

#Reaction roles
@client.command()
async def reactionrole(ctx, emoji, role: discord.Role,*,message):

    emb = discord.Embed(description=message)
    msg = await ctx.channel.send(embed=emb)
    await msg.add_reaction(emoji)