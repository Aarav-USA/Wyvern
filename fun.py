import discord
from discord.ext import commands

import json
import random
from typing import Union

class Fun(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx: commands.Context,
            user: Union[discord.User, discord.Member] = None) -> None:
        if user is None:
            user=ctx.author
        favatar=discord.Embed(title=f'{user.name}\'s Avatar',
            color = discord.Colour.gold())
        favatar.set_footer(text=f'Requested by: {ctx.author.name}')

        favatar.set_image(url=f'{user.avatar_url}')
        await ctx.send(embed=favatar)

    @commands.command()
    async def dadjoke(self, ctx: commands.Context) -> None:
        with open('dadjokes.json', 'r') as f:
            dadjokes = json.load(f)
        await ctx.send(random.choice(dadjokes))

def setup(bot: commands.Bot) -> None:
    print('Loading fun extension...')
    bot.add_cog(Fun(bot))
