from discord.ext import commands

import util

SOURCE_LINK = 'https://github.com/XxMidasTouchxX/HoneyComb.git'
SUPPORT_SERVER = 'https://discord.gg/ZAM9M2ChBE'

# HoneyComb bot information commands.
class Info(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(help='Link source code')
    async def source(self, ctx: commands.Context) -> None:
        embed = util.HoneyCombEmbed(
            title='Check out my source code!',
            url=SOURCE_LINK
        )
        await ctx.send(embed=embed)

    @commands.command(help='Link support server', aliases=['su'])
    async def support(self, ctx: commands.Context) -> None:
        await ctx.send(SUPPORT_SERVER)

def setup(bot: commands.Bot) -> None:
    print('Loading info extension...')
    bot.add_cog(Info(bot))
